# Sesión 4 · Identity governance · kit completo

| Pieza | Archivo | Para quién |
|---|---|---|
| Deck (27 slides, notas con objetivo y frases clave, links clicables; incluye un debrief con KQL) | [dist/decks/S4-Identity-governance.pdf](../../dist/decks/S4-Identity-governance.pdf) (fuente editable en deck-source/, notas en notas-presentador.md) | Presenter |
| Guía del estudiante (38 páginas, 4 visuales) | [dist/guias/S4-M4-Guia-del-estudiante.pdf](../../dist/guias/S4-M4-Guia-del-estudiante.pdf) | Estudiantes, una semana antes |
| Kahoot (10 preguntas, plantilla oficial) | S4-M4-Kahoot.xlsx (y .csv) | Presenter |
| Fuente del deck | deck-source/ | Para regenerar o editar |

Preguntas del Kahoot (banco M4): Q3, Q4, Q6, Q8, Q13, Q15, Q19, Q21, Q25, Q38.

## Estilo "estilo claro (Light)"

Fondo claro, tinta oscura, un acento para navegar (teal) y otro cálido para las frases clave (coral sobre crema), slides de golpe en cian y lima, dos o tres slides en tinta oscura para variar el ritmo. Manrope para títulos, Inter para texto, JetBrains Mono para código. Todos los links de Learn son clicables (en cada trampa, cada debrief y el slide de recursos).

## Run of show (45 minutos)

| Min | Bloque | Slides |
|---|---|---|
| 0 a 5 | Agenda, mapa y las preguntas mágicas | 1 a 4 |
| 5 a 23 | 12 trampas en 10 slides | 5 a 14 |
| 23 a 41 | Kahoot y debrief de cada pregunta | 15 a 25 |
| 41 a 45 | Tarea de la semana y recursos | 26 a 27 |

## Importar el Kahoot

kahoot.com: Create > Kahoot > Import spreadsheet > el .xlsx de esta carpeta (plantilla oficial de Kahoot, preguntas en fila 9, columnas B a H). Los slides k01 a k10 del deck son el debrief de cada pregunta, en el mismo orden.

## Regenerar la guía

```bash
python3 tools/build_guia.py M4
python3 tools/render_pdf.py dist/guias/S4-M4-Guia-del-estudiante.html
```
