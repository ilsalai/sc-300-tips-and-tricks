# M2 Tips and tricks: Implement authentication and access management (25 a 30%)

Bloque en vivo de 15 minutos. 12 trampas, más o menos 1 minuto cada una, y 3 minutos para preguntas.
Cada trampa trae: la frase que dice el presenter, la regla, las palabras de la pregunta que delatan la respuesta y el link al párrafo exacto en Learn.
Las preguntas del banco que practican cada trampa van al final de cada bloque.

---

## Trampa 1. TAP: pase de entrada, no llave maestra

Frase clave: **"La TAP es el pase de visitante: te deja registrar tu llave, pero no es tu llave."**

Regla:
- Se habilita en la Authentication methods policy y solo la usan los usuarios dentro del alcance. Vive de 10 minutos a 30 días, una por usuario, y con one-time el registro de passwordless se cierra a los 10 minutos.
- Authentication Administrator crea TAP a usuarios sin rol; Privileged Authentication Administrator también a admins. Nadie se crea una TAP a sí mismo, y no sirve con NPS extension ni con el adapter de AD FS.

Palabras que delatan: "new hires", "onboard passwordless", "lost their security key", "one-time use", "within 10 minutes", "holds an administrator role", "least privilege".

Link: https://learn.microsoft.com/entra/identity/authentication/howto-authentication-temporary-access-pass#create-a-temporary-access-pass

Practica: Q1

---

## Trampa 2. Passkeys y Authenticator: dónde se configura cada cosa

Frase clave: **"Passkey en Authenticator se configura en FIDO2, no en Authenticator. Y synced passkey con attestation no se llevan."**

Regla:
- Passkey profiles por grupo: tipo (device-bound o synced), enforce attestation y AAGUIDs (allow o block). Hasta 3 perfiles con el Default, y el opt-in no tiene regreso. Synced passkeys no soportan attestation.
- En la política de Microsoft Authenticator, el modo Passwordless es phone sign-in (no es passkey). El passkey de Authenticator es device-bound y se permite por AAGUID en Passkey (FIDO2).

Palabras que delatan: "synced passkeys", "iCloud Keychain", "Google Password Manager", "verify the make and model", "specific security key models", "pilot group", "passkeys in Microsoft Authenticator".

Link: https://learn.microsoft.com/entra/identity/authentication/how-to-authentication-passkeys-fido2#passkey-profiles

Practica: Q3, Q4

---

## Trampa 3. CBA y authentication strengths: ¿es MFA? ¿es phishing-resistant?

Frase clave: **"En CBA, policy OID le gana al issuer. En strengths, phone sign-in es passwordless pero NO phishing-resistant, y TAP solo llega a MFA."**

Regla:
- CBA: la CA va al trust store con CRL por HTTP (sin CRL no hay revocación); default single-factor y low affinity; con High affinity se caen PrincipalName y RFC822Name.
- Strengths built-in: MFA, Passwordless MFA y Phishing-resistant MFA (FIDO2, WHfB o platform credential, CBA multifactor). No se editan, y no mezclas Require MFA con Require authentication strength en la misma política.

Palabras que delatan: "smart card", "policy OID", "certificate issuer", "revoked certificate", "high affinity", "phishing-resistant", "only FIDO2 security keys", "specific key model".

Link: https://learn.microsoft.com/entra/identity/authentication/concept-authentication-strengths#built-in-authentication-strengths

Practica: Q2, Q16, Q27

---

## Trampa 4. OAuth vs OATH, y cómo se controla la sesión

Frase clave: **"OAuth es el token, OATH es el código de 6 dígitos. ¿Quieres forzar reauth? Sign-in frequency, no token lifetime."**

Regla:
- Refresh y session token lifetime ya no se configuran desde el 30 de enero de 2021. AccessTokenLifetime solo mueve access, ID y SAML tokens (10 minutos a 1 día), y el refresh token renueva en silencio.
- Persistent browser session exige All resources y le gana al "Stay signed in?" de branding. Remember MFA choca con sign-in frequency: apágalo antes.

Palabras que delatan: "re-enter credentials every X hours", "token lifetime policy", "MaxAgeMultiFactor", "must not stay signed in after closing the browser", "unmanaged devices", "OATH hardware token".

Link: https://learn.microsoft.com/entra/identity-platform/configurable-token-lifetimes#token-lifetime-policies-for-refresh-tokens-and-session-tokens-retired

Practica: Q5, Q21

---

## Trampa 5. Passwords: SSPR, writeback y password protection

Frase clave: **"Writeback se prende en dos lados, los admins viven en two-gate, y en Audit el password malo pasa."**

Regla:
- SSPR: un solo grupo en Selected desde el portal, 1 o 2 métodos. Admins con two-gate fijo (sin security questions). Writeback pide P1 y se activa en el wizard de Connect y en On-premises integration; no se garantiza con staged rollout.
- Password protection: custom list de hasta 1000 términos de 4 a 16 caracteres. On-prem: proxy en server del dominio, DC agent en todos los DCs (con reboot), DCs sin internet. Audit registra y acepta; Enforced rechaza.

