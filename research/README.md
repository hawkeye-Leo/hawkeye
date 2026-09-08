# Hawkeye Research (GitHub Pages — English)

English research notes under `/research/` on [GitHub Pages](https://hawkeye-leo.github.io/hawkeye/research/).

Chinese editions for Kanxue live in **`../_kanxue/`** (gitignored, not pushed).

## Layout

```
research/
  index.html
  capture/
    index.html
    01-display-affinity/
      index.html
      images/
```

## Adding an article

1. Add `research/<series>/<slug>/index.html` and `images/`.
2. Link from the series index and `research/index.html`.
3. Update `sitemap.xml`.
4. Push `main` to deploy (when ready).

Optional: mirror a Chinese draft under `_kanxue/research/` for Kanxue — that folder never goes to GitHub.
