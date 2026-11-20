#!/usr/bin/env python3
"""Render news-image-20261120 entry.png: 'THE WORLD IN ONE DAY' — 36 verified
stories from Friday 20 November 2026. All text drawn with PIL (real, crisp)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
M = 28                      # side margin
CW = W - 2 * M              # content width

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
def F(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)

SERIF_B = lambda s: F("DejaVuSerif-Bold.ttf", s)
SANS    = lambda s: F("DejaVuSans.ttf", s)
SANS_B  = lambda s: F("DejaVuSans-Bold.ttf", s)

# ---------- palette ----------
PAPER   = (253, 251, 243)
INK     = (24, 26, 32)
NAVY    = (18, 38, 74)
RED     = (178, 34, 34)
GREY    = (96, 100, 110)
RULE    = (180, 180, 172)
MAP_LAND= (158, 178, 198)
MAP_SEA = (233, 242, 248)
GREEN   = (38, 120, 70)
GOLD    = (176, 128, 20)
TEAL    = (16, 110, 110)

# ---------- story data (all verified 20 Nov 2026) ----------
LEADS = [
    dict(n=1, region="ASIA \u00b7 WEATHER",
         headline="Cyclone Akvan slams Odisha coast",
         summary="Severe storm makes landfall near Gopalpur at noon, winds to 110 km/h. 300,000 evacuated; 423 rescue teams deployed.",
         source="The Hindu", icon="cyclone", pin=(715, 700)),
    dict(n=2, region="AMERICAS \u00b7 POLITICS",
         headline="Trump defers Iran decision to 2027",
         summary="\u201cNo rush,\u201d the president says; he will \u201csee what happens\u201d after Jan 1. A decision on war is pushed into next year.",
         source="Reuters", icon="calendar", pin=(245, 682)),
    dict(n=3, region="EUROPE \u00b7 DIPLOMACY",
         headline="Europe ready for talks with Russia",
         summary="European leaders say they are ready to join talks on ending the Ukraine war, after the Shenzhen summit.",
         source="BBC", icon="dove", pin=(505, 668)),
    dict(n=4, region="WORLD \u00b7 CLIMATE",
         headline="COP31 closes in Antalya",
         summary="Final-day draft drops the fossil-fuel phase-out and a $120bn adaptation-finance target. Africa rejects renegotiating Paris.",
         source="The Hindu", icon="globe", pin=(545, 672)),
]

GRID = [
    dict(n=5,  region="TECH \u00b7 BUSINESS", headline="Anthropic\u2019s $81.3bn offering closes",
         summary="Shares priced at $83; firm valued near $1.5tn fully diluted.", source="Reuters", icon="chip", pin=(110, 680)),
    dict(n=6,  region="CULTURE \u00b7 GAMES", headline="GTA VI sales pass $1.8bn",
         summary="Rockstar\u2019s game tops The Odyssey\u2019s global box-office run in a day.", source="Mezha", icon="controller", pin=(200, 690)),
    dict(n=7,  region="SCIENCE \u00b7 SPACE", headline="Hayabusa2 asteroid landing called off",
         summary="Engine trouble forces Japan\u2019s probe to change plans; no touchdown.", source="Space.com", icon="rocket", pin=(800, 668)),
    dict(n=8,  region="MIDDLE EAST \u00b7 ENERGY", headline="Tanker ablaze after hitting mine",
         summary="Vessel catches fire east of the Strait of Hormuz after striking a mine.", source="Daily Baku", icon="ship", pin=(640, 688)),
    dict(n=9,  region="ASIA-PACIFIC \u00b7 DIPLOMACY", headline="Albanese meets Xi in Shenzhen",
         summary="Fifth formal meeting; iron ore, beef and trade top the agenda.", source="Reuters", icon="flags", pin=(760, 690)),
    dict(n=10, region="SPORT \u00b7 CRICKET", headline="Nicholls 146* as NZ reach 317/6",
         summary="Phillips hits 118 on day two of the first Test against India.", source="AP", icon="bat", pin=(905, 728)),
    dict(n=11, region="MIDDLE EAST \u00b7 YEMEN", headline="\u201cIt\u2019s just fireworks,\u201d mother tells son",
         summary="In besieged Taiz, families shield children from shelling; 148 civilians killed since August.", source="BBC", icon="house", pin=(600, 700)),
    dict(n=12, region="NORTH AMERICA \u00b7 TECH", headline="Canada embraces AI data centres",
         summary="Alberta pitches itself as a hub as US voters push back on new sites.", source="BBC", icon="server", pin=(150, 662)),
    dict(n=13, region="LATIN AMERICA \u00b7 HAITI", headline="34 gang members killed in Haiti offensive",
         summary="Police report 34 suspected gang members killed in Martissant operation.", source="News-Public", icon="shield", pin=(265, 695)),
    dict(n=14, region="SPORT \u00b7 BUSINESS", headline="LA Sparks near $750m sale",
         summary="WNBA record deal reported for the Los Angeles franchise.", source="News-Public", icon="ball", pin=(120, 692)),
    dict(n=15, region="AMERICAS \u00b7 SECURITY", headline="Iran still holds 2,500 missiles, US intel says",
         summary="WSJ cites US intelligence: arsenal intact despite nine-month war.", source="WSJ", icon="radar", pin=(270, 665)),
    dict(n=16, region="ASIA \u00b7 CULTURE", headline="SCO dialogue forum opens in Delhi",
         summary="Modi inaugurates first SCO Civilisational Dialogue Forum at Purana Qila.", source="MEA", icon="dome", pin=(690, 688)),
]

ALSO = [
    (17, "Bavuma ruled out of Bangladesh Test decider"),
    (18, "ASX 200 falls 1.04% to 8,730 as miners slide"),
    (19, "Hang Seng drops 1.95% to 22,841"),
    (20, "BHP and Rio Tinto chiefs meet Premier Li Qiang in Beijing"),
    (21, "Submarine cable fault disrupts internet in Pakistan"),
    (22, "Pakistan cuts petrol and diesel by Rs.3 a litre"),
    (23, "Saudi Arabia fears new Yemen war could last six months"),
    (24, "Trump to hold news conference in Washington at noon"),
    (25, "Nigeria, Cameroon, Chad, Niger sign cross-border pact"),
    (26, "Nigeria records 941 road deaths in Q3, down 12.6%"),
    (27, "Dangote Refinery may raise IPO to $2.1bn"),
    (28, "Fitch: debt interest to eat 29% of Nigeria\u2019s revenue"),
    (29, "Morocco plans SMS flood alerts with three-day warnings"),
    (30, "Morocco crush Angola 4\u20131, Amputee Football WC semis"),
    (31, "Cross River truck crash kills 9, injures 46"),
    (32, "Ibom Air posts N5.48bn profit on N147bn revenue"),
    (33, "RBA sees mixed Australian demand amid oil disruption"),
    (34, "CBO: AUKUS sub transfer would cut US Navy capacity"),
    (35, "World Children\u2019s Day marked around the globe"),
    (36, "COP31: Africa rejects renegotiating Paris Agreement"),
]

DATECHECK = [
    "ICJ: Myanmar genocide verdict (19 Nov)",
    "Trump\u2013Xi\u2013Putin Shenzhen summit (19 Nov)",
    "GTA VI midnight launch (19 Nov)",
    "Anthropic Nasdaq debut (19 Nov)",
    "Senate 51\u201348 war-powers vote (19 Nov)",
    "Houthi missile hits Riyadh KAFD (19 Nov)",
    "Crimean Bridge hit, rail halted (18\u201319 Nov)",
    "Han Duck-soo ruling (19 Nov)",
    "Voyager 1 one light-day (confirmed 19 Nov)",
    "APEC leaders meet (18\u201319 Nov)",
    "IAEA Yongbyon report (18 Nov)",
    "Pete Rose pardon (19 Nov)",
]

HEADLINES = [
    "1  TRUMP DEFERS IRAN DECISION TO 2027",
    "2  CYCLONE AKVAN HITS ODISHA \u2014 300,000 EVACUATED",
    "3  EUROPE READY FOR TALKS WITH RUSSIA",
]
NUMBERS = "300,000 evacuated   \u00b7   $81.3bn IPO closes   \u00b7   $1.8bn GTA VI sales   \u00b7   146* Nicholls   \u00b7   $120bn COP31 target dropped"

# ---------- text helpers ----------
def wrap(draw, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= max_w or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def fit_lines(draw, text, font, max_w, max_lines):
    """Wrap and cap to max_lines, adding ellipsis to the last line if truncated."""
    lines = wrap(draw, text, font, max_w)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        while lines and draw.textlength(lines[-1] + "...", font=font) > max_w:
            lines[-1] = lines[-1].rsplit(" ", 1)[0] if " " in lines[-1] else lines[-1][:-1]
        if lines:
            lines[-1] = lines[-1] + "..."
    return lines

def centre(draw, y, s, font, fill, x0=M, x1=W - M):
    w = draw.textlength(s, font=font)
    draw.text(((x0 + x1 - w) / 2, y), s, font=font, fill=fill)

def badge(draw, x, y, n, r=11, bg=RED, fg=(255, 255, 255)):
    draw.ellipse([x, y, x + 2 * r, y + 2 * r], fill=bg)
    s = str(n)
    f = SANS_B(11 if len(s) < 2 else 10)
    tw = draw.textlength(s, font=f)
    th = f.getbbox(s)[3]
    draw.text((x + r - tw / 2, y + r - th / 2 - 1), s, font=f, fill=fg)

def section_bar(draw, y, label, h=20):
    draw.rectangle([M, y, W - M, y + h], fill=NAVY)
    f = SANS_B(13)
    draw.text((M + 10, y + 3), label, font=f, fill=(255, 255, 255))
    return y + h

# ---------- icons (flat original drawings, scaled to bbox) ----------
import math

def _box(x0, y0, x1, y1):
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    s = min(x1 - x0, y1 - y0)
    return cx, cy, s

def icon_cyclone(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    pts = []
    th = 0.0
    while th <= 4.5 * math.pi:
        r = 1.0 + (s * 0.028) * th
        pts.append((cx + r * math.cos(th), cy + r * math.sin(th)))
        th += 0.10
    d.line(pts, fill=(44, 74, 107), width=max(2, int(s * 0.07)))
    d.ellipse([cx - s*0.06, cy - s*0.06, cx + s*0.06, cy + s*0.06], fill=(44, 74, 107))
    for rx, ry in ((x0 + s*0.08, y0 + s*0.06), (x1 - s*0.16, y0 + s*0.10), (x1 - s*0.10, y1 - s*0.22)):
        d.line([(rx, ry), (rx - s*0.06, ry + s*0.14)], fill=(44, 74, 107), width=max(2, int(s*0.04)))

def icon_calendar(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    d.rounded_rectangle([x0+2, y0+2, x1-2, y1-2], radius=6, fill=(255,255,255), outline=NAVY, width=2)
    d.rectangle([x0+2, y0+2, x1-2, y0+s*0.28], fill=RED)
    f = SANS_B(max(8, int(s*0.30)))
    t = "2027"
    tw = d.textlength(t, font=f)
    d.text((cx - tw/2, y0 + s*0.34), t, font=f, fill=NAVY)
    for i in range(3):
        yy = y0 + s*(0.68 + i*0.12)
        d.line([(x0+s*0.18, yy), (x1-s*0.18, yy)], fill=(150,150,150), width=2)

def icon_dove(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    # tail, body, head, beak, wing, olive branch
    d.polygon([(cx-s*0.32, cy-s*0.02), (cx-s*0.48, cy-s*0.16), (cx-s*0.46, cy+s*0.10)], fill=(255,255,255), outline=NAVY)
    d.ellipse([cx-s*0.30, cy-s*0.14, cx+s*0.22, cy+s*0.16], fill=(255,255,255), outline=NAVY)
    d.ellipse([cx+s*0.14, cy-s*0.28, cx+s*0.38, cy-s*0.04], fill=(255,255,255), outline=NAVY)
    d.polygon([(cx+s*0.36, cy-s*0.20), (cx+s*0.50, cy-s*0.14), (cx+s*0.36, cy-s*0.10)], fill=GOLD)
    d.arc([cx-s*0.16, cy-s*0.24, cx+s*0.14, cy+s*0.02], start=195, end=345, fill=NAVY, width=2)
    d.line([(cx-s*0.10, cy+s*0.34), (cx+s*0.34, cy+s*0.20)], fill=GREEN, width=2)
    d.ellipse([cx+s*0.02, cy+s*0.26, cx+s*0.16, cy+s*0.34], fill=GREEN)
    d.ellipse([cx+s*0.20, cy+s*0.18, cx+s*0.32, cy+s*0.26], fill=GREEN)

def icon_globe(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    d.ellipse([x0+2, y0+2, x1-2, y1-2], fill=(140, 190, 230), outline=NAVY, width=2)
    d.ellipse([cx-s*0.28, cy-s*0.22, cx-s*0.02, cy+s*0.02], fill=GREEN)
    d.ellipse([cx+s*0.06, cy+s*0.08, cx+s*0.30, cy+s*0.30], fill=GREEN)
    d.ellipse([cx-s*0.05, cy-s*0.38, cx+s*0.18, cy-s*0.20], fill=GREEN)
    # leaf
    d.polygon([(cx+s*0.28, cy+s*0.34), (cx+s*0.52, cy+s*0.12), (cx+s*0.52, cy+s*0.42)], fill=GREEN)

def icon_chip(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    for i in range(3):
        yy = y0 + s*(0.28 + i*0.22)
        d.line([(x0, yy), (x0+s*0.16, yy)], fill=NAVY, width=2)
        d.line([(x1-s*0.16, yy), (x1, yy)], fill=NAVY, width=2)
    d.rectangle([x0+s*0.16, y0+s*0.16, x1-s*0.16, y1-s*0.16], fill=(255,255,255), outline=NAVY, width=2)
    d.rectangle([cx-s*0.14, cy-s*0.14, cx+s*0.14, cy+s*0.14], fill=RED)

def icon_controller(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    d.rounded_rectangle([x0+2, y0+s*0.18, x1-2, y1-s*0.18], radius=8, fill=(40,40,50), outline=NAVY, width=2)
    d.ellipse([cx-s*0.28, cy-s*0.02, cx-s*0.12, cy+s*0.14], fill=(255,255,255))
    d.ellipse([cx+s*0.12, cy-s*0.02, cx+s*0.28, cy+s*0.14], fill=(255,255,255))
    d.line([(cx-s*0.02, cy-s*0.10), (cx-s*0.02, cy+s*0.10)], fill=(255,255,255), width=2)
    d.line([(cx-s*0.10, cy), (cx+s*0.06, cy)], fill=(255,255,255), width=2)
    d.ellipse([cx+s*0.22, cy-s*0.16, cx+s*0.32, cy-s*0.06], fill=RED)
    d.ellipse([cx+s*0.22, cy+s*0.02, cx+s*0.32, cy+s*0.12], fill=GOLD)

def icon_rocket(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    d.polygon([(cx, y0+s*0.02), (cx+s*0.16, y0+s*0.30), (cx-s*0.16, y0+s*0.30)], fill=RED)
    d.rectangle([cx-s*0.16, y0+s*0.28, cx+s*0.16, y0+s*0.72], fill=(255,255,255), outline=NAVY, width=2)
    d.ellipse([cx-s*0.07, cy-s*0.02, cx+s*0.07, cy+s*0.12], fill=(140,190,230), outline=NAVY, width=1)
    d.polygon([(cx-s*0.16, y0+s*0.62), (cx-s*0.34, y0+s*0.82), (cx-s*0.16, y0+s*0.78)], fill=RED)
    d.polygon([(cx+s*0.16, y0+s*0.62), (cx+s*0.34, y0+s*0.82), (cx+s*0.16, y0+s*0.78)], fill=RED)
    d.polygon([(cx-s*0.09, y0+s*0.74), (cx, y0+s*0.98), (cx+s*0.09, y0+s*0.74)], fill=(230,110,20))

def icon_ship(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    d.polygon([(cx-s*0.10, y0+s*0.30), (cx-s*0.02, y0+s*0.10), (cx+s*0.04, y0+s*0.22), (cx+s*0.12, y0+s*0.06), (cx+s*0.16, y0+s*0.30)], fill=(230,110,20))
    d.polygon([(cx-s*0.05, y0+s*0.30), (cx, y0+s*0.18), (cx+s*0.06, y0+s*0.30)], fill=(250,200,40))
    d.polygon([(x0+s*0.06, y0+s*0.62), (x1-s*0.06, y0+s*0.62), (x1-s*0.16, y0+s*0.78), (x0+s*0.16, y0+s*0.78)], fill=(34,48,60))
    d.rectangle([cx-s*0.22, y0+s*0.42, cx+s*0.02, y0+s*0.62], fill=(179,64,46))
    d.rectangle([cx+s*0.06, y0+s*0.42, cx+s*0.30, y0+s*0.62], fill=(46,127,122))
    d.line([(x0, y0+s*0.86), (x1, y0+s*0.86)], fill=(46,98,140), width=3)

def icon_flags(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    d.line([(cx-s*0.22, y0+s*0.10), (cx-s*0.22, y1-s*0.08)], fill=NAVY, width=2)
    d.line([(cx+s*0.22, y0+s*0.10), (cx+s*0.22, y1-s*0.08)], fill=NAVY, width=2)
    d.polygon([(cx-s*0.22, y0+s*0.10), (cx+s*0.10, y0+s*0.16), (cx-s*0.22, y0+s*0.34)], fill=RED)
    d.polygon([(cx+s*0.22, y0+s*0.10), (cx-s*0.10, y0+s*0.16), (cx+s*0.22, y0+s*0.34)], fill=GOLD)

def icon_bat(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    d.rounded_rectangle([cx-s*0.10, y0+s*0.28, cx+s*0.14, y0+s*0.86], radius=4, fill=(222,184,120), outline=NAVY, width=2)
    d.rectangle([cx-s*0.02, y0+s*0.06, cx+s*0.06, y0+s*0.30], fill=NAVY)
    d.ellipse([cx+s*0.18, cy-s*0.02, cx+s*0.42, cy+s*0.22], fill=RED)
    d.arc([cx+s*0.18, cy-s*0.02, cx+s*0.42, cy+s*0.22], start=200, end=340, fill=(255,255,255), width=2)

def icon_house(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    d.polygon([(cx-s*0.34, y0+s*0.42), (cx, y0+s*0.08), (cx+s*0.34, y0+s*0.42)], fill=RED)
    d.rectangle([cx-s*0.26, y0+s*0.42, cx+s*0.26, y0+s*0.86], fill=(255,255,255), outline=NAVY, width=2)
    d.rectangle([cx-s*0.07, y0+s*0.60, cx+s*0.07, y0+s*0.86], fill=NAVY)
    d.rectangle([cx-s*0.20, y0+s*0.50, cx-s*0.08, y0+s*0.62], fill=(140,190,230), outline=NAVY, width=1)
    d.rectangle([cx+s*0.08, y0+s*0.50, cx+s*0.20, y0+s*0.62], fill=(140,190,230), outline=NAVY, width=1)

def icon_server(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    for i in range(3):
        yy0 = y0 + s*(0.10 + i*0.28)
        d.rectangle([x0+s*0.12, yy0, x1-s*0.12, yy0+s*0.20], fill=(255,255,255), outline=NAVY, width=2)
        d.ellipse([x0+s*0.20, yy0+s*0.06, x0+s*0.28, yy0+s*0.14], fill=GREEN)
        d.line([(x0+s*0.38, yy0+s*0.10), (x1-s*0.22, yy0+s*0.10)], fill=(150,150,150), width=2)

def icon_shield(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    d.polygon([(cx-s*0.30, y0+s*0.10), (cx+s*0.30, y0+s*0.10), (cx+s*0.30, y0+s*0.48), (cx, y0+s*0.88), (cx-s*0.30, y0+s*0.48)], fill=(30,58,108))
    d.line([(cx-s*0.16, cy+s*0.02), (cx-s*0.02, cy+s*0.18), (cx+s*0.20, cy-s*0.14)], fill=(255,255,255), width=3)

def icon_ball(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    d.ellipse([x0+2, y0+2, x1-2, y1-2], fill=(230,120,40), outline=NAVY, width=2)
    d.line([(x0+2, cy), (x1-2, cy)], fill=NAVY, width=2)
    d.line([(cx, y0+2), (cx, y1-2)], fill=NAVY, width=2)
    d.arc([x0-s*0.20, y0-s*0.20, cx+s*0.10, cy+s*0.10], start=300, end=90, fill=NAVY, width=2)
    d.arc([cx-s*0.10, cy-s*0.10, x1+s*0.20, y1+s*0.20], start=120, end=270, fill=NAVY, width=2)

def icon_radar(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    d.ellipse([x0+2, y0+2, x1-2, y1-2], outline=GREEN, width=2)
    d.ellipse([cx-s*0.22, cy-s*0.22, cx+s*0.22, cy+s*0.22], outline=GREEN, width=1)
    d.line([(cx, cy), (cx+s*0.34, cy-s*0.30)], fill=GREEN, width=2)
    d.ellipse([cx+s*0.16, cy-s*0.16, cx+s*0.26, cy-s*0.06], fill=RED)
    d.ellipse([cx-s*0.26, cy+s*0.12, cx-s*0.18, cy+s*0.20], fill=RED)

def icon_dome(d, x0, y0, x1, y1):
    cx, cy, s = _box(x0, y0, x1, y1)
    d.line([(cx, y0+s*0.04), (cx, y0+s*0.18)], fill=GOLD, width=2)
    d.ellipse([cx-s*0.04, y0+s*0.02, cx+s*0.04, y0+s*0.10], fill=GOLD)
    d.pieslice([cx-s*0.30, y0+s*0.14, cx+s*0.30, y0+s*0.74], start=180, end=360, fill=GOLD, outline=NAVY, width=2)
    d.rectangle([cx-s*0.34, y0+s*0.44, cx+s*0.34, y0+s*0.86], fill=(255,255,255), outline=NAVY, width=2)
    d.arc([cx-s*0.08, y0+s*0.60, cx+s*0.08, y0+s*0.86], start=180, end=360, fill=NAVY, width=2)

ICONS = {
    "cyclone": icon_cyclone, "calendar": icon_calendar, "dove": icon_dove,
    "globe": icon_globe, "chip": icon_chip, "controller": icon_controller,
    "rocket": icon_rocket, "ship": icon_ship, "flags": icon_flags,
    "bat": icon_bat, "house": icon_house, "server": icon_server,
    "shield": icon_shield, "ball": icon_ball, "radar": icon_radar,
    "dome": icon_dome,
}

# ---------- layout ----------
img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# shorten a few grid summaries so they fit one line at full cell width
GRID[0]["summary"] = "Shares priced at $83; firm valued near $1.5tn."
GRID[1]["summary"] = "Rockstar\u2019s game tops The Odyssey\u2019s global box-office run."
GRID[2]["summary"] = "Engine trouble forces Japan\u2019s probe to change plans."
GRID[3]["summary"] = "Vessel catches fire east of the Strait of Hormuz."
GRID[4]["summary"] = "Fifth formal meeting; iron ore and trade top agenda."
GRID[5]["summary"] = "Phillips hits 118 on day two of the first Test."
GRID[6]["summary"] = "Families in besieged Taiz shield children from shelling."
GRID[8]["summary"] = "34 suspected gang members killed in Martissant."
GRID[10]["summary"] = "US intelligence: arsenal intact despite nine-month war."
GRID[11]["summary"] = "Modi inaugurates first SCO forum at Purana Qila."

# pin positions for the map band (y 730-800)
PIN_POS = {
    1: (710, 770), 2: (240, 752), 3: (505, 738), 4: (545, 744),
    5: (105, 744), 6: (200, 754), 7: (800, 738), 8: (640, 756),
    9: (760, 758), 10: (905, 786), 11: (600, 768), 12: (150, 734),
    13: (265, 762), 14: (115, 762), 15: (265, 738), 16: (690, 756),
}

# ----- header -----
d.rectangle([0, 0, W, 5], fill=NAVY)
centre(d, 10, "THE WORLD IN ONE DAY", SERIF_B(30), NAVY)
centre(d, 46, "Friday 20 November 2026", SERIF_B(52), INK)
centre(d, 104, "36 STORIES  \u00b7  6 REGIONS  \u00b7  EVERY ONE FROM THIS FRIDAY", SANS_B(18), RED)
centre(d, 126, "ASIA-PACIFIC 11   \u00b7   AFRICA 10   \u00b7   AMERICAS 9   \u00b7   MIDDLE EAST 3   \u00b7   EUROPE 2   \u00b7   WORLD 1",
       SANS(13), (70, 70, 80))
d.line([(M, 146), (W - M, 146)], fill=RULE, width=1)

# ----- headline strip -----
for i, hl in enumerate(HEADLINES):
    centre(d, 152 + i * 19, hl, SANS_B(17), INK)

# ----- big-numbers band -----
d.rectangle([M, 214, W - M, 238], fill=(232, 240, 248), outline=RULE, width=1)
centre(d, 219, NUMBERS, SANS_B(15), NAVY)

# ----- section label (compact) -----
def label(y, text):
    d.text((M, y), text, font=SANS_B(12), fill=NAVY)
    d.line([(M, y + 15), (W - M, y + 15)], fill=NAVY, width=1)

# ----- leads (2x2) -----
label(244, "TOP STORIES")
LEAD_W, LEAD_H, LGAP = 479, 88, 10
for i, s in enumerate(LEADS):
    col, row = i % 2, i // 2
    x = M + col * (LEAD_W + LGAP)
    y = 262 + row * (LEAD_H + 8)
    d.rectangle([x, y, x + LEAD_W, y + LEAD_H], fill=(255, 255, 255), outline=RULE, width=1)
    badge(d, x + 8, y + 8, s["n"])
    d.text((x + 36, y + 10), s["region"], font=SANS_B(10), fill=RED)
    src = "Source: " + s["source"]
    sw = d.textlength(src, font=SANS(9))
    d.text((x + LEAD_W - 88 - sw, y + 11), src, font=SANS(9), fill=GREY)
    # icon panel (right)
    ix0, iy0, ix1, iy1 = x + LEAD_W - 80, y + 8, x + LEAD_W - 8, y + 80
    d.rectangle([ix0, iy0, ix1, iy1], fill=(240, 244, 248), outline=RULE, width=1)
    ICONS[s["icon"]](d, ix0 + 4, iy0 + 4, ix1 - 4, iy1 - 4)
    # headline + summary
    tw = LEAD_W - 36 - 88
    hl = fit_lines(d, s["headline"], SANS_B(15), tw, 2)
    yy = y + 26
    for ln in hl:
        d.text((x + 36, yy), ln, font=SANS_B(15), fill=INK)
        yy += 17
    sm = fit_lines(d, s["summary"], SANS(11), tw, 2)
    yy += 3
    for ln in sm:
        d.text((x + 36, yy), ln, font=SANS(11), fill=(60, 62, 70))
        yy += 13

# ----- grid (3x4) -----
label(452, "MORE TODAY")
CELL_W, CELL_H, CGAP = 317, 56, 8
for i, s in enumerate(GRID):
    col, row = i % 3, i // 3
    x = M + col * (CELL_W + CGAP)
    y = 470 + row * (CELL_H + 4)
    d.rectangle([x, y, x + CELL_W, y + CELL_H], fill=(255, 255, 255), outline=RULE, width=1)
    badge(d, x + 5, y + 4, s["n"], r=8)
    d.rectangle([x + 25, y + 4, x + 47, y + 26], fill=(240, 244, 248), outline=RULE, width=1)
    ICONS[s["icon"]](d, x + 27, y + 6, x + 45, y + 24)
    d.text((x + 52, y + 6), s["region"], font=SANS_B(9), fill=RED)
    src = s["source"]
    sw = d.textlength(src, font=SANS(8))
    d.text((x + CELL_W - 6 - sw, y + 7), src, font=SANS(8), fill=GREY)
    hl = fit_lines(d, s["headline"], SANS_B(12), CELL_W - 10, 1)
    for ln in hl:
        d.text((x + 5, y + 28), ln, font=SANS_B(12), fill=INK)
    sm = fit_lines(d, s["summary"], SANS(10), CELL_W - 10, 1)
    for ln in sm:
        d.text((x + 5, y + 43), ln, font=SANS(10), fill=(60, 62, 70))

# ----- map -----
label(712, "WHERE IT HAPPENED \u2014 NUMBERED PINS MATCH THE STORIES ABOVE")
MY0, MY1 = 730, 800
d.rectangle([M, MY0, W - M, MY1], fill=MAP_SEA, outline=RULE, width=1)
LAND = [
    (70, 732, 280, 762), (60, 730, 180, 748), (200, 756, 260, 772),   # N America
    (265, 756, 340, 798), (255, 752, 325, 770),                       # S America
    (465, 732, 545, 752),                                              # Europe
    (465, 754, 560, 798), (560, 776, 575, 796),                       # Africa + Madagascar
    (545, 730, 820, 764), (680, 758, 730, 780), (760, 758, 820, 774), # Asia
    (800, 772, 880, 792), (895, 778, 915, 794),                       # Australia + NZ
]
for (x0, y0, x1, y1) in LAND:
    d.ellipse([x0, y0, x1, y1], fill=MAP_LAND)
for s in LEADS + GRID:
    px, py = PIN_POS[s["n"]]
    d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline=(255, 255, 255), width=1)
    t = str(s["n"])
    f = SANS_B(9 if len(t) < 2 else 8)
    tw = d.textlength(t, font=f)
    th = f.getbbox(t)[3]
    d.text((px - tw / 2, py - th / 2 - 1), t, font=f, fill=(255, 255, 255))

# ----- also today -----
label(806, "ALSO TODAY")
for i, (n, txt) in enumerate(ALSO):
    col, row = i // 10, i % 10
    x = M + col * 484
    y = 824 + row * 11
    d.text((x, y), f"{n}.", font=SANS_B(10), fill=RED)
    d.text((x + 26, y), txt, font=SANS(10), fill=INK)

# ----- date check -----
d.rectangle([M, 938, W - M, 998], fill=(246, 226, 224), outline=RED, width=1)
d.text((M + 8, 941), "DATE CHECK \u2014 DELIBERATELY LEFT OUT (FIRST REPORTED 19 NOV OR EARLIER):",
       font=SANS_B(11), fill=RED)
for i, item in enumerate(DATECHECK):
    col, row = i % 3, i // 3
    x = M + 8 + col * 317
    y = 956 + row * 11
    d.text((x, y), "\u2022 " + item, font=SANS(9), fill=(90, 30, 30))

# ----- footer -----
centre(d, 1002, "Every story here happened, or was first reported, on Friday 20 November 2026, in some time zone. Disputed claims are attributed, not stated as fact.",
       SANS(10), INK)
centre(d, 1013, "Sources: Reuters, AP, BBC, The Hindu, Space.com, Mezha, Daily Baku, WSJ, ToI, News-Public, Punch, Vanguard, ANI, MEA.  Original drawings.",
       SANS(9), GREY)

img.save("entry.png", format="PNG", optimize=True)
print("saved entry.png", img.size)
