# Notas del presentador · Sesión 3 · Workload identities

Una entrada por slide: objetivo, frase clave, trampa favorita del examen, qué preguntas del banco la practican y tiempo. No es un guion para leer; es lo que hay que entender para transmitirlo con tus palabras.

## 1. Workload identities

Objetivo: abrir con energía. Hoy el tema son las identidades que no son personas: apps, service principals y managed identities, más lo que Defender for Cloud Apps ve y controla. Frase clave: "Hoy aprendemos cuatro preguntas que resuelven casi todo el módulo: identidad, consent, entrada y Defender". Tiempo: 1 minuto.

## 2. Tú ya estudiaste. Aquí cazamos trampas

Objetivo: fijar expectativas en 30 segundos. Frase clave: "Si llegaste con el banco hecho, el Kahoot te confirma; si no, te enseña". Recordar que los datos finos (3 años del certificado, 200 y 150 grupos, 24 meses del secret, 3 horas del bloqueo con MDE) viven en la guía para consulta. Tiempo: 1 minuto.

## 3. Cuatro subdominios, cuatro preguntas

Objetivo: mapa mental sin detalle. Mostrar los cuatro subdominios, el peso de 20 a 25% y las cuatro preguntas: identidad, consent, entrada y Defender. Frase clave: "El learning path de apps no trae módulo propio de managed identities ni de Defender for Cloud Apps; esos módulos están en el slide de recursos". Tiempo: 1 minuto.

## 4. four

Objetivo: darles el marco para atacar cualquier pregunta de M3 aunque no recuerden el detalle. Frase clave: "Cuando no sepas la respuesta, pregúntate identidad, consent, entrada y Defender; con eso eliminas dos distractores". La meta de la sesión: tomar cualquier pregunta del banco, señalar las dos o tres palabras que la delatan y explicar por qué falla cada distractor. Los datos finos (3 años del certificado, 200 y 150 grupos, 24 meses del secret, 3 horas del bloqueo con MDE) viven en la guía. Tiempo: 2 minutos.

## 5. El molde y la galleta

Objetivo: que distingan el objeto que se registra del objeto que se usa. Frase clave: "App registration es el molde, enterprise app es la galleta: un molde en casa, una galleta por tenant". Contar el caso de Q22: Contoso registra HRPortal multitenant, Fabrikam consiente, y en Fabrikam aparece solo un service principal, nunca un application object. Trampa favorita: pensar que todo service principal tiene su app registration; el de una managed identity no lo tiene, por eso sus permisos de Graph se dan directo al SP. Delata: "home tenant", "multitenant", "partner tenant grants consent", "which object is created", "Managed application in local directory". Practican: Q7, Q8, Q22. Tiempo: 1.5 minutos.

## 6. ¿Qué identidad le doy al workload?

Objetivo: un árbol de decisión que resuelva cualquier pregunta de "qué identidad uso". Frase clave de la trampa 2: "System-assigned vive y muere con su recurso; user-assigned es roomie: la compartes y la borras tú". Frase clave de la trampa 3: "Managed identity no sale de Azure (salvo con Arc). Afuera: service principal con cert o federated. On-prem Windows: gMSA". La user-assigned es la recomendada para servicios de Microsoft y se puede pre-autorizar antes de crear las VMs. El certificate es mejor que el secret, que dura máximo 24 meses; la federated credential es para un IdP externo como GitHub Actions o Kubernetes. Después de asignar la identidad, se autoriza en el destino (por ejemplo Storage Blob Data Reader). User account como service account es la última opción. Segundo link: service-accounts-on-premises, choose the right type of service account. Delata: "same identity for all instances", "before the VMs are deployed", "least privilege to assign", "GitHub Actions", "no secrets stored", "behind a load balancer". Practican: Q1, Q2, Q4, Q5 (trampa 2) y Q3, Q6, Q24 (trampa 3). Tiempo: 2 minutos.

## 7. Como tú, como yo y quién aprueba

Objetivo: separar quién actúa de quién aprueba. Frase clave de la trampa 4: "Delegated = actúo como tú; application = actúo como yo. Y 'como yo' siempre lo aprueba un admin". Frase clave de la trampa 5: "Si el usuario no puede consentir, el workflow le da un botón para pedir; ser reviewer no te da superpoderes". Application permissions de Microsoft Graph las consiente Privileged Role Administrator (o Global Admin); Application Admin y Cloud Application Admin consienten todo lo demás. User consent tiene cuatro opciones: no permitir, verified publishers con permisos low impact, permitir todo, o dejar que Microsoft lo maneje (default en tenants nuevos). Risk-based step-up consent viene activo y solo actúa si hay user consent. Delata: "without a signed-in user", "daemon", "on behalf of the signed-in user", "Grant admin consent is unavailable", "Admins only", "request approval from the consent prompt", "unverified publisher", "added later as a reviewer", "AADSTS90094". Practican: Q7, Q18, Q27, Q30 (trampa 4) y Q16, Q17 (trampa 5). Tiempo: 2 minutos.

## 8. La línea roja del App Proxy

