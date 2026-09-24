# Notas del presentador · Sesión 2 · Authentication and access

Una entrada por slide: objetivo, frase clave, trampa favorita del examen, qué preguntas del banco la practican y tiempo. No es un guion para leer; es lo que hay que entender para transmitirlo con tus palabras.

## 1. Authentication and access

Objetivo: abrir con energía. Es el dominio que más pesa y el que más cambió en 2026 (Global Secure Access, retiro de las risk policies legacy el 1 de octubre). Frase clave: "Hoy aprendemos cuatro preguntas que resuelven casi todo el módulo: método, política, riesgo y tráfico". Tiempo: 1 minuto.

## 2. Tú ya estudiaste. Aquí cazamos trampas

Objetivo: fijar expectativas en 30 segundos. Frase clave: "Si llegaste con el banco hecho, el Kahoot te confirma; si no, te enseña". Tiempo: 1 minuto.

## 3. Cuatro subdominios, el que más pesa

Objetivo: mapa mental sin detalle. Frase clave: "El subdominio 4 no existía en los cursos viejos; si tu material no habla de Global Secure Access, está incompleto". Tiempo: 1 minuto.

## 4. four

Objetivo: darles el marco para atacar cualquier pregunta aunque no recuerden el detalle. Frase clave: "Cuando no sepas la respuesta, pregúntate método, política, riesgo y tráfico; con eso eliminas dos distractores". Los números (10 minutos de la TAP, 1000 términos, 99 contexts, 14 días, 28 horas) viven en la guía. Tiempo: 2 minutos.

## 5. TAP y passkeys: el pase y la llave

Objetivo: que distingan registro de autenticación. Frase clave: "La TAP es el pase de visitante". Segunda: "Passkey en Authenticator se configura en FIDO2, no en Authenticator". Trampa favorita: pedir attestation y synced passkeys al mismo tiempo (no se puede). Practican: Q1, Q3, Q4. Tiempo: 1.5 minutos.

## 6. La escalera de métodos

Objetivo: que vean las strengths como escalera incluyente: cada escalón contiene al de arriba. Frase clave: "Phone sign-in es passwordless pero no phishing-resistant, y la TAP solo llega a MFA". CBA: policy OID le gana al issuer, y sin CRL no hay revocación. Practican: Q2, Q16, Q27. Tiempo: 1.5 minutos.

## 7. OAuth no es OATH

Objetivo: matar el reflejo de "token lifetime policy" para forzar reautenticación. Frase clave: "OAuth es el token, OATH es el código de 6 dígitos". El outline dice "OAuth 2.0 tokens" pero el método de MFA se llama OATH tokens; cubrimos los dos. Practican: Q5, Q21. Tiempo: 1.5 minutos.

## 8. Passwords que todavía importan

Objetivo: tres reglas que salen siempre. Frase clave: "Writeback se prende en dos lados, los admins viven en two-gate, y en Audit el password malo pasa". Delata: "contact your administrator", "Helpdesk Administrator can't use security questions", "some domain controllers", "Audit mode". Practican: Q7, Q8, Q11. Tiempo: 1.5 minutos.

## 9. Kerberos sin PKI

Objetivo: dos recetas cortas. Frase clave: "Cloud Kerberos trust: cero PKI. Entra Kerberos en Azure Files: cero MFA para esa app". El escenario clásico: AVD con FSLogix que deja de montar perfiles después de una política de MFA para All resources. Practican: Q9, Q12. Tiempo: 1 minuto.

## 10. Construir CA sin lockout

Objetivo: la regla de oro de CA como reflejo. Frase clave: "Si nadie dice que no, Entra dice que sí". Contar el escenario de Payroll: CA01 pone MFA a Finance y todos los demás entran sin prompt; la respuesta es una segunda política de block. Delata: "only members of Finance", "users outside the group can access", "security defaults are enabled", "from a template". Practican: Q13, Q14, Q19, Q20, Q26, Q28. Tiempo: 2 minutos.

## 11. Excluir el PAW, bloquear el resto

Objetivo: que la receta de excluir y bloquear quede como patrón. Frase clave: "Un device no registrado es null, y null no se excluye". Por eso el PAW se excluye (cumple el filtro) y todo lo demás, registrado o no, se bloquea. Practican: Q15, Q17, Q18. Tiempo: 1.5 minutos.

## 12. Cortar el acceso ya

Objetivo: separar lo que CAE hace en minutos de lo que tarda hasta un día. Frase clave: "CAE corta por eventos, no por cambios de grupo, y solo entiende IPs, no países". El orden de baja en híbrido sale como drag and drop. Practican: Q10, Q22. Tiempo: 1.5 minutos.

