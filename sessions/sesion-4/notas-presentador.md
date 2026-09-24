# Notas del presentador · Sesión 4 · Identity governance

Una entrada por slide: objetivo, frase clave, trampa favorita del examen, qué preguntas del banco la practican y tiempo. No es un guion para leer; es lo que hay que entender para transmitirlo con tus palabras.

## 1. Identity governance

Objetivo: abrir con energía. Es el dominio de las decisiones: quién pide, quién aprueba, quién revisa, quién activa un rol y dónde queda la evidencia. Frase clave: "Hoy aprendemos tres preguntas que resuelven casi todo el módulo: quién decide, cuándo pasa y dónde queda el dato". Tiempo: 1 minuto.

## 2. Una idea por área, doce trampas

Objetivo: fijar expectativas en 30 segundos. Frase clave: "No vamos a recitar settings: una idea por área y las trampas que el examen repite". Si llegaste con el banco M4 hecho, el Kahoot te confirma; si no, te enseña. Tiempo: 1 minuto.

## 3. Cuatro áreas, una idea por área

Objetivo: mapa mental sin detalle. Frase clave: "Entitlement management y PIM se llevan ocho de las doce trampas; monitoreo es una sola trampa, pero la practican nueve preguntas del banco (Q32 a Q40)". Licencias: entitlement management y access reviews piden Microsoft Entra ID Governance. Tiempo: 1 minuto.

## 4. three

Objetivo: darles el marco para atacar cualquier pregunta aunque no recuerden el detalle. Frase clave: "Si puedes contestar quién decide, cuándo pasa y dónde queda el dato en cada área, ya dominas el dominio". La única excepción a todo lo JIT es la break-glass: active permanent y muy vigilada. Los números (30 días del guest, 730 días de inactive users, 1 a 24 horas de activación, 24 horas para aprobar, 7 y 30 días de retención) viven en la guía. Tiempo: 2 minutos.

## 5. Quién crea, quién asigna

Objetivo: separar quién trae recursos, quién arma paquetes y quién solo asigna. Frase clave: "Catalog owner trae los recursos, access package manager arma los paquetes, assignment manager solo mete y saca gente". Trampa favorita: el grupo que no aparece en el resource picker. Ser catalog owner no basta: hace falta permiso sobre el recurso, y lo más acotado es hacerlo owner de ese grupo. Delata: "least privilege", "create access packages but not add resources", "only assign users", "resource picker is empty", "catalog creator", "delegate to the department". Practican: Q2, Q3. Tiempo: 1.5 minutos.

## 6. Una policy, un público

Objetivo: que cuenten policies por público, no por approver. Frase clave: "Internos y externos no caben en la misma policy: son dos". Trampa favorita: el paquete para empleados y partners; el mínimo son dos policies. Segunda: la request se aprueba pero el partner nunca recibe acceso ni cuenta guest, porque la allowlist de B2B gana siempre. Delata: "employees and partners", "minimum number of policies", "any user on the internet", "connected organization", "allowlist", "no guest account is created". Practican: Q4, Q11. Tiempo: 1.5 minutos.

## 7. Aprobaciones y el reloj

Objetivo: que distingan alternate de fallback sin dudar. Frase clave: "En cada stage basta uno; si nadie decide a tiempo, la request se muere y se pide otra vez". Alternate es para cuando el approver no actúa; fallback, para cuando no se encuentra el manager. No existe un forward automático a Global Administrators. Dato extra: una extensión con "Require approval to grant extension" usa las mismas reglas de aprobación de la pestaña Requests. Delata: "doesn't respond", "backup approver", "forward", "manager can't be found", "external sponsor", "second stage", "extension requires approval". Practican: Q5, Q6, Q7, Q12. Tiempo: 2 minutos.

## 8. Externos: entrar y salir

Objetivo: seguir a un guest desde que entra hasta que se borra, y dejar claro que la ToU sola no hace nada. Frase clave trampa 4: "Último paquete perdido: bloqueado hoy, borrado en 30 días. Con 0 días, borrado ya". Frase clave trampa 5: "La ToU es un PDF que no muerde hasta que Conditional Access la pone en el Grant". La ruta: Control Configurations, Lifecycle of external users. Re-aceptación: Expire consents o Duration before re-acceptance, y el usuario vuelve a aceptar solo cuando su sesión expira. El reporte de aceptación vive lo que vive la ToU; los audit logs, 30 días. Delata: "last access package assignment", "as soon as possible", "also has access to a SharePoint site", "every device", "guest users", "create Conditional Access policy later", "declined". Practican: Q8, Q12 (lifecycle) y Q9, Q10 (ToU). Tiempo: 2 minutos.

## 9. Dónde se crea y quién revisa

