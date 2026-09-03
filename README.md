# Hawkeye

**Windows kernel security research console** — live symbols, ETW, memory, and driver-backed inspection on Windows 10/11.

> **→ [Open the official website](https://hawkeye-leo.github.io/hawkeye/)**  
> Downloads, illustrated guide, Community vs Lab, privacy & terms — all live there.

[![Website](https://img.shields.io/badge/website-hawkeye--leo.github.io%2Fhawkeye-2ea043?style=for-the-badge)](https://hawkeye-leo.github.io/hawkeye/)
[![Community releases](https://img.shields.io/github/v/release/hawkeye-Leo/hawkeye-community?label=Community&style=for-the-badge)](https://github.com/hawkeye-Leo/hawkeye-community/releases/latest)
[![Source code](https://img.shields.io/badge/source-hawkeye--community-0078D4?style=for-the-badge)](https://github.com/hawkeye-Leo/hawkeye-community)

---

## You probably want one of these

| I want… | Go here |
| --- | --- |
| **Download Hawkeye Community** (free, GPL) | [**Releases →**](https://github.com/hawkeye-Leo/hawkeye-community/releases/latest) |
| **Browse source code** | [**hawkeye-community**](https://github.com/hawkeye-Leo/hawkeye-community) |
| **Read the walkthrough** (`!probe`, `!etw`, driver setup) | [**Official site →**](https://hawkeye-leo.github.io/hawkeye/) |
| **Hawkeye Lab** (detection + `!analyze` reports) | [**Lab page →**](https://hawkeye-leo.github.io/hawkeye/lab/) |

---

## Community vs Lab

| | **Community** | **Lab** |
| --- | :---: | :---: |
| Live console + driver setup | ✓ | ✓ |
| `!probe`, `!etw`, memory tools | ✓ | ✓ |
| High-risk detection commands | — | ✓ |
| `!analyze` + scored report | — | ✓ |

Community is **open source** ([GPL-3.0-or-later](https://github.com/hawkeye-Leo/hawkeye-community/blob/main/LICENSE)).  
Lab is a **subscription** build on the same foundation — see the [Lab page](https://hawkeye-leo.github.io/hawkeye/lab/).

---

## What is this repository?

**This repo is the GitHub Pages source for the website** — HTML/CSS and guide assets.  
It is **not** where you download the app or clone C++ source.

- **Website (live):** [hawkeye-leo.github.io/hawkeye/](https://hawkeye-leo.github.io/hawkeye/)
- **Product source:** [hawkeye-Leo/hawkeye-community](https://github.com/hawkeye-Leo/hawkeye-community)

Authorized research on systems you own or may administer only. Not a bypass kit.

---

<details>
<summary>Maintainers: publish site changes</summary>

Edit files locally (`C:\Users\38105\hawkeye-pages` or your clone), then:

```powershell
git add -A
git commit -m "Update site"
git push origin main
```

GitHub Pages deploys to `https://hawkeye-leo.github.io/hawkeye/` on push to `main`.

</details>