Objetivo: que la diferencia entre los dos roles de apps quede como reflejo. Frase clave: "Cloud App Admin es App Admin sin el Proxy. Y ninguno de los dos toca CA ni Graph application permissions". Si la pregunta menciona connector groups o publicar apps on-premises, es Application Administrator. Si "Users can register applications" está en No, el mínimo para registrar es Application Developer. Ninguno de estos roles administra Conditional Access. Delata: "connector group", "publish on-premises apps", "least privilege", "users can't register applications", "configure SAML SSO", "create a Conditional Access policy for the app". Practican: Q9, Q18, Q21. Tiempo: 1.5 minutos.

## 9. App Proxy de punta a punta

Objetivo: recorrer el flujo usuario, pre-auth de Entra, servicio, connector y app. Frase clave: "Sin pre-auth de Entra no hay CA, ni MFA, ni SSO. El connector solo sale, nunca entra". La receta de KCD: en AD, el computer account del connector delega al SPN de la app con "specified services only" y "any authentication protocol"; en Entra, SSO Integrated Windows authentication con el SPN. Si el connector y la app están en dominios distintos, resource-based KCD. Custom domain: PFX con private key y un CNAME a msappproxy.net, nunca un .cer ni un A record. Delata: "Integrated Windows Authentication", "Kerberos", "SPN", "Passthrough", "no inbound ports", "custom domain", "high availability", "different domains". Practican: Q10, Q11, Q12. Tiempo: 2 minutos.

## 10. SAML sin sustos

Objetivo: tres URLs y una línea de tiempo. Frase clave: "Entity ID dice quién eres, Reply URL dice a dónde mando el token. El cert no se edita: se crea otro". Trampa favorita: poner en la app los valores de la sección "Set up"; esos son de Entra y van del lado del vendor. El certificado autogenerado dura 3 años y Entra avisa a los 60, 30 y 7 días, hasta 5 correos. La fecha de un certificado guardado no se cambia, y borrar el activo antes de tener el nuevo en la app corta el SSO. Delata: "Assertion Consumer Service", "Entity ID", "SP-initiated", "certificate expires in", "no downtime", "notification email", "change the expiration date". Practican: Q13, Q15. Tiempo: 1.5 minutos.

## 11. Esconder, filtrar o apagar

Objetivo: tres switches de la app que el examen mezcla a propósito. Frase clave: "Visible esconde, Assignment required filtra, Enabled apaga. Y los grupos anidados no cuentan". Estos son settings de app; Users can register applications y consent son de tenant. Caso Fabrikam (Q19 y Q20): Finance-Contractors, anidado en Finance, no entra a Expensely hasta que lo asignas directo; y la pestaña de finanzas en My Apps es una collection que solo muestra apps ya asignadas. Delata: "nested group", "not assigned to the app", "separate tab in My Apps", "hide the app", "stop all sign-ins without deleting", "only members of". Practican: Q14, Q19, Q20. Tiempo: 1.5 minutos.

## 12. Scope, app role o groups claim

Objetivo: traducir las palabras de la pregunta al setting correcto. Frase clave: "Scope para 'on behalf of', app role para 'sin usuario' o para roles de usuario; el groups claim topa en 200". Plataforma: Single-page application para JavaScript con PKCE, Web para apps de servidor, y el daemon no lleva redirect URI. Para autorizar usuarios dentro de la app, app role Users/Groups, que sale en el claim roles. El groups claim topa en 200 grupos en JWT y 150 en SAML; la salida es Groups assigned to the application. Delata: "React", "MSAL.js", "PKCE", "Expose an API", "roles claim", "group overage", "more than 200 groups", "Allowed member types". Practican: Q23, Q25, Q26, Q28, Q29. Tiempo: 1.5 minutos.

## 13. Unsanctioned no es un firewall

Objetivo: separar ver de bloquear. Frase clave: "Unsanctioned es una etiqueta, no un firewall: el bloqueo lo hace MDE o tu appliance". Snapshot es subir logs a mano una vez; continuous es Defender for Endpoint (sirve para home office), log collector por Syslog o FTP, Secure Web Gateway o API. El bloqueo con MDE va en orden: Cloud y Network Protection, Enforce app access, Custom network indicators y al final Unsanctioned, con hasta 3 horas de espera; con scoped profiles se acota por device group. Catalog: 4 categorías (General, Security, Compliance, Legal). Score metrics para todas las apps, Override para una sola. Delata: "one-time assessment", "exported logs", "users working from home", "continuous", "block on devices", "specific device groups", "weight", "all apps", "only this app". Practican: Q31, Q32, Q33, Q34, Q39. Tiempo: 2 minutos.

## 14. Session control: quién hace qué

