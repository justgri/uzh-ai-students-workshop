---
name: personal-planner-operator
description: Maintain a local Markdown personal planner, including planning horizons, daily priorities, small next actions, worklogs and linked project notes. Use for planning and capturing updates, not coding or software implementation.
---

# Personal Planner Operator

Operate the student's planner as a calm, low-overwhelm planning system. Use fictional or explicitly shareable exercise details.

## Read first

- Read the planner's existing `AGENTS.md` or `CLAUDE.md`, `README.md` and `FILE-INDEX.md` where present.
- Follow the planner's own taxonomy and templates if they exist; do not require the instructor's `00-system/` folder.
- Open only the project notes, plans and worklog relevant to the request. Respect all project access restrictions.
- Use [references/checklists.md](references/checklists.md) for daily planning, worklog updates and weekly reviews.

## Adapt to the planner

Resolve paths relative to the student's planner root. Reuse existing equivalents before creating new files. The exercise's example paths are:

| Purpose | Example path |
| --- | --- |
| Project notes, the source of truth | `02-projects/<category>/<project>/project.md` |
| Today | `01-planning/today.md` |
| Next three days | `01-planning/next-3-days.md` |
| Next seven days | `01-planning/next-7-days.md` |
| Longer term | `01-planning/longer-term.md` |
| Cumulative worklog | `03-worklogs/timeline.md` |
| Reference notes | `04-second-brain/` |
| Unsorted captures | `99-inbox/` |
| Session handoff | `HANDOFF.md` |

Do not rebuild the folder structure to match this table. Link actions to existing project IDs or stable project-note paths.

## Workflow

1. Identify the requested scope: planning, project update, worklog or knowledge capture. Read the canonical notes for that scope.
2. For planning, establish the reference date, local timezone, priorities and available time. State the date windows. Distinguish confirmed deadlines and appointments from suggested work dates; leave unknown dates uncertain. Propose at most three daily outcomes unless the user requests otherwise.
3. Update existing project notes before refreshing affected planning views. Keep each action small, concrete and linked to its project. Give each active project one `Next Tiny Step (<=15 min)`.
4. Mark completion only when the supplied update explicitly supports it. Never silently delete unchecked tasks: move deferred or superseded items to `Carry Forward`, `Active Backlog` or `Leftover / Superseded (Trace)`, recording the timestamp, reason and `from -> to` destination.
5. Preserve substantive, shareable user draft text verbatim in a timestamped project note or worklog before summarizing it. Preserve earlier logs and separate reported facts from suggestions and open questions.
6. Append a concise worklog entry with the source of the update, project link, what changed and next action. Use a supplied time range when available; otherwise record the capture time without inventing a work duration.
7. Refresh affected plans and update `FILE-INDEX.md` when files move or are created. Update `HANDOFF.md` when asked to leave a session handoff. Show the changed files and any unresolved questions.

## Access and scope

- This skill describes a local Markdown workflow. Installing it does not authorize running every step, contacting people, Git publication or external changes. It has no dependency on another calendar skill or on the instructor's planner.
- Calendar access is optional. Google Calendar is strictly read-only: keep any approved local mirror separate and propose changes locally. Never infer task completion from a calendar entry.
- Never access Cryptomator Vaults, locked or unlocked, through any path or tool. Never read EEG recordings, raw-signal exports, files in `EEG recording/` or station `manual-tests/` folders, or recording-derived results in folders whose names contain `human-only`. Do not request their contents.
- Keep project-specific helpers and outputs inside the planner's ignored `.agent-work/` folder, following its instructions. Do not write project artifacts to operating-system temporary folders.
