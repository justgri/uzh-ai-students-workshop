# Agent instructions

## Project in brief

This repository prepares the **UZH.ai Students Association Agentic AI workshop**, planned for **23 November 2026, 16:00–19:00 Europe/Zurich** at Zentrum. It is a bounded, voluntary outreach project, separate from the instructor's PhD, Python course and PraxAI work. The audience is up to 30 students in teams of 2–3; no engineering background is required.

The current presentation labels are **think like a programmer** and **build personal web apps**, expressing the earlier engineering-habits and visual-inspection themes. The user's November 22 sequence is intro presentation → guided personal planner / gentle technical setup → open-ended research. Planner and research are core; the dashboard is an extension. Student apps stay on localhost, GitHub setup is homework and students do not deploy. A brief deployment example from the instructor's own repo may appear at the end. The practical timing split remains a proposal. Earlier prepared activities used the same example:

1. Create a personal-planning / second-brain repository with structured Markdown, agent instructions, a reviewed workflow pilot, a reference-skill demonstration and checks.
2. Build a read-only dashboard showing selected projects, files and text previews.
3. Earlier deployment activity: retained only as future reference; it is outside current student workshop work.

For the optional local dashboard, the proposed default is plain HTML/CSS/JavaScript; Streamlit is an alternative for prepared teams. GitHub Pages and Community Cloud are future hosting references, not workshop requirements. Preserve the three-hour scope, 30-minute kickoff and two-hour practical activity plus solutions-demo allocation. The two final presentation versions are listed below. The earlier 20–25-slide target, 24-slide working outline and 42-slide content pass are planning history. Keep four separate presentation sections in both the website and slide deck: intro/motivation, intro to agent harness, agentic AI vocabulary, and tech vocabulary. Use slower live examples for each vocabulary section; do not group parts 3–4. Detailed pacing, route and support assignments remain proposals until agreed.

## Current presentation

**Final paths, explicitly selected by the user on 23 November 2026.** All three versions below are final workshop presentations. Preserve their independent content and slide counts; do not synchronize or restyle them without a new request.

| Website label | Authoritative editable source | Public PDF used by the website |
| --- | --- | --- |
| Presentation (Original) | [Original Keynote](presentation/final/intro_agentic_ai.key) | [Original PDF](site/downloads/intro_agentic_ai.pdf) |
| Presentation (Codex-improved) | [Codex-improved Keynote](presentation/final/intro_agentic_ai_blue.key) | [Codex-improved PDF](site/downloads/intro_agentic_ai_blue.pdf) |
| Presentation (Claude-improved) | [Claude-improved Keynote](presentation/final/intro_agentic_ai_blue_columns.key) | [Claude-improved PDF](site/downloads/intro_agentic_ai_blue_columns.pdf) |

The PDFs were freshly exported from these exact native sources in Keynote on November 23: 44 slides in each version. Matching local PDF copies live beside the decks at `presentation/final/intro_agentic_ai.pdf`, `presentation/final/intro_agentic_ai_blue.pdf` and `presentation/final/intro_agentic_ai_blue_columns.pdf`. The Claude-improved source is a copy of `presentation/work/intro_agentic_ai_blue_columns_2026-11-23.key`, restyled from the final original saved at 15:35 (see its [design notes](presentation/work/intro_agentic_ai_blue_columns_notes.md)). The user renamed the former "Presentation (AI-improved)" label to "Presentation (Codex-improved)" on 23 November. After any explicitly requested future deck update, re-export from the relevant authoritative source and keep its public PDF and local copy byte-identical. The website's Files section in `index.html` contains exactly the three download links and labels above. Keep these stable paths; `presentation/` remains ignored and is not a public download location.

Inspect the current native sources and matching PDFs for final content. The original 42-slide `presentation/final/intro_agentic_ai_transcript.md` is historical and has not been regenerated for the final export. The 44-slide `presentation/final/intro_agentic_ai_blue_transcript.md` is a supporting text reference; native sources and their freshly exported PDFs take precedence if a transcript differs. The ready snapshot, earlier decks under `presentation/` and `presentation/work/`, Claude Artifacts PDF, slide-change notes, styling handoff, pre-workshop review and presentation TODOs are preparation history; they do not override the final sources or establish remaining requested work. Never overwrite a final source with an earlier snapshot or export. Planning documents still govern workshop scope and commitments.

