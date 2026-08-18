#!/usr/bin/env python3
"""Generate the 1200x630 OG share card for cnliu's site, matching the site's design."""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (6, 8, 12)
C1 = (34, 211, 238)    # cyan
C2 = (129, 140, 248)   # indigo
C3 = (52, 211, 153)    # green
C4 = (192, 132, 252)   # purple
TEXT = (233, 237, 244)
DIM = (141, 153, 170)
DARK = (92, 102, 117)

img = Image.new("RGB", (W, H), BG)

# ---------- soft glow blobs ----------
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
def blob(cx, cy, r, color, peak=42):
    steps = 60
    for i in range(steps, 0, -1):
        rr = r * i / steps
        a = int(peak * (1 - i / steps) ** 2)
        gd.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=color + (a,))
blob(120, 80, 420, C1, 26)
blob(1080, 500, 460, C2, 26)
blob(950, 60, 300, C4, 18)
img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")

# ---------- seismic traces ----------
tr_img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
td = ImageDraw.Draw(tr_img)
def trace(ybase, amp, f1, f2, color, alpha, qx=None):
    pts = []
    for x in range(0, W + 4, 4):
        y = ybase + math.sin(x * f1) * amp * .5 + math.sin(x * f2 + 2) * amp * .35
        if qx is not None:  # earthquake wave packet
            y += math.exp(-((x - qx) / 70) ** 2) * math.sin((x - qx) * .09) * amp * 2.2
        pts.append((x, y))
    td.line(pts, fill=color + (alpha,), width=3)
trace(95,  16, .010, .023, C1, 95, qx=430)
trace(315, 22, .008, .019, C2, 80, qx=980)
trace(555, 14, .012, .027, C3, 75, qx=250)
img = Image.alpha_composite(img.convert("RGBA"), tr_img).convert("RGB")

d = ImageDraw.Draw(img)

# ---------- fonts ----------
def load(paths, size, index=0):
    for p, idx in paths:
        try:
            return ImageFont.truetype(p, size, index=idx)
        except Exception:
            continue
    return ImageFont.load_default()

mono_paths  = [("/System/Library/Fonts/Menlo.ttc", 0)]
monob_paths = [("/System/Library/Fonts/Menlo.ttc", 1)]
bold_paths  = [("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 0),
               ("/System/Library/Fonts/Helvetica.ttc", 1),
               ("/System/Library/Fonts/SFNS.ttf", 0)]

f_kick = load(mono_paths, 30)
f_name = load(bold_paths, 94)
f_role = load(monob_paths, 40)
f_sub  = load(mono_paths, 26)
f_url  = load(mono_paths, 24)

LX = 84  # left margin

# ---------- kicker ----------
d.text((LX, 128), "$ whoami", font=f_kick, fill=C3)

# ---------- gradient name ----------
name = "Cheng-Nan Liu"
mask = Image.new("L", (W, H), 0)
md = ImageDraw.Draw(mask)
md.text((LX - 4, 192), name, font=f_name, fill=255)
bbox = md.textbbox((LX - 4, 192), name, font=f_name)
grad = Image.new("RGB", (W, H), BG)
gdr = ImageDraw.Draw(grad)
x0, x1 = bbox[0], bbox[2]
for x in range(x0, x1 + 1):
    p = (x - x0) / max(1, (x1 - x0))
    if p < .5:
        q = p / .5
        c = tuple(int(C1[i] + (C2[i] - C1[i]) * q) for i in range(3))
    else:
        q = (p - .5) / .5
        c = tuple(int(C2[i] + (C4[i] - C2[i]) * q) for i in range(3))
    gdr.line([(x, bbox[1] - 4), (x, bbox[3] + 4)], fill=c)
img.paste(grad, (0, 0), mask)

# ---------- role + sub ----------
d.text((LX, 336), "Machine Learning Engineer", font=f_role, fill=TEXT)
d.text((LX, 406), "large-scale time-series · low-SNR signal recovery", font=f_sub, fill=DIM)
d.text((LX, 444), "prev. X, The Moonshot Factory · Ph.D. Geophysics", font=f_sub, fill=DIM)

# ---------- url footer ----------
d.text((LX, 546), "~/cnliu $", font=f_url, fill=C3)
w_ps = d.textlength("~/cnliu $ ", font=f_url)
d.text((LX + w_ps + 6, 546), "andrewntu.github.io/cnliu_web", font=f_url, fill=DARK)

# ---------- circular photo with gradient ring ----------
photo = Image.open("cnliu_web/images/photo.jpg").convert("RGB")
pw, ph_ = photo.size
side = min(pw, ph_)
top = int((ph_ - side) * 0.52)  # bias crop toward the face
photo = photo.crop(((pw - side) // 2, top, (pw + side) // 2, top + side))
SZ = 280
SS = 4  # supersample for smooth circle
photo = photo.resize((SZ * SS, SZ * SS))
pmask = Image.new("L", (SZ * SS, SZ * SS), 0)
ImageDraw.Draw(pmask).ellipse([0, 0, SZ * SS - 1, SZ * SS - 1], fill=255)
photo_c = Image.new("RGBA", (SZ * SS, SZ * SS), (0, 0, 0, 0))
photo_c.paste(photo, (0, 0), pmask)
photo_c = photo_c.resize((SZ, SZ), Image.LANCZOS)

cx, cy, R = 1008, 288, SZ // 2 + 12
ring = Image.new("RGBA", (W * SS // 2, H * SS // 2), (0, 0, 0, 0))  # supersampled ring canvas
rd = ImageDraw.Draw(ring)
def lerp3(a, b, q):
    return tuple(int(a[i] + (b[i] - a[i]) * q) for i in range(3))
segs = 180
for s in range(segs):
    a0 = s * 360 / segs - 90
    a1 = (s + 1) * 360 / segs - 90 + 1
    p = s / segs
    col = lerp3(C1, C2, p * 2) if p < .5 else lerp3(C2, C4, (p - .5) * 2)
    rd.arc([(cx - R) * SS // 2, (cy - R) * SS // 2, (cx + R) * SS // 2, (cy + R) * SS // 2],
           a0, a1, fill=col + (255,), width=5 * SS // 2)
ring = ring.resize((W, H), Image.LANCZOS)
img = Image.alpha_composite(img.convert("RGBA"), ring).convert("RGB")
img.paste(photo_c, (cx - SZ // 2, cy - SZ // 2), photo_c)

img.save("cnliu_web/images/og-card.png", optimize=True)
print("saved", img.size)
