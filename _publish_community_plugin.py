import base64
import json
import pathlib
import subprocess

REPO = "hawkeye-Leo/hawkeye-community"
ROOT = pathlib.Path(r"C:\Hawkeys-AC\Hawkeye Community")

FILES = [
    ("hawk_hot_targets.h", "Add the HawkHotTargets plugin contract header."),
    ("README.md", "Document the analyze plugin contract and sample."),
    ("samples/HawkHotTargets/HawkHotTargets.c", "Add the HawkHotTargets sample plugin."),
    ("samples/HawkHotTargets/HawkHotTargets.def", "Add the HawkHotTargets sample plugin."),
    ("samples/HawkHotTargets/HawkHotTargets.sln", "Add the HawkHotTargets sample plugin."),
    ("samples/HawkHotTargets/HawkHotTargets.vcxproj", "Add the HawkHotTargets sample plugin."),
    ("samples/HawkHotTargets/HawkHotTargetsTest.c", "Add the HawkHotTargets sample plugin."),
    ("samples/HawkHotTargets/HawkHotTargetsTest.vcxproj", "Add the HawkHotTargets sample plugin."),
]


def put(path, message):
    raw = (ROOT / path).read_bytes()
    body = {
        "message": message,
        "content": base64.b64encode(raw).decode("ascii"),
        "branch": "main",
    }
    existing = subprocess.run(
        ["gh", "api", f"repos/{REPO}/contents/{path}", "--jq", ".sha"],
        text=True,
        capture_output=True,
    )
    if existing.returncode == 0 and existing.stdout.strip():
        body["sha"] = existing.stdout.strip()
    p = subprocess.run(
        ["gh", "api", "--method", "PUT", f"repos/{REPO}/contents/{path}", "--input", "-"],
        input=json.dumps(body),
        text=True,
        capture_output=True,
    )
    if p.returncode != 0:
        raise SystemExit(f"{REPO}/{path} failed:\n{p.stderr}\n{p.stdout}")
    data = json.loads(p.stdout)
    print(data["commit"]["html_url"])


for path, message in FILES:
    put(path, message)
