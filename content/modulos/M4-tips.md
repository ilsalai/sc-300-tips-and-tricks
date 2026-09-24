# M4 Tips and tricks: Plan and automate identity governance (20 a 25%)

Bloque en vivo de 15 minutos. 12 trampas, más o menos 1 minuto cada una, y 3 minutos para preguntas.
Cada trampa trae: la frase que dice el presenter, la regla, las palabras de la pregunta que delatan la respuesta y el link al párrafo exacto en Learn.
Las preguntas del banco que practican cada trampa van al final de cada bloque.

---

## Trampa 1. Roles de entitlement management: quién crea, quién asigna

Frase clave: **"Catalog owner trae los recursos, access package manager arma los paquetes, assignment manager solo mete y saca gente."**

Regla:
- Catalog owner agrega recursos y delega. Access package manager crea y edita paquetes y policies con lo que ya está en el catalog. Access package assignment manager asigna, quita, ve requests y reprocesa, pero no crea paquetes.
- Para agregar un recurso al catalog hay que ser catalog owner y además tener permiso sobre el recurso. Identity Governance Administrator agrega apps, no grupos. User Administrator ya no crea catalogs.

Palabras que delatan: "least privilege", "create access packages but not add resources", "only assign users", "resource picker is empty", "catalog creator", "delegate to the department".

Link: https://learn.microsoft.com/entra/id-governance/entitlement-management-delegate#entitlement-management-roles

Practica: Q2, Q3

---

## Trampa 2. Quién puede pedir: una policy, un público

Frase clave: **"Internos y externos no caben en la misma policy: son dos."**

Regla:
- Una policy es "in your directory" (members, all users with guests, specific groups) o "not in your directory" (specific connected orgs, all configured connected orgs, all users). No mezcla las dos.
- "All users" crea connected orgs en estado **proposed**, y esas no entran en "All configured connected organizations". Pide email OTP. La B2B allow/block list siempre gana.

Palabras que delatan: "employees and partners", "minimum number of policies", "any user on the internet", "connected organization", "allowlist", "no guest account is created".

Link: https://learn.microsoft.com/entra/id-governance/entitlement-management-access-package-request-policy#choose-between-one-or-multiple-policies

Practica: Q4, Q11

---

## Trampa 3. Aprobación: un approver por stage, y el reloj corre

Frase clave: **"En cada stage basta uno; si nadie decide a tiempo, la request se muere y se pide otra vez."**

Regla:
- Hasta 3 stages. En cada stage decide el primero que responde. Si nadie decide en los días configurados, la request expira (se deniega).
- Alternate approvers: forward después de N días, con timeout de al menos 4 días. Fallback es otra cosa: se usa cuando no se encuentra el manager. Manager as approver solo existe para usuarios de tu directorio; para externos usas sponsors.

Palabras que delatan: "doesn't respond", "backup approver", "forward", "manager can't be found", "external sponsor", "second stage", "extension requires approval".

Link: https://learn.microsoft.com/entra/id-governance/entitlement-management-access-package-approval-policy#alternate-approvers

Practica: Q5, Q6, Q7, Q12

---

## Trampa 4. El guest que pierde su último paquete

Frase clave: **"Último paquete perdido: bloqueado hoy, borrado en 30 días. Con 0 días, borrado ya."**

Regla:
- Default: bloqueo de sign-in y borrado a los 30 días. Se cambia en Control Configurations > Lifecycle of external users.
- Solo aplica a guests que entraron por entitlement management (o convertidos a governed), y se borran aunque tengan otros accesos como un sitio de SharePoint compartido después.

Palabras que delatan: "last access package assignment", "as soon as possible", "guest account is removed", "also has access to a SharePoint site", "blocked from signing in".

Link: https://learn.microsoft.com/entra/id-governance/entitlement-management-external-users#manage-the-lifecycle-of-external-users

Practica: Q8, Q12

---

## Trampa 5. Terms of use: sin Conditional Access no pasa nada

Frase clave: **"La ToU es un PDF que no muerde hasta que Conditional Access la pone en el Grant."**

Regla:
- P1 y Conditional Access Administrator. Se hace cumplir con una política de CA. Per-device pide device registrado y no soporta B2B.
- Expire consents o Duration before re-acceptance: se vuelve a aceptar solo cuando la sesión expira. Si el usuario rechaza, queda bloqueado. El reporte de aceptación vive lo que vive la ToU; los audit logs, 30 días.

Palabras que delatan: "must accept before accessing", "every device", "guest users", "re-accept every 90 days", "create Conditional Access policy later", "declined".

