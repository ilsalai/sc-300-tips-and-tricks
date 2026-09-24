# M3 Tips and tricks: Plan and implement workload identities (20 a 25%)

Bloque en vivo de 15 minutos. 12 trampas, más o menos 1 minuto cada una, y 3 minutos para preguntas.
Cada trampa trae: la frase que dice el presenter, la regla, las palabras de la pregunta que delatan la respuesta y el link al párrafo exacto en Learn.
Las preguntas del banco que practican cada trampa van al final de cada bloque.

---

## Trampa 1. App registration contra enterprise application

Frase clave: **"App registration es el molde, enterprise app es la galleta: un molde en casa, una galleta por tenant."**

Regla:
- App registration = **application object**, uno solo, en el home tenant. Enterprise app = **service principal**, uno por cada tenant que usa la app (multitenant crea uno en cada tenant que consiente).
- Cambios al application object se reflejan en el SP del home tenant. Una managed identity tiene **solo service principal**, sin application object: sus permisos de Graph van directo al SP.

Palabras que delatan: "home tenant", "multitenant", "partner tenant grants consent", "which object is created", "Managed application in local directory", "App registrations vs Enterprise applications".

Link: https://learn.microsoft.com/entra/identity-platform/app-objects-and-service-principals#relationship-between-application-objects-and-service-principals

Practica: Q7, Q8, Q22

---

## Trampa 2. System-assigned contra user-assigned

Frase clave: **"System-assigned vive y muere con su recurso; user-assigned es roomie: la compartes y la borras tú."**

Regla:
- System-assigned: una identidad, un recurso, se borra con él. User-assigned: recurso aparte, se asigna a muchos, se puede **pre-autorizar** antes de crear las VMs, y es la recomendada para servicios de Microsoft.
- Crear user-assigned: **Managed Identity Contributor**. Asignarla a una VM: **Virtual Machine Contributor + Managed Identity Operator**. Son roles de Azure RBAC, no de Entra. Después se autoriza en el destino (por ejemplo Storage Blob Data Reader).

Palabras que delatan: "same identity for all instances", "recreated frequently", "before the VMs are deployed", "shared across", "least privilege to assign", "when the VM is deleted".

Link: https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview#differences-between-system-assigned-and-user-assigned-managed-identities

Practica: Q1, Q2, Q4, Q5

---

## Trampa 3. Workload fuera de Azure: la managed identity no llega

Frase clave: **"Managed identity no sale de Azure (salvo con Arc). Afuera: service principal con cert o federated. On-prem Windows: gMSA."**

Regla:
- Server on-premises solo tiene managed identity si es **Azure Arc-enabled** (system-assigned). Sin Arc: service principal con **certificate** (mejor que secret; el secret dura máximo 24 meses) o **federated credential** si hay un IdP externo (GitHub Actions, Kubernetes).
- Servicio Windows on-premises: **gMSA** para varios servers o load balancer, **sMSA** para uno solo. User account como service account es la última opción.

Palabras que delatan: "on-premises datacenter", "not onboarded to Azure Arc", "GitHub Actions", "no secrets stored", "more secure than a client secret", "behind a load balancer", "password rotated automatically".

Link: https://learn.microsoft.com/entra/architecture/service-accounts-on-premises#choose-the-right-type-of-service-account

Practica: Q3, Q6, Q24

---

## Trampa 4. Delegated contra application, y quién consiente

Frase clave: **"Delegated = actúo como tú; application = actúo como yo. Y 'como yo' siempre lo aprueba un admin."**

Regla:
- Delegated (scopes) = hay usuario y la app no ve más que él; consienten usuarios o admin. Application (app roles) = sin usuario, ve todo lo del permiso; **solo admin**.
- Application permissions de **Microsoft Graph** las consiente **Privileged Role Administrator** (o Global Admin). Application Admin y Cloud Application Admin consienten todo lo demás. Un scope marcado "Admins only" también pide admin.

