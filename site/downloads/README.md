# Public workshop downloads

The website's Files section contains exactly three final presentation downloads,
selected by the user on 23 November 2026:

| Label | Public PDF | Final PDF copied to the website |
| --- | --- | --- |
| Presentation (Original) | [intro_agentic_ai.pdf](intro_agentic_ai.pdf) | `presentation/final/intro_agentic_ai.pdf` |
| Presentation (Codex-improved) | [intro_agentic_ai_blue.pdf](intro_agentic_ai_blue.pdf) | `presentation/final/intro_agentic_ai_blue.pdf` |
| Presentation (Claude-improved) | [intro_agentic_ai_blue_columns.pdf](intro_agentic_ai_blue_columns.pdf) | `presentation/final/intro_agentic_ai_blue_columns.pdf` |

The workshop exports selected on 23 November contain 44 slides each. Keep the
filenames and labels stable. The human editing master is
`presentation/work/human/intro_agentic_ai.key`; agent working versions live in
`presentation/work/codex/` and `presentation/work/claude/`. Requested
presentation syncs update the selected final Keynote/PDF pairs. Provenance and
build instructions live in `presentation/final/README.md`. These local
presentation folders are ignored and are not website download locations.

To sync the website, run `python3 -B scripts/sync-presentation-pdfs.py` from the
repository root. It checks all three final source PDFs before overwriting the
three files here and verifies equal bytes. Use
`python3 -B scripts/sync-presentation-pdfs.py --check` for a read-only check.
Website sync copies existing final PDFs; it does not export, restyle, commit,
push, or deploy.

Links in root `index.html` start with `./site/downloads/`. The unused scaffold
placeholder Markdown files have been removed.

Every file in this directory is intended to be public. Do not copy private
planning or participant records into it.