Palabras que delatan: "contact your administrator", "synchronized users can't reset", "Helpdesk Administrator can't use security questions", "some domain controllers", "Audit mode", "no internet access from domain controllers".

Link: https://learn.microsoft.com/entra/identity/authentication/howto-password-ban-bad-on-premises-operations#modes-of-operation

Practica: Q7, Q8, Q11

---

## Trampa 6. Kerberos en la nube: WHfB y Azure Files

Frase clave: **"Cloud Kerberos trust: cero PKI. Entra Kerberos en Azure Files: cero MFA para esa app."**

Regla:
- WHfB híbrido sin certificados: crear el objeto Microsoft Entra Kerberos (Set-AzureADKerberosServer), activar "Use cloud trust for on-premises authentication" y enrolar con línea de vista al DC la primera vez. Si "Use certificate for on-premises authentication" está activo, gana certificate trust.
- Azure Files: habilitar Entra Kerberos en el storage account, admin consent a la app y clientes con CloudKerberosTicketRetrievalEnabled. Un solo identity source por storage account, y la app del storage se excluye de las políticas de MFA.

Palabras que delatan: "no PKI", "must not deploy certificates", "SSO to on-premises file shares", "FSLogix", "Azure Virtual Desktop", "profile containers fail to mount after an MFA policy".

Link: https://learn.microsoft.com/entra/identity/authentication/kerberos#mfa-incompatibility-for-azure-files-authentication

Practica: Q9, Q12

---

## Trampa 7. Planear y probar CA sin lockout

Frase clave: **"Si nadie dice que no, Entra dice que sí. Para 'solo Finance' necesitas un block, y antes de todo, apaga security defaults."**

Regla:
- Security defaults y CA no conviven. Si ninguna política dispara un control, el token se emite. Excluye break-glass siempre; los templates nacen en report-only y solo excluyen a quien los crea.
- What If evalúa solo políticas On o report-only y no ve service dependencies. Report-only no sirve para User Actions (Register security information, Register or join devices).

Palabras que delatan: "security defaults are enabled", "only members of Finance", "users outside the group can access", "without affecting users", "from a template", "emergency access accounts", "Register or join devices".

Link: https://learn.microsoft.com/entra/identity/conditional-access/plan-conditional-access#combining-policies

Practica: Q13, Q14, Q19, Q20, Q26, Q28

---

## Trampa 8. Assignments y device-enforced restrictions

Frase clave: **"Excluye el PAW y bloquea el resto: un device no registrado es null, y null no se excluye."**

Regla:
- Directory roles en CA: solo built-in, nada con scope de AU ni custom roles. Guests: eliges tipo de usuario externo y tenant específico.
- Filter for devices: operadores positivos no aplican a devices no registrados, los negativos sí; extensionAttributes piden Intune, compliant o hybrid. App enforced restrictions da acceso limitado en SharePoint y Exchange sin productos extra.

Palabras que delatan: "privileged access workstation", "extensionAttribute", "unregistered devices must be blocked", "limited browser-only access", "no additional products", "guests from a specific partner".

Link: https://learn.microsoft.com/entra/identity/conditional-access/concept-condition-filters-for-devices#policy-behavior-with-filter-for-devices

Practica: Q15, Q17, Q18

---

## Trampa 9. CAE y revocar sesiones

Frase clave: **"CAE corta por eventos, no por cambios de grupo, y solo entiende IPs, no países. Revoke sessions es tu botón de 'ahora mismo'."**

Regla:
- Eventos críticos: cuenta deshabilitada o borrada, password cambiado o reseteado, MFA habilitado, revoke de refresh tokens y high user risk. Hasta 15 minutos; tokens de hasta 28 horas. Guests no.
- Cambios de grupo o de política tardan hasta un día. Híbrido: deshabilitar en AD, reset doble, Revoke-MgUserSignInSession y deshabilitar devices; sin CAE el access token vive hasta expirar.

Palabras que delatan: "near real time", "terminated employee", "account is synchronized", "country location", "added to an excluded group", "immediately".

Link: https://learn.microsoft.com/entra/identity/conditional-access/concept-continuous-access-evaluation#critical-event-evaluation

Practica: Q10, Q22

---

## Trampa 10. Authentication context, protected actions y PIM

Frase clave: **"El context es la etiqueta, la policy pone las reglas, y el que la pega es SharePoint, PIM o protected actions. Y la policy va en On, no en report-only."**

Regla:
- Authentication context: c1 a c99 con Publish to apps; SharePoint lo pega con sensitivity label o Set-SPOSite; PIM lo pide al activar (sin mezclarlo con el directory role en la misma política).
- Protected actions: CA sobre permisos (CA policies, named locations, cross-tenant settings, hard delete) sin importar el rol. Lo configura CA Admin o Security Admin; Azure PowerShell falla, Graph PowerShell no.

Palabras que delatan: "specific SharePoint site", "at the moment of activation", "regardless of the role", "when administrators modify Conditional Access policies", "step-up", "Publish to apps".

