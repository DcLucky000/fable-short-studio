#!/usr/bin/env python3
"""Batch Seedance (Ark) video generation for 置顶的人 shots."""
from __future__ import annotations

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = "https://ark.cn-beijing.volces.com/api/v3"
MODEL = "doubao-seedance-1-0-pro-fast-251015"
PROMPT_MD = Path("/workspace/fable-short-studio/packages/置顶的人-出片提示.md")
OUT_DIR = Path("/workspace/fable-short-studio/output/置顶的人/shots")
ORDER = [1, 3, 5, 4, 2, 6, 7]
DURATIONS = {1: 5, 2: 5, 3: 8, 4: 7, 5: 10, 6: 5, 7: 5}
MAX_RETRIES = 2
POLL_INTERVAL = 12


def api_key() -> str:
    key = os.environ.get("ARK_API_KEY", "").strip()
    if not key:
        raise SystemExit("ARK_API_KEY not set")
    return key


def parse_prompts(md_path: Path) -> dict[int, str]:
    text = md_path.read_text(encoding="utf-8")
    # Skip the first global-prefix-only code block; take shot blocks under ### 镜 N
    prompts: dict[int, str] = {}
    for m in re.finditer(
        r"### 镜\s*(\d+)[^\n]*\n(?:.*?\n)*?```\n(.*?)```",
        text,
        re.DOTALL,
    ):
        n = int(m.group(1))
        body = m.group(2).strip()
        # join paragraphs with blank line preserved as single text
        prompts[n] = body
    if len(prompts) < 7:
        raise SystemExit(f"parsed only {sorted(prompts)} from {md_path}")
    return prompts


def http_json(method: str, path: str, body: dict | None = None) -> dict:
    url = f"{BASE}{path}"
    data = None if body is None else json.dumps(body, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {api_key()}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code}: {err_body}") from e


def create_task(prompt: str, duration: int, with_resolution: bool = True) -> str:
    payload: dict = {
        "model": MODEL,
        "content": [{"type": "text", "text": prompt}],
        "ratio": "9:16",
        "duration": duration,
        "watermark": False,
        "generate_audio": False,
    }
    if with_resolution:
        payload["resolution"] = "720p"
    try:
        result = http_json("POST", "/contents/generations/tasks", payload)
    except RuntimeError as e:
        msg = str(e)
        # drop unsupported fields and retry once at create level
        if with_resolution and ("resolution" in msg.lower() or "InvalidParameter" in msg):
            return create_task(prompt, duration, with_resolution=False)
        if "generate_audio" in msg.lower() or "GenerateAudio" in msg:
            payload.pop("generate_audio", None)
            if with_resolution:
                payload["resolution"] = "720p"
            result = http_json("POST", "/contents/generations/tasks", payload)
        else:
            raise
    tid = result.get("id")
    if not tid:
        raise RuntimeError(f"no task id in create response: {result}")
    return tid


def poll_task(task_id: str, timeout_s: int = 600) -> dict:
    deadline = time.time() + timeout_s
    while time.time() < deadline:
        info = http_json("GET", f"/contents/generations/tasks/{task_id}")
        status = info.get("status", "")
        print(f"  poll {task_id}: {status}", flush=True)
        if status in ("succeeded", "failed", "cancelled"):
            return info
        time.sleep(POLL_INTERVAL)
    raise TimeoutError(f"task {task_id} timed out after {timeout_s}s")


def download(url: str, dest: Path) -> None:
    req = urllib.request.Request(url, method="GET")
    with urllib.request.urlopen(req, timeout=300) as resp:
        dest.write_bytes(resp.read())


