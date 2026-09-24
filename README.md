# SC-300 Tips and Tricks

Curso comunitario, en español, para preparar el examen **SC-300: Microsoft Identity and Access Administrator**. Cinco sesiones de 45 minutos con modelo invertido: estudias con la guía y el banco de preguntas por tu cuenta, y en vivo se cazan trampas y se juega Kahoot con el porqué de cada distractor.

> **Sin dumps.** Todo el contenido es original. Cada afirmación está anclada a Microsoft Learn con links directos a los párrafos (608 links únicos). No hay preguntas del examen real ni material filtrado, y las contribuciones que lo incluyan se rechazan. Ver [CONTRIBUTING.md](CONTRIBUTING.md).

Este proyecto no está afiliado a Microsoft ni respaldado por Microsoft. SC-300, Microsoft Entra y Microsoft Learn son marcas de Microsoft. Basado en el skills outline oficial vigente al 27 de abril de 2026.

## Qué hay

| Sesión | Deck | Guía del estudiante | Kahoot | Notas del presentador |
|---|---|---|---|---|
| 1 · Identities (20 a 25%) | [PDF](dist/decks/S1-Identities.pdf) · [fuente](sessions/sesion-1/deck-source) | [PDF, 40 preguntas](dist/guias/S1-M1-Guia-del-estudiante.pdf) | [xlsx](sessions/sesion-1/S1-M1-Kahoot.xlsx) | [md](sessions/sesion-1/notas-presentador.md) |
| 2 · Authentication and access (25 a 30%) | [PDF](dist/decks/S2-Authentication-and-access.pdf) · [fuente](sessions/sesion-2/deck-source) | [PDF, 44 preguntas](dist/guias/S2-M2-Guia-del-estudiante.pdf) | [xlsx](sessions/sesion-2/S2-M2-Kahoot.xlsx) | [md](sessions/sesion-2/notas-presentador.md) |
| 3 · Workload identities (20 a 25%) | [PDF](dist/decks/S3-Workload-identities.pdf) · [fuente](sessions/sesion-3/deck-source) | [PDF, 40 preguntas](dist/guias/S3-M3-Guia-del-estudiante.pdf) | [xlsx](sessions/sesion-3/S3-M3-Kahoot.xlsx) | [md](sessions/sesion-3/notas-presentador.md) |
| 4 · Identity governance (20 a 25%) | [PDF](dist/decks/S4-Identity-governance.pdf) · [fuente](sessions/sesion-4/deck-source) | [PDF, 40 preguntas](dist/guias/S4-M4-Guia-del-estudiante.pdf) | [xlsx](sessions/sesion-4/S4-M4-Kahoot.xlsx) | [md](sessions/sesion-4/notas-presentador.md) |
| 5 · Labs, estrategia y simulacro | [PDF](dist/decks/S5-Labs-estrategia-simulacro.pdf) · [fuente](sessions/sesion-5/deck-source) | [Simulacro de 30 preguntas](dist/guias/S5-Simulacro-30-preguntas.pdf) | | [md](sessions/sesion-5/notas-presentador.md) |

En números: 164 preguntas originales estilo examen (en inglés, con explicación por distractor en español), 48 trampas con frase clave, 10 labs oficiales explicados en imágenes con 71 capturas de Microsoft Learn, 10 diagramas, 4 Kahoots y un simulacro.

## Cómo usarlo

**Si vas a estudiar solo:** baja la guía del módulo, léela (20 minutos), contesta el banco sin ver respuestas (90 minutos) y revisa el "por qué las otras no". Repite con los cuatro módulos, haz el simulacro y el [practice assessment oficial](https://learn.microsoft.com/credentials/certifications/exams/sc-300/practice/assessment?assessment-type=practice&assessmentId=60), que es gratis.

**Si vas a dar el curso:** cada carpeta `sessions/sesion-N` trae un README con el run of show de 45 minutos, el deck, las notas del presentador (objetivo y frases clave, no un guion) y el Kahoot listo para importar. Manda la guía una semana antes de cada sesión.

**Cómo piensa el examen** (lo que el curso enseña antes que cualquier concepto): te da tres datos y te pregunta por el cuarto; "least privilege" es el rol más chico que alcanza; "minimize administrative effort" es la opción más automática; los Yes/No en serie son independientes; los labs se califican por estado final. El detalle está en [plan/00-plan.md](plan/00-plan.md).

## Estructura del repositorio

```
plan/        00-plan.md (diseño del curso, playbook, ritual post-examen) y DECK-SPEC.md (formato de los decks)
content/     fuente de verdad: banco/ (preguntas), sources/ (deep links por skill), modulos/ (trampas), labs/, visuals/
sessions/    un kit por sesión: deck-source, Kahoot, notas del presentador, README con run of show
tools/       build_guia.py, build_simulacro.py, render_pdf.py, render_deck.py
dist/        PDFs generados: guías, simulacro y decks
```

Regenerar todo:

```bash
pip install markdown openpyxl playwright && playwright install chromium
python3 tools/build_guia.py M1        # también M2, M3, M4
python3 tools/build_simulacro.py
python3 tools/render_pdf.py           # HTML de dist/guias a PDF
python3 tools/render_deck.py sessions/sesion-1/deck-source dist/decks/S1-Identities.pdf
```

## Contribuir

Las tres formas que más ayudan, en orden:

1. **Debrief después de tu examen** (issue): qué dominios pesaron, qué tipo de escenarios costaron, qué labs salieron. Por tema, nunca preguntas literales. Con eso se reponderan las trampas.
2. **Una pregunta nueva** (pull request): escenario original, cuatro opciones, por qué la correcta es correcta, por qué cada distractor no, y el link a Learn que lo respalda.
3. **Un link roto o un dato que cambió** (issue): Learn cambia seguido; el outline y las risk policies de ID Protection cambiaron en 2026.

Reglas completas en [CONTRIBUTING.md](CONTRIBUTING.md).

## Vigencia

Revisar antes de cada cohort: el skills outline (cambió el 27 de abril de 2026), las risk policies legacy de ID Protection (se retiran el 1 de octubre de 2026; todo va por Conditional Access), passkey profiles y registration campaigns. La lista está en [plan/00-plan.md](plan/00-plan.md), sección 7b.

## Licencia

Código (`tools/`): [MIT](LICENSE). Contenido (preguntas, guías, decks, diagramas): [CC BY 4.0](LICENSE-CONTENT.md). Las capturas de pantalla y los labs citados son de Microsoft Learn y del repositorio MicrosoftLearning, con sus propias licencias; ver [ATTRIBUTION.md](ATTRIBUTION.md).

Este material nació en Bright Minds, una iniciativa de estudio entre pares, y se publica aquí para que cualquiera lo use y lo mejore.