Palabras que delatan: "without a signed-in user", "daemon", "background service", "on behalf of the signed-in user", "Microsoft Graph application permission", "Grant admin consent is unavailable", "Admins only".

Link: https://learn.microsoft.com/entra/identity-platform/permissions-consent-overview#types-of-permissions

Practica: Q7, Q18, Q27, Q30

---

## Trampa 5. User consent, step-up y admin consent workflow

Frase clave: **"Si el usuario no puede consentir, el workflow le da un botón para pedir; ser reviewer no te da superpoderes."**

Regla:
- User consent: no permitir, **verified publishers con permisos low impact**, permitir todo, o dejar que Microsoft lo maneje (default en tenants nuevos). Risk-based step-up consent viene activo y solo actúa si hay user consent. Apps con Assignment required siempre piden admin consent.
- Admin consent workflow: reviewers por usuario, grupo o rol; para **aprobar** necesitan el rol adecuado; los reviewers nuevos no ven solicitudes viejas; las solicitudes expiran en los días que configuras.

Palabras que delatan: "request approval from the consent prompt", "unverified publisher", "reviewers", "expires after", "added later as a reviewer", "risky consent request", "AADSTS90094".

Link: https://learn.microsoft.com/entra/identity/enterprise-apps/configure-admin-consent-workflow#enable-the-admin-consent-workflow

Practica: Q16, Q17

---

## Trampa 6. Application Admin contra Cloud Application Admin

Frase clave: **"Cloud App Admin es App Admin sin el Proxy. Y ninguno de los dos toca CA ni Graph application permissions."**

Regla:
- **Application Administrator**: todo en enterprise apps y app registrations, más **Application Proxy** (apps y connector groups). **Cloud Application Administrator**: igual, sin App Proxy.
- Si "Users can register applications" está en No, el rol mínimo para registrar es **Application Developer**. Ninguno de estos roles administra Conditional Access.

Palabras que delatan: "connector group", "publish on-premises apps", "least privilege", "users can't register applications", "configure SAML SSO", "create a Conditional Access policy for the app".

Link: https://learn.microsoft.com/entra/identity/role-based-access-control/delegate-app-roles#assign-built-in-application-administrator-roles

Practica: Q9, Q18, Q21

---

## Trampa 7. Application Proxy: pre-auth, connectors, custom domain y KCD

Frase clave: **"Sin pre-auth de Entra no hay CA, ni MFA, ni SSO. El connector solo sale, nunca entra."**

Regla:
- Pre-auth **Microsoft Entra ID** (default) da CA, MFA, SSO y monitoreo con Defender; **Passthrough** no. Connectors solo outbound (80 y 443), mínimo **dos por connector group**. Custom domain = **PFX con private key + CNAME** a msappproxy.net. Licencia P1 o P2.
- SSO a apps IWA = **KCD**: en AD, el computer account del connector delega al SPN de la app ("specified services only" + "any authentication protocol"); en Entra, SSO Integrated Windows authentication con el SPN. Dominios distintos: resource-based KCD.

Palabras que delatan: "Integrated Windows Authentication", "Kerberos", "SPN", "Passthrough", "no inbound ports", "custom domain", "expenses.contoso.com", "high availability", "different domains".

Link: https://learn.microsoft.com/entra/identity/app-proxy/how-to-configure-sso-with-kcd#configure-single-sign-on

Practica: Q10, Q11, Q12

---

## Trampa 8. SAML: los campos y el rollover del certificado

Frase clave: **"Entity ID dice quién eres, Reply URL dice a dónde mando el token. El cert no se edita: se crea otro."**

Regla:
- **Identifier (Entity ID)** y **Reply URL (ACS)** son obligatorios; **Sign on URL** solo para SP-initiated. El Login URL y el Microsoft Entra Identifier de "Set up" van del lado del vendor.
- Certificado autogenerado: **3 años**, avisos a 60, 30 y 7 días (hasta 5 correos). Renovar sin downtime: nuevo cert con fecha traslapada, descargar, subir a la app, **Make certificate active**, probar.

