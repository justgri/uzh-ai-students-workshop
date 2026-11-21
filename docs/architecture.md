# Architecture

## Components

The website is plain HTML, CSS, and JavaScript. It has no build step, package
dependencies, external assets, backend, or database.

| File or folder | Responsibility |
| --- | --- |
| `index.html` | Intro: session details, outline, and download links |
| `site/tech.html` | Software, download links, and workshop subscription requirement |
| `site/basics.html` | Agent terminology and repository-setup prompts |
| `site/planner.html` | Synthetic planner structure, skills, dashboard, and publishing prompts |
| `site/research.html` | Research PRD, reviewed pilots, skill validation, and bounded-loop prompts |
| `site/assets/styles.css` | Layout, colors, keyboard focus, and responsive styles |
| `site/assets/script.js` | Prompt copy buttons and manual-copy fallback |
| `site/downloads/` | Files deliberately selected for public download |
| `docs/` | Contributor documentation about the project |

All five pages contain the same navigation with the current page marked by
`aria-current="page"`. Navigation works without JavaScript. The root page loads
CSS from `site/assets/`; the pages in `site/` use `assets/`. Exercise pages also
load the shared copy script. Download links request a specific file from
`site/downloads/`. Prompts are stored once, in read-only textareas on Basics,
Planner, and Research; JavaScript copies that same text.

Copying uses the browser's Clipboard API when available. If access is denied
or unavailable, the script selects the prompt and explains how to copy it
manually. With JavaScript disabled, the prompts remain manually selectable.

## Layout decisions

- `index.html` stays at the repository root so GitHub Pages can publish from
  a branch without a custom workflow file.
- `site/` groups supporting pages and assets; `docs/` keeps its role as project
  documentation.
- Navigation, asset, and download URLs are relative to each page. They work at a
  localhost root and below a GitHub Pages repository path.
- The original `apps/html_website/` scaffold remains unchanged and ignored.
  The public copy is maintained independently; changes are not synchronized.
- Only the HTML, CSS, JavaScript, and two placeholder downloads were copied.
  Local app logs and other app variants were not copied into the public site.
- The Planner example is synthetic. It was not copied from a personal planning
  repository. Tech uses the software list supplied for this workshop; the
  inherited installation guide was not imported.
- The paid plan is a workshop setup requirement, not a claim that all agent
  platforms require payment. Research prompts describe a method; they do not
  report benchmark results or claim an installed automation.

## Publication scope

Root-based publishing can serve other eligible tracked repository files too.
Moving a file outside `site/` does not make it private. `admin/`, `apps/`, and
`.agent-work/` are ignored local directories; Git-ignore rules do not remove
files already tracked or committed in history. See [deployment](deployment.md).
