# SC-300 Tips and Tricks: plan editorial (borrador consultable)

Estado: borrador de trabajo, no pulido. Sirve para revisar orden, alcance y decisiones antes de producir los decks finales.

Fuente de verdad del alcance: skills outline oficial "as of April 27, 2026"
https://learn.microsoft.com/credentials/certifications/resources/study-guides/sc-300

---

## 1. Objetivo del curso

Subir la cantidad de aciertos lo más posible. No enseñar Entra desde cero.

Qué significa eso en diseño:

- Cada concepto se presenta en 4 formas: punto clave (1 a 2 líneas), visual, link principal, link directo al párrafo.
- Cada pregunta trae por qué la correcta es correcta y por qué cada distractor está mal. El SC-300 se pierde en los distractores, no en la teoría.
- Los labs se ven en imágenes con las capturas oficiales de Learn, no se hacen en vivo. Ahorra horas.
- Sesión en vivo = tips and tricks + Kahoot de lo más fallado. El estudio pesado va por cuenta del estudiante con la guía (modelo invertido).

---

## 2. Datos duros del examen (verificados en Learn)

| Dato | Valor |
|---|---|
| Score para pasar | 700 de 1000 |
| Dominios y peso | Identities 20 a 25%, Auth & Access 25 a 30% (el detalle del outline dice 20 a 25, el "at a glance" dice 25 a 30), Workload identities 20 a 25%, Governance 20 a 25% |
| Practice assessment gratis | https://learn.microsoft.com/credentials/certifications/exams/sc-300/practice/assessment?assessment-type=practice&assessmentId=60 |
| Exam sandbox (tipos de pregunta) | https://aka.ms/examdemo |
| Renovación | Gratis, anual, assessment online en Learn |
| Idioma | Si no está en tu idioma preferido puedes pedir 30 min extra |
| Preview features | Pueden salir si son de uso común; la mayoría es GA |

Nota sobre labs en el examen: los reportes de quienes presentan (incluido el propio Sil) hablan de una sección práctica con tareas en portal. Por eso la sesión 5 es labs. No hay documento oficial que liste esas tareas; lo que usamos es el repo oficial de labs del curso, que cubre las mismas habilidades.

---

## 3. Qué cambió en el outline 2026 vs lo que suele enseñarse

Hay que ajustar el foco porque el examen sí lo pregunta:

- Global Secure Access (Private Access, Internet Access, M365 Internet Access) ahora está dentro de Auth & Access.
- Defender for Cloud Apps (cloud discovery, session policies, OAuth apps, app control) está dentro de Workload identities.
- Cross-tenant synchronization y cross-tenant access settings están en Identities (vale la pena dedicarle tiempo).
- Custom security attributes, protected actions, authentication context, CAE, passkeys FIDO2, TAP, CBA: todos nombrados explícitamente.
- Hybrid: Cloud Sync junto a Connect Sync, y migración desde AD FS.
- Managed identities y managed service accounts: nombrados en la selección de identidad para workloads.

---

## 4. Estructura del cohort: 5 sesiones de 45 minutos

| Sesión | Módulo | Minutos en vivo | Trabajo previo del estudiante |
|---|---|---|---|
| 1 | Kickoff (10 min) + M1 Identities | 45 | Leer guía M1, contestar banco M1 |
| 2 | M2 Authentication & Access | 45 | Guía M2, banco M2, practice assessment oficial |
| 3 | M3 Workload identities & apps | 45 | Guía M3, banco M3 |
| 4 | M4 Governance & monitoring | 45 | Guía M4, banco M4 |
| 5 | Labs en imágenes + estrategia de examen + simulacro corto | 45 | Repasar los 10 labs, hacer simulacro de 30 preguntas |

Ritmo dentro de cada sesión de 45:

| Bloque | Min | Contenido |
|---|---|---|
| Tips and tricks | 15 | Las 8 a 10 trampas del dominio, palabras clave que delatan la respuesta |
| Visuales clave | 10 | 3 a 4 diagramas: cómo piensa el examen el concepto |
| Kahoot | 15 | 10 preguntas del banco, las más falladas en el trabajo previo |
| Debrief y cierre | 5 | Qué estudiar esta semana, quién presenta pronto |

