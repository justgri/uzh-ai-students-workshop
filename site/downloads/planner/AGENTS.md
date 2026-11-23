# Agent Instructions

## Purpose

This repository is a personal planner and knowledge base. Use it to plan,
prioritize, log progress and connect work across academic, professional,
hobby, personal and volunteering projects. Use fictional or explicitly
shareable details during the workshop.

## Canonical Files and Folders

- Planning horizons under `01-planning/`: `today.md`, `next-3-days.md`, `next-7-days.md` and `longer-term.md`.
- Project notes: `02-projects/<area>/<project-slug>/project.md`.
- Detailed project worklogs: `02-projects/<area>/<project-slug>/worklog.md`.
- Cross-project timeline: `03-worklogs/timeline.md`.
- Knowledge notes: `04-second-brain/<area>/`.
- Fast capture: `99-inbox/quick-capture.md`.
- Structure and navigation: `README.md` and `FILE-INDEX.md`.
- Session continuity: `HANDOFF.md`.
- Optional system rules and templates: `00-system/`.
- Optional local planner calendar: `01-planning/calendar.md`.
- Optional imported Google Calendar mirror: `01-planning/google-calendar.md`.

Reuse existing equivalent paths. Start small; do not create every optional
file or folder unless it is needed. Project notes are the source of truth;
plans and summaries link back to them.

## Areas and Projects

Use an area for an ongoing part of life and a project for a concrete outcome.
These are fictional examples, not commitments:

| Area | Example project | Example project note |
| --- | --- | --- |
| Academic | Course assignment | `02-projects/academic/course-assignment/project.md` |
| Professional | Internship search | `02-projects/professional/internship-search/project.md` |
| Hobbies | Weekend hiking trip | `02-projects/hobbies/weekend-trip/project.md` |
| Personal | Set up a weekly routine | `02-projects/personal/weekly-routine/project.md` |
| Volunteering | Student association event | `02-projects/probono/student-event/project.md` |

Adapt the areas to the user's needs. Give each project a goal, current state
and one next action. Keep related reference notes or drafts with their
project rather than creating a project for every small task.

## Operating Rules

1. Follow existing filenames, headings and templates. Keep `FILE-INDEX.md` current when files are added or moved, and give content folders a short README when useful.
2. Use ISO dates (`YYYY-MM-DD`) and 24-hour time. State the reference date, timezone and date windows when planning. Distinguish confirmed deadlines from suggested work dates.
3. Keep one `Next Tiny Step (<=15 min)` checkbox in every active project note.
4. Mark a task complete only when the user or a supplied source explicitly reports completion. A scheduled date or calendar entry does not prove completion.
5. Reflect completed work in the corresponding project worklog. Keep the cross-project timeline concise, with key outcomes and time spent only when reported.
6. Update a suitable existing file before creating a new one.
7. Keep plans realistic: at most three must-move outcomes per day, adjusted to the user's priorities and available time.
8. Never silently delete an unchecked plan item. Move deferred or superseded items to `Carry Forward`, `Active Backlog` or `Leftover / Superseded (Trace)`, with a timestamp and reason.
9. Preserve plan traceability: record the `from -> to` destination and timestamp for every removed or replaced unchecked item.
10. Preserve substantive, shareable user-pasted drafts or notes verbatim with a timestamp before summarizing them. If the destination is unclear, capture them in the relevant project worklog or inbox, then cross-link the eventual destination.
11. When a commitment changes, update its project note, affected planning views and the local planner calendar if one is already in use. Do not require an external calendar or an uninstalled skill.
12. Keep reported facts, proposals and open questions distinct. Ask about uncertainty that changes a commitment rather than inventing an owner, deadline, duration or completion status.

## Planning Protocol

When asked to update plans:

1. Read `01-planning/today.md`, the relevant horizon files and the project notes needed for the request.
2. Establish priorities and available time. Convert goals into concrete steps of 15 minutes or less where practical.
3. Preserve any substantive, shareable source notes before condensing them.
4. Before removing or replacing an unchecked item, record its destination, timestamp and reason in a trace entry.
5. Update the source project notes, then affected plans, the optional local planner calendar and corresponding worklogs.
6. Check that no unresolved checkbox disappeared without a destination, and show the user the changed files and open questions.