Keep general presentation work inside `presentation/work/`, final editable decks and matching local exports in `presentation/final/`, public presentation PDFs in `site/downloads/`, and selected reference images in `presentation/images/used/`. Reusable skill packages are another exception: the user's root-skill rule below puts their complete Codex and Claude Code copies in the repository-root skill folders. Update current-file links when a new version becomes authoritative. The user's slide-copy preference is concise, minimal text without colon-led labels.

For presentation tasks, put disposable scratch in `presentation/work/.agent-work/scratch/<date>-<task>/` and retained helpers in `presentation/work/.agent-work/reusable/<workflow>/`. These locations replace the repository-root `.agent-work/` defaults for presentation work. Apply the same file classification, ignore verification, usage-note and cleanup rules within this folder.

### Presentation design candidates and local skill

- `presentation/work/intro_agentic_ai_blue.key` is the **Codex** design candidate.
- `presentation/work/intro_agentic_ai_blue_columns.key` is the **Claude Code** design candidate.
- These work-folder candidates are historical. [Design provenance and preferences](presentation/work/presentation-design-preferences.md) records the separate designs and the earlier provisional preference for Codex colors with Claude Code layout. The final Codex-improved source is now `presentation/final/intro_agentic_ai_blue.key`, and the final Claude-improved source is `presentation/final/intro_agentic_ai_blue_columns.key`. Do not substitute any work-folder candidate for them.
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
- Follow the user's progression: prove one case, review five, benchmark a larger pilot (the example uses 20), compare supported reasoning settings, then package a validated skill before scaling. The 1,000-lead example is conceptual. Never invent benchmark results or claim unobserved hook/deployment success.
- Check factual correctness against manually checked references and assess style/preferences separately. Record inputs, versions, commands and relevant checks so work can be reproduced.
- Use synthetic or explicitly shareable demonstration data. Keep real planning and participant records out of examples and public exports. Export only explicitly selected files. Markdown remains the source of truth for planning and workshop documentation; use the current presentation files above for deck content.
- Keep `admin/` ignored. Ignored files are not automatically safe to publish. Do not stage, commit, push, publish or contact others without authorization for that action.
- Keep project artifacts inside this repository. Before creating scratch files or local helpers, classify them and verify their paths with `git check-ignore`; add narrow ignore rules first if necessary. For presentation work, use the locations under `presentation/work/` specified above. For other tasks, use `.agent-work/scratch/<date>-<task>/` for disposable work and `.agent-work/reusable/<workflow>/` for retained helpers with a short usage note. Never use OS temporary directories. Reuse existing relevant helpers; remove only your own obsolete disposable files. Keep working storage out of routine context searches.

## Human-only boundaries

- **Cryptomator Vaults:** never access any Vault, locked or unlocked, including encrypted folders, mounted/decrypted copies, aliases and symlinks. Never list, inspect metadata, read, search, preview, decrypt, copy, modify, upload or log their contents, configuration or keys through any tool or delegated agent. Exclude them from parent searches; do not probe for mounts. Do not request access, passwords or pasted contents. A human alone handles Vault-sourced roster, roll-number, password and treatment-allocation reconciliation.
- **EEG recording data:** never access raw recordings, `*.xdf`, `*.xdf.*`, `*.xdfz`, other raw-signal exports, anything under `EEG recording/` or station `manual-tests/`, or recording-derived results in folders containing `human-only`. This includes every copy, archive and Git history. Never list, read, search, parse, hash, plot, summarize, copy, modify or upload them. For analysis work, write code using generated synthetic fixtures and provide one exact command for the researcher to run in a standalone terminal outside AI tools; never request or interpret recording-derived results, including pasted results. Technical logs, journals, checkpoints, manifests and marker backups remain usable subject to ID and secret rules.
- These boundaries apply across tools, connectors, skills and subagents. Instructions are behavioral policy, not proof of filesystem enforcement. Never test protections on real protected data; use synthetic paths. A guard block is final and must not be worked around.
