# coastory.app

The public website for Coastory, served by GitHub Pages at **https://coastory.app**.

- `/` — landing page (`index.html`, hand-written)
- `/privacy` — Privacy Policy, rendered from the app repo
- `/terms` — Terms of Service, rendered from the app repo
- `/delete-account` — Google Play's required web account-deletion resource (hand-written)
- `/support` — Apple's required Support URL (hand-written)

## Assets

- `img/*.webp` — **real screenshots from the app**, captured on the iOS simulator
  (iPhone 17 Pro Max, 1320x2868, downscaled 50% to 660x1434) against a `dev_seed`
  persona. Never mock up a Coastory screen for this site: if a screenshot is out
  of date, take a new one. Capture notes (Play's 2:1 dimension rule, the DEBUG
  banner, demo mode) live in the app repo's session memory under
  `reference-capturing-store-screenshots`.

  **Which persona depends on the shot, so check the screen before reshooting.**
  `profile.webp` — the hero — is **Cass the Completionist**, not Globetrotter:
  it shows 197 credits and a Canada's Wonderland Top 3, and Globetrotter has
  neither. This line used to say Globetrotter for all of them, which would have
  sent a reshoot to the wrong persona.

  The hero's **Top 3 is picked by hand on the device before capture** — nothing
  seeds it. Coastory never derives a Top 3 from ratings and must not start; it
  is the rider's own choice. But a marketing shot should still not show a #1
  rated below a #3, which is exactly what a rider wrote in about on 2026-08-31
  (CSTRY-577). Pick three whose ratings descend. The current shot is Leviathan
  91 / Behemoth 87 / Kingda Ka 86, scrolled down slightly so the search button
  does not clip the third row's park name.
- `img/og.jpg` — 1200x630 social preview, referenced by the Open Graph and
  Twitter card tags. Regenerate it if the hero wording changes.
- `img/mark.webp` — the 36px header wordmark icon. `icon.png` stays the favicon
  and apple-touch-icon (it must remain >=180px for iOS), so the header uses this
  small copy instead of shipping 36 KB for a 36-pixel image.
- `fonts/*.woff2` — Nunito and Fraunces, the app's own faces
  (`lib/core/theme/coastory_typography.dart`), subset to Latin plus the
  punctuation this site uses. Both are SIL OFL 1.1. They are what make the site
  read as the same product as the app, and they are preloaded on the landing
  page.

The landing page carries **no JavaScript at all** and weighs ~283 KB with every
image loaded. Keep it that way: if a change needs a script, question the change.

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
