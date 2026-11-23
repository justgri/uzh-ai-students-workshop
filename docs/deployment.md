# GitHub Pages deployment

This repository uses a root `index.html` with supporting files under `site/`.
No custom YAML workflow, package installation, or local build step is required.
Scaffolding the files does not enable Pages or publish the repository.

## Configure Pages

After the approved public files have been committed and pushed by an
authorized operator:

1. Open the GitHub repository's **Settings → Pages**.
2. Set **Source** to **Deploy from a branch**.
3. Choose the publishing branch, normally **main**, and **/(root)**.
4. Save, wait for deployment to complete, and follow the returned site URL.

GitHub runs the deployment internally even though this repository does not
provide its own workflow YAML.

## Default Pages processing

Branch-based Pages publishing uses GitHub's default Jekyll processing. The
website is plain HTML, CSS, and JavaScript, with no local build step or custom
workflow to maintain.

## Public files and ignored storage

Keep `index.html`, `site/`, `docs/`, and shared repository
instructions eligible for Git tracking. Keep `admin/`, `apps/`, `.agent-work/`,
secrets, environments, and caches local and ignored.

Root publishing has a broader scope than publishing only `site/`: other
eligible files in the publishing root can also be served. Everything pushed
to a public GitHub repository is accessible through GitHub as well.
Ignore rules do not untrack existing files or erase earlier commits. Review
the selected public files and existing history before the first public push.

## Verify publication

Open Intro and all four supporting pages directly, then follow their navigation.
Check the shared stylesheet, prompt copying on each exercise page, and all three
final presentation PDFs linked from Files: Presentation (Original),
Presentation (Codex-improved) and Presentation (Claude-improved).
For a project URL such as `https://OWNER.github.io/REPOSITORY/`, the stylesheet
is at `site/assets/styles.css` below that URL. Relative links keep the
repository path intact.

Replace the placeholder content with approved workshop materials before
sharing. Make one small visible source update, publish it, and confirm it
appears at the live URL. Do not claim deployment is verified until observed.

## References

- [GitHub: publishing sources](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [GitHub: creating a Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)
