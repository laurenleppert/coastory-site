# coastory.app

The public website for Coastory, served by GitHub Pages at **https://coastory.app**.

- `/` — landing page (`index.html`, hand-written)
- `/get` — permanent QR download page; both store choices always available
- `/privacy` — Privacy Policy, rendered from the app repo
- `/terms` — Terms of Service, rendered from the app repo
- `/delete-account` — Google Play's required web account-deletion resource (hand-written)
- `/support` — Apple's required Support URL (hand-written)

## Assets

- The active home page uses genuine app captures from October 2026. The
  `profile-2026-10-29*` and `credit-2026-10-29*` images are the approved rider
  profile and Racer examples; matching light and dark captures are included.
  `meal-*-2026-10-29*` are real meal-plan screens, and the remaining images show
  live waits, ratings, and a selected Adventure timeline export. Preserve the
  identity and provenance of each capture when updating copy or images.
- `img/*-2026-09.jpg` are historical genuine captures of Coastory 0.9.3 (18),
  taken September 12, 2026. That older profile used Lauren's own Pixel profile
  with permission. The other older captures used an isolated fictional rider;
  the Rita and Alton Towers photos in them are CC0 1.0 by Christophe Badoux.
- The current Racer example was recreated through the app: Red and Blue are
  ridden and count together as one credit; Backwards is also recorded and counts
  as one more. Both credit choices belong to the sample rider.
- Previous `.webp` screenshots remain as historical assets. The social preview
  uses the same approved rider profile capture as the current home page.
  Reshoot actual screens when designs change; do not mock up replacement app UI
  or add personal rider data without permission.

- `img/og-launch-2026-11-10.jpg` — 1200x630 launch social preview, referenced
  by the Open Graph and Twitter card tags. Its editable source is `img/og.html`;
  render it through the local site server at a 1200x630 viewport and capture
  the full viewport.
  Regenerate it if the hero or availability wording changes, and use a new image filename
  when publishing so social services can fetch the updated preview.
- `img/mark.webp` — the 36px header wordmark icon. `icon.png` stays the favicon
  and apple-touch-icon (it must remain >=180px for iOS), so the header uses this
  small copy instead of shipping 36 KB for a 36-pixel image.
- `fonts/*.woff2` — Nunito and Fraunces, the app's own faces
  (`lib/core/theme/coastory_typography.dart`), subset to Latin plus the
  punctuation this site uses. Both are SIL OFL 1.1. They are what make the site
  read as the same product as the app, and they are preloaded on the landing
  page.

The homepage carries **no JavaScript at all**. Keep it that way. The focused `/get` route is a deliberate exception: `get/device.js` adds only a local device hint to highlight a store link. It performs no redirects, tracking, storage, or network calls; both download links work without JavaScript.

## Updating the legal pages

The **source of truth is the app repo**: `Coastory/docs/legal/privacy-policy.md` and
`terms-of-service.md`. Never edit `privacy/index.html` or `terms/index.html` by hand.

```bash
# from a checkout of this repo, with the app repo checked out beside it
python3 build.py                        # or: python3 build.py --source /path/to/Coastory/docs/legal
git add privacy/index.html terms/index.html
git commit -m "legal: re-render from Coastory <sha>"
```

Review and publish the legal commit separately from any held marketing changes.
GitHub Pages redeploys when `main` is pushed (about a minute). The render is dependency-free
(standard library only) so it is identical on any machine.

## Hosting

GitHub Pages, deploy-from-branch (`main`, root). `CNAME` pins the custom domain;
`.nojekyll` keeps Pages from running Jekyll over the files. `.app` is on the HSTS
preload list, so the domain must answer HTTPS on the first request — Pages does
this once "Enforce HTTPS" is on and the certificate has been issued.

DNS lives at Dynadot (see the CSTRY-420 notes in the app repo for the records).


## QR download page

Share **https://coastory.app/get**. GitHub Pages normalizes this directory route to `/get/`; direct visits and refreshes work without a client-side router. Keep the QR destination permanent and free of tracking parameters.

- `get/index.html`: self-contained download entry with the existing app identity and real sample-rider preview.
- `get/get.css`: scoped layout; shared colors and fonts come from `style.css`.
- `get/device.js`: iPhone/iPad and Android convenience hints; both links remain in a stable keyboard order and unknown devices receive equal choices. User-agent detection is a heuristic, never an access rule.
- `assets/badges/`: locally served, unmodified official store badges and provenance.
- `assets/qr/coastory-get.svg` and `.png`: print and digital QR assets; reproduction instructions in that directory.

No website analytics infrastructure was present when this page shipped. There is no page-view or click tracking, and no new tracking provider was added. The QR URL identifies the landing destination, not a particular card or visitor.

Verification (no package installation or site build needed):

```sh
node --check get/device.js
node --test tests/get-device.test.cjs
python3 -m py_compile build.py tools/generate_get_qr.py
python3 -m http.server 8774 --bind 127.0.0.1
```

Check `/get` and `/get/`, small/large phones and desktop, light/dark themes, visible keyboard focus, and both store links. The legal renderer remains a separate workflow: do not regenerate legal pages as part of a download-page change. Publish through this repository’s current Pages source after confirming its settings; do not import a different publishing script from an unpublished branch.
