import re, json, markdown, html, pathlib
BASE = pathlib.Path(__file__).resolve().parents[1]
SEL = json.load(open(BASE / 'sessions/sesion-5/simulacro.json'))
md = lambda s: markdown.markdown(s, extensions=['tables', 'fenced_code'])

def fix_lists(s):
    out, prev = [], ''
    for line in s.split('\n'):
        if line.startswith('- ') and prev.strip() and not prev.startswith('- '):
            out.append('')
        out.append(line); prev = line
    return '\n'.join(out)

NAMES = {'M1': 'Identities', 'M2': 'Authentication and access', 'M3': 'Workload identities', 'M4': 'Identity governance'}
items = []
n = 0
for mod, ids in SEL.items():
    banco = (BASE / f'content/banco/{mod}-banco.md').read_text(encoding='utf-8')
    chunks = re.split(r'\n(?=## Subdominio |### Case study|### Q\d+ ·)', banco)
    qmap = {}
    for c in chunks:
        m = re.match(r'### (Q\d+) · (.+?) · (.+)', c.strip())
        if m: qmap[m.group(1)] = (m.group(2), m.group(3), re.sub(r'\n---\s*$', '', c.strip()))
    for qid in ids:
        skill, fmt, body = qmap[qid]
        body = body.split('\n', 1)[1]
        qpart, apart = body.split('**Respuesta:**', 1)
        qpart = fix_lists(re.sub(r'^([A-G]\. .+)$', r'\1  ', qpart, flags=re.M))
        n += 1
        items.append((n, mod, qid, skill, fmt, md(qpart.strip()), md(fix_lists('**Respuesta:**' + apart))))

CSS = (BASE / 'tools/build_guia.py').read_text(encoding='utf-8').split("CSS = '''")[1].split("'''")[0]
CSS += """
.sheet { border: 1.5px solid #E2E8F0; border-radius: 10pt; padding: 10pt 14pt; margin: 10pt 0; page-break-inside: avoid }
.sheet table td { padding: 5pt 8pt }
.score { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8pt }
.score .box { margin: 0; text-align: center }
.score b { font-size: 16pt; color: #0F172A }
"""

cover = '''
<div class="cover">
  <div>
    <p class="eyebrow">SC-300 Tips and Tricks · SC-300 · Sesión 5 de 5</p>
    <h1>Simulacro<br>30 preguntas</h1>
    <p class="big">8 de Identities, 8 de Authentication and access, 7 de Workload identities, 7 de Identity governance. En inglés, como el examen.</p>
    <p class="big"><b>45 minutos, sin apuntes.</b> Anota tus respuestas en la hoja de la página siguiente. Las respuestas y explicaciones van al final; no las mires hasta terminar.</p>
  </div>
  <div>
    <p class="meta"><span class="pill">Meta</span> 21 de 30 (70%). El examen real califica en escala ajustada a 700 de 1000, así que 70% es una referencia, no una garantía.</p>
    <p class="meta">Yes/No series, select two y drag/order cuentan todo o nada, como en el examen.</p>
  </div>
</div>
'''

sheet_rows = ''.join(f'<tr><td>{i}</td><td>{mod}</td><td style="width:38%"></td><td style="width:12%"></td></tr>' for i, mod, *_ in items)
sheet = f'''
<h2>Hoja de respuestas</h2>
<div class="sheet">
<table><tr><th style="width:8%">#</th><th style="width:12%">Dominio</th><th>Tu respuesta</th><th>Correcta</th></tr>{sheet_rows}</table>
</div>
<div class="score">
  <div class="box"><b>M1</b><p>___ de 8</p></div>
  <div class="box"><b>M2</b><p>___ de 8</p></div>
  <div class="box"><b>M3</b><p>___ de 7</p></div>
  <div class="box"><b>M4</b><p>___ de 7</p></div>
</div>
<p class="meta">Cómo leer tu resultado: el dominio con menos aciertos es el que estudias primero. Lleva la hoja al debrief de la sesión 5.</p>
'''

qhtml = ''.join(f'<div class="q"><div class="q-h"><span class="qid">{i}</span><span class="fmt">{html.escape(fmt)}</span><span class="skill-tag">{mod} · {qid} · {html.escape(skill)}</span></div>{q}</div>' for i, mod, qid, skill, fmt, q, a in items)
ahtml = ''.join(f'<div class="a"><div class="q-h"><span class="qid">{i}</span><span class="fmt">{html.escape(fmt)}</span><span class="skill-tag">{mod} · {qid}</span></div>{a}</div>' for i, mod, qid, skill, fmt, q, a in items)

doc = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SC-300 Tips and Tricks · Simulacro</title><style>{CSS}</style></head><body>
{cover}
{sheet}
<h2>Preguntas</h2>
<p class="meta">30 preguntas tomadas de los bancos de los cuatro módulos, ninguna usada en los Kahoots. Los ids (M2 · Q15) te llevan a la guía del módulo si quieres profundizar.</p>
{qhtml}
<h2>Respuestas y explicaciones</h2>
<p class="meta">Lee el "por qué las otras no" incluso en las que acertaste: ahí está la diferencia entre acertar por suerte y acertar por método.</p>
{ahtml}
</body></html>'''
out = BASE / 'dist/guias/S5-Simulacro-30-preguntas.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(doc, encoding='utf-8')
print(len(items), 'questions', len(doc) // 1024, 'KB')
