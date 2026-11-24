# UZH.ai Students Intro to Agentic AI Workshop

[Workshop website](https://justgri.github.io/uzh-ai-students-workshop/)

Workshop website and shareable materials for the UZH.ai Students Association.
The planned session is 23 November 2026, 16:00–19:00 Europe/Zurich at Zentrum,
room **SOE-E-02**.

Five static pages cover Intro, Tech, Basics, Planner, and Research. Exercise
prompts use bracketed placeholders for participants' inputs. Intro presents
four separate sections: motivation, agent harness, agentic AI vocabulary,
and tech vocabulary. Files offers the final [Presentation (Original)](site/downloads/intro_agentic_ai.pdf),
[Presentation (Codex-improved)](site/downloads/intro_agentic_ai_blue.pdf) and
[Presentation (Claude-improved)](site/downloads/intro_agentic_ai_blue_columns.pdf) PDFs.

## Repository map

```text
index.html             Website entry point and editable page content
site/*.html            Tech, Basics, Planner, and Research pages
site/assets/           Website CSS and JavaScript
site/downloads/        Final presentation PDFs and public download notes
site/downloads/code/   Shared example scripts and their usage instructions
docs/                  Project architecture, development, and deployment notes
scripts/               Maintained local website-update helpers
presentation/work/     Human, Codex, and Claude working sources; ignored by Git
presentation/final/    Three final Keynote/PDF pairs and provenance README; ignored by Git
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

- Edit the intro, outline, and file links in `index.html`; edit the other pages
  in `site/tech.html`, `site/basics.html`, `site/planner.html`, and
  `site/research.html`.
- Edit appearance in `site/assets/styles.css` and copying behavior in
  `site/assets/script.js`.
- Put approved public PDFs, guides, and examples in `site/downloads/` and
  add relative links beginning with `./site/downloads/` to the page.
- Edit the plain presentation in `presentation/work/human/intro_agentic_ai.key`.
  Requested presentation syncs refresh the relevant Keynote/PDF pairs in
  `presentation/final/`; Codex and Claude revisions live in
  `presentation/work/codex/` and `presentation/work/claude/` and preserve their
  separate styles. The final stems are `intro_agentic_ai`,
  `intro_agentic_ai_blue`, and `intro_agentic_ai_blue_columns`.
- To sync the website downloads, run `python3 -B scripts/sync-presentation-pdfs.py`.
  This overwrites only the three public PDFs with the matching PDFs from
  `presentation/final/`. It does not export or restyle decks, commit, or publish.
  Use `python3 -B scripts/sync-presentation-pdfs.py --check` to check equality
  without writing. See the [download notes](site/downloads/README.md).
- Writing preference: use as few headings and subheadings as possible. Remove
  explanatory text that merely repeats the surrounding interface. Exercise
  pages need one main idea, action steps, and prompts with task-specific inputs.

See [development](docs/development.md) for editing checks and
[deployment](docs/deployment.md) for GitHub Pages setup without a custom YAML
workflow. Publishing from the repository root includes other eligible tracked
files, so `site/` is an organizational folder rather than a publication filter.

Private preparation, original app variants, and agent working storage stay
local. Ignore rules do not untrack existing files or remove Git history.
