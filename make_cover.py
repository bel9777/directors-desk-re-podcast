"""Generate 1400x1400 Apple Podcasts cover art for Director's Desk: Institutional Real Estate."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

S = 1400
FOREST = "#13302B"
BRASS = "#E0A458"
CREAM = "#F7F4EE"

img = Image.new("RGB", (S, S), FOREST)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, S, 48], fill=BRASS)
d.rectangle([0, S - 48, S, S], fill=BRASS)
d.rectangle([110, 810, S - 110, 822], fill=BRASS)

fonts = Path(r"C:\Windows\Fonts")
serif = str(fonts / "georgiab.ttf")
sans = str(fonts / "segoeuib.ttf")
sans_reg = str(fonts / "segoeui.ttf")


def fit(text, font_path, start, max_w):
    size = start
    while size > 36:
        f = ImageFont.truetype(font_path, size)
        if d.textlength(text, font=f) <= max_w:
            return f
        size -= 4
    return f


f_tag = fit("DAILY CRE & PORTFOLIO MASTERY", sans, 54, S - 220)
d.text((S / 2, 210), "DAILY CRE & PORTFOLIO MASTERY", font=f_tag, fill=BRASS, anchor="mm")

f1 = fit("DIRECTOR'S", serif, 210, S - 200)
d.text((S / 2, 470), "DIRECTOR'S", font=f1, fill=CREAM, anchor="mm")

f2 = fit("DESK", serif, 230, S - 220)
d.text((S / 2, 680), "DESK", font=f2, fill=CREAM, anchor="mm")

f3 = fit("INSTITUTIONAL REAL ESTATE", sans, 66, S - 200)
d.text((S / 2, 955), "INSTITUTIONAL REAL ESTATE", font=f3, fill=CREAM, anchor="mm")

f4 = fit("DEALS · GOVERNANCE · ASC 842", sans_reg, 48, S - 240)
d.text((S / 2, 1080), "DEALS · GOVERNANCE · ASC 842", font=f4, fill=BRASS, anchor="mm")

out = Path(__file__).resolve().parent / "docs" / "cover.png"
out.parent.mkdir(parents=True, exist_ok=True)
img.save(out)
print("wrote", out)