Link: https://learn.microsoft.com/entra/identity/role-based-access-control/protected-actions-overview#what-permissions-can-be-used-with-protected-actions

Practica: Q23, Q24, Q25, Q27

---

## Trampa 11. Riesgo: quién se cura con qué

Frase clave: **"User risk se cura con password (o risk remediation); sign-in risk se cura con MFA. Nunca al revés y nunca en la misma policy."**

Regla:
- Require risk remediation cubre usuarios con password y passwordless, y agrega auth strength y SIF Every time. Políticas basadas en riesgo piden P2; las legacy de ID Protection se retiran el 1 de octubre de 2026. Report suspicious activity pone High user risk.
- Registro: MFA registration policy (14 días) y campaign (un método a la vez, Authenticator en Any o Push, 3 snoozes). Workload identities: CA de riesgo pide Workload Identities Premium, solo single-tenant, sin MFA posible.

Palabras que delatan: "users at risk", "leaked credentials", "passwordless users", "self-remediate", "nudge users", "snooze", "service principal", "managed identity", "least privilege to dismiss risk".

Link: https://learn.microsoft.com/entra/id-protection/concept-identity-protection-policies#require-risk-remediation-control

Practica: Q6, Q29, Q30, Q31, Q32, Q33, Q34, Q35, Q36, Q37, Q38

---

## Trampa 12. Global Secure Access en un dibujo

Frase clave: **"Microsoft primero, luego Private, luego Internet. Private Access mata la VPN, compliant network mata el token robado, y tenant restrictions cierra la puerta a otros tenants."**

Regla:
- Cliente Windows: joined, hybrid o registered (registered solo Private Access); sin AVD multi-session; apagar QUIC y DNS over HTTPS. Private Access: connector, Quick Access, asignar sin nested groups, habilitar el profile; per-app access para CA distinto.
- Internet Access: filtering policy, security profile y CA con "All internet resources with Global Secure Access". Microsoft traffic profile (P1): compliant network check, universal tenant restrictions (TRv2) y source IP restoration.

Palabras que delatan: "replace the VPN", "different Conditional Access for one app", "block a web category for one group", "stolen tokens replayed", "without maintaining IP lists", "sign in to other tenants", "real public IP in sign-in logs".

Link: https://learn.microsoft.com/entra/global-secure-access/concept-traffic-forwarding#traffic-forwarding

Practica: Q39, Q40, Q41, Q42, Q43, Q44

---

## Objetivo de la sesión

El presenter no tiene que recitar números ni menús. Tiene que entender que casi todas las preguntas de M2 se resuelven con cuatro preguntas: **qué tan fuerte es el método** (MFA, passwordless o phishing-resistant, y dónde se configura cada uno), **qué decide la política** (si nadie dice que no, el token sale; el block, la exclusión de break-glass y el context se diseñan a propósito), **qué riesgo es y cómo se cura** (user risk con password o risk remediation, sign-in risk con MFA, workload identities con otra licencia) y **por dónde pasa el tráfico** (Microsoft, Private o Internet profile, y qué agrega cada uno). Si el presenter puede tomar cualquier pregunta del banco, señalar las dos o tres palabras que la delatan y explicar con sus palabras por qué cada distractor falla, la sesión cumplió. Los números (10 minutos de la TAP, 1000 términos, 99 contexts, 240 políticas, 14 días, 28 horas) se quedan en la guía para consulta.

---

## Orden sugerido de slides (10)

| # | Título | Para qué sirve |
|---|---|---|
| 1 | M2 en un vistazo | Mostrar los 4 subdominios, el peso de 25 a 30% y las cuatro preguntas: método, política, riesgo y tráfico. |
| 2 | La escalera de métodos | Tabla MFA, Passwordless y Phishing-resistant con TAP, passkeys, Authenticator y CBA en su escalón (trampas 1, 2 y 3). |
| 3 | Tokens y sesiones | OAuth contra OATH, sign-in frequency, persistent browser y por qué ya no existe el refresh token lifetime (trampa 4). |
| 4 | Passwords que todavía importan | SSPR con writeback en dos lados, admins en two-gate y password protection en Audit contra Enforced (trampa 5). |
| 5 | Kerberos sin PKI | Cloud Kerberos trust para WHfB y Entra Kerberos para Azure Files, con su limitación de MFA (trampa 6). |
| 6 | Construir CA sin lockout | Security defaults, combinar políticas, break-glass, templates y What If contra report-only (trampas 7 y 8). |
| 7 | Cortar el acceso ya | CAE, sus eventos críticos y el flujo de revocar sesiones en híbrido (trampa 9). |
| 8 | Etiquetas y permisos | Authentication context en SharePoint y PIM, y protected actions para cambios de CA (trampa 10). |
| 9 | Riesgo: quién se cura con qué | User risk contra sign-in risk, risk remediation, registration campaign y workload identities (trampa 11). |
| 10 | GSA en un dibujo | Los tres profiles en orden, Quick Access, web filtering, compliant network y tenant restrictions, como cierre antes del Kahoot (trampa 12). |
