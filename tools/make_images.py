#!/usr/bin/env python3
"""Generate the placeholder artwork for the microsite.

Everything is SVG (a few KB each) so the whole image folder stays tiny and
stays sharp on any screen. Swap these for the client's real JPG/WebP photos
later -- the HTML only needs the filename to match.
"""
import os
import subprocess

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site", "images")
os.makedirs(OUT, exist_ok=True)

FILES = {}

# --------------------------------------------------------------- work-1
# "Northline banking app on a phone screen, balance card + transactions"
rows = ""
for i, (label, amt) in enumerate([("Coffee Hoxton", "-3.40"), ("Salary", "+2,480.00"),
                                  ("Metro card", "-12.00"), ("Rent", "-890.00")]):
    y = 318 + i * 54
    rows += f'''
    <rect x="316" y="{y}" width="168" height="40" rx="8" fill="#ffffff" opacity=".07"/>
    <circle cx="336" cy="{y+20}" r="10" fill="#6fd3b4" opacity=".55"/>
    <rect x="354" y="{y+11}" width="62" height="7" rx="3.5" fill="#ffffff" opacity=".55"/>
    <rect x="354" y="{y+23}" width="38" height="6" rx="3" fill="#ffffff" opacity=".28"/>
    <rect x="432" y="{y+15}" width="42" height="8" rx="4" fill="#6fd3b4" opacity=".75"/>'''