Objetivo: que ubiquen dónde nace cada review antes de pensar en settings. Frase clave: "Grupos y apps en Access reviews, roles en PIM, paquetes en entitlement management. Fallback solo si hay managers u owners". Trampa favorita: revisar las asignaciones de Global Administrator; eso se crea en PIM. Segunda: la review toma una foto al inicio, así que un owner agregado a mitad de la review entra hasta la siguiente instancia. Delata: "review Global Administrator assignments", "group has no owner", "guest users only", "all Microsoft 365 groups", "group owners create reviews", "quarterly". Practican: Q13, Q14, Q17. Tiempo: 1.5 minutos.

## 10. La review que borra todo

Objetivo: que elijan la opción de no respuesta pensando en el daño que hace con auto apply, y que sepan cuándo se cobra el deny. Frase clave trampa 7: "If reviewers don't respond más auto apply es un botón de borrar: elige con cuidado". Frase clave trampa 8: "En access reviews no gana la mayoría, gana el último. Y el deny se cobra al final". Ojo: Remove access y Take recommendations con auto apply pueden quitar todo el acceso. La acción "block 30 days, then remove" para guests aplica también a los que se niegan por no respuesta. Para auditoría de muchas reviews, el reporte Review History (CSV disponible 30 días). Delata: "if the reviewer doesn't respond", "inactive users lose access", "active users keep access", "two reviewers disagree", "removed immediately", "auto apply was disabled", "synced from on-premises", "single CSV for auditors". Practican: Q14, Q15, Q16, Q18, Q19, Q20. Tiempo: 2 minutos.

## 11. PIM: eligible vs active

Objetivo: la matriz eligible y active por permanent y time-bound como reflejo, más las perillas que salen en Yes/No. Frase clave: "Eligible es JIT, time-bound es con fecha de muerte. El ticket es de adorno y el approver no necesita rol". Reglas de aprobación: el approver no necesita rol, nadie aprueba lo suyo, la primera decisión resuelve y en roles de Entra hay 24 horas para aprobar, sin setting para cambiarlo. Sin approvers configurados, en roles de Entra aprueban los Privileged Role Administrators y Global Administrators activos; en Azure resources y Groups no hay approvers por default. Método fuerte en la activación: authentication context más authentication strength, con la política de CA para todos o para los eligible, no para el rol, porque al activar todavía no lo tienen. Delata: "only when needed", "for six months", "no approvers selected", "ticket number", "approver doesn't respond", "even if they already completed MFA", "phishing-resistant at activation". Practican: Q21, Q22, Q23, Q30, Q31. Tiempo: 2 minutos.

## 12. PIM fuera de Entra roles

Objetivo: que no lleven las reglas de roles de Entra a Azure resources ni a Groups. Frase clave: "En Azure, los settings no bajan de la suscripción al resource group. En Groups, el grupo no tiene que ser role-assignable". Trampa favorita: aprobación configurada en la suscripción y alguien activa Owner en un resource group sin aprobación, porque ese recurso tiene su propia policy. Segunda: en un grupo role-assignable nadie más cambia las credenciales de sus miembros, ni de los eligible que aún no activan. Delata: "configured on the subscription", "resource group", "managed identity", "discover resources", "not role-assignable", "dynamic group", "reset the password of an eligible member". Practican: Q24, Q25, Q26, Q27. Tiempo: 1.5 minutos.

## 13. Break-glass bien hecha

Objetivo: el checklist de la cuenta de emergencia y la query de alerta en vivo. Frase clave: "La break-glass no espera aprobación: GA active permanent, FIDO2 en la caja fuerte y una alerta que grita en cada sign-in". Trampa favorita: break-glass eligible con aprobación; si la emergencia es que nadie puede aprobar, la cuenta no sirve. Segunda: el mito viejo de break-glass sin MFA; hoy es passkey FIDO2 o CBA, distinto al de los admins. La query sale de Learn y filtra SigninLogs por el object ID (UserId) de cada cuenta, sin filtrar por resultado: con ResultType "0" solo verías los éxitos. Delata: "emergency access", "all admins are eligible", "approval required and no approvers", "federation outage", "alert whenever the account signs in", "report-only". Practican: Q28, Q29. Tiempo: 2 minutos.

## 14. Del log a la respuesta

Objetivo: retención, destinos y tablas en un solo slide, porque es la trampa con más preguntas del banco. Frase clave: "Free 7, P1/P2 30, y el upgrade no revive datos. Cada categoría llena su tabla, y el workbook come de Log Analytics". Trampa favorita: el tenant que pasa de Free a P1 hoy y pide sign-ins de hace 20 días; ya no existen. Segunda: la query a AADNonInteractiveUserSignInLogs que no devuelve nada porque falta esa categoría en la diagnostic setting. Datos extra: el audit de PIM guarda 30 días, para más se usa diagnostic settings; en AADProvisioningLogs, ResultType Failure con ResultSignature da el código de error. Delata: "upgraded today", "20 days ago", "two years at low cost", "third-party SIEM", "query returns no results", "workbook is empty", "non-Microsoft MFA", "score doesn't change". Practican: Q32 a Q40. Después de este slide, abrir Kahoot. Tiempo: 2 minutos.

