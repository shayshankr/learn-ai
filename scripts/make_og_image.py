"""Generates the social share card (assets/img/og-cover.png) used in <meta og:image>.
Run: python scripts/make_og_image.py
"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630
BG = (11, 14, 23)
ACCENT = (124, 140, 255)
ACCENT2 = (255, 124, 224)
ACCENT3 = (77, 230, 196)
TEXT = (238, 241, 251)
TEXT_DIM = (154, 164, 196)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img, "RGBA")

# soft radial-ish glow blobs (approximate with translucent circles)
def blob(cx, cy, r, color, alpha):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, alpha))
    overlay = overlay.filter(__import__("PIL.ImageFilter", fromlist=["ImageFilter"]).GaussianBlur(120))
    img.paste(Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB"), (0, 0))

blob(150, 80, 380, ACCENT, 60)
blob(1080, 200, 340, ACCENT2, 45)
blob(950, 560, 300, ACCENT3, 30)

draw = ImageDraw.Draw(img, "RGBA")

FONTS = "C:\\Windows\\Fonts"
title_font = ImageFont.truetype(os.path.join(FONTS, "segoeuib.ttf"), 78)
sub_font = ImageFont.truetype(os.path.join(FONTS, "segoeui.ttf"), 34)
pill_font = ImageFont.truetype(os.path.join(FONTS, "seguisb.ttf"), 24)
brand_font = ImageFont.truetype(os.path.join(FONTS, "segoeuib.ttf"), 30)

# brand row: logo dot + wordmark
dot_x, dot_y, dot_r = 80, 90, 22
draw.rounded_rectangle([dot_x, dot_y, dot_x + dot_r * 2, dot_y + dot_r * 2], radius=12, fill=ACCENT)
draw.text((dot_x + dot_r * 2 + 16, dot_y - 3), "Learn AI", font=brand_font, fill=TEXT)

# pill badge
pill_text = "FREE  ·  NO SIGN-UP  ·  8 INTERACTIVE LESSONS"
pill_box = draw.textbbox((0, 0), pill_text, font=pill_font)
pw, ph = pill_box[2] - pill_box[0], pill_box[3] - pill_box[1]
px, py = 80, 190
pad_x, pad_y = 22, 12
draw.rounded_rectangle([px, py, px + pw + pad_x * 2, py + ph + pad_y * 2], radius=999, outline=(38, 46, 70), width=2, fill=(19, 24, 38))
draw.text((px + pad_x, py + pad_y - 2), pill_text, font=pill_font, fill=ACCENT)

# title
draw.text((78, 250), "Learn AI, one 10-minute", font=title_font, fill=TEXT)
draw.text((78, 340), "lesson at a time.", font=title_font, fill=TEXT)

# subtitle
draw.text((80, 460), "A free, interactive course teaching chatbots, prompt engineering,", font=sub_font, fill=TEXT_DIM)
draw.text((80, 505), "coding assistants, image gen, agents, and using AI responsibly.", font=sub_font, fill=TEXT_DIM)

# url footer
url_font = ImageFont.truetype(os.path.join(FONTS, "seguisb.ttf"), 26)
draw.text((80, 565), "shayshankr.github.io/learn-ai", font=url_font, fill=ACCENT3)

os.makedirs("assets/img", exist_ok=True)
img.save("assets/img/og-cover.png", optimize=True)
print("saved assets/img/og-cover.png", img.size)
