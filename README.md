# UX-FR Hugo Site

Static Hugo migration of [ux-fr.com](https://ux-fr.com/) using the
[PaperMod](https://github.com/adityatelange/hugo-PaperMod) theme.

## What is included

- 96 migrated WordPress posts and 2 static pages.
- Original post/page URLs preserved through explicit Hugo front matter.
- Local copies of available WordPress images under `static/wp-content/uploads/`.
- A shared placeholder for missing images at `static/images/placeholder.svg`.
- GitHub Pages deployment workflow in `.github/workflows/hugo.yml`.

## Local usage

```sh
git submodule update --init --recursive
hugo server
```

Build the static site:

```sh
hugo --minify
```

## Refresh migration

The migration script is idempotent and can be rerun:

```sh
python3 scripts/migrate_wordpress.py --clean
```

It writes a summary to `migration-report.json`.

## Deployment

The site is configured for GitHub Pages with the custom domain `ux-fr.com`.
The generated `public/` directory is ignored locally; GitHub Actions builds and
publishes the site.
