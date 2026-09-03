# Hawkeye — official website (GitHub Pages)

**Live site:** [https://hawkeye-leo.github.io/](https://hawkeye-leo.github.io/)

| Edition | Page | Source |
| --- | --- | --- |
| **Hawkeye Community** (open source) | [/](https://hawkeye-leo.github.io/) | [hawkeye-community](https://github.com/hawkeye-Leo/hawkeye-community) |
| **Hawkeye Lab** (subscription) | [/lab/](https://hawkeye-leo.github.io/lab/) | Commercial build |

Hawkeye is a **Windows kernel security research console** — live memory & process analysis, driver-assisted bench commands (`!probe`, `!etw`, …). Community is GPL; Lab adds automated detection and `!analyze` reports.

This repository is **`hawkeye-Leo.github.io`** — static site only. It is **not** the product source code.

## Publish

From this folder:

```powershell
git add -A
git commit -m "Update site"
git push origin main
```

GitHub Pages builds automatically (user site → `hawkeye-leo.github.io`).

Legacy project site `/hawkeye/` on repo `hawkeye-Leo/hawkeye` is retired; use the root URL above.
