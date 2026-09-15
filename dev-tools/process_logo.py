#!/usr/bin/env python3
"""Turn the supplied Arrow Athletics logo into the asset variants the site needs:
full-colour lockup, white knockout for dark backgrounds, and the arrow mark alone."""
from PIL import Image
import os

SRC = "/root/.claude/uploads/e0ef2a2c-cc71-5f83-8871-646b06e1982f/76b75e8c-image.png"
OUT = "images"
os.makedirs(OUT, exist_ok=True)

NAVY = (1, 27, 70)
BLUE = (0, 89, 252)

ALPHA_FLOOR = 24   # the source art carries faint near-transparent noise; ignore it


def solid_alpha(img):
    """Alpha channel with near-transparent noise knocked out."""
    return img.getchannel("A").point(lambda v: 255 if v > ALPHA_FLOOR else 0)


def trim(img):
    box = solid_alpha(img).getbbox()
    return img.crop(box) if box else img


im = Image.open(SRC).convert("RGBA")
im = trim(im)
print("trimmed lockup:", im.size)

def save(img, name, width=None):
    if width:
        h = max(1, round(img.height * width / img.width))
        img = img.resize((width, h), Image.LANCZOS)
    img.save(os.path.join(OUT, name))
    print("wrote", name, img.size)

# ---------- 1. Full-colour lockup (for light backgrounds) ----------
save(im, "logo.png", 900)

# ---------- 2. White knockout (navy -> white, blue kept) ----------
def knockout(img):
    out = img.copy()
    px = out.load()
    for y in range(out.height):
        for x in range(out.width):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            # distance to each brand colour decides which part of the mark this is
            dn = (r - NAVY[0]) ** 2 + (g - NAVY[1]) ** 2 + (b - NAVY[2]) ** 2
            db = (r - BLUE[0]) ** 2 + (g - BLUE[1]) ** 2 + (b - BLUE[2]) ** 2
            if dn <= db:
                px[x, y] = (255, 255, 255, a)          # navy -> white
            else:
                px[x, y] = (77, 143, 255, a)           # blue -> lifted blue for contrast
    return out

white = knockout(im)
save(white, "logo-white.png", 900)

# ---------- 3. Arrow mark on its own (for the favicon) ----------
# The arrowhead tip runs right up against the "A" of ARROW, so there is no empty
# column to split on. The pinch point between them is the column carrying the
# fewest painted pixels, so split there.
alpha = solid_alpha(im)
occupancy = []
for x in range(int(im.width * 0.33), int(im.width * 0.52)):
    col = alpha.crop((x, 0, x + 1, im.height))
    occupancy.append((sum(col.point(lambda v: 1 if v else 0).getdata()), x))

split = min(occupancy)[1]
print(f"mark/wordmark pinch point at x = {split} ({split / im.width:.0%} across)")

mark = trim(im.crop((0, 0, split, im.height)))
save(mark, "mark.png", 400)
save(knockout(mark), "mark-white.png", 400)

# ---------- 4. Favicon: mark centred on navy, square ----------
size = 512
fav = Image.new("RGBA", (size, size), NAVY + (255,))
m = knockout(mark)
scale = int(size * 0.72)
h = max(1, round(m.height * scale / m.width))
m = m.resize((scale, h), Image.LANCZOS)
fav.alpha_composite(m, ((size - scale) // 2, (size - h) // 2))
fav.convert("RGB").save(os.path.join(OUT, "favicon.png"))
fav.resize((180, 180), Image.LANCZOS).convert("RGB").save(os.path.join(OUT, "apple-touch-icon.png"))
print("wrote favicon.png / apple-touch-icon.png")