## 13. Etiquetas y permisos

Objetivo: que el flujo de tres pasos quede claro y que recuerden que la policy va en On. Frase clave: "El context es la etiqueta, la policy pone las reglas, y el que la pega es SharePoint, PIM o protected actions". Trampa: combinar el context con el directory role en la misma política; al activar, el usuario aún no tiene el rol. Practican: Q23, Q24, Q25, Q27. Tiempo: 1.5 minutos.

## 14. Riesgo: quién se cura con qué

Objetivo: la distinción más rentable del módulo. Frase clave: "User risk se cura con password; sign-in risk se cura con MFA. Nunca al revés y nunca en la misma policy". Fecha que sí importa: 1 de octubre de 2026, las legacy se retiran y todo va por CA con Require risk remediation. Delata: "users at risk", "leaked credentials", "passwordless users", "self-remediate". Practican: Q6, Q29 a Q38. Tiempo: 2 minutos.

## 15. GSA en un dibujo

Objetivo: que vean los tres perfiles como capas en orden y sepan qué agrega cada uno. Frase clave: "Microsoft primero, luego Private, luego Internet". Delata: "replace the VPN", "different Conditional Access for one app", "stolen tokens replayed", "sign in to other tenants". Practican: Q39 a Q44. Después de este slide, abrir Kahoot. Tiempo: 2 minutos.

## 16. Kahoot

Objetivo: cambiar el ritmo. Abrir Kahoot en otra ventana, lanzar el PIN y correr las 10 preguntas. Después de cada una, pasar al slide de debrief y explicar en 45 segundos por qué cada distractor está mal. Frase clave: "Aquí nadie pierde; el que se equivoca hoy es el que no se equivoca en el examen". Tiempo: 18 minutos.

## 17. Dos grupos, dos reglas de passkeys

Debrief de 45 segundos. Delata: "verify the make and model" y "iCloud Keychain" en la misma pregunta: dos reglas incompatibles en una sola política, así que son perfiles. Frase clave: "synced passkey con attestation no se llevan".

## 18. Reautenticar cada 8 horas

Debrief de 45 segundos. Frase clave: "¿Quieres forzar reauth? Sign-in frequency, no token lifetime". Si muchos eligieron B, explicar que el usuario nunca ve vencer un access token: el refresh lo renueva sin prompt.

## 19. Megan no puede usar SSPR

Debrief de 30 segundos. Delata: "Helpdesk Administrator" y "security questions" en la misma pregunta. Frase clave: "los admins viven en two-gate".

## 20. Los perfiles dejaron de montar

Debrief de 30 segundos. Delata: "profile containers fail to mount" y "MFA policy" juntos. Frase clave: "Entra Kerberos en Azure Files: cero MFA para esa app".

## 21. Solo Finance entra a Payroll

Debrief de 45 segundos. Frase clave: "Si nadie dice que no, Entra dice que sí". Delata: "users outside the group can access" y "only Finance".

## 22. Solo desde el PAW

Debrief de 45 segundos. Frase clave: "Excluye el PAW y bloquea el resto: un device no registrado es null, y null no se excluye". Si muchos eligieron A, es la confusión de include vs exclude en el filtro.

## 23. Phishing-resistant solo al activar

Debrief de 45 segundos. Frase clave: "El context es la etiqueta, la policy pone las reglas, y el que la pega es PIM". Delata: "at the moment of activation".

## 24. User risk para todos, con y sin password

Debrief de 45 segundos. Frase clave: "User risk se cura con password o risk remediation; sign-in risk con MFA". Delata: "passwordless users" y "self-remediate".

## 25. Leaked credentials con P1

Debrief de 30 segundos. Frase clave: "leaked credentials se cura con password". Detalle que vale puntos: es nonpremium, se ve con P1, y el reset en la nube cuenta gracias a PHS.

## 26. Una app privada con otra política

Debrief de 45 segundos. Frase clave: "Quick Access es el bloque general; per-app es la segmentación". Cerrar el Kahoot con el podio y pasar a la tarea de la semana.

## 27. Antes de la sesión 3: Workload identities

Objetivo: tres tareas concretas. Frase clave: "M3 es terreno de apps: si no has registrado una app en tu vida, esta semana registra una". Tiempo: 1 minuto.

## 28. Todo es público y de Microsoft Learn

Cierre. Dejar el slide abierto mientras anotan. Todos los links del deck son clicables, incluidos los de cada trampa y cada debrief. Preguntar quién presenta este mes para agendar su debrief.
