import base64
import json
import os
import pathlib
import subprocess

for key in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
    os.environ.pop(key, None)


def put(repo, path, local, message):
    raw = pathlib.Path(local).read_bytes()
    body = {
        "message": message,
        "content": base64.b64encode(raw).decode("ascii"),
        "branch": "main",
    }
    existing = subprocess.run(
        ["gh", "api", f"repos/{repo}/contents/{path}", "--jq", ".sha"],
        text=True,
        capture_output=True,
    )
    if existing.returncode == 0 and existing.stdout.strip():
        body["sha"] = existing.stdout.strip()
    p = subprocess.run(
        ["gh", "api", "--method", "PUT", f"repos/{repo}/contents/{path}", "--input", "-"],
        input=json.dumps(body),
        text=True,
        capture_output=True,
    )
    if p.returncode != 0:
        raise SystemExit(f"{repo}/{path} failed:\n{p.stderr}\n{p.stdout}")
    data = json.loads(p.stdout)
    print(data["commit"]["html_url"])


ROOT = pathlib.Path(r"C:\Users\38105\hawkeye-pages")
REPO = "hawkeye-Leo/hawkeye-Leo.github.io"

put(REPO, "terms/index.html", ROOT / "terms" / "index.html", "Terms: Community pre-check, refund policy, Lab driver parity.")
put(REPO, "lab/early-access/index.html", ROOT / "lab" / "early-access" / "index.html", "Subscribe page: link Terms refund policy.")
