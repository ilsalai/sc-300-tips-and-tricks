import re, markdown, html, pathlib, sys
MOD = sys.argv[1] if len(sys.argv)>1 else 'M1'
CFG = {
 'M1': dict(num='1', name='Identities', full='Implement and manage user identities', weight='20 a 25%', visuals=['04-phs-pta-federation.svg','09-external-identities-map.svg','05-cloud-sync-vs-connect-sync.svg'], captions=['<b>Si se cae on-prem.</b> PHS sigue funcionando; PTA y federación no. El cambio de sign-in method en Entra Connect es manual.','<b>Dirección.</b> El trust MFA es inbound y vive en el tenant de recursos. En cross-tenant sync el source empuja y el target solo abre la puerta.','<b>Connect Sync vs Cloud Sync.</b> Forest desconectado o varios agentes activos: Cloud Sync. Hybrid join, PTA o reglas complejas: Connect Sync.'], magic='Alcance, dirección y dependencia de on-prem', magic_items=['<b>Alcance:</b> ¿quién puede hacer qué, y sobre quién? (AU, restricted AU, custom role, matriz de reset)','<b>Dirección:</b> ¿en qué tenant y de qué lado se configura? (inbound vs outbound, source vs target, member vs guest)','<b>Dependencia de on-prem:</b> ¿qué deja de funcionar si se cae AD? (PTA y federación sí, PHS no)'], nextmod='sesión 2 (Authentication and access, 25 a 30% del examen)', nextbank='M2 y empecé su banco de 44 preguntas', nq='40', session='1'),
 'M2': dict(num='2', name='Authentication and access', full='Implement authentication and access management', weight='25 a 30%', visuals=['01-ca-evaluation-flow.svg','02-user-risk-vs-signin-risk.svg'], captions=['<b>Cómo evalúa Conditional Access.</b> Señales, decisión y sesión. Si ninguna política dispara un control, el token se emite. Report-only y What If para probar; break-glass siempre excluido.','<b>Riesgo.</b> User risk se cura con password o Require risk remediation; sign-in risk se cura con MFA. Nunca al revés y nunca en la misma policy. Las legacy se retiran el 1 de octubre de 2026.'], magic='Método, política, riesgo y tráfico', magic_items=['<b>Método:</b> ¿qué tan fuerte es? MFA, passwordless o phishing-resistant, y dónde se configura cada uno.','<b>Política:</b> ¿qué decide? Si nadie dice que no, el token sale. El block, el break-glass y el context se diseñan a propósito.','<b>Riesgo:</b> ¿cuál es y cómo se cura? User risk con password o risk remediation, sign-in risk con MFA, workload identities con otra licencia.','<b>Tráfico:</b> ¿por dónde pasa? Microsoft, Private o Internet profile, y qué agrega cada uno.'], nextmod='sesión 3 (Workload identities, 20 a 25% del examen)', nextbank='M3 y empecé su banco de 40 preguntas', nq='44', session='2'),
 'M3': dict(num='3', name='Workload identities', full='Plan and implement workload identities', weight='20 a 25%', visuals=['03-app-registration-vs-enterprise-app.svg'], captions=['<b>App registration vs enterprise application.</b> El application object vive en el home tenant; el service principal existe en cada tenant donde se usa la app. Delegated permissions las consiente el usuario; application permissions solo un admin.'], magic='Objeto, identidad, consentimiento y control', magic_items=['<b>Objeto:</b> ¿es el application object (app registration) o el service principal (enterprise app)? Cada uno guarda cosas distintas.','<b>Identidad:</b> ¿managed identity, service principal o cuenta? System-assigned muere con el recurso; user-assigned se comparte; fuera de Azure la managed identity no llega sin Arc.','<b>Consentimiento:</b> ¿delegated o application? ¿user consent o admin consent? Quién puede consentir decide la respuesta.','<b>Control:</b> ¿lo hace Entra (assignment, roles, App Proxy) o Defender for Cloud Apps (discovery, session policies)?'], nextmod='sesión 4 (Identity governance, 20 a 25% del examen)', nextbank='M4 y empecé su banco de 40 preguntas', nq='40', session='3'),
 'M4': dict(num='4', name='Identity governance', full='Plan and automate identity governance', weight='20 a 25%', visuals=['07-entitlement-management.svg','08-access-review-decisions.svg','06-pim-lifecycle.svg','10-logs-and-diagnostic-settings.svg'], captions=['<b>Entitlement management.</b> Catalog, access package, policy y el ciclo de vida del acceso, incluido el bloqueo y borrado del externo que pierde su último paquete.','<b>Access reviews.</b> Quién revisa, qué recomienda el sistema, y qué pasa cuando nadie responde con auto apply prendido.','<b>PIM.</b> Eligible, active y permanent; las perillas del rol (MFA, justificación, aprobación, duración) y el break-glass que vive fuera de PIM.','<b>Logs.</b> Cuánto duran según licencia, a dónde van con diagnostic settings y en qué tabla de Log Analytics caen.'], magic='Quién decide, cuándo pasa y dónde queda el dato', magic_items=['<b>¿Quién decide?</b> Catalog owner, access package manager, approver, reviewer, PIM approver: cada rol decide una cosa y ninguna otra.','<b>¿Cuándo pasa?</b> Al pedir, al aprobar, al expirar, al activar, cuando nadie responde: el examen pregunta por el momento exacto.','<b>¿Dónde queda el dato?</b> Sign-in, audit o provisioning logs; 7 o 30 días; Log Analytics, storage o Event Hub; SigninLogs o AuditLogs.'], nextmod='sesión 5 (labs en imágenes, estrategia de examen y simulacro de 30 preguntas)', nextbank='la sesión 5: repasé los 10 labs en imágenes e hice el simulacro', nq='40', session='4'),
}[MOD]

