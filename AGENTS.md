# Agent instructions

## Project in brief

This repository prepares the **UZH.ai Students Association Agentic AI workshop**, planned for **23 November 2026, 16:00–19:00 Europe/Zurich** at Zentrum. It is a bounded, voluntary outreach project, separate from the instructor's PhD, Python course and PraxAI work. The audience is up to 30 students in teams of 2–3; no engineering background is required.

The two teaching messages are **think like a software engineer** and **visualize agent work**. Three connected activities use the same example:

1. Create a personal-planning / second-brain repository with structured Markdown, agent instructions, a reviewed workflow pilot, a reference-skill demonstration and checks.
2. Build a read-only dashboard showing selected projects, files and text previews.
3. Deploy the demonstration and verify that a source update reaches the live view.

The proposed default is plain HTML/CSS/JavaScript with GitHub Pages; Streamlit with Community Cloud is an alternative for prepared teams. Preserve the three-hour scope, 30-minute / 15-slide kickoff and two-hour practical activity plus solutions-demo allocation. Detailed pacing, route and support assignments remain proposals until agreed.

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
- Use synthetic or explicitly shareable demonstration data. Keep real planning and participant records out of examples and public exports. Export only explicitly selected files; Markdown remains the source of truth.
- Keep `admin/` ignored. Ignored files are not automatically safe to publish. Do not stage, commit, push, publish or contact others without authorization for that action.
- Keep project artifacts inside this repository. Before creating scratch files or local helpers, classify them and verify their paths with `git check-ignore`; add narrow ignore rules first if necessary. Use `.agent-work/scratch/<date>-<task>/` for disposable work and `.agent-work/reusable/<workflow>/` for retained helpers with a short usage note. Never use OS temporary directories. Reuse existing relevant helpers; remove only your own obsolete disposable files. Keep working storage out of routine context searches.

## Human-only boundaries

- **Cryptomator Vaults:** never access any Vault, locked or unlocked, including encrypted folders, mounted/decrypted copies, aliases and symlinks. Never list, inspect metadata, read, search, preview, decrypt, copy, modify, upload or log their contents, configuration or keys through any tool or delegated agent. Exclude them from parent searches; do not probe for mounts. Do not request access, passwords or pasted contents. A human alone handles Vault-sourced roster, roll-number, password and treatment-allocation reconciliation.
- **EEG recording data:** never access raw recordings, `*.xdf`, `*.xdf.*`, `*.xdfz`, other raw-signal exports, anything under `EEG recording/` or station `manual-tests/`, or recording-derived results in folders containing `human-only`. This includes every copy, archive and Git history. Never list, read, search, parse, hash, plot, summarize, copy, modify or upload them. For analysis work, write code using generated synthetic fixtures and provide one exact command for the researcher to run in a standalone terminal outside AI tools; never request or interpret recording-derived results, including pasted results. Technical logs, journals, checkpoints, manifests and marker backups remain usable subject to ID and secret rules.
- These boundaries apply across tools, connectors, skills and subagents. Instructions are behavioral policy, not proof of filesystem enforcement. Never test protections on real protected data; use synthetic paths. A guard block is final and must not be worked around.