Link: https://learn.microsoft.com/entra/identity/conditional-access/terms-of-use#per-device-terms-of-use

Practica: Q9, Q10

---

## Trampa 6. Access reviews: dónde se crean y quién revisa

Frase clave: **"Grupos y apps en Access reviews, roles en PIM, paquetes en entitlement management. Fallback solo si hay managers u owners."**

Regla:
- Reviewers: group owners, selected users or groups, self review, managers. Fallback solo con managers u owners. Cuentan los owners que existían al inicio de la review.
- Scope Guest users only o Everyone, con inactive users hasta 730 días. "All Microsoft 365 groups with guest users" solo revisa guests y no deja elegir la acción para guests denegados.

Palabras que delatan: "review Global Administrator assignments", "group has no owner", "guest users only", "all Microsoft 365 groups", "group owners create reviews", "quarterly".

Link: https://learn.microsoft.com/entra/id-governance/access-reviews-overview#where-do-you-create-reviews

Practica: Q13, Q14, Q17

---

## Trampa 7. Nadie respondió y auto apply está prendido

Frase clave: **"If reviewers don't respond más auto apply es un botón de borrar: elige con cuidado."**

Regla:
- Opciones: No change, Remove access, Approve access, Take recommendations. Take recommendations usa el helper "No sign-in within 30 days": quita a los inactivos y deja a los activos.
- Remove access o Take recommendations con auto apply pueden quitar todo el acceso. La acción "block 30 days, then remove" para guests aplica también a los que se niegan por no respuesta.

Palabras que delatan: "if the reviewer doesn't respond", "inactive users lose access", "active users keep access", "automatically", "guest is blocked".

Link: https://learn.microsoft.com/entra/id-governance/create-access-review#next-settings

Practica: Q14, Q15

---

## Trampa 8. Decisiones: gana la última y nada pasa hasta el final

Frase clave: **"En access reviews no gana la mayoría, gana el último. Y el deny se cobra al final."**

Regla:
- Con varios reviewers se guarda la última respuesta. En multi-stage, la etapa posterior sobrescribe. Don't know deja el acceso. El denegado sale al final o al Stop, y una review detenida no se reinicia.
- Sin auto apply: Review history > instancia > Apply. Apply no cambia grupos de on-premises ni grupos dinámicos. Para auditoría de muchas reviews, el reporte Review History (CSV 30 días).

Palabras que delatan: "two reviewers disagree", "removed immediately", "only approved users go to the next stage", "auto apply was disabled", "synced from on-premises", "single CSV for auditors".

Link: https://learn.microsoft.com/entra/id-governance/perform-access-review#manually-review-access-for-one-or-more-users

Practica: Q16, Q18, Q19, Q20

---

## Trampa 9. PIM: eligible, active, permanent y las perillas del rol

Frase clave: **"Eligible es JIT, time-bound es con fecha de muerte. El ticket es de adorno y el approver no necesita rol."**

Regla:
- Activation maximum duration de 1 a 24 horas. Ticket solo informativo. En roles de Entra, sin approvers configurados aprueban los PRA y GA activos. En Azure resources y Groups no hay approvers por default.
- El approver no necesita rol, nadie aprueba lo suyo, la primera decisión resuelve, 24 horas para aprobar (roles de Entra). Para forzar un método fuerte en la activación: authentication context más authentication strength, con la política de CA para todos o los eligible, no para el rol.

Palabras que delatan: "only when needed", "for six months", "no approvers selected", "ticket number", "approver doesn't respond", "even if they already completed MFA", "phishing-resistant at activation".

Link: https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings#require-approval-to-activate

Practica: Q21, Q22, Q23, Q30, Q31

---

## Trampa 10. PIM for Azure resources y PIM for Groups

Frase clave: **"En Azure, los settings no bajan de la suscripción al resource group. En Groups, el grupo no tiene que ser role-assignable."**

Regla:
- Azure resources: settings con Owner o User Access Administrator, por rol y por recurso, sin herencia. No hay eligible para service principals ni managed identities. Discovery legacy pone a MS-PIM como User Access Administrator y no se deshace.
- PIM for Groups: JIT de member u owner, dos policies por grupo, no aplica a grupos dinámicos ni synced. Role-assignable protege credenciales y no acepta grupos anidados activos. Para Exchange o SharePoint conviene PIM for Entra roles.

Palabras que delatan: "configured on the subscription", "resource group", "managed identity", "discover resources", "not role-assignable", "dynamic group", "reset the password of an eligible member".

Link: https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-resource-roles-configure-role-settings#overview

Practica: Q24, Q25, Q26, Q27

---

