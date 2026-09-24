# Sesión 1 · Identities · kit completo

| Pieza | Archivo | Para quién |
|---|---|---|
| Deck (29 slides, notas de presentador con objetivo y frases clave) | [dist/decks/S1-Identities.pdf](../../dist/decks/S1-Identities.pdf) (fuente editable en deck-source/, notas en notas-presentador.md) | Presenter |
| Guía del estudiante (47 páginas) | [dist/guias/S1-M1-Guia-del-estudiante.pdf](../../dist/guias/S1-M1-Guia-del-estudiante.pdf) | Estudiantes, se manda una semana antes |
| Kahoot (10 preguntas, plantilla oficial) | S1-M1-Kahoot.xlsx (y .csv de respaldo) | Presenter, se importa una vez |
| Generador de la guía | tools/build_guia.py | Para regenerar si cambia el banco o los tips |

## Run of show (45 minutos)

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0 a 3 | Kickoff | 1 a 2 | Modelo invertido: estudiaron antes, hoy cazamos trampas |
| 3 a 8 | Cómo piensa el examen | 3 a 4 | 700 puntos, pesos, las 6 frases de lectura |
| 8 a 11 | M1 en un vistazo | 5 a 6 | Cuatro subdominios y las 3 preguntas mágicas |
| 11 a 26 | Tips and tricks | 7 a 15 | 12 trampas en 9 slides, 1.5 min cada uno |
| 26 a 41 | Kahoot + debrief | 16 a 26 | 10 preguntas; después de cada una, su slide de "por qué" |
| 41 a 45 | Cierre | 27 a 29 | Tarea de la semana, ritual post-examen, recursos |

Cada slide trae en las notas: objetivo del slide, frase clave, trampa favorita del examen, qué preguntas del banco la practican y tiempo sugerido.

## Importar el Kahoot

1. En kahoot.com: Create > Kahoot > Add question > Import spreadsheet (o "Import questions").
2. Sube S1-M1-Kahoot.xlsx. Está sobre la plantilla oficial de Kahoot (preguntas en fila 9, columnas B a H).
3. Revisa que las 10 preguntas cargaron con su tiempo (60 s la mayoría, 30 s las cortas) y su respuesta correcta.

Las preguntas del Kahoot son versiones cortas (límite de 120 y 75 caracteres) de estas del banco: Q4, Q1, Q15, Q16, Q18, Q21, Q25, Q27, Q31, Q35. Los slides 17 a 26 del deck son el debrief de cada una.

## Regenerar la guía

```bash
python3 tools/build_guia.py M1
python3 tools/render_pdf.py dist/guias/S1-M1-Guia-del-estudiante.html
```

Lee content/sources, content/modulos, content/banco y content/visuals, y produce el HTML. El PDF se genera con Chromium (Playwright) en tamaño A4.