BASE = pathlib.Path(__file__).resolve().parents[1]
md = lambda s: markdown.markdown(s, extensions=['tables', 'fenced_code'])

# ---------- sources ----------
src = (BASE / f'content/sources/{MOD}-sources.md').read_text(encoding='utf-8')
subdomains = []
for part in re.split(r'^## Subdominio ', src, flags=re.M)[1:]:
    title = part.split('\n', 1)[0].strip()
    head = part.split('| Skill')[0]
    mods = re.findall(r'(https://learn\.microsoft\.com/training/modules/\S+)', head)
    mod = ', '.join(mods) if mods else ''
    rows = []
    for line in part.splitlines():
        if line.startswith('| ') and not line.startswith('| Skill') and not line.startswith('|---'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) == 4:
                links = [l.strip() for l in cells[3].split('<br>') if l.strip()]
                rows.append((cells[0], cells[1], cells[2], links))
    subdomains.append((title, mod, rows))

def linklabel(u):
    u = u.replace('https://learn.microsoft.com/', '')
    if '#' in u:
        page, anchor = u.split('#', 1)
        return f'{page.split("/")[-1]} <span class="anchor">#{anchor}</span>'
    return u.split('/')[-1] or u

def sources_html():
    out = []
    for i, (title, mod, rows) in enumerate(subdomains, 1):
        out.append(f'<h3 class="sub">Subdominio {html.escape(title)}</h3>')
        links = ' · '.join(f'<a href="{m}">{m.replace("https://learn.microsoft.com/training/modules/","").strip("/")}</a>' for m in mod.split(', ') if m)
        out.append(f'<p class="mod">Módulos oficiales en Learn: {links}</p>')
        for skill, punto, main, links in rows:
            li = ''.join(f'<li><a href="{l}">{linklabel(l)}</a></li>' for l in links)
            out.append(f'''<div class="skill">
  <div class="skill-h"><span class="tag">Skill</span> {html.escape(skill)}</div>
  <p class="punto">{md(punto)[3:-4]}</p>
  <p class="main">Link principal: <a href="{main}">{main.replace("https://learn.microsoft.com/","")}</a></p>
  <ul class="deep">{li}</ul>
</div>''')
    return '\n'.join(out)

