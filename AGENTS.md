# Agent instructions

## Project in brief

This repository contains materials for the **UZH.ai Students Association Agentic AI workshop**, held on **23 November 2026, 16:00–19:00 Europe/Zurich** at Zentrum. The user confirmed on November 24 that the workshop is over. Current work is materials maintenance; earlier preparation tasks below are history, not outstanding requests. This is a bounded, voluntary outreach project, separate from the instructor's PhD, Python course and PraxAI work. The audience was up to 30 students in teams of 2–3; no engineering background was required.

The current presentation labels are **think like a programmer** and **build personal web apps**, expressing the earlier engineering-habits and visual-inspection themes. The user's November 22 sequence is intro presentation → guided personal planner / gentle technical setup → open-ended research. Planner and research are core; the dashboard is an extension. Student apps stay on localhost, GitHub setup is homework and students do not deploy. A brief deployment example from the instructor's own repo may appear at the end. The practical timing split remains a proposal. Earlier prepared activities used the same example:

1. Create a personal-planning / second-brain repository with structured Markdown, agent instructions, a reviewed workflow pilot, a reference-skill demonstration and checks.
2. Build a read-only dashboard showing selected projects, files and text previews.
3. Earlier deployment activity: retained only as future reference; it is outside current student workshop work.

For the optional local dashboard, the proposed default is plain HTML/CSS/JavaScript; Streamlit is an alternative for prepared teams. GitHub Pages and Community Cloud are future hosting references, not workshop requirements. Preserve the three-hour scope, 30-minute kickoff and two-hour practical activity plus solutions-demo allocation as the workshop design record. The three final presentation versions are listed below. The earlier 20–25-slide target, 24-slide working outline and 42-slide content pass are planning history. Keep four separate presentation sections in both the website and slide deck: intro/motivation, intro to agent harness, agentic AI vocabulary, and tech vocabulary. Use slower live examples for each vocabulary section; do not group parts 3–4. Earlier pacing and support proposals do not establish new post-workshop work.

## Current presentation

**Final versions selected on 23 November; maintenance workflow revised by the user on 24 November 2026.** Keep exactly these three Keynote/PDF pairs and [README.md](presentation/final/README.md) in `presentation/final/`. The README explains builds, provenance and history. Preserve independent content/styles; synchronize only the requested versions.

| Website label | Final editable output | Public PDF used by the website |
| --- | --- | --- |
| Presentation (Original) | [Original Keynote](presentation/final/intro_agentic_ai.key) | [Original PDF](site/downloads/intro_agentic_ai.pdf) |
| Presentation (Codex-improved) | [Codex-improved Keynote](presentation/final/intro_agentic_ai_blue.key) | [Codex-improved PDF](site/downloads/intro_agentic_ai_blue.pdf) |
| Presentation (Claude-improved) | [Claude-improved Keynote](presentation/final/intro_agentic_ai_blue_columns.key) | [Claude-improved PDF](site/downloads/intro_agentic_ai_blue_columns.pdf) |

Matching final PDFs live beside each `.key` with the same stem. At cleanup, all three PDFs had 44 pages and matched their website copies byte-for-byte; the six final files were preserved without editing or re-export. A historical slide count is not a constraint on later requested edits. The website's Files section in `index.html` already contains exactly the three stable download links and labels above. `presentation/` remains ignored and is not a public download location.

### Editing sources and presentation sync

- The human edits and saves the plain white main presentation at [work/human/intro_agentic_ai.key](presentation/work/human/intro_agentic_ai.key). Keep **only this one Keynote** in `work/human/`. It was seeded from the latest final Original, not the older human-named snapshot.
- A request to **sync presentations** or **sync Original** copies the saved human master over `final/intro_agentic_ai.key` and exports that exact native content to `final/intro_agentic_ai.pdf`. It does not silently refresh styled variants.
- **Sync blue** reconciles the latest human content into the Codex design in `work/codex/`, then validates and overwrites the final `intro_agentic_ai_blue.key`/`.pdf` pair. **Sync blue_columns** does the equivalent in `work/claude/` for the final `intro_agentic_ai_blue_columns.key`/`.pdf` pair. Use the current corresponding final styled deck as the design baseline. Reconcile independent edits; preserve native text, notes, figures and links. Sync all three when explicitly requested.
- Export with Keynote and verify each changed pair before promotion. Keep transcripts, notes, revisions and other supporting files in the appropriate agent work folder, outside `final/`. Preserve open unsaved work. Do not replay historical builders or replace current content with an old snapshot/transcript.

