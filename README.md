# UZH.ai Agentic AI workshop

Workshop website and shareable materials for the UZH.ai Students Association.
The planned session is 23 November 2026, 16:00–19:00 Europe/Zurich at Zentrum.

The website is a copy of the original HTML app scaffold. Its outline, room,
setup requirements, prompts, and two sample downloads still contain explicit
placeholders. Replace them with approved public content before sharing.

## Repository map

```text
index.html             Website entry point and editable page content
.nojekyll              Empty marker for plain static GitHub Pages publishing
site/assets/           Website CSS and JavaScript
site/downloads/        Approved public downloads and current sample files
site/downloads/code/   Shared example scripts and their usage instructions
docs/                  Project architecture, development, and deployment notes
admin/                 Private preparation; ignored by Git
apps/                  Original app scaffolds, kept unchanged; ignored by Git
.agent-work/           Local agent helpers and scratch files; ignored by Git
```

Start with the [documentation index](docs/README.md). Agent work must also
follow [AGENTS.md](AGENTS.md), including its file-access and human-only rules.

## Preview locally

From the repository root, run:

```sh
python3 -B -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000/>. Stop the server with Ctrl+C when finished.
No package installation or build step is required. Opening `index.html`
directly also displays the page; clipboard behavior may differ on local files.

## Edit and share

- Edit the outline, session details, download cards, and prompt text in
  `index.html`.
- Edit appearance in `site/assets/styles.css` and copying behavior in
  `site/assets/script.js`.
- Put approved public PDFs, guides, and examples in `site/downloads/` and
  add relative links beginning with `./site/downloads/` to the page.
- Keep Markdown as the editable source for written guides; a PDF can be an
  additional downloadable export. The presentation and installation guide
  have not been added yet.

See [development](docs/development.md) for editing checks and
[deployment](docs/deployment.md) for GitHub Pages setup without a custom YAML
workflow. Publishing from the repository root includes other eligible tracked
files, so `site/` is an organizational folder rather than a publication filter.

Private preparation, original app variants, and agent working storage stay
local. Ignore rules do not untrack existing files or remove Git history.
