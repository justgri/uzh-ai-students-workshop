# Development

## Preview

From the repository root:

```sh
python3 -B -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000/> and stop the server with Ctrl+C when finished.
The page also opens as a local HTML file. Clipboard access is intended for
HTTPS or localhost; manual selection remains available when copying fails.

## Edit the pages

Intro content lives in `index.html`. The four other pages are `site/tech.html`,
`site/basics.html`, `site/planner.html`, and `site/research.html`. Appearance
lives in `site/assets/styles.css`; prompt-copy behavior lives in
`site/assets/script.js`. The HTML files are the maintained source; no generator
or build step is needed to edit them.

The shared header and Intro hero use `site/assets/uzh-ai-students-logo.svg`.
It retains the supplied association artwork with a horizontal 825 × 274
viewport. Preserve its aspect ratio and artwork when resizing it.

Use as few headings and subheadings as possible. Remove sentences that merely
restate adjacent content, navigation, or controls. Keep explanations only when
they help the participant make a decision or take an action. Exercise pages
lead with one main idea, then action steps and prompts with bracketed inputs.

Keep the five navigation links and the current-page marker consistent. Root
links to a supporting page begin `./site/`; links between supporting pages use
`./`, and links back to Intro use `../index.html`.

Prompt text belongs directly inside its textarea. New prompt cards need unique
heading and textarea IDs, and the copy button's `data-copy-target` must match
the textarea ID. Escape literal `&` and `<` characters as `&amp;` and `&lt;`
when inserting them into HTML, including inside textareas.

## Add downloads

Put public PDFs, guides, and examples in `site/downloads/`. Keep runnable
examples and their instructions in `site/downloads/code/`. Maintain a single
source copy of each script. Add a file link in `index.html` with a relative
link such as `./site/downloads/presentation.pdf` after the file exists.

Keep a written guide's Markdown source beside its PDF export when both are
shared. Do not add empty PDFs or links to materials that are not present yet.
See the [download notes](../site/downloads/README.md).

## Check changes

- Check desktop and phone widths, browser zoom, and visible keyboard focus.
- Follow all five navigation links from both the root and supporting pages,
  and check every download link. Each page must open directly at its own URL.
- Check all copy buttons on localhost or HTTPS. Check manual selection when
  clipboard access is unavailable and with JavaScript disabled.
- Check relative links below a repository URL path as well as at `/`.
- Confirm that only approved public materials will be published.

Keep local checks, previews, and scratch outputs inside the ignored
`.agent-work/` directory. Agent activity remains subject to `AGENTS.md`; this
document does not grant access to private or human-only material.

## Content references

Setup and terminology were checked against official sources on 2026-11-21:

- [Claude downloads](https://claude.com/download) and [pricing](https://claude.com/pricing).
- [Codex](https://openai.com/codex/), [ChatGPT Plus](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus), and [Codex plan access](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan).
- [Git](https://git-scm.com/install), [VS Code](https://code.visualstudio.com/download), and [Python](https://www.python.org/downloads/).
- [Codex instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [skills](https://learn.chatgpt.com/docs/build-skills), and [hooks](https://learn.chatgpt.com/docs/hooks).
- [Claude instructions](https://code.claude.com/docs/en/memory#agentsmd), [skills](https://code.claude.com/docs/en/skills), and [hooks](https://code.claude.com/docs/en/hooks-guide).

The roughly US$20/month plan is the workshop baseline; local prices and usage
limits vary. Codex also has free-plan access. Python is for workshop scripts,
not a prerequisite for every harness. Instruction and skill lookup follows the
selected harness; writing an instruction does not configure or activate a hook.