### Website file sync

A separate request to **sync the website** copies and overwrites exactly the three `presentation/final/*.pdf` files above into their matching `site/downloads/` paths. Run `python3 scripts/sync-presentation-pdfs.py`; use `--check` for read-only equality verification. This does not export or restyle presentations. Presentation sync changes website files only when that is also requested. Committing, pushing and deploying still require authorization for those actions.

### Work organization and provenance

Agent-produced decks and their non-scratch work files live under [work/codex/](presentation/work/codex/) and [work/claude/](presentation/work/claude/). The Claude folder includes the separate Claude Artifacts PDF/project. Former extra final files are retained under `work/codex/final-history/`; earlier root-level white decks/PDFs are retained as source inputs under `work/codex/source-history/`, without changing their original authorship. The historical 42-slide Original transcript and supporting 44-slide blue transcript are in `final-history/`. Native final decks/PDFs take precedence over transcripts. The ready snapshot, handoffs, reviews, TODOs and older candidates are preparation history, not pending work. `presentation/presented/` remains an untouched snapshot; reference sources and images retain their existing folders.

Keep agent presentation work inside the corresponding `presentation/work/codex/` or `presentation/work/claude/` folder, the six final outputs and README in `presentation/final/`, website PDFs in `site/downloads/`, and selected reference images in `presentation/images/used/`. Reusable skill packages are the exception: complete Codex and Claude Code copies stay in repository-root skill folders. The user's slide-copy preference is concise, minimal text without colon-led labels.

For presentation tasks, put disposable scratch in `presentation/work/.agent-work/scratch/<date>-<task>/` and retained helpers in `presentation/work/.agent-work/reusable/<workflow>/`. These locations replace the repository-root `.agent-work/` defaults for presentation work. Apply the same file classification, ignore verification, usage-note and cleanup rules within this folder.

### Presentation design candidates and local skill

- `presentation/work/codex/intro_agentic_ai_blue.key` is the historical **Codex** design candidate.
- `presentation/work/claude/intro_agentic_ai_blue_columns.key` is the current **Claude Code** working copy. On 24 November, the user explicitly requested overwriting it from the final human-updated presented deck without rerunning the Claude design pipeline. Its matching working/final PDFs were natively refreshed; the older unversioned candidate is backed up in `presentation/work/.agent-work/scratch/2026-11-24-claude-human-updates/`. See the Claude design notes for the copy/export log; historical references calling this unversioned path a candidate predate that replacement.
- [Design provenance and preferences](presentation/work/codex/presentation-design-preferences.md) records the separate designs and the earlier provisional preference for Codex colors with Claude Code layout. Current design baselines are the corresponding final styled decks. Historical candidates are references, not replacement inputs.
- For creating/updating either design, load [local-keynote-design](.agents/skills/local-keynote-design/SKILL.md). It preserves each profile's colors, shades, layout and editing mechanics independently. Complete matching packages live in repository-root `.agents/skills/local-keynote-design/` and `.claude/skills/local-keynote-design/`.
- The candidates originated from a newer **39-slide native source** than the 38-slide original export/transcript. Use the current user-selected content source and reconcile changes; do not fix slide counts or replay the historical scratch builders as updaters.

## Repository-local skills

Owner rule, 23 November 2026: create skills in the **main repository root**, and always create/update mirrors for **both Codex and Claude Code**. Before creating, relocating or changing a repository skill, load [skill-authorization](.agents/skills/skill-authorization/SKILL.md) (also mirrored at `.claude/skills/skill-authorization/SKILL.md`).