Palabras que delatan: "Assertion Consumer Service", "Entity ID", "SP-initiated", "certificate expires in", "no downtime", "notification email", "change the expiration date".

Link: https://learn.microsoft.com/entra/identity/enterprise-apps/tutorial-manage-certificates-for-federated-single-sign-on#renew-a-certificate-that-is-set-to-expire-soon

Practica: Q13, Q15

---

## Trampa 9. Visible, Assignment required, Enabled, grupos y collections

Frase clave: **"Visible esconde, Assignment required filtra, Enabled apaga. Y los grupos anidados no cuentan."**

Regla:
- **Visible to users** solo esconde en My Apps. **Assignment required** = solo asignados obtienen token. **Enabled for users to sign in = No** = no hay tokens para nadie, sin perder la configuración. Estos son settings de app; Users can register applications y consent son de tenant.
- Asignar grupos pide **P1 o P2** y **no cascada a grupos anidados**. **Collections** (App launchers, P1 o P2) agrupan apps en una pestaña de My Apps, pero solo muestran apps ya asignadas.

Palabras que delatan: "nested group", "not assigned to the app", "separate tab in My Apps", "hide the app", "stop all sign-ins without deleting", "only members of".

Link: https://learn.microsoft.com/entra/identity/enterprise-apps/application-properties#assignment-required

Practica: Q14, Q19, Q20

---

## Trampa 10. Configurar la app: plataforma, scope, app role o groups claim

Frase clave: **"Scope para 'on behalf of', app role para 'sin usuario' o para roles de usuario; el groups claim topa en 200."**

Regla:
- Redirect por **plataforma**: Single-page application para JavaScript con PKCE, Web para apps de servidor, daemon sin redirect. "On behalf of user" = **scope** en Expose an API (App ID URI primero); "sin usuario" = **app role** con Allowed member types Applications.
- Autorizar usuarios dentro de la app: app role **Users/Groups** (claim roles). Groups claim: límite **200 en JWT y 150 en SAML**; usa **Groups assigned to the application**. App role dado a un grupo con un service principal no emite roles.

Palabras que delatan: "React", "MSAL.js", "PKCE", "Expose an API", "roles claim", "group overage", "more than 200 groups", "Allowed member types".

Link: https://learn.microsoft.com/entra/identity-platform/howto-add-app-roles-in-apps#declare-roles-for-an-application

Practica: Q23, Q25, Q26, Q28, Q29

---

## Trampa 11. Cloud Discovery, catalog y el mito del Unsanctioned

Frase clave: **"Unsanctioned es una etiqueta, no un firewall: el bloqueo lo hace MDE o tu appliance."**

Regla:
- **Snapshot** = subes logs a mano, una vez. **Continuous** = Defender for Endpoint (también fuera de la oficina), log collector (Syslog o FTP), SWG o API. Bloqueo con MDE: Cloud y Network Protection, Enforce app access, Custom network indicators y luego Unsanctioned (hasta 3 horas; scoped profiles por device group).
- Catalog: más de 31,000 apps, 4 categorías (General, Security, Compliance, Legal). **Score metrics** cambia pesos para todas las apps; **Override** cambia una; **Request score update** le pide a Microsoft.

Palabras que delatan: "one-time assessment", "exported logs", "users working from home", "continuous", "block on devices", "specific device groups", "weight", "all apps", "only this app".

Link: https://learn.microsoft.com/defender-cloud-apps/set-up-cloud-discovery#snapshot-and-continuous-risk-assessment-reports

Practica: Q31, Q32, Q33, Q34, Q39

---

## Trampa 12. Session control: quién hace qué