Por qué 15 min de Kahoot y no más: el valor está en la explicación de cada distractor. 10 preguntas bien explicadas valen más que 25 corridas.

---

## 5. Mapa de módulos contra el outline

### M1: Implement and manage user identities (20 a 25%)

Subdominios del outline:
1. Configure and manage a Microsoft Entra tenant (roles, custom roles, AUs, effective permissions, domains, branding, tenant/user/group/device settings)
2. Create, configure, and manage identities (users, groups, custom security attributes, bulk ops con admin center y PowerShell, device join/registration, licenses)
3. External users and tenants (collaboration settings, invite, cross-tenant access settings, cross-tenant sync, external IdPs SAML/WS-Fed)
4. Hybrid identity (Connect Sync, Cloud Sync, PHS, PTA, Seamless SSO, migrar desde AD FS, Connect Health)

Trampas típicas (para tips and tricks):
- Restricted management AU vs AU normal: quién puede tocar los objetos.
- Custom role: solo permisos permitidos, scope a AU o a app.
- Group-based licensing: errores por conflicto de service plans, no se quita la licencia al salir hasta el siguiente ciclo.
- Dynamic groups: sintaxis de reglas y qué atributos sirven para devices vs users.
- Guest vs member userType, y "external member" en cross-tenant.
- Cross-tenant sync: outbound en el source, inbound en el target, y el usuario aparece como external member.
- PHS vs PTA vs federation: cuál sigue funcionando si se cae on-prem.
- Cloud Sync vs Connect Sync: qué soporta cada uno. Ojo: Learn ya marca Exchange hybrid y group writeback como soportados en ambos. Las diferencias que siguen vigentes: hybrid join device sync, configurar PTA y AD FS, sync rules avanzadas, forests desconectados, varios agentes activos, límite de 150K objetos por dominio en Cloud Sync.
- Seamless SSO: solo con PHS o PTA, no con federación.
- Staging mode y Connect Health alerts.

### M2: Implement authentication and access management (25 a 30%)

Subdominios:
1. User authentication (métodos: CBA, TAP, OAuth tokens, Authenticator, passkeys FIDO2; MFA tenant-wide; SSPR; WHfB; disable/revoke sessions; password protection; Entra Kerberos)
2. Conditional Access (plan, assignments, controls, test/troubleshoot, session, device restrictions, CAE, authentication context, protected actions, templates)
3. ID Protection (user risk, sign-in risk, MFA registration campaigns, investigate/remediate, workload identity risk)
4. Global Secure Access (clients, Private Access, Internet Access, Internet Access for M365)

Trampas típicas:
- Authentication strengths: built-in vs custom, y cómo se combinan con CA.
- TAP: es para registrar passwordless, tiene tiempo de vida y usos.
- SSPR: número de métodos, writeback requiere Connect Sync o Cloud Sync con la opción.
- Security defaults vs CA: mutuamente excluyentes.
- CA: report-only, What If, exclusiones de break-glass, "All cloud apps" vs targeted.
- User risk → remediación con password change; sign-in risk → remediación con MFA. Nunca al revés.
- CAE: qué eventos revoca y qué apps lo soportan.
- Authentication context: se liga a una CA policy y se invoca desde SharePoint, Purview, PIM.
- Protected actions: CA sobre acciones específicas (CA policy management) no sobre apps.
- Password protection: custom banned list, on-prem agent y proxy, audit vs enforce.
- Revocar sesiones: revoke refresh tokens + CAE para que aplique rápido.
- GSA: Private Access reemplaza VPN, Internet Access filtra web, M365 profile.

### M3: Plan and implement workload identities (20 a 25%)

Subdominios:
1. Identities for apps and Azure workloads (managed identity system vs user assigned, service principal, user account, managed service accounts; crear, asignar, usar)
2. Enterprise applications (app-level y tenant-level settings, roles para administrar apps, Application Proxy, SaaS, users/groups/app roles, user y admin consent, app collections)
3. App registrations (plan, create, auth config, API permissions, app roles)
4. Defender for Cloud Apps (cloud discovery, connected apps, app-enforced restrictions, CA app control, access y session policies, OAuth apps policies, cloud app catalog)