Use `.agents/skills/<name>/` as the authoring copy and `.claude/skills/<name>/` as the complete, byte-identical mirror. Keep both as real directories, include supporting files, verify narrow ignore rules before creation, and validate/synchronize both before completion. Do not keep the actual package in a nested work folder or replace it with discovery symlinks. A local skill request covers its matching counterpart; it does not grant unrelated execution, protected-data access, global installation or Git/publication permissions.

## Planning sources

Read the relevant canonical document before changing material:

- [Project brief](admin/planning/project.md): scope, commitments, responsibilities and open decisions.
- [Workshop outline](admin/planning/workshop-outline.md): teaching framing, slides, agenda and demo.
- [Activity prompts](admin/planning/activity-prompts.md): student exercises, contracts and checkpoints.
- [Worklog](admin/planning/worklog.md): history and the user's original notes; preserve verbatim captures.

The [installation guide](admin/sources/installation_guide/installation_guide.md) is inherited course material to adapt, not an agreed workshop setup specification. Do not follow links into unrelated personal repositories as part of routine workshop preparation.

## Working conventions

- Keep explanations beginner-friendly and examples small, inspectable and reproducible. Prefer the agreed core path; keep advanced integrations and larger automation optional.
- Treat current explicit decisions as authoritative over older brainstorming. Distinguish proposals, prepared assets and verified results. Update canonical documents and add a concise worklog entry when materially changing the plan.
- Follow the user's current research progression (24 November): prove one case, learn from three, make a skill, use it on five new cases, compare observed research time per new case with the preceding iteration without a skill, then verify outputs, give feedback and update the skill. A larger pilot (the example uses 20), supported-reasoning comparison and bounded automation are optional extensions after review. The earlier client-lead progression remains a historical teaching example; its 1,000-lead run is conceptual. Never invent benchmark results or claim unobserved hook/deployment success.
- Check factual correctness against manually checked references and assess style/preferences separately. Record inputs, versions, commands and relevant checks so work can be reproduced.
- Use synthetic or explicitly shareable demonstration data. Keep real planning and participant records out of examples and public exports. Export only explicitly selected files. Markdown remains the source of truth for planning and workshop documentation; use the current presentation files above for deck content.
- Keep `admin/` ignored. Ignored files are not automatically safe to publish. Do not stage, commit, push, publish or contact others without authorization for that action.
- Keep project artifacts inside this repository. Before creating scratch files or local helpers, classify them and verify their paths with `git check-ignore`; add narrow ignore rules first if necessary. For presentation work, use the locations under `presentation/work/` specified above. For other tasks, use `.agent-work/scratch/<date>-<task>/` for disposable work and `.agent-work/reusable/<workflow>/` for retained helpers with a short usage note. Never use OS temporary directories. Reuse existing relevant helpers; remove only your own obsolete disposable files. Keep working storage out of routine context searches.

## Human-only boundaries

- **Cryptomator Vaults:** never access any Vault, locked or unlocked, including encrypted folders, mounted/decrypted copies, aliases and symlinks. Never list, inspect metadata, read, search, preview, decrypt, copy, modify, upload or log their contents, configuration or keys through any tool or delegated agent. Exclude them from parent searches; do not probe for mounts. Do not request access, passwords or pasted contents. A human alone handles Vault-sourced roster, roll-number, password and treatment-allocation reconciliation.
- **EEG recording data:** never access raw recordings, `*.xdf`, `*.xdf.*`, `*.xdfz`, other raw-signal exports, anything under `EEG recording/` or station `manual-tests/`, or recording-derived results in folders containing `human-only`. This includes every copy, archive and Git history. Never list, read, search, parse, hash, plot, summarize, copy, modify or upload them. For analysis work, write code using generated synthetic fixtures and provide one exact command for the researcher to run in a standalone terminal outside AI tools; never request or interpret recording-derived results, including pasted results. Technical logs, journals, checkpoints, manifests and marker backups remain usable subject to ID and secret rules.
- These boundaries apply across tools, connectors, skills and subagents. Instructions are behavioral policy, not proof of filesystem enforcement. Never test protections on real protected data; use synthetic paths. A guard block is final and must not be worked around.
