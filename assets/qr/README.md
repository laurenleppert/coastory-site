# Coastory download QR

Both assets encode **exactly** `https://coastory.app/get` with no tracking parameters. Use the SVG for print, cards, and Wallet artwork; use the PNG where a raster image is required. Keep the included white margin intact and avoid resizing the PNG with smoothing.

- QR Code Model 2, Version 3, error correction H
- Black modules on white; four-module quiet zone on every side
- PNG: 2,220 × 2,220 pixels, 60 pixels per module

To regenerate from the site repository root, install `segno==1.6.6` in a development virtual environment and run `python tools/generate_get_qr.py`. Segno is only a generation tool; the published site has no dependency on it. After regeneration, scan the PNG with an independent QR decoder and verify the exact URL before distributing it.