# ---------- tips ----------
tips = (BASE / f'content/modulos/{MOD}-tips.md').read_text(encoding='utf-8')
trap_blocks = re.split(r'^## Trampa ', tips, flags=re.M)[1:]
traps = []
for b in trap_blocks:
    if b.startswith('Objetivo') : continue
    head = b.split('\n', 1)[0]
    num, name = head.split('.', 1)
    frase = re.search(r'Frase clave: \*\*(.+?)\*\*', b).group(1)
    regla = re.search(r'Regla:\n((?:- .+\n?)+)', b).group(1)
    delata = re.search(r'Palabras que delatan: (.+)', b).group(1)
    link = re.search(r'Link: (\S+)', b).group(1)
    practica = re.search(r'Practica: (.+)', b).group(1)
    traps.append((num.strip(), name.strip(), frase, regla, delata, link, practica))
objetivo = re.search(r'## Objetivo de la sesión\n\n(.+?)\n\n---', tips, flags=re.S).group(1)

def tips_html():
    out = []
    for num, name, frase, regla, delata, link, practica in traps:
        out.append(f'''<div class="trap">
  <div class="trap-h"><span class="num">{num}</span> {html.escape(name)}</div>
  <p class="frase">{html.escape(frase)}</p>
  {md(regla)}
  <p class="delata"><b>Palabras que delatan:</b> {html.escape(delata)}</p>
  <p class="meta">Learn: <a href="{link}">{linklabel(link)}</a> · Practica con {html.escape(practica)}</p>
</div>''')
    return '\n'.join(out)

# ---------- banco ----------
banco = (BASE / f'content/banco/{MOD}-banco.md').read_text(encoding='utf-8')
blocks = []
for chunk in re.split(r'\n(?=## Subdominio |### Case study|### Q\d+ ·)', banco):
    chunk = chunk.strip()
    chunk = re.sub(r'\n---\s*$', '', chunk).strip()
    blocks.append(chunk)
def fix_lists(s):
    out, prev = [], ''
    for line in s.split('\n'):
        if line.startswith('- ') and prev.strip() and not prev.startswith('- '):
            out.append('')
        out.append(line); prev = line
    return '\n'.join(out)

questions, answers = [], []
current_sub = None
for b in blocks:
    if b.startswith('## Subdominio'):
        current_sub = b.split('\n', 1)[0].replace('## ', '')
        questions.append(('sub', current_sub)); answers.append(('sub', current_sub)); continue
    if b.startswith('### Case study'):
        questions.append(('case', md(fix_lists(b.replace('### ', '#### '))))); continue
    m = re.match(r'### (Q\d+) · (.+?) · (.+)', b)
    if not m: continue
    qid, skill, fmt = m.groups()
    body = b.split('\n', 1)[1]
    qpart, apart = body.split('**Respuesta:**', 1)
    qpart = fix_lists(re.sub(r'^([A-G]\. .+)$', r'\1  ', qpart, flags=re.M))
    apart = fix_lists('**Respuesta:**' + apart)
    questions.append(('q', qid, skill, fmt, md(qpart.strip())))
    answers.append(('a', qid, fmt, md(apart)))

def banco_html():
    out = []
    for item in questions:
        if item[0] == 'sub': out.append(f'<h3 class="sub">{html.escape(item[1])}</h3>')
        elif item[0] == 'case': out.append(f'<div class="case">{item[1]}</div>')
        else:
            _, qid, skill, fmt, body = item
            out.append(f'<div class="q"><div class="q-h"><span class="qid">{qid}</span><span class="fmt">{html.escape(fmt)}</span><span class="skill-tag">{html.escape(skill)}</span></div>{body}</div>')
    return '\n'.join(out)

def answers_html():
    out = []
    for item in answers:
        if item[0] == 'sub': out.append(f'<h3 class="sub">{html.escape(item[1])}</h3>')
        else:
            _, qid, fmt, body = item
            out.append(f'<div class="a"><div class="q-h"><span class="qid">{qid}</span><span class="fmt">{html.escape(fmt)}</span></div>{body}</div>')
    return '\n'.join(out)

