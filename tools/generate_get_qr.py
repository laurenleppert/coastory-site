"""Generate the print-ready Coastory /get QR assets.

Run from the site repository root with Segno 1.6.6 installed:
    python tools/generate_get_qr.py
"""

from pathlib import Path

import segno


URL = "https://coastory.app/get"
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "qr"
BORDER_MODULES = 4
PNG_MODULE_SCALE = 60


def main() -> None:
    qr = segno.make(URL, error="h", micro=False, boost_error=False)
    if qr.version != 3 or qr.error != "H":
        raise RuntimeError(f"Unexpected QR format: version {qr.version}, {qr.error}")

    OUTPUT.mkdir(parents=True, exist_ok=True)
    qr.save(
        OUTPUT / "coastory-get.svg",
        kind="svg",
        border=BORDER_MODULES,
        dark="#000000",
        light="#ffffff",
        xmldecl=True,
        omitsize=True,
    )
    qr.save(
        OUTPUT / "coastory-get.png",
        kind="png",
        scale=PNG_MODULE_SCALE,
        border=BORDER_MODULES,
        dark="#000000",
        light="#ffffff",
    )
    width, height = qr.symbol_size(scale=PNG_MODULE_SCALE, border=BORDER_MODULES)
    print(f"{URL} | version {qr.version} | ECC {qr.error} | "
          f"quiet zone {BORDER_MODULES} modules | PNG {width}x{height}")


if __name__ == "__main__":
    main()