## 15. Kahoot

Objetivo: cambiar el ritmo. Abrir Kahoot en otra ventana, lanzar el PIN y correr las 10 preguntas. Cubren diez de las doce trampas, una por trampa. Después de cada una, pasar al slide de debrief y explicar en 45 segundos por qué cada distractor está mal. Frase clave: "Aquí nadie pierde; el que se equivoca hoy es el que no se equivoca en el examen". Tiempo: 18 minutos.

## 16. El grupo no sale en el picker

Debrief de 45 segundos. Delata: "least privilege" y "resource picker". Frase clave: "Catalog owner trae los recursos, pero además necesita permiso sobre el recurso". Si muchos eligieron A, es la trampa clásica: en la tabla de Learn, Identity Governance Administrator agrega apps pero no grupos.

## 17. Empleados y partners, un paquete

Debrief de 30 segundos. Frase clave: "Internos y externos no caben en la misma policy: son dos". Delata: "minimum number of policies" y un escenario con empleados y una connected organization. El approver distinto (manager contra sponsor) es consecuencia del público, no la razón.

## 18. Carol nunca contestó

Debrief de 30 segundos. Frase clave: "En cada stage basta uno; si nadie decide a tiempo, la request se muere y se pide otra vez". Delata: "doesn't act" y "second stage". Si alguien pregunta cómo evitarlo: alternate approvers con forward después de N días y timeout de al menos 4 días.

## 19. Ana pierde su último paquete

Debrief de 30 segundos. Frase clave: "Último paquete perdido: bloqueado hoy, borrado en 30 días. Con 0 días, borrado ya". Delata: "last access package assignment" y "also has access to a SharePoint site". Si muchos eligieron A, repetir que el ciclo de vida aplica a los guests que entraron por entitlement management, tengan lo que tengan después.

## 20. Revisar a los Global Admins

Debrief de 30 segundos. Frase clave: "Grupos y apps en Access reviews, roles en PIM, paquetes en entitlement management". Delata: "review Global Administrator assignments". Pregunta rápida al grupo: ¿y si fuera un rol de Azure en una suscripción? También PIM.

## 21. Nadie respondió la review

Debrief de 30 segundos. Frase clave: "If reviewers don't respond más auto apply es un botón de borrar: elige con cuidado". Delata: "inactive users lose access" y "active users keep access" en la misma pregunta: eso es el helper, así que es Take recommendations. El escenario del banco: Sales-Apps, revisan los managers.

## 22. Alice aprueba, Bob deniega

Debrief de 30 segundos. Frase clave: "En access reviews no gana la mayoría, gana el último. Y el deny se cobra al final". Delata: "two reviewers disagree" y "removed immediately". Contraste útil: en entitlement management y en PIM decide el primero que responde; en access reviews vale la última respuesta.

## 23. Seis meses, solo cuando se necesite

Debrief de 30 segundos. Frase clave: "Eligible es JIT, time-bound es con fecha de muerte". Delata: "only when needed" (eligible) y "for six months" con "without cleanup" (time-bound). Volver a la matriz del slide de la trampa 9: la única casilla que cumple las dos es eligible time-bound.

## 24. Owner en RG1 sin aprobación

Debrief de 30 segundos. Frase clave: "En Azure, los settings no bajan de la suscripción al resource group". Delata: "configured on the subscription" y "resource group". Si muchos eligieron D, aclarar que el discovery es la experiencia legacy y aquí no es el problema.

## 25. La query que no devuelve nada

Debrief de 45 segundos. En Kahoot solo sale el texto; aquí mostramos la query del banco (sin el take 100 final) para leerla juntos. Frase clave: "Cada categoría llena su tabla". Delata: "query returns no results" y una diagnostic setting con solo AuditLogs y SignInLogs. Cerrar el Kahoot con el podio y pasar a la tarea de la semana.

## 26. Antes de la sesión 5: labs y simulacro

Objetivo: tres tareas concretas para llegar a la última sesión. Frase clave: "Para el examen importa reconocer la pantalla, el nombre exacto del campo y el estado final; la guía de labs en imágenes está hecha para eso". La sesión 5 es labs en imágenes, estrategia de examen y simulacro corto: quien llegue con los 10 labs repasados y el simulacro de 30 preguntas hecho, aprovecha la sesión. Tiempo: 1 minuto.

## 27. Todo es público y de Microsoft Learn

Cierre. Dejar el slide abierto mientras anotan. Todos los links del deck son clicables, incluidos los de cada trampa y cada debrief. Los módulos de access reviews y de monitoreo están dentro del learning path de M4. Preguntar quién presenta este mes para agendar su debrief.