# ---------- visuals ----------
def svg(name):
    s = (BASE / 'content/visuals' / name).read_text(encoding='utf-8')
    s = re.sub(r'<\?xml[^>]*\?>', '', s)
    return s

CSS = '''
@page { size: A4; margin: 16mm 14mm; }
* { box-sizing: border-box }
body { font-family: "Segoe UI", Inter, Arial, sans-serif; color: #1E293B; line-height: 1.5; font-size: 10.5pt; margin: 0 }
a { color: #0E7490; text-decoration: none; word-break: break-all }
h1 { font-size: 30pt; color: #0B1F3A; margin: 0 0 6pt; line-height: 1.1 }
h2 { font-size: 20pt; color: #0F172A; margin: 30pt 0 10pt; padding-bottom: 6pt; border-bottom: 3px solid #22D3EE; page-break-after: avoid; letter-spacing: -0.3px }
h3.sub { font-size: 13.5pt; color: #0E7490; margin: 18pt 0 6pt; page-break-after: avoid }
h4 { margin: 0 0 4pt; color: #0B1F3A }
p { margin: 4pt 0 }
ul, ol { margin: 4pt 0 4pt 18pt; padding: 0 }
li { margin: 2pt 0 }
code { font-family: Consolas, "JetBrains Mono", Menlo, monospace; font-size: 9pt; background: #F1F5F9; padding: 1px 4px; border-radius: 3px }
table { border-collapse: collapse; width: 100%; margin: 6pt 0; font-size: 9.5pt }
th, td { border: 1px solid #CBD5E1; padding: 4pt 6pt; vertical-align: top; text-align: left }
th { background: #0B1F3A; color: #fff }
.cover { background: #0B1F3A; color: #F1F5F9; padding: 36pt 32pt; border-radius: 14pt; margin-bottom: 18pt; page-break-after: always; min-height: 240mm; display: flex; flex-direction: column; justify-content: space-between }
.cover h1 { color: #fff; font-size: 40pt }
.cover .eyebrow { color: #22D3EE; letter-spacing: 3px; text-transform: uppercase; font-weight: 700; font-size: 10pt }
.cover .big { font-size: 15pt; color: #BFD8F0 }
.cover .meta { color: #94A3B8; font-size: 10pt }
.pill { display: inline-block; background: #22D3EE; color: #0B1F3A; font-weight: 700; padding: 3pt 10pt; border-radius: 999px; font-size: 9pt; margin-right: 6pt }
.box { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 10pt; padding: 10pt 14pt; margin: 8pt 0; page-break-inside: avoid }
.box.cyan { border-color: #22D3EE; background: #ECFEFF }
.box.amber { border-color: #FBBF24; background: #FFFBEB }
.grid3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8pt }
.grid3 .box { margin: 0 }
.mod { font-size: 9.5pt; color: #475569; margin-bottom: 8pt }
.skill { border: 1px solid #E2E8F0; border-radius: 8pt; padding: 8pt 12pt; margin: 6pt 0; page-break-inside: avoid }
.skill-h { font-weight: 700; color: #0B1F3A; margin-bottom: 3pt }
.tag { display: inline-block; background: #0B1F3A; color: #22D3EE; font-size: 8pt; padding: 1pt 6pt; border-radius: 4px; margin-right: 6pt; letter-spacing: 1px }
.punto { margin: 3pt 0 }
.main { font-size: 9.5pt; color: #475569 }
.deep { font-size: 9.5pt; margin-left: 16pt }
.anchor { color: #94A3B8 }
.trap { border: 1.5px solid #E2E8F0; border-radius: 12pt; padding: 12pt 16pt; margin: 10pt 0; page-break-inside: avoid; background: #fff }
.trap-h { font-weight: 700; font-size: 12.5pt; color: #0B1F3A }
.num { display: inline-block; width: 22pt; height: 22pt; line-height: 22pt; text-align: center; background: #0B1F3A; color: #22D3EE; border-radius: 50%; font-size: 10.5pt; margin-right: 6pt }
.frase { font-size: 12.5pt; color: #9A3412; font-weight: 700; margin: 6pt 0; background: #FFF1E6; padding: 6pt 10pt; border-radius: 8pt }
.delata { font-size: 9.5pt }
.meta { font-size: 9pt; color: #64748B }
.visual { margin: 10pt 0 14pt; page-break-inside: avoid }
.visual svg { width: 100%; height: auto; border-radius: 10pt }
.visual p { font-size: 9.5pt; color: #475569; margin-top: 4pt }
.case { background: #FFFBEB; border: 1px solid #FBBF24; border-radius: 8pt; padding: 8pt 12pt; margin: 8pt 0; page-break-inside: avoid }
.q, .a { border: 1.5px solid #E2E8F0; border-radius: 10pt; padding: 10pt 14pt; margin: 9pt 0; page-break-inside: avoid }
.a { background: #F8FAFC }
.q-h { display: flex; gap: 6pt; align-items: center; margin-bottom: 4pt; flex-wrap: wrap }
.qid { font-weight: 800; color: #0B1F3A; font-size: 12pt }
.fmt { background: #ECFEFF; color: #0E7490; font-size: 8.5pt; padding: 1pt 7pt; border-radius: 999px; font-weight: 600 }
.skill-tag { color: #64748B; font-size: 8.5pt }
.checklist li { list-style: none; margin: 4pt 0 }
.checklist li:before { content: "\\2610\\00a0\\00a0"; color: #0E7490 }
.toc { columns: 2; font-size: 10pt }
.toc li { margin: 2pt 0 }
'''

