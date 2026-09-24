# Notas del presentador · Sesión 1 · Identities

Una entrada por slide: objetivo, frase clave, trampa favorita del examen, qué preguntas del banco la practican y tiempo. No es un guion para leer; es lo que hay que entender para transmitirlo con tus palabras.

## 1. Identities

Objetivo del slide: abrir con energía y dejar claro que esta no es una clase de Entra, es una sesión para subir aciertos. Frase clave: "Ustedes ya leyeron la guía; hoy vamos a ver cómo el examen intenta engañarlos". Tiempo: 1 minuto.

## 2. Estudias antes, aquí cazamos trampas

Objetivo: que entiendan que la sesión no sustituye el estudio. Frase clave: "Si llegas sin haber contestado el banco, el Kahoot te va a doler; si llegas con el banco hecho, el Kahoot te confirma lo que ya sabes". Recalcar que el debrief post-examen reemplaza a los dumps: acumula señal legítima sin guardar preguntas. Tiempo: 2 minutos.

## 3. Cuatro dominios, 700 puntos para pasar

Objetivo: quitar el mito del "70%". El 700 es escala ajustada, así que una pregunta difícil no vale lo mismo que una fácil. Frase clave: "El examen nuevo (abril 2026) metió Global Secure Access y Defender for Cloud Apps como skills explícitos; los cursos viejos no los tocan". Mencionar que el practice assessment es la mejor muestra legítima del estilo de las preguntas. Tiempo: 2 minutos.

## 4. Te da tres datos y pregunta el cuarto

Objetivo: instalar el hábito de leer las palabras clave antes de leer las opciones. Frase clave: "Subraya mentalmente 'must not', 'least privilege' y 'minimize effort' y ya tienes la mitad de la respuesta". Contar la anécdota propia: en los intentos que no pasaron, la mayoría de los errores fueron por leer las opciones antes que el requisito. Tiempo: 3 minutos.

## 5. Cuatro subdominios, doce trampas

Objetivo: mapa mental del módulo, sin detalle. Frase clave: "El subdominio 3 es el que más cambió en el outline 2026: cross-tenant sync y cross-tenant access settings ya son skills explícitos, y es lo que más cambió en Entra en el último año". Tiempo: 1 minuto.

## 6. magic

Objetivo: darles un marco para atacar cualquier pregunta del módulo aunque no recuerden el detalle. Frase clave: "Cuando no sepas la respuesta, pregúntate alcance, dirección y dependencia de on-prem; con eso eliminas dos distractores". Los números (50 devices, 40 minutos, 150K objetos) viven en la guía, no aquí. Tiempo: 2 minutos.

## 7. Delegar sin regalar el tenant

Objetivo: que distingan las tres herramientas por lo que protegen, no por su nombre. Frases clave: "El AU recorta al admin, el restricted AU blinda al objeto" y "custom role = menú cerrado, P1 por usuario y cero clonar built-ins". Trampa favorita del examen: meter un grupo al AU y creer que sus miembros entran. Otra: pensar que los AUs se anidan como OUs. Practican: Q2, Q3, Q4, Q6. Tiempo: 1.5 minutos.

## 8. ¿Quién resetea a quién?

Objetivo: que vean la escalera de reset como jerarquía, no como lista para memorizar. Frase clave: "El de abajo nunca resetea al de arriba, y estar en un role-assignable group te sube al piso 4 aunque no tengas rol". Segunda idea: Entra y Azure RBAC no se hablan; el toggle de elevación es la única puerta y se cierra al terminar. Practican: Q1, Q7, Q8. Tiempo: 1.5 minutos.

## 9. Grupos y devices que se llenan solos

Objetivo: leer una regla dinámica en voz alta y cazar el error de precedencia; es la pregunta más común de este subdominio. Frase clave: "Sin paréntesis, -and se come al -or". Luego los tres valores de deviceTrustType con la rima: AzureAD joined, ServerAD hybrid, Workplace registered. Practican: Q15, Q16, Q19. Tiempo: 1.5 minutos.

## 10. Licencias por grupo sin sustos

Objetivo: que el orden de mover usuarios entre grupos con licencia quede como reflejo. Frase clave: "Agregar, confirmar, quitar; si quitas primero, el usuario se queda sin correo hasta el siguiente ciclo". Los otros dos errores que salen: usage location vacío y conflicto E1 con E3. Practican: Q12, Q17, Q18. Tiempo: 1 minuto.

## 11. Guest, member, external, internal

Objetivo: separar dos cosas que el examen mezcla a propósito: qué es la cuenta (member o guest) y con qué se autentica. Frase clave: "Cambiar el UserType es cambiar la etiqueta, no la llave". Segunda frase: "reset redemption status es la solución moderna; borrar y reinvitar es la trampa vieja que pierde grupos y apps". En invitaciones, la regla de tres: allow o block (no ambas), bulk invite no es bulk create, y el cmdlet no manda correo si no se lo pides. Practican: Q11, Q21, Q22, Q23, Q24. Tiempo: 1.5 minutos.

## 12. Cross-tenant: quién abre, quién empuja

Objetivo: que el concepto de dirección quede dibujado en la cabeza: dos flechas, dos reglas. Frase clave: "El trust vive donde está el recurso, y la sync vive donde está el usuario". El error de Test connection que nombra al source es outbound automatic redemption; el que nombra al target es inbound allow sync. Practican: Q25, Q26, Q27, Q29, Q30. Tiempo: 2 minutos.

