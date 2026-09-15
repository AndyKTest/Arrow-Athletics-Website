#!/usr/bin/env python3
"""Generate the site's brand imagery: angular sports-graphic panels built from the
Arrow Athletics logo palette and its speed-shard motif.

These are designed to look like intentional brand art, not 'missing photo' boxes,
so the site looks finished until real match photography is dropped in.
Replace any file in images/gallery/ or images/blog/ with a real photo of the same
name and the site picks it up with no code changes."""
import math
import os
import random
from PIL import Image, ImageDraw, ImageFilter

OUT = "images"
os.makedirs(f"{OUT}/gallery", exist_ok=True)
os.makedirs(f"{OUT}/blog", exist_ok=True)

NAVY_DEEP = (2, 13, 38)
NAVY = (1, 27, 70)
NAVY_MID = (6, 40, 99)
BLUE = (0, 89, 252)
BLUE_LIFT = (77, 143, 255)
WHITE = (255, 255, 255)

SS = 2  # supersample factor


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def base_gradient(w, h, c1, c2, diagonal=True):
    """Smooth two-tone base, drawn small then scaled up (fast + band-free)."""
    small = Image.new("RGB", (64, 64))
    px = small.load()
    for y in range(64):
        for x in range(64):
            t = ((x / 63) * 0.55 + (y / 63) * 0.45) if diagonal else (y / 63)
            px[x, y] = lerp(c1, c2, t)
    return small.resize((w, h), Image.BICUBIC)


def shard(draw, x, y, length, width, angle_deg, color):
    """A long, thin triangle — the speed-streak shape from the logo."""
    a = math.radians(angle_deg)
    dx, dy = math.cos(a), math.sin(a)
    px_, py_ = -dy, dx
    tip = (x + dx * length, y + dy * length)
    b1 = (x + px_ * width / 2, y + py_ * width / 2)
    b2 = (x - px_ * width / 2, y - py_ * width / 2)
    draw.polygon([b1, tip, b2], fill=color)


def shard_field(layer, w, h, seed, density=7, hue=BLUE, angle=-24):
    d = ImageDraw.Draw(layer, "RGBA")
    rnd = random.Random(seed)
    for _ in range(density):
        L = rnd.randint(int(w * 0.35), int(w * 0.95))
        W = rnd.randint(int(h * 0.02), int(h * 0.10))
        x = rnd.randint(int(-w * 0.15), int(w * 0.75))
        y = rnd.randint(int(h * 0.05), int(h * 0.95))
        a = rnd.uniform(0, 1)
        col = hue + (rnd.randint(28, 80),) if a > 0.32 else WHITE + (rnd.randint(14, 30),)
        shard(d, x, y, L, W, angle + rnd.uniform(-5, 5), col)


