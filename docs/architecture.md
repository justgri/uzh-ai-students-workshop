# Architecture

## Components

The website is plain HTML, CSS, and JavaScript. It has no build step, package
dependencies, external assets, backend, or database.

| File or folder | Responsibility |
| --- | --- |
| `index.html` | Session details, outline, download links, and prompt text |
| `site/assets/styles.css` | Layout, colors, keyboard focus, and responsive styles |
| `site/assets/script.js` | Prompt copy buttons and manual-copy fallback |
| `site/downloads/` | Files deliberately selected for public download |
| `docs/` | Contributor documentation about the project |

The root page loads its CSS and JavaScript from `site/assets/`. Download links
request a specific file from `site/downloads/`. Prompts are stored once, in
read-only textareas in `index.html`; JavaScript copies that same text.

Copying uses the browser's Clipboard API when available. If access is denied
or unavailable, the script selects the prompt and explains how to copy it
manually. With JavaScript disabled, the prompts remain manually selectable.

## Layout decisions

- `index.html` stays at the repository root so GitHub Pages can publish from
  a branch without a custom workflow file.
- `site/` groups supporting website files; `docs/` keeps its role as project
  documentation.
- Asset and download URLs are relative to the root page. They work both at a
  localhost root and below a GitHub Pages repository path.
- The original `apps/html_website/` scaffold remains unchanged and ignored.
  The public copy is maintained independently; changes are not synchronized.
- Only the HTML, CSS, JavaScript, and two placeholder downloads were copied.
  Local app logs and other app variants were not copied into the public site.

## Publication scope

Root-based publishing can serve other eligible tracked repository files too.
Moving a file outside `site/` does not make it private. `admin/`, `apps/`, and
`.agent-work/` are ignored local directories; Git-ignore rules do not remove
files already tracked or committed in history. See [deployment](deployment.md).
