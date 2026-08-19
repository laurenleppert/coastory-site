# coastory.app

The public website for Coastory, served by GitHub Pages at **https://coastory.app**.

- `/` — landing page (`index.html`, hand-written)
- `/privacy` — Privacy Policy, rendered from the app repo
- `/terms` — Terms of Service, rendered from the app repo

## Updating the legal pages

The **source of truth is the app repo**: `Coastory/docs/legal/privacy-policy.md` and
`terms-of-service.md`. Never edit `privacy/index.html` or `terms/index.html` by hand.

```bash
# from a checkout of this repo, with the app repo checked out beside it
python3 build.py                        # or: python3 build.py --source /path/to/Coastory/docs/legal
git add -A && git commit -m "legal: re-render from Coastory <sha>" && git push
```

GitHub Pages redeploys on push (about a minute). The render is dependency-free
(standard library only) so it is identical on any machine.

## Hosting

GitHub Pages, deploy-from-branch (`main`, root). `CNAME` pins the custom domain;
`.nojekyll` keeps Pages from running Jekyll over the files. `.app` is on the HSTS
preload list, so the domain must answer HTTPS on the first request — Pages does
this once "Enforce HTTPS" is on and the certificate has been issued.

DNS lives at Dynadot (see the CSTRY-420 notes in the app repo for the records).
