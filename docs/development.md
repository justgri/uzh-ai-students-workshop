# Development

## Preview

From the repository root:

```sh
python3 -B -m http.server 8000 --bind 127.0.0.1
```

Open <http://127.0.0.1:8000/> and stop the server with Ctrl+C when finished.
The page also opens as a local HTML file. Clipboard access is intended for
HTTPS or localhost; manual selection remains available when copying fails.

## Edit the page

Page content lives in `index.html`; appearance lives in
`site/assets/styles.css`; prompt-copy behavior lives in `site/assets/script.js`.
Keep the draft notice until the placeholders have been replaced and reviewed.

Prompt text belongs directly inside its textarea. New prompt cards need unique
heading and textarea IDs, and the copy button's `data-copy-target` must match
the textarea ID. Escape literal `&` and `<` characters as `&amp;` and `&lt;`
when inserting them into HTML, including inside textareas.

## Add downloads

Put public PDFs, guides, and examples in `site/downloads/`. Keep runnable
examples and their instructions in `site/downloads/code/`. Maintain a single
source copy of each script. Add a download card in `index.html` with a relative
link such as `./site/downloads/presentation.pdf` after the file exists.

Keep a written guide's Markdown source beside its PDF export when both are
shared. Do not add empty PDFs or links to materials that are not present yet.
See the [download notes](../site/downloads/README.md).

## Check changes

- Check desktop and phone widths, browser zoom, and visible keyboard focus.
- Follow the navigation and every download link.
- Check all copy buttons on localhost or HTTPS. Check manual selection when
  clipboard access is unavailable and with JavaScript disabled.
- Check relative links below a repository URL path as well as at `/`.
- Confirm that only approved public materials will be published.

Keep local checks, previews, and scratch outputs inside the ignored
`.agent-work/` directory. Agent activity remains subject to `AGENTS.md`; this
document does not grant access to private or human-only material.