Frase clave: **"Session policy sin el CA 'Use Conditional Access App Control' es perro sin dientes. Y app enforced solo muerde en Exchange y SharePoint."**

Regla:
- Access y session policies necesitan una política de CA con **Session > Use Conditional Access App Control**. **Access policy** = entrar o no (con Client app = Mobile and desktop bloquea clientes nativos). **Session policy** = qué haces dentro, solo browser. **Use app enforced restrictions** = solo EXO y SPO, sin licencia de Defender for Cloud Apps.
- **App connector** = API (actividad, cuentas, archivos), sin proxy. **OAuth app policy** = Permission level, Community use y usuarios que autorizaron; acción Revoke app; pide el connector.

Palabras que delatan: "session policy has no effect", "desktop sync client", "native client", "browser only", "limited web-only access", "no Defender for Cloud Apps licenses", "through the vendor's API", "without a proxy", "rare community use", "high permission level".

Link: https://learn.microsoft.com/defender-cloud-apps/session-policy-aad#prerequisites

Practica: Q35, Q36, Q37, Q38, Q40

---

## Objetivo de la sesión

El presenter no tiene que recitar menús ni números. Tiene que entender que casi todas las preguntas de M3 se resuelven con cuatro preguntas: **¿quién es la identidad?** (application object o service principal, system o user-assigned, y si vive dentro o fuera de Azure), **¿quién actúa y quién aprueba?** (delegated o application, qué rol puede consentir y qué hace el workflow cuando el usuario no puede), **¿por dónde entra el usuario a la app?** (SAML directo, App Proxy con pre-auth y KCD, y qué settings de la app filtran, esconden o apagan) y **¿qué ve y qué controla Defender for Cloud Apps?** (discovery por tráfico, connectors por API, proxy por Conditional Access). Si el presenter puede tomar cualquier pregunta del banco, señalar las dos o tres palabras que la delatan y explicar con sus palabras por qué cada distractor falla, la sesión cumplió. Los datos finos (3 años del certificado, 200 y 150 grupos, 24 meses del secret, 3 horas del bloqueo con MDE) se quedan en la guía para consulta.

---

## Orden sugerido de slides (10)

| # | Título | Para qué sirve |
|---|---|---|
| 1 | M3 en un vistazo | Mostrar los 4 subdominios, el peso de 20 a 25% y las cuatro preguntas: identidad, consent, entrada y Defender. |
| 2 | El molde y la galleta | Dibujo de application object en el home tenant y service principals por tenant, más el SP sin molde de la managed identity (trampa 1). |
| 3 | Qué identidad le doy a este workload | Árbol de decisión: Azure con recurso compartido, Azure solo, fuera de Azure con o sin Arc, GitHub, servicio Windows on-prem (trampas 2 y 3). |
| 4 | Permisos y consent | Tabla delegated contra application, quién consiente cada uno, user consent settings y admin consent workflow (trampas 4 y 5). |
| 5 | Roles para administrar apps | App Admin, Cloud App Admin, Application Developer y Privileged Role Admin, con la línea roja del App Proxy (trampa 6). |
| 6 | Application Proxy de punta a punta | Flujo usuario, Entra pre-auth, servicio, connector outbound, KCD al SPN y custom domain con CNAME (trampa 7). |
| 7 | SAML sin sustos | Los tres URLs del Basic SAML Configuration y la línea de tiempo del rollover del certificado (trampa 8). |
| 8 | Configurar la app bien | Visible, Assignment required, Enabled y collections; luego plataforma de redirect, scopes, app roles y groups claim (trampas 9 y 10). |
| 9 | Defender for Cloud Apps: ver | Snapshot contra continuous, Unsanctioned y bloqueo con MDE, catalog y score metrics (trampa 11). |
| 10 | Defender for Cloud Apps: controlar | CA App Control, access contra session, app enforced restrictions, connectors y OAuth app policies, como cierre antes del Kahoot (trampa 12). |
