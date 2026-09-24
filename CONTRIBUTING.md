# Contribuir

Gracias por querer mejorar el curso. Tres reglas primero, luego el cómo.

## Las tres reglas

1. **Cero dumps.** No se aceptan preguntas del examen real, parafraseadas o "inspiradas" en material filtrado. Compartirlas viola el NDA del examen de Microsoft y pone en riesgo la certificación de quien lo hace. Si dudas si algo es "demasiado parecido", no lo mandes.
2. **Todo se ancla a Microsoft Learn.** Cada pregunta, trampa o dato lleva un link a la página de Learn que lo respalda, con el ancla al párrafo cuando exista. Sin link, no entra.
3. **El porqué es obligatorio.** Una pregunta sin "por qué las otras no" no sirve para aprender. Es la parte que más trabajo cuesta y la que más vale.

## Cómo agregar una pregunta

1. Abre `content/banco/M<N>-banco.md` del dominio que corresponda.
2. Copia este formato exacto (los generadores lo parsean):

```
### Q<n> · <skill del outline> · <Multiple choice | Yes/No series | Select two | Drag/order>

<Escenario en inglés, 3 a 6 líneas, con un requisito explícito ("least privilege", "minimize effort", "must not").>

A. ...
B. ...
C. ...
D. ...

**Respuesta:** B

**Por qué es correcta:** ...

**Por qué las otras no:**
- A. ...
- C. ...
- D. ...

**Fuente:** https://learn.microsoft.com/...#ancla
```

3. Preguntas en inglés (el idioma del examen), explicaciones en español, simple y directo. Sin guiones largos.
4. Regenera la guía para comprobar que parsea: `python3 tools/build_guia.py M<N>`.
5. Abre el pull request con la plantilla. Di qué trampa practica la pregunta.

## Cómo reportar tu debrief post-examen

Abre un issue con la plantilla "Debrief post-examen". Se piden cinco cosas: resultado y score por dominio, dominios que pesaron, tipos de escenario que costaron (por tema), labs que salieron (por tarea) y qué hubieras estudiado más. **Nunca preguntas literales.** Con diez debriefs se reponderan las trampas del curso.

## Cómo corregir un dato o un link

Issue con la plantilla "Error en el contenido": qué archivo, qué dice, qué debería decir y el link a Learn que lo prueba. Si es un cambio pequeño, mejor un pull request directo.

## Estilo

- Español simple, sin relleno. Términos de producto en inglés (Conditional Access, access package).
- Negritas solo en frases clave, no en palabras sueltas.
- Nunca guiones largos (em dash). Comas, dos puntos, paréntesis o punto y seguido.
- Los decks siguen `plan/DECK-SPEC.md`. Si cambias un slide, respeta el presupuesto de 824 px de alto y el mínimo de 24 px de tipografía.

## Qué no va a entrar

Dumps, contenido de un examen real, capturas de un examen, material con licencia que no permita redistribución, y contenido que no se pueda respaldar con Learn.
