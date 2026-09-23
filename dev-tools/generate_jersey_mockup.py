#!/usr/bin/env python3
"""Generates the placeholder jersey mockup for the Merch page: a flat, light-blue
athletic tee with the Arrow Athletics mark and a 'YOUR TEAM NAME HERE' placeholder,
plus a diagonal "Coming Soon" ribbon. Swap this file out once real product photos
of the jersey exist -- see merch.html / page_merch() in build.py."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 950
NAVY = (1, 27, 70)
NAVY_SOFT = (6, 44, 99)
BLUE = (0, 89, 252)
LIGHT_BLUE_TOP = (203, 230, 255)
LIGHT_BLUE_BOTTOM = (158, 205, 248)
WHITE = (255, 255, 255)

FONT_DIR = "/mnt/skills/examples/canvas-design/canvas-fonts"


def font(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGBA", (W, H), (0, 0, 0, 0))

# ---------- ground shadow ----------
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(shadow).ellipse((350, 800, 850, 855), fill=(1, 27, 70, 55))
shadow = shadow.filter(ImageFilter.GaussianBlur(22))
img.alpha_composite(shadow)

# ---------- t-shirt silhouette (clockwise) ----------
tee_points = [
    (530, 255), (600, 310), (670, 255),    # collar / neck dip
    (745, 245),                             # right shoulder
    (855, 265), (845, 355),                 # right sleeve outer top -> bottom
    (735, 350),                             # right armpit
    (760, 780), (440, 780),                 # hem right -> hem left
    (465, 350),                             # left armpit
    (355, 355), (345, 265),                 # left sleeve outer bottom -> top
    (455, 245),                             # left shoulder
]

grad = Image.new("RGB", (1, H), (0, 0, 0))
for y in range(H):
    t = y / H
    rgb = tuple(round(LIGHT_BLUE_TOP[i] + (LIGHT_BLUE_BOTTOM[i] - LIGHT_BLUE_TOP[i]) * t) for i in range(3))
    grad.putpixel((0, y), rgb)
grad = grad.resize((W, H))

mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask).polygon(tee_points, fill=255)
tee_fill = Image.new("RGBA", (W, H), (0, 0, 0, 0))
tee_fill.paste(grad.convert("RGBA"), (0, 0), mask)
img.alpha_composite(tee_fill)

# subtle fold shadow on the right half only
shade = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ImageDraw.Draw(shade).polygon(
    [(600, 310), (670, 255), (745, 245), (855, 265), (845, 355), (735, 350), (760, 780), (600, 780)],
    fill=(1, 27, 70, 26),
)
shade_mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(shade_mask).polygon(tee_points, fill=255)
shade_out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
shade_out.paste(shade, (0, 0), shade_mask)
img.alpha_composite(shade_out)

draw = ImageDraw.Draw(img)
draw.line(tee_points + [tee_points[0]], fill=NAVY_SOFT + (255,), width=6, joint="curve")
draw.line([(600, 330), (600, 775)], fill=(255, 255, 255, 55), width=3)

# collar rib
draw.arc((525, 265, 675, 385), start=15, end=165, fill=NAVY + (255,), width=12)
draw.arc((525, 265, 675, 385), start=15, end=165, fill=BLUE + (255,), width=4)

# ---------- logo mark on the chest ----------
mark = Image.open("images/mark.png").convert("RGBA")
mark_w = 220
mark_h = round(mark.height * mark_w / mark.width)
mark_resized = mark.resize((mark_w, mark_h), Image.LANCZOS)
mark_x = (W - mark_w) // 2
mark_y = 420
img.alpha_composite(mark_resized, (mark_x, mark_y))

# ---------- "YOUR TEAM NAME HERE" jersey lettering ----------
draw = ImageDraw.Draw(img)
team_font = font(f"{FONT_DIR}/BigShoulders-Bold.ttf", 48)
text = "YOUR TEAM NAME HERE"
spacing = 4
widths = [draw.textlength(ch, font=team_font) for ch in text]
total_w = sum(widths) + spacing * (len(text) - 1)
x = (W - total_w) / 2
y = 555
for ch, wch in zip(text, widths):
    draw.text((x, y), ch, font=team_font, fill=NAVY + (255,))
    x += wch + spacing

sub_font = font(f"{FONT_DIR}/BigShoulders-Regular.ttf", 28)
sub = "YOUR NAME HERE"
sw = draw.textlength(sub, font=sub_font)
draw.text(((W - sw) / 2, 618), sub, font=sub_font, fill=NAVY_SOFT + (215,))

# ---------- "Coming Soon" ribbon ----------
ribbon = Image.new("RGBA", (520, 140), (0, 0, 0, 0))
rd = ImageDraw.Draw(ribbon)
rd.rectangle((0, 40, 520, 100), fill=BLUE + (255,))
ribbon_font = font(f"{FONT_DIR}/BigShoulders-Bold.ttf", 42)
rtext = "COMING SOON"
rw = rd.textlength(rtext, font=ribbon_font)
rd.text(((520 - rw) / 2, 49), rtext, font=ribbon_font, fill=WHITE + (255,))
ribbon = ribbon.rotate(-32, expand=True, resample=Image.BICUBIC)
img.alpha_composite(ribbon, (W - ribbon.width + 55, -45))

img.save("images/merch-jersey.png")
print("wrote images/merch-jersey.png", img.size)
