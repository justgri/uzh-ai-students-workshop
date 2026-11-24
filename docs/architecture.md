# Architecture

## Components

The website is plain HTML, CSS, and JavaScript. It has no build step, package
dependencies, external assets, backend, or database.

| File or folder | Responsibility |
| --- | --- |
| `index.html` | Intro: session details, outline, and download links |
| `site/tech.html` | Software, download links, and workshop subscription requirement |
| `site/basics.html` | Reusable travel-planning scaffold, dream trip, feedback and handoff; optional reasoning, parallel work, instructions, skill and synthetic-hook exercises |
| `site/planner.html` | Synthetic second brain, planning skill and updates; optional read-only calendar, meetings and local dashboard |
| `site/research.html` | Cumulative 1 → 3 → 5 calibration; optional 20-case pilot, skill validation and bounded automation |
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

Exercise pages begin with Task / Learn / Workflow, followed by short prompt
cards with a purpose, a grey explanatory example and a human inspection step.
Prompts contain two to four sentences. Later-stage work is grouped under
“Go further”; each exercise page has an expandable “Starting a project” guide,
alongside the Planner scaffold and Basics glossary/scaffold. The setup guides
cover creating and opening a local project folder, distinguish working scope
from enforced file permissions, and explain how saved files and handoffs support
new conversations in the same folder. Their examples match each exercise;
the first prompts initialize the folder the participant has already opened.
Textareas fit their content on load, resize and expansion, while retaining
manual resizing and no-JavaScript access. Unknown participant inputs remain
bracketed placeholders. Planner offers a generic, downloadable instruction
template at `site/downloads/planner/AGENTS.md` and links to the complete public
skill template in `site/downloads/skills/personal-planner-operator/`. The
downloaded instructions belong in the student's planner; they do not replace
this workshop repository's root `AGENTS.md`.

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
- The scaffold originally included HTML, CSS, JavaScript, and two placeholder
  downloads. Files now links only to the three final presentation PDFs selected
  on 23 November 2026. Presentation syncs produce the requested Keynote/PDF
  pairs in `presentation/final/` from the human, Codex, and Claude working
  sources; website sync is a separate copy of those three final PDFs using
  `scripts/sync-presentation-pdfs.py`. Stable paths and provenance are recorded
  in `AGENTS.md`, `presentation/final/README.md`, and `site/downloads/README.md`.
  Local app logs and other app variants were not copied into the public site.
- The Planner records are synthetic. Its public skill template is adapted
  from the instructor's planning workflow, with a self-contained checklist
  and exercise paths; no personal planner records were copied. Tech uses the
  workshop software list; the inherited installation guide was not imported.
- The paid plan is a workshop setup requirement, not a claim that all agent
  platforms require payment. Research prompts describe a method; they do not
  report benchmark results or claim an installed automation.

## Publication scope

Root-based publishing can serve other eligible tracked repository files too.
Moving a file outside `site/` does not make it private. `admin/`, `apps/`, and
`.agent-work/` are ignored local directories; Git-ignore rules do not remove
files already tracked or committed in history. See [deployment](deployment.md).