Objetivo: saber qué pieza controla qué, como cierre antes del Kahoot. Frase clave: "Session policy sin el CA 'Use Conditional Access App Control' es perro sin dientes. Y app enforced solo muerde en Exchange y SharePoint". Access y session policies necesitan una política de CA con Session, Use Conditional Access App Control. Access policy decide si entras; session policy controla lo que haces dentro, solo en browser. App connector trabaja por API (actividad, cuentas, archivos), sin proxy. OAuth app policy filtra por Permission level, Community use y usuarios que autorizaron, con la acción Revoke app, y pide el connector. Delata: "session policy has no effect", "desktop sync client", "native client", "browser only", "limited web-only access", "no Defender for Cloud Apps licenses", "through the vendor's API", "without a proxy", "rare community use", "high permission level". Practican: Q35, Q36, Q37, Q38, Q40. Después de este slide, abrir Kahoot. Tiempo: 2 minutos.

## 15. Kahoot

Objetivo: cambiar el ritmo. Abrir Kahoot en otra ventana, lanzar el PIN y correr las 10 preguntas. Después de cada una, pasar al slide de debrief y explicar en 45 segundos por qué cada distractor está mal. Las preguntas cubren diez de las doce trampas; la 4 entra de lado en la primera pregunta y la 8 (SAML) se practica en el banco con Q13 y Q15. Frase clave: "Aquí nadie pierde; el que se equivoca hoy es el que no se equivoca en el examen". Tiempo: 18 minutos.

## 16. Graph para una managed identity

Debrief de 45 segundos. Frase clave: "Una galleta sin molde: la managed identity solo tiene service principal". Delata: "managed identity" y "Microsoft Graph application permission" en la misma pregunta. De paso toca la trampa 4: para dar application permissions de Graph se necesita Privileged Role Administrator. Si muchos eligieron C, es la confusión entre Azure RBAC y permisos de Graph.

## 17. Una identidad para todo el scale set

Debrief de 30 segundos. Frase clave: "User-assigned es roomie: la compartes y la borras tú". Delata: "re-created", "same identity" y "before the new instances are deployed". Si muchos eligieron B, recordar que la system-assigned no se puede pre-autorizar porque todavía no existe.

## 18. GitHub sin secretos

Debrief de 45 segundos. Frase clave: "Managed identity no sale de Azure (salvo con Arc). Afuera: service principal con cert o federated". Delata: "GitHub Actions" y "no secrets stored". Si muchos eligieron D, repetir que el runner de GitHub no es un recurso de Azure.

## 19. Pedir aprobación desde el prompt

Debrief de 45 segundos. Contexto del banco: el tenant solo permite user consent para verified publishers con permisos seleccionados, y la app pide Files.Read delegated. Frase clave: "Si el usuario no puede consentir, el workflow le da un botón para pedir". Delata: "request approval from the consent prompt" y "unverified publisher".

## 20. App Proxy con least privilege

Debrief de 30 segundos. Frase clave: "Cloud App Admin es App Admin sin el Proxy". Delata: "connector groups" y "least privilege" juntos. Si muchos eligieron A, es exactamente la trampa que busca el examen.

## 21. expenses.contoso.com con App Proxy

Debrief de 30 segundos. Frase clave: "Custom domain es PFX con private key más CNAME; el connector solo sale, nunca entra". Delata: "custom domain" y "expenses.contoso.com". El certificado se sube una vez por dominio y se reusa en apps nuevas.

## 22. Finance-Contractors no entra

Debrief de 30 segundos. Es el case study 1 del banco (Fabrikam). Frase clave: "Visible esconde, Assignment required filtra, Enabled apaga. Y los grupos anidados no cuentan". Delata: "nested group" y "not assigned to the app".

## 23. Un claim con Survey.Create

Debrief de 45 segundos. Frase clave: "Scope para 'on behalf of', app role para 'sin usuario' o para roles de usuario". Delata: "roles claim" y "users and security groups". Asignar grupos a app roles pide P1 o superior. Si muchos eligieron A, repetir: el scope lo pide el cliente a la API; el app role dice qué es el usuario.

## 24. Logs exportados, una sola vez

Debrief de 30 segundos. Frase clave: "Snapshot es una vez y a mano; continuous es MDE, log collector, SWG o API". Delata: "one-time assessment" y "exported logs". Si muchos eligieron B, subrayar que el log collector se despliega y la pregunta dice "deploying nothing".

## 25. La session policy no hace nada

Debrief de 45 segundos. Frase clave: "Session policy sin el CA 'Use Conditional Access App Control' es perro sin dientes". Delata: "session policy has no effect" y "no Conditional Access policy targets". Cerrar el Kahoot con el podio y pasar a la tarea de la semana.

## 26. Antes de la sesión 4: Governance

Objetivo: tres tareas concretas. Frase clave: "Si hoy pudiste explicar por qué falla cada distractor, M3 está listo; M4 es otro dominio de 20 a 25%". Sobre el aviso: en Learn y en el banco el connector de Application Proxy aparece como Microsoft Entra private network connector. Tiempo: 1 minuto.

## 27. Todo es público y de Microsoft Learn

Cierre. Dejar el slide abierto mientras anotan. El learning path de apps trae cuatro módulos (enterprise apps, SSO y app registration) pero no trae módulo propio de managed identities ni de Defender for Cloud Apps; por eso van aparte los módulos de managed identities y de Defender for Cloud Apps. Todos los links del deck son clicables, incluidos los de cada trampa y cada debrief. Preguntar quién presenta este mes para agendar su debrief.
