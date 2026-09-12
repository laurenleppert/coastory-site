# coastory.app

The public website for Coastory, served by GitHub Pages at **https://coastory.app**.

- `/` — landing page (`index.html`, hand-written)
- `/privacy` — Privacy Policy, rendered from the app repo
- `/terms` — Terms of Service, rendered from the app repo
- `/delete-account` — Google Play's required web account-deletion resource (hand-written)
- `/support` — Apple's required Support URL (hand-written)

## Assets

- `img/*-2026-09.jpg` are genuine captures of Coastory 0.9.3 (18), taken
  September 12, 2026. The hero uses Lauren’s own Pixel profile with her permission.
  Its native capture is 1206x2410 and the website copy is 660x1319. No rider photos
  appear on that profile screen.
- The other five captures use the fictional Cass the Completionist sample in a
  fresh, isolated iPhone 17 Pro Max simulator. Native 1320x2868 captures are
  downscaled to 660x1434. The screenshot build uses source `675274fe` with only the
  debug banner hidden. Store apps and Lauren’s personal profiles were preserved.
  Demo status bars show 9:41 and a full battery; temporary overrides are cleared
  after each capture. JPEG conversion and proportional resizing are the only
  post-processing. The website displays each screenshot in full.
- The Racer example was recreated through the app: Red and Blue ridden, counted
  together once, and Backwards experienced but recorded in history only. This adds
  one credit after the milestone capture, so the two sample totals differ by one.
- Photo provenance: the Rita and Alton Towers photographs are **CC0 1.0** by
  Christophe Badoux, dated August 16, 2012, verified on Wikimedia Commons:
  [Rita (Alton Towers).JPG](https://commons.wikimedia.org/wiki/File:Rita_(Alton_Towers).JPG)
  and [Castle Alton Towers.JPG](https://commons.wikimedia.org/wiki/File:Castle_Alton_Towers.JPG).
  They were added only to the isolated sample account. Rita’s framing uses the
  app’s own cover controls. Never pair an unrelated sample photo with a named ride.
- Previous `.webp` screenshots remain as historical assets, no longer referenced
  by the landing page. Reshoot actual screens when designs change; do not mock up
  replacement app UI. Use Lauren’s profile only for the profile shot, and fictional
  data with verified image sources for the remaining shots.

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

The landing page carries **no JavaScript at all**. Keep it that way: if a change needs a script, question the change.

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