def write_fail(shot: int, task_ids: list[str], errors: list[str]) -> None:
    path = OUT_DIR / f"FAIL_shot{shot}.md"
    lines = [
        f"# FAIL shot {shot}",
        "",
        f"- task ids: {', '.join(task_ids) if task_ids else '(none)'}",
        "",
        "## errors",
        "",
    ]
    for e in errors:
        lines.append("```")
        lines.append(e)
        lines.append("```")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    prompts = parse_prompts(PROMPT_MD)
    only = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else ORDER
    status_rows: list[dict] = []

    # load prior STATUS if continuing
    status_path = OUT_DIR / "STATUS.md"
    prior: dict[int, dict] = {}
    if status_path.exists():
        # not parsed rigidly; we overwrite at end
        pass

    for shot in only:
        prompt = prompts[shot]
        duration = DURATIONS[shot]
        out_mp4 = OUT_DIR / f"ZT_shot{shot}.mp4"
        print(f"\n=== Shot {shot} duration={duration}s ===", flush=True)
        task_ids: list[str] = []
        errors: list[str] = []
        ok = False
        last_tid = ""
        for attempt in range(1, MAX_RETRIES + 2):  # initial + 2 retries
            try:
                print(f"  create attempt {attempt}...", flush=True)
                tid = create_task(prompt, duration)
                last_tid = tid
                task_ids.append(tid)
                print(f"  task id: {tid}", flush=True)
                info = poll_task(tid)
                if info.get("status") == "succeeded":
                    video_url = (info.get("content") or {}).get("video_url")
                    if not video_url:
                        raise RuntimeError(f"succeeded but no video_url: {json.dumps(info, ensure_ascii=False)[:800]}")
                    print(f"  downloading -> {out_mp4}", flush=True)
                    download(video_url, out_mp4)
                    size = out_mp4.stat().st_size
                    print(f"  saved {size} bytes", flush=True)
                    status_rows.append(
                        {
                            "shot": shot,
                            "ok": True,
                            "path": str(out_mp4),
                            "size": size,
                            "task_id": tid,
                            "error": "",
                        }
                    )
                    fail_path = OUT_DIR / f"FAIL_shot{shot}.md"
                    if fail_path.exists():
                        fail_path.unlink()
                    ok = True
                    break
                else:
                    err = json.dumps(info, ensure_ascii=False)
                    errors.append(err)
                    print(f"  FAILED: {err[:500]}", flush=True)
            except Exception as e:
                errors.append(str(e))
                print(f"  ERROR: {e}", flush=True)
        if not ok:
            write_fail(shot, task_ids, errors)
            status_rows.append(
                {
                    "shot": shot,
                    "ok": False,
                    "path": str(OUT_DIR / f"FAIL_shot{shot}.md"),
                    "size": 0,
                    "task_id": last_tid or (task_ids[-1] if task_ids else ""),
                    "error": errors[-1][:500] if errors else "unknown",
                }
            )

    # merge with existing STATUS for shots not in this run
    write_status(status_rows, only)
    return 0 if all(r["ok"] for r in status_rows) else 1


def write_status(rows: list[dict], ran: list[int]) -> None:
    status_path = OUT_DIR / "STATUS.md"
    by_shot: dict[int, dict] = {}
    if status_path.exists():
        # re-scan filesystem for truth
        pass
    for r in rows:
        by_shot[r["shot"]] = r
    # fill from disk for all 1-7
    lines = [
        "# 《置顶的人》Seedance 出片 STATUS",
        "",
        f"- model: `{MODEL}`",
        f"- generated_at: {time.strftime('%Y-%m-%d %H:%M:%S')} Asia/Shanghai",
        f"- order_ran: {ran}",
        "",
        "| 镜 | 状态 | 文件 | 大小 | task id | 备注 |",
        "|---|---|---|---|---|---|",
    ]
    for shot in range(1, 8):
        mp4 = OUT_DIR / f"ZT_shot{shot}.mp4"
        fail = OUT_DIR / f"FAIL_shot{shot}.md"
        if shot in by_shot:
            r = by_shot[shot]
            if r["ok"] and mp4.exists():
                lines.append(
                    f"| {shot} | ✅ succeeded | `{mp4}` | {r['size']} | `{r['task_id']}` | |"
                )
            else:
                lines.append(
                    f"| {shot} | ❌ failed | `{fail}` | — | `{r.get('task_id','')}` | {(r.get('error') or '')[:120]} |"
                )
        elif mp4.exists():
            lines.append(
                f"| {shot} | ✅ succeeded (prior) | `{mp4}` | {mp4.stat().st_size} | — | |"
            )
        elif fail.exists():
            lines.append(f"| {shot} | ❌ failed (prior) | `{fail}` | — | — | see FAIL file |")
        else:
            lines.append(f"| {shot} | ⏳ pending | — | — | — | |")
    lines.append("")
    must = [1, 3, 5]
    must_ok = all((OUT_DIR / f"ZT_shot{s}.mp4").exists() for s in must)
    lines.append(f"- 必保 1/3/5 齐: {'YES' if must_ok else 'NO'}")
    all_ok = all((OUT_DIR / f"ZT_shot{s}.mp4").exists() for s in range(1, 8))
    lines.append(f"- 七镜齐: {'YES' if all_ok else 'NO'}")
    lines.append(f"- 可通知剪辑: {'YES' if must_ok else 'NO（必保未齐）'}")
    lines.append("")
    status_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"\nWrote {status_path}", flush=True)


if __name__ == "__main__":
    raise SystemExit(main())