cover = f'''
<div class="cover">
  <div>
    <p class="eyebrow">SC-300 Tips and Tricks · SC-300 · Sesión {CFG['session']} de 5</p>
    <h1>Guía del estudiante<br>Módulo {CFG['num']}: {CFG['name']}</h1>
    <p class="big">{CFG['full']}. {CFG['weight']} del examen.</p>
    <p class="big">Modelo invertido: <b>esta guía se estudia antes de la sesión</b>. En vivo cazamos trampas y jugamos Kahoot con el porqué de cada distractor.</p>
  </div>
  <div>
    <p class="meta"><span class="pill">Sin dumps</span> Todo el contenido es original y está anclado a Microsoft Learn con links directos a los párrafos. Skills outline vigente: 27 de abril de 2026.</p>
    <p class="meta">Contiene: mapa de skills con deep links · 12 trampas con frase clave · 3 visuales · {CFG['nq']} preguntas estilo examen con explicación por distractor · plan de la semana y ritual post-examen.</p>
  </div>
</div>
'''

howto = f'''
<h2>0. Cómo usar esta guía (20 minutos de lectura, 90 de práctica)</h2>
<div class="grid3">
  <div class="box cyan"><b>1. Lee el mapa</b><p>Sección 1. Un punto clave por skill del outline. Si algo no te suena, abre el deep link: cae justo en el párrafo que el examen pregunta.</p></div>
  <div class="box cyan"><b>2. Aprende las 12 trampas</b><p>Sección 2. Cada una trae la frase que la resume, la regla, y las palabras de la pregunta que la delatan.</p></div>
  <div class="box cyan"><b>3. Contesta el banco sin ver respuestas</b><p>Sección 4. Anota tus respuestas. Luego revisa la sección 5 y lee el "por qué las otras no": ahí está el valor.</p></div>
</div>
<div class="box amber">
  <b>Las preguntas que resuelven casi todo M{CFG['num']}: {CFG['magic']}.</b> Cuando no sepas la respuesta, pregúntate:
  <ol>{''.join('<li>'+i+'</li>' for i in CFG['magic_items'])}</ol>
  Con eso eliminas dos distractores en la mayoría de las preguntas del módulo.
</div>
<div class="box">
  <b>Datos duros del examen.</b> 700 de 1000 para pasar (escala ajustada, no 70% de aciertos). Practice assessment oficial gratis:
  <a href="https://learn.microsoft.com/credentials/certifications/exams/sc-300/practice/assessment?assessment-type=practice&amp;assessmentId=60">learn.microsoft.com/credentials/certifications/exams/sc-300/practice/assessment</a>.
  Exam sandbox: <a href="https://aka.ms/examdemo">aka.ms/examdemo</a>. Study guide oficial:
  <a href="https://learn.microsoft.com/credentials/certifications/resources/study-guides/sc-300">learn.microsoft.com/credentials/certifications/resources/study-guides/sc-300</a>.
</div>
'''

