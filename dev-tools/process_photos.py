#!/usr/bin/env python3
"""Process real match photography into the web-ready files the site
references: 12 gallery photos, the home hero background, and the About-page
story image. Not run as part of a normal build — the processed output is
already committed in images/. Re-run this only when swapping in new photos:
drop full-resolution originals in dev-tools/photo_sources/ (not tracked in
the repo, since raw exports run tens of MB) using the filenames below, or
edit GALLERY to point at whatever you named them."""
from PIL import Image, ImageOps
import os

SRC_DIR = "dev-tools/photo_sources"
OUT_DIR = "images/gallery"
os.makedirs(OUT_DIR, exist_ok=True)

# gallery number -> source file (drop your originals in dev-tools/photo_sources/
# using these names, or edit the filenames to match whatever you have)
GALLERY = {
    1: "boy-red-strike.jpg",         # boy in red, striking the ball
    2: "boys-huddle-kneeling.jpg",   # boys' team huddle
    3: "girls-action-maroon.jpg",    # girls' match action
    4: "boys-chase-wing.jpg",        # two boys racing for the ball
    5: "girls-throw-in.jpg",         # girls' throw-in
    6: "boys-team-photo-lights.jpg", # team photo under lights
    7: "boy-stripes-shot.jpg",       # boy striking a shot, stripes kit
    8: "ball-closeup.jpg",           # ball close-up on grass
    9: "midfield-challenge.jpg",     # midfield challenge
    10: "matchday-open-field.jpg",   # open-field match action
    11: "boys-huddle-portrait.jpg",  # boys' huddle, portrait (also About-page source)
    12: "wide-match-action.jpg",     # wide match action (also hero source)
}

GALLERY_MAX = 1500  # longest side, px


def load(name):
    im = Image.open(os.path.join(SRC_DIR, name))
    im = ImageOps.exif_transpose(im)  # phones store orientation in EXIF, not pixels
    return im.convert("RGB")


def resize_max(im, max_side):
    if max(im.size) <= max_side:
        return im
    ratio = max_side / max(im.size)
    return im.resize((round(im.width * ratio), round(im.height * ratio)), Image.LANCZOS)


def crop_to_ratio(im, ratio):
    """Centre-crop to a target width/height ratio without distorting."""
    w, h = im.size
    target_w = h * ratio
    if target_w <= w:
        x0 = (w - target_w) / 2
        return im.crop((round(x0), 0, round(x0 + target_w), h))
    target_h = w / ratio
    y0 = (h - target_h) / 2
    return im.crop((0, round(y0), w, round(y0 + target_h)))


# ---- gallery photos ----
for n, name in GALLERY.items():
    im = resize_max(load(name), GALLERY_MAX)
    path = os.path.join(OUT_DIR, f"gallery-{n}.jpg")
    im.save(path, "JPEG", quality=84, optimize=True)
    print("wrote", path, im.size)

# ---- home hero background (wide match action, cropped to a cinematic band) ----
hero = load(GALLERY[12])
hero = crop_to_ratio(hero, 16 / 8.2)
hero = resize_max(hero, 2400)
hero.save("images/hero.jpg", "JPEG", quality=82, optimize=True)
print("wrote images/hero.jpg", hero.size)

# ---- About page / home "our story" image (team huddle) ----
# The source is a tall portrait with a lot of empty sky above the team and a
# blurred foreground below; crop that down to the huddle itself (roughly the
# middle 50% of the frame, vertically) before resizing.
about = load(GALLERY[11])
w, h = about.size
about = about.crop((0, round(h * 0.30), w, round(h * 0.80)))
about = resize_max(about, 1500)
about.save("images/about.jpg", "JPEG", quality=85, optimize=True)
print("wrote images/about.jpg", about.size)
