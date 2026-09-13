#!/usr/bin/env python3
"""Generate placeholder brand imagery for the Arrow Cup site.
These are stand-ins so the site looks finished; swap in real photos later."""
import math
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

random.seed(42)

NAVY = (13, 27, 58)
NAVY_DARK = (8, 17, 38)
ORANGE = (245, 98, 46)
ORANGE_LIGHT = (255, 138, 76)
PINK = (224, 65, 123)
BLUE = (46, 134, 245)
WHITE = (255, 255, 255)
CREAM = (250, 247, 240)

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def diagonal_gradient(w, h, c1, c2, angle_bias=1.0):
    img = Image.new("RGB", (w, h), c1)
    px = img.load()
    for y in range(h):
        for x in range(0, w, 2):
            t = ((x / w) * 0.5 + (y / h) * 0.5) ** angle_bias
            color = lerp(c1, c2, t)
            px[x, y] = color
            if x + 1 < w:
                px[x + 1, y] = color
    return img

def add_ball_pattern(img, count, seed_offset=0):
    draw = ImageDraw.Draw(img, "RGBA")
    w, h = img.size
    rnd = random.Random(seed_offset)
    for _ in range(count):
        r = rnd.randint(18, 60)
        x = rnd.randint(-r, w + r)
        y = rnd.randint(-r, h + r)
        alpha = rnd.randint(10, 26)
        draw.ellipse([x - r, y - r, x + r, y + r], outline=(255, 255, 255, alpha), width=3)
    return img

def get_font(size, bold=True):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            continue
    return ImageFont.load_default()

def caption_card(w, h, c1, c2, title, subtitle, tag, tag_color, outpath, angle_bias=1.0, seed=0):
    # Clean gradient background only — no baked-in text/chip, since every
    # page already overlays its own tag + caption in HTML. Baking text in
    # here caused duplicated/cropped captions once object-fit:cover cropped
    # these images to a different aspect ratio per placement.
    img = diagonal_gradient(w, h, c1, c2, angle_bias)
    img = add_ball_pattern(img, 14, seed)
    img = img.filter(ImageFilter.GaussianBlur(0.4))

    # subtle bottom scrim so any future overlay text stays legible
    scrim_h = int(h * 0.35)
    scrim = Image.new("RGBA", (w, scrim_h), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(scrim)
    for i in range(scrim_h):
        a = int(90 * (i / scrim_h))
        sdraw.line([(0, i), (w, i)], fill=(6, 12, 26, a))
    img.paste(scrim, (0, h - scrim_h), scrim)

    img.convert("RGB").save(outpath, quality=88)
    print("wrote", outpath)

# ---- Gallery images (800x600) ----
gallery_specs = [
    ("gallery-1.jpg", NAVY, ORANGE, "Opening Whistle", "Arrow Cup Kickoff Weekend", "ARROW CUP", ORANGE, 1.0, 1),
    ("gallery-2.jpg", (120, 20, 60), PINK, "Girls U14 Final", "Championship Saturday", "GIRLS", PINK, 0.8, 2),
    ("gallery-3.jpg", NAVY_DARK, BLUE, "Boys U12 Match Day", "Group Stage, Field 3", "BOYS", BLUE, 1.2, 3),
    ("gallery-4.jpg", (30, 60, 40), (90, 200, 130), "Skills Clinic", "Summer Training Camp", "TRAINING", (60, 160, 100), 0.9, 4),
    ("gallery-5.jpg", (90, 20, 90), PINK, "Girls U16 Semifinal", "Under the Lights", "GIRLS", PINK, 1.1, 5),
    ("gallery-6.jpg", NAVY, BLUE, "Boys U10 Kickoff", "First Goals of the Season", "BOYS", BLUE, 0.85, 6),
    ("gallery-7.jpg", (120, 60, 10), ORANGE_LIGHT, "Team Huddle", "Pregame Traditions", "ARROW CUP", ORANGE, 1.0, 7),
    ("gallery-8.jpg", NAVY_DARK, (150, 60, 160), "Trophy Presentation", "Closing Ceremony", "ARROW CUP", (150, 60, 160), 0.95, 8),
]
for fname, c1, c2, title, sub, tag, tagc, ab, seed in gallery_specs:
    caption_card(800, 600, c1, c2, title, sub, tag, tagc, f"images/gallery/{fname}", ab, seed)

# ---- Blog thumbnails (900x520) ----
blog_specs = [
    ("blog-1.jpg", NAVY, ORANGE, "Registration Is Open", "2026 Arrow Cup Season", "NEWS", ORANGE, 1.0, 11),
    ("blog-2.jpg", (90, 20, 90), PINK, "5 Tips Before Tryouts", "Girls & Boys Divisions", "TIPS", PINK, 0.9, 12),
    ("blog-3.jpg", NAVY_DARK, BLUE, "Meet the Coaches", "Building Our 2026 Staff", "COMMUNITY", BLUE, 1.1, 13),
]
for fname, c1, c2, title, sub, tag, tagc, ab, seed in blog_specs:
    caption_card(900, 520, c1, c2, title, sub, tag, tagc, f"images/blog/{fname}", ab, seed)

# ---- Hero image (1600x900) ----
hero = diagonal_gradient(1600, 900, NAVY_DARK, NAVY, 1.0)
hero = add_ball_pattern(hero, 40, 99)
hero.save("images/hero.jpg", quality=90)
print("wrote images/hero.jpg")

# ---- About page image (1200x800) ----
about_img = diagonal_gradient(1200, 800, (20, 40, 80), ORANGE, 0.9)
about_img = add_ball_pattern(about_img, 24, 55)
about_img.save("images/about.jpg", quality=88)
print("wrote images/about.jpg")

print("done")
