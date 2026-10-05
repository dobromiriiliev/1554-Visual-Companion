# Publishing the documentation

The repository includes a GitHub Pages workflow in `.github/workflows/pages.yml`.

## One-time repository setup

On GitHub:

1. open **Settings → Pages**;
2. choose **GitHub Actions** as the build and deployment source;
3. merge the workflow to the default branch;
4. run the workflow manually once if necessary.

## Local preview

```bash
python -m pip install -e ".[docs]"
mkdocs serve
```

## Strict build

```bash
mkdocs build --strict
```

The ordinary `Docs` CI workflow performs a build check on pull requests. The Pages workflow publishes only from the default branch or a manual dispatch.
