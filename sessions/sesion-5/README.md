# Sesión 5 · Labs, estrategia y simulacro · kit completo

| Pieza | Archivo | Para quién |
|---|---|---|
| Deck (19 slides: estrategia por tipo de pregunta, 10 labs en imágenes con 20 capturas oficiales de Learn, simulacro y ritual post-examen) | [dist/decks/S5-Labs-estrategia-simulacro.pdf](../../dist/decks/S5-Labs-estrategia-simulacro.pdf) (fuente editable en deck-source/, notas en notas-presentador.md) | Presenter |
| Simulacro de 30 preguntas (26 páginas: hoja de respuestas, preguntas, respuestas con explicación) | [dist/guias/S5-Simulacro-30-preguntas.pdf](../../dist/guias/S5-Simulacro-30-preguntas.pdf) | Estudiantes, se hace ANTES de la sesión, 45 min |
| Labs en imágenes, guía larga | [content/labs/labs-en-imagenes.md](../../content/labs/labs-en-imagenes.md) | Estudiantes que quieran el paso a paso completo con las 71 capturas |
| Capturas descargadas | img/ | Las 20 que usa el deck |
| Selección del simulacro | simulacro.json | 8 M1, 8 M2, 7 M3, 7 M4, ninguna usada en los Kahoots |

## Run of show (45 minutos)

| Min | Bloque | Slides |
|---|---|---|
| 0 a 8 | Datos duros, cómo piensa el examen, estrategia por tipo de pregunta | 1 a 5 |
| 8 a 30 | Los 10 labs en imágenes: objetivo, ruta, pasos, trampas | 6 a 16 |
| 30 a 40 | Debrief del simulacro: los dominios con menos aciertos del grupo | 17 |
| 40 a 45 | Ritual post-examen y cierre | 18 a 19 |

## Cómo usar el simulacro

1. Se manda con la guía de la sesión 4. Cada quien lo hace en 45 minutos, sin apuntes, y anota sus respuestas en la hoja.
2. Califica con la sección de respuestas: 21 de 30 es la meta. Yes/No series, select two y drag/order cuentan todo o nada.
3. En la sesión 5 cada quien dice su dominio más flojo; el presenter dedica el debrief a las trampas de ese dominio.

Regenerar: `python3 tools/build_simulacro.py` y luego `python3 tools/render_pdf.py` (lee simulacro.json y los cuatro bancos).