## Worklog Protocol

When asked to log work:

1. Append detailed updates to `02-projects/<area>/<project-slug>/worklog.md`, using `YYYY-MM-DD HH:MM` followed by a concise status line.
2. Record key decisions, explicitly completed steps, blockers and scope changes. Identify the source of the update.
3. Include trace entries for moved or superseded tasks. Link to any timestamped verbatim captures.
4. Add only a high-level summary to `03-worklogs/timeline.md`. Include a work time range or time split only when supplied; otherwise record the capture time.
5. If progress changes the project's status or next action, update `project.md` and affected plans.

When leaving a session handoff, keep `HANDOFF.md` brief: current priorities,
recent changes, open questions, the next action and links to source notes.

## Optional Calendar Context

- No calendar connection is required for this planner. Use calendar data only when requested and authorized.
- Google Calendar is read-only for agents. Never create, edit, move, delete, cancel, RSVP to, relabel or otherwise write events, calendars, sharing, settings or metadata, through any tool, script, connector, browser or delegated agent. Propose changes locally for the human to apply. Planning or syncing requests do not revoke this rule; changing it requires an explicit revision of the rule itself.
- Keep an imported Google Calendar mirror separate from the local planner calendar. An import is an observation, not a new commitment or evidence that work was completed. Do not automatically copy events into the planner calendar or write planner changes back to Google.
- Identify whether an answer uses live calendar data, a local mirror or the planner calendar. State a mirror's last-sync time and known coverage; preserve failed reads and unknown coverage as unknown rather than empty.
- If asked to refresh an existing mirror, retain cumulative coverage and append sync/change records. Never truncate earlier mirror history or sync-log entries.
- Do not claim that instructions or an approval setting enforce a technical read-only boundary. Never test the rule by attempting a live write.

## Data and Scope

- Keep workshop examples fictional or explicitly shareable. Do not import private planning or participant records into public examples.
- Never access Cryptomator Vaults, locked or unlocked, including alternate paths or copies. Never read EEG recordings, raw-signal exports, content in `EEG recording/` or station `manual-tests/` folders, or recording-derived results in folders whose names contain `human-only`. Do not request their contents. These boundaries apply to every tool and delegated agent.
- Preserve historical worklogs. Do not rename top-level folders, build an application, add automation, publish files or contact others without a request authorizing that action.
- If a local dashboard is requested, keep Markdown as the source of truth and make the view read-only. Workshop apps stay on localhost.

## Agent Working Files

- Keep project-specific helpers, intermediate data, previews, checks and outputs inside this repository. Never place them in operating-system temporary folders or another project.
- Before creating working files, verify their paths are Git-ignored; add narrow ignore rules when needed. Ignore rules do not untrack files or authorize publication.
- Use ordinary commands for trivial checks. Save nontrivial one-off logic and outputs in `.agent-work/scratch/<date>-<task>/`. After validation and a concise result note, remove only that task's clearly disposable agent-created files, unless a live follow-up still needs them. Silence or a number of follow-up messages alone is not a cleanup signal.
- Keep reusable local helpers in `.agent-work/reusable/<workflow>/`, with a short note covering inputs, outputs, command, dependencies and validation. Retain them until superseded or cleanup is requested. Exclude working storage from routine context searches.
- When a procedure is established and expected to recur, extend a suitable existing skill or keep a small skill and its scripts together in the repository-root `.agents/skills/<name>/`, with a complete, identical `.claude/skills/<name>/` mirror. Verify both local working folders are ignored before creating them. Do not create a skill for every one-off check.
- Intentional deliverables and maintained shared tooling may belong in `scripts/` or deliberately published shared skills. Do not blanket-ignore scripts, source extensions or deliverable folders.
- Automatic scratch cleanup never includes source inputs, user files, deliverables, worklogs, retained helpers or protected paths. Do not bulk-delete or migrate existing artifacts. Keep useful results in existing worklogs; a trivial check does not need a separate README.
