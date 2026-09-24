"""Renderiza un deck (sessions/sesion-N/deck-source) a PDF 1920x1080 con Chromium.
Uso: python3 tools/render_deck.py sessions/sesion-1/deck-source dist/decks/S1-Identities.pdf
Es una vista previa fiel del contenido: los slides fueron escritos en el formato del artifact
(HTML con estilos inline). Aquí se traducen x-shape, x-icon y las fuentes de Google al HTML normal.
"""
import asyncio, json, pathlib, re, sys
from playwright.async_api import async_playwright
BASE = pathlib.Path(__file__).resolve().parents[1]
ICONS = json.load(open(BASE / 'tools/icons.json'))
SHAPES = {
    'ellipse': 'border-radius:50%;',
    'rounded': 'border-radius:24px;',
    'rect': '',
    'diamond': 'clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%);',
    'arrow-right': 'clip-path:polygon(0 30%,60% 30%,60% 0,100% 50%,60% 100%,60% 70%,0 70%);',
    'arrow-left': 'clip-path:polygon(100% 30%,40% 30%,40% 0,0 50%,40% 100%,40% 70%,100% 70%);',
    'arrow-up': 'clip-path:polygon(30% 100%,30% 40%,0 40%,50% 0,100% 40%,70% 40%,70% 100%);',
    'arrow-down': 'clip-path:polygon(30% 0,30% 60%,0 60%,50% 100%,100% 60%,70% 60%,70% 0);',
    'line': 'height:4px;',
}

def shape(m):
    kind, style = m.group(1), m.group(2)
    return f'<div style="{style}; {SHAPES.get(kind, "")} flex:none"></div>'

def icon(m):
    name, style = m.group(1), m.group(2)
    color = re.search(r'color:\s*([^;]+)', style)
    svg = ICONS.get(name, ICONS['Star'])
    svg = svg.replace('<svg ', f'<svg style="color:{color.group(1) if color else "#000"}; display:block" ', 1)
    return f'<div style="{style}; flex:none">{svg}</div>'

def convert(section):
    s = re.sub(r'<x-shape kind="([^"]+)" style="([^"]*)"></x-shape>', shape, section)
    s = re.sub(r'<x-icon name="([^"]+)" style="([^"]*)"></x-icon>', icon, s)
    s = re.sub(r'<aside>.*?</aside>', '', s, flags=re.S)
    return s

def build(root):
    deck = json.load(open(root / 'deck.json'))
    fonts = ''.join(f'<link rel="stylesheet" href="{f["href"]}">' for f in deck['faces'].values() if 'href' in f)
    assets = json.load(open(root / 'assets.json')) if (root / 'assets.json').exists() else {}
    pages = []
    for sid in deck['order']:
        sec = (root / 'slides' / f'{sid}.html').read_text(encoding='utf-8')
        for blob, local in assets.items():
            sec = sec.replace(f'src="{blob}"', f'src="{(root / local).resolve().as_uri()}"')
        pages.append(f'<div class="page">{convert(sec)}</div>')
    css = '''
    * { box-sizing: border-box } html, body { margin:0; padding:0 }
    .page { width:1920px; height:1080px; overflow:hidden; page-break-after:always; position:relative }
    section { position:relative; width:1920px; height:1080px; margin:0 }
    h1,h2,h3,p,ul,ol { margin:0 } ul, ol { padding-left:1.2em } li { margin:0 }
    a { color:inherit; text-decoration:none } b { font-weight:700 }
    table { border-collapse:collapse; width:100% } th, td { border:1px solid rgba(120,130,150,0.35); padding:0.35em 0.6em; text-align:left; vertical-align:top }
    img { display:block }
    '''
    return f'<!doctype html><html><head><meta charset="utf-8">{fonts}<style>{css}</style></head><body>{"".join(pages)}</body></html>'

async def main(src, out):
    root = pathlib.Path(src); out = pathlib.Path(out); out.parent.mkdir(parents=True, exist_ok=True)
    html_path = out.with_suffix('.html'); html_path.write_text(build(root), encoding='utf-8')
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1920, 'height': 1080})
        await pg.goto(html_path.resolve().as_uri()); await pg.wait_for_timeout(2500)
        await pg.pdf(path=str(out), width='1920px', height='1080px', print_background=True, prefer_css_page_size=False, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'})
        await b.close()
    html_path.unlink(); print('ok', out)

if __name__ == '__main__':
    asyncio.run(main(sys.argv[1], sys.argv[2]))