FILES["work-1.svg"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600" role="img" aria-label="Northline banking app on a phone screen">
  <defs><linearGradient id="n1" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#17352e"/><stop offset="1" stop-color="#0d1f1b"/></linearGradient></defs>
  <rect width="800" height="600" fill="url(#n1)"/>
  <circle cx="660" cy="120" r="150" fill="#1f6f5c" opacity=".35"/>
  <circle cx="120" cy="520" r="110" fill="#6fd3b4" opacity=".14"/>
  <!-- phone -->
  <rect x="290" y="70" width="220" height="460" rx="34" fill="#0b1513" stroke="#6fd3b4" stroke-opacity=".3" stroke-width="2"/>
  <rect x="360" y="86" width="80" height="9" rx="4.5" fill="#ffffff" opacity=".16"/>
  <!-- balance card -->
  <rect x="312" y="118" width="176" height="120" rx="14" fill="#1f6f5c"/>
  <rect x="330" y="142" width="54" height="8" rx="4" fill="#ffffff" opacity=".6"/>
  <text x="330" y="190" font-family="Georgia, serif" font-size="30" fill="#ffffff">€4,218</text>
  <rect x="330" y="206" width="90" height="7" rx="3.5" fill="#ffffff" opacity=".4"/>
  <rect x="452" y="140" width="22" height="16" rx="3" fill="#ffffff" opacity=".5"/>
  <!-- section label -->
  <rect x="316" y="262" width="74" height="9" rx="4.5" fill="#ffffff" opacity=".4"/>
  {rows}
  <!-- tab bar -->
  <rect x="300" y="492" width="200" height="30" rx="15" fill="#ffffff" opacity=".07"/>
  <circle cx="344" cy="507" r="6" fill="#6fd3b4"/><circle cx="400" cy="507" r="6" fill="#ffffff" opacity=".3"/>
  <circle cx="456" cy="507" r="6" fill="#ffffff" opacity=".3"/>
  <text x="56" y="86" font-family="Georgia, serif" font-size="34" fill="#ffffff" opacity=".9">Northline</text>
  <text x="56" y="116" font-family="Helvetica, Arial, sans-serif" font-size="14" fill="#6fd3b4" letter-spacing="3">MOBILE BANKING</text>
</svg>'''

# --------------------------------------------------------------- work-2
# "Petalbox brand identity: pink flower mark beside packaging mock-ups"
petals = ""
for a in range(0, 360, 60):
    petals += f'<ellipse cx="0" cy="-34" rx="17" ry="34" fill="#e0608f" transform="rotate({a})" opacity=".9"/>'

FILES["work-2.svg"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600" role="img" aria-label="Petalbox brand identity with a flower mark and packaging">
  <rect width="800" height="600" fill="#fdf3f5"/>
  <circle cx="110" cy="80" r="130" fill="#f6d9e2" opacity=".7"/>
  <circle cx="730" cy="540" r="120" fill="#f6d9e2" opacity=".6"/>
  <!-- flower mark -->
  <g transform="translate(222,214)">{petals}<circle r="15" fill="#fdf3f5"/><circle r="7" fill="#e0608f"/></g>
  <text x="130" y="360" font-family="Georgia, serif" font-size="46" fill="#4a2230">Petalbox</text>
  <rect x="131" y="382" width="184" height="3" fill="#e0608f"/>
  <text x="131" y="414" font-family="Helvetica, Arial, sans-serif" font-size="14" fill="#8a6673" letter-spacing="4">SLOW FLOWERS, POSTED</text>
  <!-- boxes -->
  <g>
    <rect x="430" y="150" width="200" height="200" rx="8" fill="#ffffff" stroke="#e8cdd6"/>
    <rect x="430" y="150" width="200" height="56" rx="8" fill="#e0608f"/>
    <g transform="translate(530,178) scale(.42)">{petals}<circle r="15" fill="#e0608f"/><circle r="7" fill="#ffffff"/></g>
    <rect x="462" y="238" width="136" height="9" rx="4.5" fill="#4a2230" opacity=".7"/>
    <rect x="462" y="258" width="92" height="8" rx="4" fill="#8a6673" opacity=".5"/>
    <rect x="462" y="300" width="60" height="22" rx="11" fill="#fdf3f5" stroke="#e0608f"/>
  </g>
  <g transform="translate(60,0)">
    <rect x="520" y="300" width="160" height="230" rx="8" fill="#f9e7ec" stroke="#e8cdd6"/>
    <g transform="translate(600,360) scale(.6)">{petals}<circle r="15" fill="#f9e7ec"/><circle r="7" fill="#e0608f"/></g>
    <rect x="552" y="430" width="96" height="8" rx="4" fill="#4a2230" opacity=".6"/>
    <rect x="552" y="448" width="64" height="7" rx="3.5" fill="#8a6673" opacity=".45"/>
  </g>
</svg>'''

# --------------------------------------------------------------- work-3
# "Atlas Review editorial layout, big headline + two-column grid"
col = ""
for c in (0, 1):
    for i in range(9):
        w = [196, 196, 170, 188, 196, 152, 196, 180, 120][i]
        col += f'<rect x="{300 + c*224}" y="{300 + i*22}" width="{w}" height="8" rx="4" fill="#2a2a28" opacity=".30"/>'

FILES["work-3.svg"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600" role="img" aria-label="Atlas Review editorial layout">
  <rect width="800" height="600" fill="#f4f1ea"/>
  <rect x="0" y="0" width="800" height="70" fill="#2a2a28"/>
  <text x="40" y="46" font-family="Georgia, serif" font-size="27" fill="#f4f1ea" letter-spacing="1">ATLAS REVIEW</text>
  <text x="640" y="44" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#f4f1ea" opacity=".7" letter-spacing="2">ISSUE 14</text>
  <text x="40" y="150" font-family="Georgia, serif" font-size="54" fill="#2a2a28">The long way</text>
  <text x="40" y="208" font-family="Georgia, serif" font-size="54" fill="#2a2a28">round</text>
  <rect x="40" y="236" width="720" height="2" fill="#2a2a28" opacity=".25"/>
  <text x="40" y="272" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#9a4b2f" letter-spacing="3">ESSAY · 18 MIN READ</text>
  <!-- lead image -->
  <rect x="40" y="300" width="232" height="246" rx="4" fill="#d9d2c4"/>
  <path d="M40 470 L112 400 L168 452 L214 410 L272 466 L272 546 L40 546 Z" fill="#9a4b2f" opacity=".55"/>
  <circle cx="226" cy="346" r="20" fill="#f4f1ea" opacity=".8"/>
  {col}
  <rect x="300" y="548" width="100" height="8" rx="4" fill="#9a4b2f" opacity=".8"/>
</svg>'''

# --------------------------------------------------------------- work-4
# "Metro wayfinding signs: white arrows + station names on dark blue"
FILES["work-4.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600" role="img" aria-label="Metro wayfinding signage">
  <rect width="800" height="600" fill="#e8e9ec"/>
  <rect x="0" y="420" width="800" height="180" fill="#d5d7dc"/>
  <!-- big sign -->
  <rect x="60" y="90" width="680" height="150" rx="6" fill="#102a54"/>
  <path d="M112 165 l40 -34 v22 h56 v24 h-56 v22 z" fill="#ffffff"/>
  <text x="240" y="152" font-family="Helvetica, Arial, sans-serif" font-size="34" fill="#ffffff">Riverside</text>
  <text x="240" y="196" font-family="Helvetica, Arial, sans-serif" font-size="34" fill="#ffffff" opacity=".82">Market Hall</text>
  <rect x="620" y="118" width="86" height="86" rx="43" fill="#ffffff" opacity=".12"/>
  <text x="648" y="174" font-family="Helvetica, Arial, sans-serif" font-size="40" fill="#ffffff">M</text>
  <!-- small sign -->
  <rect x="60" y="268" width="330" height="104" rx="6" fill="#1b3f78"/>
  <path d="M348 320 l-40 -34 v22 h-56 v24 h56 v22 z" fill="#ffffff"/>
  <text x="92" y="312" font-family="Helvetica, Arial, sans-serif" font-size="23" fill="#ffffff">Platforms</text>
  <text x="92" y="346" font-family="Helvetica, Arial, sans-serif" font-size="23" fill="#ffffff" opacity=".8">1 &#8211; 4</text>
  <!-- colour key -->
  <rect x="420" y="268" width="320" height="104" rx="6" fill="#ffffff" stroke="#c6c9d1"/>
  <circle cx="452" cy="300" r="11" fill="#c8402f"/><rect x="474" y="294" width="120" height="11" rx="5.5" fill="#102a54" opacity=".6"/>
  <circle cx="452" cy="336" r="11" fill="#1f6f5c"/><rect x="474" y="330" width="90" height="11" rx="5.5" fill="#102a54" opacity=".45"/>
  <!-- post + type specimen -->
  <rect x="384" y="420" width="18" height="170" fill="#9aa0ac"/>
  <text x="60" y="494" font-family="Helvetica, Arial, sans-serif" font-size="62" fill="#102a54" opacity=".9">Aa</text>
  <text x="60" y="534" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#4b556b" letter-spacing="3">WAYFINDING GROTESK</text>
  <text x="440" y="494" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#4b556b" letter-spacing="3">48 STATIONS · 2023</text>
</svg>'''

# --------------------------------------------------------------- work-5
# "Harvest Co. shop page: product grid of vegetable boxes with prices"
cards = ""
veg = [("#6a9a3c", "#c0d49a", "Weekly veg box", "€18"),
       ("#c87f2a", "#eccf9e", "Roots &amp; squash", "€22"),
       ("#4f8f72", "#b6d9c6", "Salad crate", "€14"),
       ("#a8442f", "#e3b3a4", "Tomato haul", "€16"),
       ("#7b6aa8", "#cdc3e4", "Aubergine box", "€19"),
       ("#3f7f8f", "#aed2da", "Market mix", "€25")]
for i, (dark, light, name, price) in enumerate(veg):
    x = 56 + (i % 3) * 236
    y = 196 + (i // 3) * 194
    cards += f'''
    <rect x="{x}" y="{y}" width="212" height="172" rx="10" fill="#ffffff" stroke="#e6e1d6"/>
    <rect x="{x}" y="{y}" width="212" height="96" rx="10" fill="{light}"/>
    <circle cx="{x+72}" cy="{y+56}" r="26" fill="{dark}" opacity=".85"/>
    <circle cx="{x+114}" cy="{y+66}" r="18" fill="{dark}" opacity=".6"/>
    <circle cx="{x+144}" cy="{y+50}" r="13" fill="{dark}" opacity=".45"/>
    <text x="{x+16}" y="{y+126}" font-family="Helvetica, Arial, sans-serif" font-size="15" fill="#2d2a22">{name}</text>
    <text x="{x+16}" y="{y+153}" font-family="Georgia, serif" font-size="19" fill="{dark}">{price}</text>
    <rect x="{x+150}" y="{y+134}" width="46" height="24" rx="12" fill="#2d6a3f"/>'''

FILES["work-5.svg"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600" role="img" aria-label="Harvest Co. online shop product grid">
  <rect width="800" height="600" fill="#faf8f2"/>
  <rect x="0" y="0" width="800" height="64" fill="#2d6a3f"/>
  <text x="56" y="41" font-family="Georgia, serif" font-size="23" fill="#ffffff">Harvest Co.</text>
  <rect x="560" y="22" width="80" height="20" rx="10" fill="#ffffff" opacity=".25"/>
  <rect x="660" y="22" width="84" height="20" rx="10" fill="#ffffff" opacity=".25"/>
  <text x="56" y="128" font-family="Georgia, serif" font-size="32" fill="#2d2a22">This week&#8217;s boxes</text>
  <rect x="56" y="146" width="300" height="2" fill="#2d6a3f" opacity=".3"/>
  {cards}
</svg>'''

# --------------------------------------------------------------- work-6
# "Illustrated hiking map, green & cream, contour lines + dotted trail"
contours = ""
for i in range(7):
    rx, ry = 70 + i * 46, 44 + i * 30
    contours += (f'<ellipse cx="300" cy="300" rx="{rx}" ry="{ry}" fill="none" '
                 f'stroke="#4a7a4e" stroke-opacity="{0.5 - i*0.05:.2f}" stroke-width="2" '
                 f'transform="rotate({-18 + i*2} 300 300)"/>')

FILES["work-6.svg"] = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600" role="img" aria-label="Illustrated hiking map with contour lines and a dotted trail">
  <rect width="800" height="600" fill="#f3efdf"/>
  {contours}
  <path d="M60 530 C 180 470, 190 360, 290 330 S 470 300, 520 200 S 640 120, 740 96"
        fill="none" stroke="#9a4b2f" stroke-width="5" stroke-linecap="round" stroke-dasharray="2 16"/>
  <path d="M660 430 q 60 -20 110 10" fill="none" stroke="#3f7f8f" stroke-width="7" stroke-linecap="round" opacity=".55"/>
  <path d="M620 470 q 70 -24 150 14" fill="none" stroke="#3f7f8f" stroke-width="7" stroke-linecap="round" opacity=".35"/>
  <circle cx="290" cy="330" r="9" fill="#9a4b2f"/><circle cx="290" cy="330" r="17" fill="none" stroke="#9a4b2f" stroke-width="2"/>
  <circle cx="740" cy="96" r="9" fill="#9a4b2f"/>
  <path d="M120 180 l26 -46 l26 46 z" fill="#4a7a4e" opacity=".8"/>
  <path d="M164 180 l20 -34 l20 34 z" fill="#4a7a4e" opacity=".55"/>
  <text x="112" y="214" font-family="Georgia, serif" font-size="17" fill="#3c5a3e">Pico Alto</text>
  <text x="300" y="368" font-family="Georgia, serif" font-size="17" fill="#9a4b2f">Refuge</text>
  <rect x="56" y="520" width="190" height="4" fill="#3c5a3e"/>
  <rect x="56" y="512" width="4" height="20" fill="#3c5a3e"/><rect x="242" y="512" width="4" height="20" fill="#3c5a3e"/>
  <text x="56" y="556" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#3c5a3e" letter-spacing="2">2 KM</text>
  <g transform="translate(728,528)"><circle r="26" fill="none" stroke="#3c5a3e" stroke-width="2"/>
    <path d="M0 -20 l7 20 l-7 -6 l-7 6 z" fill="#9a4b2f"/>
    <text x="-5" y="-26" font-family="Helvetica, Arial, sans-serif" font-size="13" fill="#3c5a3e">N</text></g>
</svg>'''

# --------------------------------------------------------------- portrait
FILES["portrait.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 720" width="640" height="720" role="img" aria-label="Illustrated portrait">
  <rect width="640" height="720" fill="#efe9dd"/>
  <circle cx="320" cy="300" r="210" fill="#e2d8c6"/>
  <!-- shoulders / green jumper -->
  <path d="M120 720 q 0 -190 200 -210 q 200 20 200 210 z" fill="#1f6f5c"/>
  <path d="M276 500 h88 v44 q -44 26 -88 0 z" fill="#d8a98c"/>
  <!-- head -->
  <ellipse cx="320" cy="372" rx="118" ry="140" fill="#e8bb9b"/>
  <!-- hair -->
  <path d="M202 362 q 6 -150 118 -150 t 118 150 q -20 -72 -118 -72 t -118 72 z" fill="#3a2b22"/>
  <path d="M198 356 q -16 70 12 116 q -28 -70 -12 -116 z" fill="#3a2b22"/>
  <path d="M442 356 q 16 70 -12 116 q 28 -70 12 -116 z" fill="#3a2b22"/>
  <!-- round glasses -->
  <circle cx="276" cy="378" r="38" fill="#ffffff" fill-opacity=".35" stroke="#2f2a26" stroke-width="7"/>
  <circle cx="366" cy="378" r="38" fill="#ffffff" fill-opacity=".35" stroke="#2f2a26" stroke-width="7"/>
  <path d="M314 378 h14" stroke="#2f2a26" stroke-width="7"/>
  <path d="M238 372 l-32 -8" stroke="#2f2a26" stroke-width="7" stroke-linecap="round"/>
  <path d="M404 372 l32 -8" stroke="#2f2a26" stroke-width="7" stroke-linecap="round"/>
  <circle cx="276" cy="378" r="7" fill="#2f2a26"/><circle cx="366" cy="378" r="7" fill="#2f2a26"/>
  <path d="M318 400 q 8 26 -8 32" fill="none" stroke="#c98f68" stroke-width="5" stroke-linecap="round" opacity=".5"/>
  <path d="M292 452 q 30 20 60 0" fill="none" stroke="#9c5f49" stroke-width="7" stroke-linecap="round"/>
  <!-- collar -->
  <path d="M276 532 l44 42 l44 -42 l26 14 l-70 62 l-70 -62 z" fill="#175647" opacity=".5"/>
</svg>'''

# --------------------------------------------------------------- favicon
FILES["favicon.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect width="64" height="64" rx="14" fill="#1f6f5c"/>
  <text x="32" y="43" text-anchor="middle" font-family="Helvetica, Arial, sans-serif"
        font-size="28" font-weight="bold" fill="#ffffff" letter-spacing="1">JA</text>
</svg>'''

# --------------------------------------------------------------- og card
FILES["og-card.svg"] = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630" role="img" aria-label="Jordan Avery social preview card">
  <rect width="1200" height="630" fill="#fbfaf7"/>
  <rect x="0" y="0" width="1200" height="14" fill="#1f6f5c"/>
  <rect x="80" y="150" width="86" height="86" rx="20" fill="#1f6f5c"/>
  <text x="123" y="205" text-anchor="middle" font-family="Helvetica, Arial, sans-serif" font-size="34" font-weight="bold" fill="#ffffff">JA</text>
  <text x="80" y="330" font-family="Georgia, serif" font-size="66" fill="#15181c">Jordan Avery</text>
  <text x="80" y="398" font-family="Helvetica, Arial, sans-serif" font-size="30" fill="#5c6470">Product designer &amp; illustrator, Lisbon</text>
  <rect x="80" y="440" width="180" height="5" fill="#1f6f5c"/>
</svg>'''

for name, data in FILES.items():
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(data)
    print("wrote", name, len(data), "bytes")

# A PNG copy of the favicon for older iOS/Android home-screen icons.
png = os.path.join(OUT, "apple-touch-icon.png")
try:
    subprocess.run(["rsvg-convert", "-w", "180", "-h", "180",
                    os.path.join(OUT, "favicon.svg"), "-o", png], check=False)
except FileNotFoundError:
    pass  # rsvg-convert is optional; the Pillow fallback below draws it instead
if not os.path.exists(png):
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new("RGBA", (180, 180), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, 179, 179], radius=40, fill=(31, 111, 92, 255))
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 76)
    except OSError:
        f = ImageFont.load_default()
    d.text((90, 88), "JA", font=f, fill=(255, 255, 255, 255), anchor="mm")
    im.save(png)
print("wrote apple-touch-icon.png")
