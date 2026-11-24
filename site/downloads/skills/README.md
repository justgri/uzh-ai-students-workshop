# Planner skill template

[Personal Planner Operator](personal-planner-operator/SKILL.md) is the reference
skill for the Planner exercise. Its complete package has two files:

```text
personal-planner-operator/
├── SKILL.md
└── references/
    └── checklists.md
```

Read both files before using it. Copy the complete folder into your planner's
`.agents/skills/` for Codex or `.claude/skills/` for Claude Code, then ask your
agent to adapt the example paths to your existing planner. Keep the source
repository URL and commit SHA with your installed copy so you can identify
the version you used. Try it on fictional projects and inspect the changes.

The [downloadable ZIP](personal-planner-operator.zip) contains both files. Rebuild
it from the exported package whenever either file changes.

Adapted on 23 November 2026 from the instructor's `personal-planner-operator`
skill. The planning workflow and checklists are retained; instructor-specific
system folders and the mandatory `master-calendar` skill dependency are
replaced with the exercise's local Markdown paths. The template includes no
personal planner records and requires no calendar connection.

Maintainers: edit the repository-root `.agents/skills/personal-planner-operator/`
authoring copy and keep the complete `.claude/skills/personal-planner-operator/`
mirror byte-identical, as required by the repository instructions. Those
working packages are ignored. Deliberately export only their reviewed
`SKILL.md` and `references/checklists.md` here; compare all three packages and
run the skill validator before publishing an update. This public copy is an
exercise resource, not a skill installed in the student's planner.