Trampas típicas:
- App registration (objeto en home tenant) vs enterprise application (service principal en cada tenant).
- Delegated vs application permissions y quién puede consentir cada una.
- Admin consent workflow: reviewers, expiración.
- User consent settings: allow, allow verified publishers, disable.
- System-assigned MI muere con el recurso, user-assigned vive sola y se comparte.
- Application Proxy: connector, pre-authentication (Entra vs passthrough), KCD para SSO integrado.
- SAML: Reply URL, Identifier, claims, certificate rollover.
- Roles: Application Administrator vs Cloud Application Administrator (App Proxy es la diferencia).
- Defender for Cloud Apps: session policy necesita CA app control y la app en CA con "Use Conditional Access App Control".
- Cloud discovery: log collector, snapshot vs continuous, Defender for Endpoint integration.

### M4: Plan and automate identity governance (20 a 25%)

Subdominios:
1. Entitlement management (catalogs, access packages, requests, ToU, lifecycle de externos, connected organizations)
2. Access reviews (plan, create, monitor, respond)
3. Privileged access (PIM para Entra roles, PIM para Azure resources, PIM for Groups, request/approval, audit, break-glass)
4. Monitoring (sign-in, audit, provisioning logs; diagnostic settings a Log Analytics, storage, Event Hubs; KQL; workbooks; Identity Secure Score)

Trampas típicas:
- Catalog owner vs access package manager: quién puede qué.
- Access package policy: quién puede pedir (internos, connected orgs, cualquier externo), aprobación multi-etapa, expiración.
- Connected organization: dominio o tenant, sponsors.
- Lifecycle de externos: bloquear y borrar tras X días sin access package.
- Access review: reviewers (self, managers, group owners), auto-apply, "if reviewers don't respond" opciones.
- PIM: eligible vs active, activation duration, require justification/MFA/approval, permanent assignments.
- PIM for Groups vs role-assignable groups.
- Break-glass: cloud-only, Global Admin activo permanente (no eligible en PIM), excluido de las CA policies que bloquean, con passkey FIDO2 o CBA distinto al de los admins normales (Learn ya no dice "sin MFA"), y alerta en sign-in logs vía Log Analytics.
- Diagnostic settings: qué categorías de logs existen (SignInLogs, AuditLogs, NonInteractive, ServicePrincipal, ManagedIdentity, ProvisioningLogs, RiskyUsers, etc.).
- Retención por defecto de logs según licencia (7 días Free, 30 días P1/P2; risky sign-ins 90 días con P2).
- PIM para Azure resources: el "Discover resources" ya es la experiencia legacy; la nueva no necesita onboarding.
- Catalogs: User Administrator ya no puede crearlos; Learn recomienda Identity Governance Administrator.
- Workbooks: necesitan Log Analytics.

### Sesión 5: Labs y estrategia

Los 10 labs que más pegan (basados en el repo oficial MicrosoftLearning/SC-300):
1. Lab 01 Manage user roles
2. Lab 03 Assign licenses via group membership
3. Lab 05 Add guest users (+ Lab 04 external collaboration settings)
4. Lab 08 Enable MFA (+ Lab 09 SSPR)
5. Lab 13 Implement and test a Conditional Access policy
6. Lab 14 User risk and sign-in risk policies
7. Lab 19 Register an application (+ Lab 21 admin consent)
8. Lab 22 Entitlement management catalog and access package
9. Lab 25 Access reviews
10. Lab 26 PIM for Entra roles

Índice oficial: https://microsoftlearning.github.io/SC-300-Identity-and-Access-Administrator/

---

## 6. Playbook "cómo pasar el SC-300" (abre el curso, 10 min)

Objetivo del bloque: que entiendan que el examen mide lectura de escenario, no memoria.

