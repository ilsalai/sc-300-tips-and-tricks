# estilo claro (Light): spec for building a session deck (Slides artifact format)

You write one folder: `<ROOT>/project/deck.json` plus one file per slide at `<ROOT>/project/slides/<id>.html`. Write every file with the Write tool (never generate them with a script). Do NOT publish anything; the lead publishes.

## The canonical example

Read ALL of these first and copy their exact structure, style tokens and idioms:
- sessions/sesion-2/deck-source/deck.json
- sessions/sesion-2/deck-source/slides/*.html (28 files: cover, agenda, m2-overview, four, t-*.html trap slides, kahoot-intro, k01..k10 debrief slides, week, resources)

## Format rules (hard)

- A slide file holds EXACTLY ONE `<section id="<id>" data-transition="fade" style="...">` whose id equals the file name. Nothing before or after it. Last child is ONE `<aside>` with plain-text speaker notes (objetivo del slide, frase clave, trampa favorita, qué preguntas del banco la practican, tiempo).
- Canvas 1920x1080; every style inline; allowed elements: h1 h2 h3 p ul ol li br b i u a span div img table tr th td svg hr x-shape x-icon. NO classes, NO `<style>`, NO margin, NO em/rem/%, no `<a style=...>` (style a link as `<a href="..."><span style="color:#0E7490">label</span></a>`).
- Section style: `background:#F6F8FB; color:#0F172A; font-family:'Inter', Arial, sans-serif; padding:128px 128px 160px; display:flex; flex-direction:column; gap:30px` (content slides). The inside area is 1664 x 824 px. Nothing may exceed 824 px of stacked height: heading ≈ font-size × lines × 1.1; a paragraph line ≈ font-size × 1.45; a table row ≈ 2.1 × font-size per text line; cards add their padding. Text wraps only at spaces; a line holds about (box width) / (0.6 × font-size) characters. Keep titles ≤ 38 characters at 68px. If content does not fit, cut words; nothing shrinks.
- Minimum font-size anywhere: 24px. Body 26px, cards 25 a 26px, eyebrow 24px, h2 68px (60px on debrief slides), frase clave 36px.
- Footer: one pinned row at bottom:64px: left `<p style="position:absolute; left:128px; bottom:64px; font-size:24px; color:#64748B">Learn: <a href="URL"><span style="color:#0E7490">short label</span></a></p>` and right page number `<p style="position:absolute; right:128px; bottom:64px; width:200px; text-align:right; font-size:24px; color:#64748B">N / TOTAL</p>`. Page numbers must be correct and sequential.
- x-icon names allowed (exact): Activity Book Chart Chat Check CheckCircle Clock Cloud Code Database Globe GraduationCap Home Key Lightbulb Lightning Link Lock PaperPlane Play Search Settings Star ThumbsUp Tool Trust Users Verified Warning Wrench.
- x-shape kinds: rect rounded ellipse diamond arrow-right arrow-left arrow-up arrow-down line. Arrows near 2:1 ratio (e.g. width:64px; height:32px).
- Never use em dashes or en dashes anywhere. Spanish text simple and direct; product terms in English. Bold only for key phrases.
- Escape `&` as `&amp;` inside text and URLs.

## Design tokens ("estilo claro (Light)")

- Paper #F6F8FB (default) and #FFFFFF (alternate content slides). Ink #0F172A. Body text #334155 / #475569. Muted #64748B. Borders #E2E8F0.
- Accent for eyebrows and links: #0E7490. Frase clave band: background #FFF1E6, text #9A3412, Manrope 36px 700.
- Punch slides: cyan #22D3EE with ink text (the "preguntas" statement slide), lime #A3E635 with ink text (Kahoot intro). Two or three content slides may use ink background #0F172A with light text (#F6F8FB, cards #1E293B, accents #22D3EE and #A3E635) to vary rhythm.
- Cards: `background:#FFFFFF; border:2px solid #E2E8F0; border-radius:24px; padding:32px 36px` (on paper) or `background:#F6F8FB; border:2px solid #E2E8F0` (on white). Chips: `background:#FFFFFF; border:2px solid #CBD5E1; border-radius:999px; padding:8px 20px; font-size:24px`.
- Fonts: headings Manrope 800 (letter-spacing:-1px), body Inter, code JetBrains Mono. deck.json `faces` exactly as in the S2 example.
- Debrief (Kahoot) slides: left column = question card + 4 option rows (correct one: `background:#ECFDF5; border:3px solid #10B981` with `<x-icon name="CheckCircle" style="color:#059669; width:34px; height:34px">`; others: letter in #94A3B8 700), right column width 640px ink card (#0F172A) titled "Por qué" in #22D3EE with the correct reason and one line per wrong option.
- Vary layouts across trap slides: two cards, three-step row with arrows, a comparison table, a ladder of bands, a 2x2 grid with icons. Do not repeat the same layout more than twice in a row.

## Deck structure (content slides)

1. `cover`: light paper, big cyan/lime/ink circles pinned at right, eyebrow pills, h1 124px module name, weight line, presenter line "Sil Gaitán" and "Skills outline vigente: 27 abril 2026".
2. `agenda`: 4 timing cards (5' mapa, 18' trampas, 18' Kahoot, 4' cierre) with session-specific wording.
3. `mN-overview`: big weight number card + 2x2 grid of the 4 subdomains (from the outline) with "Trampas X, Y" mention.
4. `four` (or `three`): cyan statement slide with the "preguntas mágicas" from the tips file's "Objetivo de la sesión" paragraph.
5. Trap slides `t-*`: follow the tips file's "Orden sugerido de slides" table (10 slides covering 12 traps). Each: eyebrow "Trampa N · subdominio", short h2, frase clave band (from tips), 2 or 3 rules (from tips, condensed), "Delata" chips or line, footer with 1 or 2 clickable Learn links (from tips) and page number, aside notes (objetivo, frase clave, delata, practican Qx, tiempo).
6. `kahoot-intro`: lime statement slide.
7. `k01`..`k10`: debrief slides for 10 questions chosen from the bank (choose single-answer multiple choice or select-two rewritten as single; cover different traps; prefer the questions the tips file lists under "Practica"). Each question rewritten SHORT for Kahoot: question ≤ 120 characters, each of the 4 answers ≤ 75 characters, in English; explanations in Spanish from the bank's "Por qué" sections. Eyebrow: "Kahoot n de 10 · Trampa X · Banco Qn".
8. `week`: ink slide, 3 cards: estudia el siguiente módulo, repasa este, un aviso relevante.
9. `resources`: 2x3 grid of cards each with a Link icon, title and a clickable Learn link (study guide, practice assessment, learning path of this module, one or two module-specific pages, labs index).

## Also write

`<ROOT>/kahoot.json`: a JSON list of the 10 Kahoot questions in deck order: `[{"q": "...", "a": ["...","...","...","..."], "t": 60, "correct": 1}]` (correct = 1..4 position in the answers list; time 30 or 60). Keep the same order and the same text as the debrief slides.

## Validate before finishing

Run this and fix anything it reports:

```
python3 - <<'EOF'
import glob,re,json,sys
from xml.dom import minidom
ROOT='<ROOT>'
order=json.load(open(ROOT+'/project/deck.json'))['order']
files=[f.split('/')[-1][:-5] for f in glob.glob(ROOT+'/project/slides/*.html')]
print("missing:",[o for o in order if o not in files],"extra:",[f for f in files if f not in order])
bad=[]
for f in glob.glob(ROOT+'/project/slides/*.html'):
    t=open(f,encoding='utf-8').read()
    if '—' in t or '–' in t: bad.append((f,'dash'))
    try: minidom.parseString('<root>'+t.replace('<br>','<br/>')+'</root>')
    except Exception as e: bad.append((f,str(e)[:80]))
    if re.search(r'<section id="([^"]+)"',t).group(1)!=f.split('/')[-1][:-5]: bad.append((f,'id'))
    if t.count('<aside>')!=1: bad.append((f,'aside'))
    for s in re.findall(r'font-size:(\d+)px',t):
        if int(s)<24: bad.append((f,'font '+s))
    if re.search(r'<a [^>]*style=',t): bad.append((f,'style on a'))
    if 'class=' in t or '<style' in t: bad.append((f,'class/style'))
print(bad or "all ok", len(files), "files")
EOF
```

Reply with: the ROOT path, the slide order, the 10 Kahoot question ids used, and anything you could not fit.