def pitch_lines(layer, w, h, alpha=22):
    """Soccer pitch geometry as faint line work."""
    d = ImageDraw.Draw(layer, "RGBA")
    col = WHITE + (alpha,)
    lw = max(2, int(h * 0.006))
    cx, cy = int(w * 0.5), int(h * 0.5)
    r = int(h * 0.30)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=lw)
    d.line([(cx, 0), (cx, h)], fill=col, width=lw)
    d.ellipse([cx - lw * 2, cy - lw * 2, cx + lw * 2, cy + lw * 2], fill=col)
    bw, bh = int(w * 0.16), int(h * 0.46)
    d.rectangle([0, cy - bh // 2, bw, cy + bh // 2], outline=col, width=lw)
    d.rectangle([w - bw, cy - bh // 2, w, cy + bh // 2], outline=col, width=lw)
    ar = int(h * 0.10)
    d.arc([-ar, -ar, ar, ar], 0, 90, fill=col, width=lw)
    d.arc([w - ar, h - ar, w + ar, h + ar], 180, 270, fill=col, width=lw)


def halftone(layer, w, h, seed, alpha_max=46, hue=BLUE):
    d = ImageDraw.Draw(layer, "RGBA")
    step = max(12, int(h / 26))
    for gy in range(0, h + step, step):
        for gx in range(0, w + step, step):
            t = 1 - (gx / w * 0.65 + gy / h * 0.35)
            if t <= 0.02:
                continue
            rad = step * 0.42 * t
            if rad < 0.7:
                continue
            a = int(alpha_max * t)
            d.ellipse([gx - rad, gy - rad, gx + rad, gy + rad], fill=hue + (a,))


def net_mesh(layer, w, h, alpha=20):
    d = ImageDraw.Draw(layer, "RGBA")
    col = WHITE + (alpha,)
    step = max(18, int(h / 16))
    for i in range(-h, w + h, step):
        d.line([(i, 0), (i + h, h)], fill=col, width=2)
        d.line([(i, h), (i + h, 0)], fill=col, width=2)


def mark_watermark(canvas, w, h, scale=0.85, pos="right", alpha=34):
    """The arrow mark itself, oversized and faded, bleeding off an edge."""
    path = f"{OUT}/mark-white.png"
    if not os.path.exists(path):
        return
    m = Image.open(path).convert("RGBA")
    tw = int(w * scale)
    th = max(1, round(m.height * tw / m.width))
    m = m.resize((tw, th), Image.LANCZOS)
    a = m.getchannel("A").point(lambda v: int(v * alpha / 255))
    m.putalpha(a)
    x = int(w * 0.30) if pos == "right" else int(-w * 0.12)
    canvas.alpha_composite(m, (x, (h - th) // 2))


def vignette(canvas, w, h, strength=90):
    v = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(v)
    d.ellipse([-w * 0.35, -h * 0.5, w * 1.35, h * 1.5], fill=strength)
    v = v.filter(ImageFilter.GaussianBlur(int(min(w, h) * 0.12)))
    dark = Image.new("RGBA", (w, h), NAVY_DEEP + (255,))
    inv = v.point(lambda p: 255 - p)
    dark.putalpha(inv.point(lambda p: int(p * 0.55)))
    canvas.alpha_composite(dark)


def build(style, w, h, seed, out, flip=False):
    W, H = w * SS, h * SS
    if style in ("blue", "blue-mark"):
        base = base_gradient(W, H, NAVY, BLUE)
    elif style == "deep":
        base = base_gradient(W, H, NAVY_DEEP, NAVY_MID)
    else:
        base = base_gradient(W, H, NAVY_DEEP, NAVY)
    canvas = base.convert("RGBA")

    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if style in ("pitch", "deep"):
        pitch_lines(layer, W, H, alpha=26)
    if style == "halftone":
        halftone(layer, W, H, seed, hue=BLUE_LIFT)
    if style == "mesh":
        net_mesh(layer, W, H, alpha=18)
    canvas.alpha_composite(layer)

    if style in ("mark", "blue-mark"):
        mark_watermark(canvas, W, H, scale=0.95, pos="right", alpha=40)

    shards = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shard_field(shards, W, H, seed, density=8 if style != "mesh" else 5,
                hue=BLUE_LIFT if style in ("deep", "pitch") else BLUE)
    canvas.alpha_composite(shards)

    vignette(canvas, W, H)

    img = canvas.convert("RGB").resize((w, h), Image.LANCZOS)
    if flip:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img.save(out, quality=90, optimize=True)
    print("wrote", out)


# ---- Hero + section imagery ----
build("blue-mark", 1920, 1080, 1, f"{OUT}/hero.jpg")
build("pitch", 1200, 800, 2, f"{OUT}/about.jpg")

# ---- Gallery: eight distinct compositions ----
gallery = [
    ("mark", 11, False), ("pitch", 12, False), ("blue", 13, True), ("halftone", 14, False),
    ("deep", 15, True), ("mesh", 16, False), ("blue-mark", 17, False), ("pitch", 18, True),
]
for i, (style, seed, flip) in enumerate(gallery, start=1):
    build(style, 1000, 750, seed, f"{OUT}/gallery/gallery-{i}.jpg", flip)

# ---- Blog thumbnails ----
blogs = [("blue", 21, False), ("halftone", 22, True), ("deep", 23, False)]
for i, (style, seed, flip) in enumerate(blogs, start=1):
    build(style, 1000, 560, seed, f"{OUT}/blog/blog-{i}.jpg", flip)

print("done")