## Trampa 11. Break-glass: permanente, fuerte y vigilada

Frase clave: **"La break-glass no espera aprobación: GA active permanent, FIDO2 en la caja fuerte y una alerta que grita en cada sign-in."**

Regla:
- Dos o más cuentas cloud-only en .onmicrosoft.com, GA active permanent, passkey FIDO2 o CBA distinto al de los admins, excluidas de CA que bloquea o restringe (Report-only no necesita exclusión).
- Monitoreo: SigninLogs en Log Analytics, alert rule con Custom log search sobre los object IDs, umbral mayor que 0, sin filtrar por éxito. Validar cada 90 días.

Palabras que delatan: "emergency access", "all admins are eligible", "approval required and no approvers", "federation outage", "alert whenever the account signs in", "report-only".

Link: https://learn.microsoft.com/entra/identity/role-based-access-control/security-emergency-access#create-an-alert-rule

Practica: Q28, Q29

---

## Trampa 12. Logs: cuánto duran, a dónde van y en qué tabla caen

Frase clave: **"Free 7, P1/P2 30, y el upgrade no revive datos. Cada categoría llena su tabla, y el workbook come de Log Analytics."**

Regla:
- Storage account para archivo barato y largo, event hub para SIEM de terceros, Log Analytics para KQL, workbooks y alertas. La diagnostic setting la crea un Security Administrator y el destino existe antes. PIM audit guarda 30 días; para más, diagnostic settings.
- Tablas: SigninLogs, AADNonInteractiveUserSignInLogs, AADServicePrincipalSignInLogs, AADManagedIdentitySignInLogs, AuditLogs, AADProvisioningLogs. En provisioning, ResultType Failure con ResultSignature. Secure Score: cada 24 horas, Risk accepted no suma, Resolved through third party sí.

Palabras que delatan: "upgraded today", "20 days ago", "two years at low cost", "third-party SIEM", "query returns no results", "workbook is empty", "non-Microsoft MFA", "score doesn't change".

Link: https://learn.microsoft.com/entra/identity/monitoring-health/concept-log-monitoring-integration-options-considerations#integration-options

Practica: Q32, Q33, Q34, Q35, Q36, Q37, Q38, Q39, Q40

---

## Objetivo de la sesión

El presenter no tiene que recitar settings. Tiene que entender **una idea por área** y explicarla con sus palabras. En entitlement management, el access package es un contrato: un catalog pone los recursos, la policy dice quién pide, quién aprueba y cuándo vence, y el ciclo de vida del guest limpia al final. En access reviews, la review toma una foto al inicio, gana la última decisión y nada cambia hasta el final o hasta Apply, así que el setting de "no respuesta" con auto apply es lo que más daño o más limpieza hace. En PIM, eligible es acceso JIT y las reglas viven en el rol (y en Azure, en cada recurso, sin herencia), mientras que la break-glass es la única excepción: active permanent y muy vigilada. En monitoreo, la licencia define cuánto guardas, la diagnostic setting define a dónde va cada categoría y cada categoría cae en su propia tabla de Log Analytics. Si el presenter puede contestar "¿quién decide?, ¿cuándo pasa?, ¿dónde queda el dato?" en cada área, ya domina el dominio.

---

## Orden sugerido de slides (10)

| # | Título | Propósito |
|---|---|---|
| 1 | Identity governance en un mapa | Ubicar las 4 áreas y su peso (20 a 25%) antes de entrar a trampas. |
| 2 | Catalog, access package, policy | Mostrar el contrato del access package y los roles que lo manejan (trampas 1 y 2). |
| 3 | Aprobaciones y el reloj | Explicar stages, timeouts, alternate y fallback con un solo diagrama (trampa 3). |
| 4 | Externos: entrar y salir | Seguir a un guest desde la connected org hasta su borrado, más la ToU con CA (trampas 4 y 5). |
| 5 | Access reviews: dónde y quién | Tabla de dónde se crea cada review y quién revisa, con fallback (trampa 6). |
| 6 | La review que borra todo | Caso de "If reviewers don't respond" con auto apply y decisiones que se pisan (trampas 7 y 8). |
| 7 | PIM: eligible vs active | Matriz eligible/active por permanent/time-bound y las perillas del rol (trampa 9). |
| 8 | PIM fuera de Entra roles | Azure resources sin herencia y PIM for Groups vs role-assignable (trampa 10). |
| 9 | Break-glass bien hecha | Checklist de la cuenta de emergencia y la query de alerta en vivo (trampa 11). |
| 10 | Del log a la respuesta | Retención, destinos, tablas y una query KQL de provisioning, más Secure Score (trampa 12). |