## 13. Si se cae on-prem

Objetivo: que la tabla se lea como árbol de decisión: si la pregunta menciona caída de on-prem, la única que sobrevive es PHS; si menciona logon hours o estado de cuenta en vivo, es PTA o federación. Frase clave: "PHS es el paracaídas pero no se abre solo: el cambio en Entra Connect es manual". Trampa favorita: creer que Entra hace failover automático a PHS. Practican: Q31, Q32, Q33, Q39. Tiempo: 1.5 minutos.

## 14. De AD FS a la nube, en orden

Objetivo: que el orden de la migración quede como secuencia, porque el examen la pregunta en drag and drop. Frase clave: "Staged rollout prueba, no convierte; el cutover es Update-MgDomain". Segunda: "Seamless SSO solo baila con PHS o PTA". Detalle que sí sale: la URL de autologon en Intranet zone por GPO. Practican: Q34, Q38. Tiempo: 1.5 minutos.

## 15. Connect Sync vs Cloud Sync

Objetivo: cerrar el bloque de tips con la decisión más frecuente del subdominio hybrid. Frase clave: "Si la pregunta habla de forests que no se ven, es Cloud Sync; si habla de hybrid join o PTA, es Connect Sync". Recalcar el cambio 2026: Exchange hybrid ya no diferencia. Staging mode: importa y sincroniza pero no exporta, y para tomar el control se quita el staging en el wizard. Practican: Q35, Q36, Q37, Q40. Tiempo: 1.5 minutos. Después de este slide, abrir Kahoot.

## 16. Kahoot

Objetivo: cambiar el ritmo. Abrir Kahoot en otra ventana, lanzar el PIN y correr las 10 preguntas. Después de cada una, pasar al slide de debrief correspondiente y explicar en 45 segundos por qué cada distractor está mal. Frase clave: "Aquí nadie pierde; el que se equivoca hoy es el que no se equivoca en el examen". Tiempo: 15 minutos en total.

## 17. Proteger al CEO y al CFO

Debrief de 45 segundos. Palabras que delatan: "even Global Admins" y "no role can be removed". Frase clave: "El AU recorta al admin; el restricted AU blinda al objeto". Si alguien eligió B, es la confusión más común: creer que el AU protege lo que tiene adentro.

## 18. El rol justo para el service desk

Debrief de 45 segundos. Palabras que delatan: "but never for User Admins" y "least privilege". Frase clave: "El de abajo nunca resetea al de arriba". Si muchos eligieron D, aclarar que Authentication Administrator no es un rol de passwords.

## 19. Solo members de Sales o Marketing

Debrief de 45 segundos. Leer B en voz alta y preguntar al grupo "¿quién entra?". Frase clave: "Sin paréntesis, -and se come al -or". Si alguien eligió C, recordar que objectId -ne null es la regla de todos los usuarios, guests incluidos.

## 20. Todos los Windows hybrid joined

Debrief de 30 segundos. Frase clave: "AzureAD joined, ServerAD hybrid, Workplace registered". Recordar que el rule builder no sirve para devices y que M365 groups no aceptan devices.

## 21. La licencia que no se asigna

Debrief de 45 segundos. Enseñar a usar los datos del escenario para descartar: "150 licencias libres" mata B. Frase clave: "Si hay licencias y hay usage location, el error es conflicto de service plans".

## 22. Carla quiere invitar guests

Debrief de 30 segundos. Frase clave: "Guest Inviter brinca el candado de 'solo admins', pero no el de 'nadie'". Si alguien eligió B, es el clásico de olvidar least privilege.

## 23. El segundo MFA de Fabrikam

Debrief de 45 segundos. Frase clave: "Trust MFA siempre es inbound y se configura donde está el recurso". Dibujar con la mano las dos flechas si hace falta: los usuarios de Fabrikam entran a Contoso, así que es inbound de Contoso.

## 24. Test connection falla

Debrief de 45 segundos. Enseñar a leer el mensaje de error: qué tenant nombra. Frase clave: "El source empuja; el target solo abre la puerta". El error que nombra al source es outbound redemption; el que nombra al target es inbound allow sync.

## 25. Ransomware y nadie puede entrar

Debrief de 45 segundos. Frase clave: "PHS es el paracaídas, pero no se abre solo". Si muchos eligieron A, es la creencia más extendida del módulo y vale la pena detenerse.

## 26. El forest que no se ve

Debrief de 45 segundos. Frase clave: "Forest desconectado: Cloud Sync". Cerrar el Kahoot con el podio y pasar a la tarea de la semana.

## 27. Esta semana: Authentication and access

Objetivo: que salgan con tres tareas concretas, no con "estudien". Frase clave: "M2 es el dominio que más pesa; llegar sin el banco hecho es llegar a medias". Tiempo: 1 minuto.

## 28. Lo que sí compartimos tras el examen

Objetivo: instalar el ritual como parte de la cultura del cohort. Frase clave: "Temas sí, preguntas no; así todos aprendemos y nadie arriesga su certificación". Decirlo con naturalidad, sin sermón. Tiempo: 1 minuto.

## 29. Todo es público y de Microsoft Learn

Cierre. Dejar el slide abierto mientras la gente anota. Recordar dónde está la guía y el banco. Preguntar quién presenta este mes para agendar su debrief.
