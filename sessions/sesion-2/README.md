# Sesión 2 · Authentication and access · kit completo (estilo nuevo)

| Pieza | Archivo | Para quién |
|---|---|---|
| Deck (28 slides, notas con objetivo y frases clave, links clicables) | [dist/decks/S2-Authentication-and-access.pdf](../../dist/decks/S2-Authentication-and-access.pdf) (fuente editable en deck-source/, notas en notas-presentador.md) | Presenter |
| Guía del estudiante (58 páginas) | [dist/guias/S2-M2-Guia-del-estudiante.pdf](../../dist/guias/S2-M2-Guia-del-estudiante.pdf) | Estudiantes, una semana antes |
| Kahoot (10 preguntas, plantilla oficial) | S2-M2-Kahoot.xlsx (y .csv) | Presenter |

## Estilo "estilo claro (Light)" (propuesta de revamp)

- Fondo claro (#F6F8FB y blanco), tinta #0F172A. Contraste alto en todo el texto.
- Un acento para navegación y links (teal #0E7490), un acento cálido para las frases clave (coral #9A3412 sobre #FFF1E6).
- Slides de "golpe" en cian (#22D3EE) y lima (#A3E635) con tinta oscura, y dos o tres slides en tinta oscura para variar el ritmo. No todo es congruente a propósito.
- Tipografías: Manrope (títulos, 800) e Inter (texto), JetBrains Mono para reglas y código.
- Menos texto por slide, tipografía de 26 px o más, tarjetas con aire.
- Todos los links de Learn son clicables: en cada trampa, en cada debrief y en el slide de recursos.

## Run of show (45 minutos)

| Min | Bloque | Slides |
|---|---|---|
| 0 a 5 | Agenda, mapa y las 4 preguntas (método, política, riesgo, tráfico) | 1 a 4 |
| 5 a 23 | 12 trampas en 11 slides | 5 a 15 |
| 23 a 41 | Kahoot y debrief de cada pregunta | 16 a 26 |
| 41 a 45 | Tarea de la semana y recursos | 27 a 28 |

## Kahoot

Preguntas cortas basadas en el banco: Q3, Q5, Q8, Q12, Q14, Q18, Q24, Q29, Q36, Q41. Los slides 17 a 26 son su debrief. Importar en kahoot.com: Create > Kahoot > Import spreadsheet > S2-M2-Kahoot.xlsx (plantilla oficial, preguntas en fila 9, columnas B a H).

## Regenerar la guía

```bash
python3 tools/build_guia.py M2
python3 tools/render_pdf.py dist/guias/S2-M2-Guia-del-estudiante.html
```