Frases clave:
- "El examen te da 3 datos y te pregunta por el cuarto. Los 3 datos son pistas, no contexto."
- "Si la pregunta dice 'minimize administrative effort', la respuesta es la más automática (dynamic group, group-based licensing, access package, PIM for Groups)."
- "Si dice 'least privilege', la respuesta es el rol más chico que alcance, nunca Global Admin."
- "Si dice 'users must' o 'must be prompted', es Conditional Access. Si dice 'users at risk', es ID Protection."
- "Preview no suele salir, pero si es de uso común sí. GA es la regla."
- "Nunca respondas con lo que harías en tu trabajo; responde con lo que Microsoft dice en Learn."

Estrategia de examen:
- Case studies: leer las preguntas primero, luego el caso. Marcar requisitos técnicos y de negocio.
- Preguntas Yes/No en serie: son independientes, no se puede regresar. Cada una se evalúa sola.
- Drag and drop y hot area: el orden importa, buscar la secuencia lógica del portal.
- Labs: hacer primero lo que se sabe, dejar lo largo al final, el portal se califica por estado final, no por pasos.
- Tiempo: no gastar más de 2 min en una pregunta de opción múltiple. Marcar para revisar.

---

## 7. Ritual de debrief post-examen (reemplaza a los dumps)

Cada persona que presenta llena esto el mismo día, sin preguntas literales:

| Campo | Qué anotar |
|---|---|
| Resultado | Pass / no pass y score aproximado por dominio (el score report lo da) |
| Dominios que más pesaron | Por sensación: cuál dominó |
| Tipos de escenario que costaron | Por tema, ejemplo: "CA con authentication context", "PIM for Groups vs role-assignable" |
| Labs que salieron | Por tarea, ejemplo: "crear access package con aprobación", no pasos exactos |
| Qué hubiera estudiado más | Libre |

Por qué funciona: acumula señal legítima sobre el peso real de cada tema y se convierte en el input para ajustar tips and tricks cada cohort. No se guarda ninguna pregunta.

---

## 7b. Vigencia: cosas que cambian entre sept y oct 2026 (revisar antes de cada cohort)

| Cambio | Fecha | Dónde pega |
|---|---|---|
| Legacy ID Protection risk policies se retiran; se reemplazan con CA + "Require risk remediation" | 1 oct 2026 | M2 (Q3, Q4, Q6, Q29, Q32, Q33), Lab 14 |
| Registration campaign ahora puede apuntar a Authenticator o passkeys; rollout termina fin de sept 2026 | sept 2026 | M2 |
| Passkeys usan passkey profiles | 2026 | M2 |
| "Report suspicious activity" reemplazó a fraud alert | ya | M2 |
| Approved client app grant en retiro | ya | M2 |
| Entitlement management y access reviews requieren Entra ID Governance (algunas funciones con P2) | ya | M4, Labs 22 a 25 |
| Outline dice "OAuth 2.0 tokens" pero el método en Learn es OATH tokens (TOTP); se cubren ambos | ya | M2 |
| Managed identity on-prem: sí existe con Azure Arc | ya | M3 (Q3) |

---

## 8. Decisiones editoriales tomadas (cambiables)

- Preguntas del banco en inglés (el idioma del examen), explicaciones en Spanglish. Practicar en el idioma real quita fricción el día del examen.
- Screenshots: primero las oficiales de Learn (URL directa). Lo que falte y sea crítico, captura de Sil en su tenant. Búsqueda de imágenes como último recurso.
- Formato de entrega: Markdown consultable ahora; decks pptxgenjs con diseño SC-300 Tips and Tricks cuando se apruebe el contenido.
- Diseño: navy/cyan SC-300 Tips and Tricks, mismo esqueleto en los 4 módulos.

---

## 9. Archivos de esta carpeta

| Archivo | Qué es |
|---|---|
| 00-plan.md | Este documento |
| content/sources/M1..M4-sources.md | Links principales y links directos a párrafos por skill del outline |
| content/banco/M1..M4-banco.md | Preguntas originales con explicación por distractor |
| content/labs/labs-en-imagenes.md | Walkthrough de los 10 labs con URLs de screenshots oficiales |
| content/visuals/*.svg | Diagramas de soporte |
| content/modulos/M1..M4-tips.md | Tips and tricks listos para deck (frases clave + objetivo por slide) |
