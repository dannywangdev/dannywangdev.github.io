from PIL import Image, ImageDraw, ImageFont
import os, math

WIDTH, HEIGHT = 1200, 630

img = Image.new("RGB", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)

# dark metallic blue background with wormhole ripple effect
cx, cy = WIDTH // 2, HEIGHT // 2
for y in range(HEIGHT):
    for x in range(WIDTH):
        dx = x - cx
        dy = y - cy
        dist = math.sqrt(dx * dx + dy * dy)
        angle = math.atan2(dy, dx)

        # wormhole ripple
        ripple = math.sin(dist * 0.03 - angle * 3) * 0.5 + 0.5
        pulse = math.sin(dist * 0.015 + 2.0) * 0.3 + 0.7
        falloff = max(0, 1.0 - dist / 1000)

        r = int((10 + ripple * 25 + pulse * 15) * falloff)
        g = int((40 + ripple * 60 + pulse * 50) * falloff)
        b = int((80 + ripple * 90 + pulse * 70) * falloff)

        draw.point((x, y), fill=(r, g, b))

# fonts
try:
    font_name = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 76)
    font_title = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 36)
    font_url = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 28)
except:
    font_name = ImageFont.load_default()
    font_title = ImageFont.load_default()
    font_url = ImageFont.load_default()

# subtle dark overlay behind text for readability
overlay = Image.new("RGBA", (600, 200), (0, 0, 20, 140))
img.paste(overlay, (50, 170), overlay)

draw.text((80, 200), "Danny Wang", fill=(220, 235, 255), font=font_name)
draw.text((80, 290), "Student & Software Developer", fill=(180, 215, 240), font=font_title)
draw.text((80, 420), "dannywang.dev", fill=(120, 180, 220), font=font_url)

# glow accent underline
draw.rectangle([80, 288, 200, 294], fill=(100, 200, 255))

out_path = os.path.join(os.path.dirname(__file__), "portfolio-preview.png")
img.save(out_path, "PNG", optimize=True)
print(f"Saved to {out_path}")