visuals = '<h2>3. Visuales para no olvidar</h2>' + ''.join(f'<div class="visual">{svg(v)}<p>{c}</p></div>' for v,c in zip(CFG['visuals'],CFG['captions']))

closing = f'''
<h2>6. Plan de la semana y ritual post-examen</h2>
<div class="box cyan">
  <b>Checklist antes de la {CFG['nextmod']}</b>
  <ul class="checklist">
    <li>Leí el mapa y las 12 trampas de M{CFG['num']}.</li>
    <li>Contesté las {CFG['nq']} preguntas de M{CFG['num']} sin ver respuestas y revisé el "por qué las otras no".</li>
    <li>Anoté las preguntas que fallé para el Kahoot.</li>
    <li>Hice una vez el practice assessment oficial de Learn, sin estudiar antes.</li>
    <li>Recibí la guía de {CFG['nextbank']}.</li>
  </ul>
</div>
<div class="box amber">
  <b>Si presentas el examen esta semana: llena el debrief el mismo día.</b> Temas sí, preguntas no. Así el cohort acumula señal legítima y nadie arriesga su certificación.
  <table>
    <tr><th style="width:30%">Campo</th><th>Qué anotar</th></tr>
    <tr><td>Resultado</td><td>Pass o no pass y el score por dominio que trae el reporte</td></tr>
    <tr><td>Dominios que pesaron</td><td>Por sensación: cuál dominó y cuál casi no salió</td></tr>
    <tr><td>Escenarios que costaron</td><td>Por tema, por ejemplo "AU vs restricted AU", "cross-tenant sync con error de consent"</td></tr>
    <tr><td>Labs que salieron</td><td>Por tarea, por ejemplo "crear un AU y asignar un rol con scope", nunca pasos exactos</td></tr>
    <tr><td>Qué hubiera estudiado más</td><td>Libre, en dos líneas</td></tr>
  </table>
</div>
<div class="box"><b>Objetivo de la sesión en vivo, para que sepas qué esperar.</b> {md(objetivo)}</div>
'''

doc = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>SC-300 Tips and Tricks · Guía {MOD} {CFG['name']}</title><style>{CSS}</style></head><body>
{cover}
{howto}
<h2>1. Mapa del módulo: skills, punto clave y deep links</h2>
<p class="meta">Cada fila corresponde a un bullet del skills outline oficial. El punto clave es lo que el examen realmente mide; los deep links caen en el párrafo exacto de Learn.</p>
{sources_html()}
<h2>2. Las 12 trampas de M{CFG['num']}</h2>
<p class="meta">Memoriza la frase, entiende la regla, reconoce las palabras que delatan. Los números son para consultar, no para memorizar.</p>
{tips_html()}
{visuals}
<h2>4. Banco de preguntas: {CFG['nq']} preguntas estilo examen</h2>
<p class="meta">En inglés, como el examen. Contesta sin ver la sección 5. En las series Yes/No cada afirmación se evalúa sola; en drag/order solo cuentan las acciones que sí van, en orden. Los case studies aplican a las dos preguntas que los siguen.</p>
{banco_html()}
<h2>5. Respuestas y explicaciones</h2>
<p class="meta">Lee siempre el "por qué las otras no". El SC-300 se pierde en los distractores, no en la teoría.</p>
{answers_html()}
{closing}
</body></html>'''

out = BASE / 'dist/guias' / f'S{CFG["session"]}-{MOD}-Guia-del-estudiante.html'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(doc, encoding='utf-8')
print(len(doc) // 1024, 'KB', len(questions), 'question items', len(traps), 'traps', sum(len(r) for _, _, r in subdomains), 'skills')
