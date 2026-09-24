# M2 Banco de preguntas: Implement authentication and access management (25 a 30%)

44 preguntas originales, escritas para SC-300 Tips and Tricks con base en Microsoft Learn (revisado en septiembre 2026). No vienen de dumps ni de preguntas filtradas. Las preguntas y opciones están en inglés (el idioma del examen) y las explicaciones en español.

Cómo usarlo:
- Contesta primero sin ver la respuesta. Luego lee el "por qué las otras no": ahí está el valor.
- En las series Yes/No, **cada afirmación se evalúa sola**. En el examen real no puedes regresar a ellas.
- En drag/order solo cuentan las acciones que sí van, en el orden correcto.
- En select two, necesitas las dos respuestas para sumar el punto.

| Subdominio | Preguntas |
|---|---|
| Plan, implement, and manage Microsoft Entra user authentication | Q1 a Q12 |
| Plan, implement, and manage Microsoft Entra Conditional Access | Q13 a Q28 (Q27 y Q28 son el case study 1) |
| Manage risk by using Microsoft Entra ID Protection | Q29 a Q38 |
| Implement Global Secure Access | Q39 a Q44 (Q43 y Q44 son el case study 2) |

| Formato | Cantidad | Preguntas |
|---|---|---|
| Multiple choice (una respuesta) | 24 | Q3, Q4, Q5, Q8, Q12, Q13, Q14, Q15, Q17, Q18, Q20, Q24, Q26, Q27, Q28, Q29, Q31, Q32, Q35, Q36, Q37, Q41, Q43, Q44 |
| Yes/No series | 9 | Q1, Q2, Q6, Q11, Q19, Q22, Q25, Q30, Q33 |
| Drag/order | 4 | Q9, Q10, Q23, Q40 |
| Select two | 7 | Q7, Q16, Q21, Q34, Q38, Q39, Q42 |
| Case study (dentro de los formatos anteriores) | 2 casos, 4 preguntas | Q27 y Q28, Q43 y Q44 |

---

## Subdominio 1: Plan, implement, and manage Microsoft Entra user authentication

### Q1 · Implement and manage authentication methods (Temporary Access Pass) · Yes/No series

Contoso enables the Temporary Access Pass (TAP) method in the Authentication methods policy and targets it to a group named NewHires. The TAP settings are: default lifetime 1 hour, maximum lifetime 8 hours, and one-time use set to Yes. Sam is assigned only the Authentication Administrator role.

For each of the following statements, select Yes or No.

1. Sam can create a TAP for Ana, a member of NewHires who holds the Helpdesk Administrator role.
2. Sam can create a TAP for Luis, a contractor who isn't a member of NewHires, but Luis can't use it to sign in.
3. A new hire who signs in with a TAP to register a FIDO2 security key must finish the registration within 10 minutes of that sign-in.

**Respuesta:** 1 = No, 2 = Yes, 3 = Yes

**Por qué es correcta:**
- 1 No. El Authentication Administrator crea TAP solo para usuarios sin rol de admin (members). Para alguien con rol de admin, como Helpdesk Administrator, hace falta **Privileged Authentication Administrator**. Y ninguno de los dos puede crearse una TAP a sí mismo.
- 2 Yes. Learn lo dice así: puedes crear una TAP para cualquier usuario, pero **solo los usuarios dentro del alcance de la política pueden iniciar sesión con ella**.
- 3 Yes. Con una TAP de un solo uso, registrar un método passwordless tiene que terminar **en 10 minutos**. Ese límite no aplica a una TAP de varios usos.

**Por qué las otras no:**
- Trampa de la 1: pensar que Authentication Administrator sirve para todos. La escalera es Authentication Admin (members) y Privileged Authentication Admin (members y admins).
- Trampa de la 2: confundir crear la TAP con poder usarla. El alcance de la política decide el uso.
- Trampa de la 3: creer que el lifetime (1 hora) es el límite. Con TAP one-time, el registro se cierra a los 10 minutos.

**Fuente:** https://learn.microsoft.com/entra/identity/authentication/howto-authentication-temporary-access-pass#create-a-temporary-access-pass y https://learn.microsoft.com/entra/identity/authentication/howto-authentication-temporary-access-pass#limitations

---

### Q2 · Implement and manage authentication methods (certificate-based authentication) · Yes/No series

Fabrikam enables Microsoft Entra certificate-based authentication (CBA) for a group named SmartCardUsers. A Privileged Authentication Administrator uploaded the issuing CA (CN=FabrikamIssuing) to the PKI-based trust store but left the Certificate Revocation List URL empty.

The authentication binding policy is configured as follows:
- Default protection level: Single-factor authentication
- Rule 1: Certificate issuer CN=FabrikamIssuing, protection level Single-factor authentication
- Rule 2: Policy OID 1.3.6.1.4.1.311.21.8.5, protection level Multifactor authentication

The username binding policy uses the default mapping of PrincipalName to userPrincipalName.

For each of the following statements, select Yes or No.

1. If a user's certificate is revoked on the issuing CA, the user can still sign in with that certificate.
2. A certificate issued by CN=FabrikamIssuing that contains policy OID 1.3.6.1.4.1.311.21.8.5 satisfies a Conditional Access policy that requires multifactor authentication.
3. If you set Required affinity binding to High at the tenant level, users can keep signing in with the current username binding.

**Respuesta:** 1 = Yes, 2 = Yes, 3 = No

**Por qué es correcta:**
- 1 Yes. Si la CA no tiene CRL configurado, **Microsoft Entra ID no revisa revocación** y la autenticación no se bloquea. Por eso el CRL por HTTP es prerrequisito.
- 2 Yes. En el ejemplo de Learn, cuando un certificado cumple una regla de issuer (single-factor) y una de policy OID (multifactor), **la regla de policy OID tiene precedencia** y el certificado cuenta como MFA.
- 3 No. PrincipalName es un binding de **low affinity**. Con High a nivel tenant, Entra quita los bindings low de la lista y solo evalúa SKI, SHA1PublicKey o IssuerAndSerialNumber contra certificateUserIds. Learn avisa que puedes dejar fuera a todo el tenant.

**Por qué las otras no:**
- Trampa de la 1: pensar que "revocado en la CA" bloquea solo. Sin CRL URL en Entra, no hay chequeo.
- Trampa de la 2: creer que gana la regla más general (issuer). Gana la de policy OID.
- Trampa de la 3: confundir affinity (qué tan único es el mapeo) con protection level (single-factor o MFA). Son dos perillas distintas.

**Fuente:** https://learn.microsoft.com/entra/identity/authentication/how-to-certificate-based-authentication#prerequisites, https://learn.microsoft.com/entra/identity/authentication/how-to-certificate-based-authentication#test-custom-authentication-binding-rules y https://learn.microsoft.com/entra/identity/authentication/concept-certificate-based-authentication-technical-deep-dive#username-binding-policy

---

### Q3 · Implement and manage authentication methods (passkeys FIDO2) · Multiple choice

Contoso is deploying passkeys (FIDO2). The requirements are:

- Members of the IT-Admins group must use only device-bound passkeys on two approved FIDO2 security key models, and Microsoft Entra ID must verify the make and model at registration.
- Members of the HR group must be able to register synced passkeys stored in iCloud Keychain or Google Password Manager.
- Administrative effort must be minimized.

What should you do?

A. Keep a single Passkey (FIDO2) configuration for all users with Enforce attestation set to Yes and key restrictions that allow only the AAGUIDs of the two approved models.
B. Opt in to passkey profiles. Create a profile for IT-Admins with passkey type Device-bound, Enforce attestation set to Yes, and key restrictions that allow the two AAGUIDs. Create a second profile for HR with passkey types Device-bound and Synced, and Enforce attestation set to No.
C. Enable the Microsoft Authenticator method for HR with Authentication mode set to Passwordless, and enable Passkey (FIDO2) only for IT-Admins.
D. Leave the Passkey (FIDO2) method with its default settings and create a Conditional Access policy that requires the built-in Phishing-resistant MFA authentication strength for IT-Admins.

**Respuesta:** B

**Por qué es correcta:** Los **passkey profiles** existen justo para esto: reglas distintas por grupo (tipo de passkey, attestation y AAGUIDs). Un perfil estricto para admins y otro flexible para HR. Recuerda: hasta **3 perfiles** incluyendo el Default, y después de hacer opt-in ya no puedes regresar.

**Por qué las otras no:**
- A. **Los synced passkeys no soportan attestation**. Con attestation obligatoria y una allow list de dos llaves, HR no puede registrar iCloud Keychain ni Google Password Manager.
- C. Authenticator en modo Passwordless es phone sign-in, no un synced passkey. No cumple el requisito de HR.
- D. Una authentication strength controla el sign-in, no el registro, y la built-in acepta cualquier llave FIDO2. No verifica marca y modelo al registrar.

**Fuente:** https://learn.microsoft.com/entra/identity/authentication/how-to-authentication-passkeys-fido2#passkey-profiles y https://learn.microsoft.com/entra/identity/authentication/how-to-authentication-passkeys-fido2#synced-passkeys-fido2

---

### Q4 · Implement and manage authentication methods (Microsoft Authenticator) · Multiple choice

Contoso wants a pilot group named Pilot-PK to sign in with passkeys stored in Microsoft Authenticator on their phones. All other users must keep using Authenticator push notifications for MFA and must not be able to register passkeys in Authenticator.

What should you configure?

A. In the Microsoft Authenticator method policy, target Pilot-PK and set Authentication mode to Passwordless.
B. In the Passkey (FIDO2) method policy, use passkey profiles: one profile for Pilot-PK that is Device-bound and allows the Microsoft Authenticator AAGUIDs, and one profile for all other users that blocks the Microsoft Authenticator AAGUIDs.
C. Create a registration campaign that targets Pilot-PK with Microsoft Authenticator as the authentication method.
D. Create a Conditional Access policy for Pilot-PK that requires the built-in Passwordless MFA authentication strength.

**Respuesta:** B

**Por qué es correcta:** Un passkey en Authenticator es una credencial **FIDO2 device-bound**. Por eso se controla en la política **Passkey (FIDO2)**, con key restrictions por AAGUID (Authenticator for iOS y for Android). Learn trae este mismo patrón para un rollout piloto: un perfil que bloquea los AAGUIDs de Authenticator para todos y otro que los permite para los grupos piloto. Si un usuario está en varios perfiles, basta con que el passkey cumpla uno.

**Por qué las otras no:**
- A. El modo Passwordless de la política de Authenticator es **passwordless phone sign-in** (notificación con número), no un passkey. Es la confusión clásica.
- C. La campaign solo empuja a registrar algo. No habilita passkeys en Authenticator ni impide que otros los registren.
- D. Una authentication strength no habilita ningún método. Y Passwordless MFA también acepta phone sign-in.

**Fuente:** https://learn.microsoft.com/entra/identity/authentication/how-to-enable-authenticator-passkey#configure-a-profile-for-passkeys-in-authenticator y https://learn.microsoft.com/entra/identity/authentication/how-to-authentication-passkeys-fido2#passkey-profiles

---

### Q5 · Implement and manage authentication methods (OAuth 2.0 tokens) · Multiple choice

For a finance web app, Contoso's security team requires that users re-enter their credentials at least every 8 hours. A colleague proposes creating a token lifetime policy with MaxAgeMultiFactor set to 08:00:00 and assigning it to the app.

What should you do?

A. Create and assign the token lifetime policy as proposed.
B. Create a token lifetime policy with AccessTokenLifetime set to 08:00:00 and assign it to the app.
C. Create a Conditional Access policy that targets the app and sets the Sign-in frequency session control to 8 hours.
D. Enable Remember multifactor authentication on trusted devices in the MFA service settings.

**Respuesta:** C

**Por qué es correcta:** Desde el **30 de enero de 2021** los lifetimes de refresh token y session token ya no se configuran con token lifetime policies. Learn dice que para controlar cada cuánto se vuelve a iniciar sesión se usa **Conditional Access sign-in frequency**.

**Por qué las otras no:**
- A. MaxAgeMultiFactor es una propiedad retirada. Si existe en una política, **se ignora**.
- B. AccessTokenLifetime (de 10 minutos a 1 día) cambia access, ID y SAML tokens. Cuando el access token vence, el cliente usa el refresh token en silencio y el usuario no vuelve a escribir nada.
- D. Remember MFA es una configuración legacy en días, reduce prompts en vez de forzarlos y Learn pide apagarla antes de usar sign-in frequency.

Dato extra para el examen: access token por default de 60 a 90 minutos, refresh token de 90 días (24 horas para SPA). Y ojo: el outline dice OAuth, pero el método de MFA se llama **OATH tokens (TOTP)**.

**Fuente:** https://learn.microsoft.com/entra/identity-platform/configurable-token-lifetimes#token-lifetime-policies-for-refresh-tokens-and-session-tokens-retired y https://learn.microsoft.com/entra/identity/conditional-access/concept-session-lifetime#user-sign-in-frequency

---

### Q6 · Implement and manage tenant-wide multifactor authentication (MFA) settings · Yes/No series

Contoso has Microsoft Entra ID P1 licenses only. An Authentication Policy Administrator sets Report suspicious activity to Enabled for all users in Authentication methods > Settings. The legacy MFA service settings contain a trusted IP range for the head office public IP address.

For each of the following statements, select Yes or No.

1. When a user reports an unexpected MFA prompt as suspicious, the user is set to high user risk.
2. Contoso can use a user risk-based Conditional Access policy to block the reporting users automatically.
3. Contoso can add the internal range 10.10.0.0/16 to trusted IPs so that users on the LAN skip MFA prompts.

**Respuesta:** 1 = Yes, 2 = No, 3 = No

**Por qué es correcta:**
- 1 Yes. Report suspicious activity está integrado con ID Protection y **pone al usuario en High User Risk** (no pasa si el usuario hizo passwordless).
- 2 No. Las políticas basadas en riesgo **piden Entra ID P2**. Con P1 usas las risk detections para actuar a mano o automatizas con Microsoft Graph.
- 3 No. En MFA de nube, trusted IPs **solo acepta rangos públicos**. Rangos privados solo con MFA Server. Learn recomienda named locations de CA en lugar de trusted IPs.

**Por qué las otras no:**
- Trampa de la 1: buscar "Fraud alert". Ya no existe: Report suspicious activity lo reemplazó el 1 de marzo de 2025.
- Trampa de la 2: asumir que ver el riesgo es lo mismo que automatizar con él. Automatizar es P2.
- Trampa de la 3: pensar en la IP que ve el usuario en su tarjeta de red. Entra ve la IP pública de salida.

**Fuente:** https://learn.microsoft.com/entra/identity/authentication/howto-mfa-mfasettings#report-suspicious-activity y https://learn.microsoft.com/entra/identity/authentication/howto-mfa-mfasettings#trusted-ips

---

### Q7 · Configure and deploy self-service password reset (SSPR) · Select two

Contoso synchronizes users from AD DS by using Microsoft Entra Connect Sync with password hash synchronization. Contoso has Microsoft Entra ID P1. SSPR is enabled for all users, and users have registered their methods. Cloud-only users can reset their passwords, but synchronized users see a message telling them to contact their administrator.

You need to ensure that synchronized users can reset their passwords by using SSPR.

Which two actions should you perform? Each correct answer presents part of the solution.

A. Run the Microsoft Entra Connect wizard, select Customize synchronization options, and select Password writeback on the Optional features page.
B. In the Microsoft Entra admin center, go to Password reset > On-premises integration and select Write back passwords to your on-premises directory.
C. Enable staged rollout for the synchronized users.
D. Enable seamless single sign-on in Microsoft Entra Connect.
E. Change Number of methods required to reset to 2.

**Respuesta:** A y B

**Por qué es correcta:** Si el password se administra on-prem (PHS, PTA o federación) y **no hay writeback**, SSPR le dice al usuario que contacte a su admin. El writeback se prende **en los dos lados**: en el wizard de Connect (Optional features) y en Password reset > On-premises integration (rol mínimo Hybrid Identity Administrator). Además, la cuenta de Connect necesita permisos en AD: Reset password, Change password, escribir lockoutTime y pwdLastSet, y Unexpire Password.

**Por qué las otras no:**
- C. Learn dice que SSPR con writeback **no está garantizado** cuando staged rollout está activo para un grupo. Empeora el escenario.
- D. Seamless SSO es para iniciar sesión sin escribir password en la red corporativa. No tiene nada que ver con reset.
- E. El número de métodos no es la causa del mensaje.

**Fuente:** https://learn.microsoft.com/entra/identity/authentication/concept-sspr-howitworks#how-does-the-password-reset-process-work, https://learn.microsoft.com/entra/identity/authentication/tutorial-enable-sspr-writeback#enable-password-writeback-in-microsoft-entra-connect y https://learn.microsoft.com/entra/identity/authentication/tutorial-enable-sspr-writeback#enable-password-writeback-for-sspr

---

### Q8 · Configure and deploy self-service password reset (SSPR) · Multiple choice

Contoso enables SSPR for a group named SSPR-Users by selecting Selected in the Password reset properties. Number of methods required to reset is set to 1, and the available methods are Mobile phone, Email, and Security questions.

Megan is a member of SSPR-Users and holds the Helpdesk Administrator role. She registered only security questions. She can't reset her password by using SSPR, while standard users who registered only security questions can.

What is the cause?

A. SSPR is disabled for administrator accounts by default.
B. Administrator accounts use a two-gate policy that requires two methods and doesn't allow security questions, and the policy can't be changed.
C. Megan must be added to SSPR-Users directly because nested groups aren't supported.
D. The tenant must migrate to the Authentication methods policy before security questions can be used.

**Respuesta:** B

**Por qué es correcta:** Las cuentas con rol de administrador (Helpdesk Administrator está en la lista) tienen SSPR habilitado por default con una **política two-gate**: dos métodos, **sin security questions**, y no se puede cambiar. Por eso Learn recomienda **probar SSPR con un usuario sin rol de admin**.

**Por qué las otras no:**
- A. Al revés: SSPR para admins está habilitado por default. Se puede apagar con AllowedToUseSspr en false.
- C. SSPR sí soporta nested groups, y Megan ya es miembro directo. Ojo con el dato real: en el portal solo puedes elegir **un grupo** en Selected.
- D. Al revés: security questions hoy **solo se habilitan en la política legacy** de SSPR.

**Fuente:** https://learn.microsoft.com/entra/identity/authentication/concept-sspr-policy#administrator-reset-policy-differences y https://learn.microsoft.com/entra/identity/authentication/tutorial-enable-sspr#enable-self-service-password-reset

---

### Q9 · Implement and manage Windows Hello for Business · Drag/order

Contoso has Microsoft Entra hybrid joined Windows 11 devices and uses password hash synchronization. Contoso doesn't have an enterprise PKI. Users must sign in with Windows Hello for Business and get single sign-on to on-premises file shares. The solution must not require deploying certificates.

Which three actions should you perform in sequence? (Two actions aren't used.)

A. Deploy AD FS as a certificate registration authority and issue authentication certificates to users.
B. On the Microsoft Entra Connect server, install the AzureADHybridAuthenticationManagement module and run Set-AzureADKerberosServer to create the Microsoft Entra Kerberos server object in each domain.
C. Deploy a Group Policy or Intune policy that enables Use Windows Hello for Business and Use cloud trust for on-premises authentication.
D. Have each user sign in to the device while it has line of sight to a domain controller and complete Windows Hello for Business provisioning.
E. Enable the Use certificate for on-premises authentication policy setting.

**Respuesta:** B, C, D (en ese orden)

**Por qué es correcta:** **Cloud Kerberos trust** es el modelo recomendado y **el único híbrido que no pide PKI**. Los pasos de Learn son: desplegar Microsoft Entra Kerberos (crea el objeto AzureADKerberos, que se ve como un RODC), configurar las dos políticas y enrolar. En hybrid joined, el primer sign-in con la credencial nueva necesita **línea de vista a un DC**.

**Por qué las otras no:**
- A. Eso es certificate trust: pide PKI y AD FS como registration authority, y no soporta PHS ni PTA. Rompe el requisito.
- E. Si "Use certificate for on-premises authentication" está activo, **certificate trust le gana** a cloud Kerberos trust. Debe quedar sin configurar.
- Orden: sin el objeto Kerberos, el chequeo de prerrequisitos de provisioning en hybrid joined falla (no hay partial TGT).

**Fuente:** https://learn.microsoft.com/windows/security/identity-protection/hello-for-business/deploy/hybrid-cloud-kerberos-trust#deploy-microsoft-entra-kerberos, https://learn.microsoft.com/windows/security/identity-protection/hello-for-business/deploy/hybrid-cloud-kerberos-trust#configure-windows-hello-for-business-policy-settings y https://learn.microsoft.com/windows/security/identity-protection/hello-for-business/deploy/#pki-requirements

---

### Q10 · Disable accounts and revoke user sessions · Drag/order

A Contoso employee is terminated effective immediately and might try to access company data. The account is synchronized from on-premises AD DS by Microsoft Entra Connect Sync, and the user has a Microsoft Entra joined laptop. You must follow Microsoft guidance for hybrid environments.

Which four actions should you perform in sequence? (Two actions aren't used.)

A. Disable the account in AD DS by running Disable-ADAccount.
B. Reset the user's password twice in AD DS by running Set-ADAccountPassword.
C. Revoke the user's refresh tokens by running Revoke-MgUserSignInSession.
D. Disable the user's registered devices by running Update-MgDevice with -AccountEnabled:$false.
E. Delete the user from Microsoft Entra ID.
F. Require the user to re-register for multifactor authentication.

**Respuesta:** A, B, C, D (en ese orden)

**Por qué es correcta:** Es el flujo de Learn para híbrido: primero on-prem (deshabilitar y **resetear el password dos veces** para mitigar pass-the-hash), después Entra (revocar refresh tokens) y al final deshabilitar los devices del usuario. Como la cuenta es sincronizada, el estado disabled llega a Entra con la sync; por eso también revocas sesiones.

**Por qué las otras no:**
- E. Borrar al usuario no es un paso del procedimiento. Además, en un usuario sincronizado el origen de verdad es AD.
- F. Pedir re-registro de MFA no corta los tokens ya emitidos.
- Dato clave: después de revocar, las apps con **access token** siguen funcionando hasta que el token expira (alrededor de 1 hora). Solo las **apps con CAE** cortan casi en tiempo real.

**Fuente:** https://learn.microsoft.com/entra/identity/users/users-revoke-access#revoke-access-for-a-user-in-the-hybrid-environment y https://learn.microsoft.com/entra/identity/users/users-revoke-access#when-access-is-revoked

---

### Q11 · Implement and manage Microsoft Entra password protection · Yes/No series

Contoso has one AD DS domain with 10 domain controllers and Microsoft Entra ID P1 licenses. You install the Microsoft Entra Password Protection proxy service on two member servers and register the proxy and the forest. You install the DC agent on 4 of the 10 domain controllers and restart them.

In the Microsoft Entra admin center, Enable password protection on Windows Server Active Directory is set to Yes and Mode is set to Audit. The custom banned password list contains Contoso and Seattle.

For each of the following statements, select Yes or No.

1. A user who changes the password to C0ntos0Seattle! on a domain controller that runs the DC agent receives an error, and the password isn't changed.
2. Password changes processed by the six domain controllers without the DC agent aren't validated against the banned password lists.
3. The domain controllers that run the DC agent need outbound internet access to download the password policy.

**Respuesta:** 1 = No, 2 = Yes, 3 = No

**Por qué es correcta:**
- 1 No. En **modo Audit** los passwords malos solo generan eventos en el log, pero **se aceptan**. Solo Enforced rechaza.
- 2 Yes. La política se aplica **solo donde está instalado el DC agent**. Learn dice que el deployment parcial no es seguro y solo sirve para pruebas.
- 3 No. Principio de diseño: **los DCs nunca hablan directo con internet**. El DC agent pide la política al proxy, y el proxy la pide a Entra.

**Por qué las otras no:**
- Trampa de la 1: olvidar el modo. En la vida real primero se corre en Audit y luego se pasa a Enforced.
- Trampa de la 2: creer que con un DC agent ya queda protegido todo el dominio. El cliente elige cualquier DC.
- Trampa de la 3: pensar que el DC necesita salida a internet. Solo el proxy la necesita.

Datos rápidos: custom list de hasta **1000 términos** de 4 a 16 caracteres; el DC agent revisa la política cada hora; si no hay política local, el password se acepta y se registra un evento.

**Fuente:** https://learn.microsoft.com/entra/identity/authentication/howto-password-ban-bad-on-premises-operations#modes-of-operation, https://learn.microsoft.com/entra/identity/authentication/concept-password-ban-bad-on-premises#design-principles y https://learn.microsoft.com/entra/identity/authentication/concept-password-ban-bad-on-premises#incremental-deployment

---

### Q12 · Enable Microsoft Entra Kerberos authentication for hybrid identities · Multiple choice

Contoso uses Azure Virtual Desktop with Microsoft Entra joined session hosts and stores FSLogix profile containers in Azure Files. Users are hybrid identities synchronized by Microsoft Entra Connect Sync. You enabled Microsoft Entra Kerberos on the storage account, granted admin consent to the storage account application, and configured the session hosts with CloudKerberosTicketRetrievalEnabled.

Everything worked until a new Conditional Access policy that requires MFA for All resources was turned on. Now profile containers fail to mount, while other apps work.

What should you do?

A. Exclude the storage account application from the Conditional Access policy that requires MFA.
B. Enable on-premises AD DS authentication on the same storage account as a second identity source.
C. Add the kdc_enable_cloud_group_sids tag to the storage account application manifest.
D. Configure a host name to Kerberos realm mapping on the session hosts.

**Respuesta:** A

**Por qué es correcta:** Learn lo marca como limitación: **Microsoft Entra Kerberos para Azure Files no soporta MFA**. Las políticas de CA que exigen MFA tienen que **excluir la app del storage account**, o la autenticación falla.

**Por qué las otras no:**
- B. Un storage account acepta **un solo identity source** a la vez (Entra Kerberos, AD DS o Entra Domain Services).
- C. Ese tag es para identidades cloud-only y el límite de 1010 group SIDs. Aquí los usuarios son híbridos y el problema empezó con la política de MFA.
- D. El realm mapping es para convivir con storage accounts que usan AD DS. No arregla un bloqueo de CA.

**Fuente:** https://learn.microsoft.com/entra/identity/authentication/kerberos#mfa-incompatibility-for-azure-files-authentication y https://learn.microsoft.com/azure/storage/files/storage-files-identity-auth-hybrid-identities-enable#prerequisites

---

## Subdominio 2: Plan, implement, and manage Microsoft Entra Conditional Access

### Q13 · Plan Conditional Access policies · Multiple choice

Contoso's Microsoft Entra tenant was created in 2023 and has security defaults enabled. The company buys Microsoft Entra ID P1 licenses for all users. The new requirements are:

- Users must perform MFA only when they access the Payroll app from outside the office.
- A service account used by a multifunction printer must be excluded from MFA.

You need to implement the requirements by using Conditional Access. What should you do first?

A. Create the Conditional Access policies and turn them on. Security defaults are disabled automatically.
B. Disable security defaults.
C. Enable per-user MFA for all users.
D. Add the office public IP range to trusted IPs in the MFA service settings.

**Respuesta:** B

**Por qué es correcta:** Security defaults y CA **no se combinan**. Learn dice que las organizaciones que implementan CA para reemplazar security defaults **deben deshabilitarlos**. El rol mínimo para tocar security defaults es **Conditional Access Administrator**. Al deshabilitarlos, Microsoft ofrece Microsoft-managed policies para no perder la protección base.

**Por qué las otras no:**
- A. No hay apagado automático. Es un paso explícito en Properties > Manage security defaults.
- C. Per-user MFA es legacy y no permite condiciones por app ni por ubicación.
- D. Trusted IPs es de la configuración legacy de MFA, no de CA, y no resuelve la exclusión de la cuenta de servicio.

**Fuente:** https://learn.microsoft.com/entra/fundamentals/security-defaults#disabling-security-defaults y https://learn.microsoft.com/entra/fundamentals/security-defaults#move-from-security-defaults-to-conditional-access

---

### Q14 · Plan Conditional Access policies · Multiple choice

Contoso has a Conditional Access policy named CA01 that is turned on:

- Users: include the Finance group
- Target resources: Payroll
- Grant: Require multifactor authentication

Users outside Finance can open Payroll without any prompt. Only Finance users must be able to access Payroll. You must use only Conditional Access, and emergency access accounts must not be blocked.

What should you do?

A. Change CA01 to include All users.
B. Create CA02: include All users, exclude Finance and the emergency access accounts, target Payroll, and select Block access. Turn CA02 on.
C. In CA01, change the grant setting to Require one of the selected controls.
D. Create CA02 in Report-only: include All users, target Payroll, and select Block access.

**Respuesta:** B

**Por qué es correcta:** Regla de oro de Learn: **si ninguna política dispara un control, el access token se emite por default**. CA01 solo pone MFA a Finance; no bloquea a nadie más. Para "solo Finance entra" hace falta una **segunda política de block** que incluya a todos y excluya a Finance (y a break-glass).

**Por qué las otras no:**
- A. Todos entrarían con MFA. No es "solo Finance".
- C. AND u OR entre controles no cambia a quién aplica la política.
- D. Report-only no aplica controles. Además, al incluir All users sin excluir a Finance, si la pasas a On bloqueas a Finance.

**Fuente:** https://learn.microsoft.com/entra/identity/conditional-access/plan-conditional-access#combining-policies

---

### Q15 · Implement Conditional Access policy assignments · Multiple choice

Contoso collaborates with two partners, Fabrikam and Tailspin, by using B2B collaboration. Guests from Fabrikam must perform MFA when they access Contoso's SharePoint Online. Guests from Tailspin must not be affected by this policy.

What should you configure in the Users assignment of the policy?

A. Include > Select users and groups > Guest or external users > B2B collaboration guest users, and then specify Fabrikam's Microsoft Entra tenant.
B. Include > Directory roles > Guest Inviter.
C. Include a dynamic group with the membership rule (user.userType -eq "Guest").
D. Include All users, and exclude Guest or external users with all external user types selected.

**Respuesta:** A

**Por qué es correcta:** En Guest or external users puedes elegir **el tipo de usuario externo** (B2B collaboration guest, B2B collaboration member, B2B direct connect, local guest, service provider, other) y **uno o varios tenants** específicos. Así la política pega solo a Fabrikam.

**Por qué las otras no:**
- B. Guest Inviter es un rol para invitar, no representa a los guests.
- C. El grupo dinámico incluye a los guests de Tailspin también.
- D. Deja fuera a todos los guests, incluido Fabrikam.

Trampa extra de assignments: en Directory roles, CA **solo soporta roles built-in**. No aplica a roles con scope de administrative unit ni a custom roles.

**Fuente:** https://learn.microsoft.com/entra/identity/conditional-access/concept-conditional-access-users-groups#include-users

---

### Q16 · Implement Conditional Access policy controls · Select two

Contoso has a Conditional Access policy that targets administrator roles with the grant control Require authentication strength set to the built-in Phishing-resistant MFA strength. Administrators currently sign in with the following methods:

- FIDO2 security key
- Certificate-based authentication with certificates mapped to multifactor in the authentication binding policy
- Microsoft Authenticator phone sign-in
- Temporary Access Pass
- Password plus Microsoft Authenticator push notification

Which two methods satisfy the policy? Each correct answer presents a complete solution.

A. FIDO2 security key
B. Certificate-based authentication (multifactor)
C. Microsoft Authenticator phone sign-in
D. Temporary Access Pass
E. Password plus Microsoft Authenticator push notification

**Respuesta:** A y B

**Por qué es correcta:** La strength built-in **Phishing-resistant MFA** acepta FIDO2 security key, Windows Hello for Business o platform credential, y **CBA multifactor**. Son métodos que necesitan interacción entre el método y la superficie de sign-in.

**Por qué las otras no:**
- C. Authenticator phone sign-in cumple **Passwordless MFA**, pero no phishing-resistant.
- D. TAP (one-time o multi-use) solo cumple la **strength MFA**.
- E. Password más algo que tienes solo cumple la **strength MFA**.

Reglas extra: las 3 strengths built-in no se editan; no puedes usar **Require multifactor authentication** y **Require authentication strength** en la misma política; y la strength no limita la autenticación inicial (el usuario puede escribir su password y luego se le pide el método fuerte).

**Fuente:** https://learn.microsoft.com/entra/identity/authentication/concept-authentication-strengths#built-in-authentication-strengths y https://learn.microsoft.com/entra/identity/authentication/concept-authentication-strengths#limitations

---

### Q17 · Implement device-enforced restrictions · Multiple choice

Contoso requirements for SharePoint Online and Exchange Online:

- Users on unmanaged devices can use only the browser, with a limited experience (for example, no download or sync).
- Users on compliant or Microsoft Entra hybrid joined devices get full access.
- Administrative effort must be minimized, and no additional products can be deployed.

What should you configure in Conditional Access?

A. A grant control that requires the device to be marked as compliant for SharePoint Online and Exchange Online.
B. The session control Use app enforced restrictions for SharePoint Online and Exchange Online, with limited access configured in those services.
C. The session control Use Conditional Access App Control with a Microsoft Defender for Cloud Apps session policy that blocks downloads.
D. A filter for devices condition that excludes devices with trustType equal to AzureAD, with the grant control Block access.

**Respuesta:** B

**Por qué es correcta:** Con **app enforced restrictions**, Entra le pasa a la app la información del device (compliant o domain-joined) y la app decide: **experiencia limitada** en device no administrado y completa en device administrado. Funciona con SharePoint y Exchange. Hasta existe un template: "Use application enforced restrictions for unmanaged devices".

**Por qué las otras no:**
- A. Require compliant **bloquea el device no administrado**. No da acceso limitado.
- C. Funciona, pero necesita Defender for Cloud Apps. El requisito prohíbe productos extra.
- D. Bloquea en lugar de limitar.

**Fuente:** https://learn.microsoft.com/entra/identity/conditional-access/concept-conditional-access-session#application-enforced-restrictions y https://learn.microsoft.com/entra/identity/conditional-access/concept-conditional-access-policy-common#template-categories

---

### Q18 · Implement device-enforced restrictions · Multiple choice

Administrators must access the Windows Azure Service Management API only from privileged access workstations (PAWs). PAWs are Intune managed, compliant, and have device.extensionAttribute1 set to "PAW". Access from any other device, including devices that aren't registered in Microsoft Entra ID, must be blocked.

Which Conditional Access policy should you create for the administrator roles?

A. Target resource: Windows Azure Service Management API. Filter for devices: include filtered devices, rule device.extensionAttribute1 -eq "PAW". Grant: Block access.
B. Target resource: Windows Azure Service Management API. Filter for devices: exclude filtered devices, rule device.extensionAttribute1 -eq "PAW". Grant: Block access.
C. Target resource: Windows Azure Service Management API. Filter for devices: include filtered devices, rule device.extensionAttribute1 -eq "PAW". Grant: Require multifactor authentication.
D. Target resource: Microsoft Admin Portals. Device platforms: include Windows. Grant: Require Microsoft Entra hybrid joined device.

**Respuesta:** B

**Por qué es correcta:** Es el escenario de Learn: **excluir los devices que cumplen el filtro y bloquear todo lo demás**. En un device no registrado todas las propiedades son null, así que la regla con operador positivo (Equals) no lo excluye y **queda bloqueado**. Los PAW sí se excluyen porque son Intune managed y compliant (requisito para leer extensionAttributes).

**Por qué las otras no:**
- A. Bloquearía justo a los PAW.
- C. Con operador positivo el filtro **no aplica** a devices no registrados, y pedir MFA no restringe a PAW.
- D. Microsoft Admin Portals no es Azure Resource Manager, y hybrid joined no significa PAW.

**Fuente:** https://learn.microsoft.com/entra/identity/conditional-access/concept-condition-filters-for-devices#common-scenarios y https://learn.microsoft.com/entra/identity/conditional-access/concept-condition-filters-for-devices#policy-behavior-with-filter-for-devices

---

### Q19 · Test and troubleshoot Conditional Access policies · Yes/No series

A user reports that she's prompted for MFA in Microsoft Teams, and you don't know which policy causes it. You open the Conditional Access What If tool.

For each of the following statements, select Yes or No.

1. What If evaluates policies whose state is Off, so you can see what would happen if you turned them on.
2. If you simulate access to Microsoft Teams, the result also lists the policies that apply to Exchange Online and SharePoint Online because Teams depends on them.
3. For each policy that doesn't apply, What If shows the first condition that wasn't satisfied.

**Respuesta:** 1 = No, 2 = No, 3 = Yes

**Por qué es correcta:**
- 1 No. What If **solo incluye políticas On o en report-only**.
- 2 No. Learn lo dice directo: What If **no prueba service dependencies**. Si simulas Teams, no ves la política de Exchange Online.
- 3 Yes. La lista de políticas que no aplican trae la razón: **la primera condición que no se cumplió**.

**Por qué las otras no:**
- Trampa de la 1: usar What If para "probar" una política apagada. Primero pásala a report-only.
- Trampa de la 2: pensar que What If entiende las dependencias de Teams. No las entiende; para eso target al grupo Office 365.
- Dato extra: en el What If nuevo (basado en API), grupos de apps como Office 365 no hacen match; se da el App ID.

**Fuente:** https://learn.microsoft.com/entra/identity/conditional-access/what-if-tool#how-it-works y https://learn.microsoft.com/entra/identity/conditional-access/what-if-tool#evaluation

---

### Q20 · Test and troubleshoot Conditional Access policies · Multiple choice

You plan a Conditional Access policy that requires MFA for the user action Register or join devices. Before you enforce it, you need to verify whether the policy would apply to a specific test user who is also covered by several other policies. No user must be prompted during the verification.

What should you use?

A. Set the policy to Report-only and review the Report-only tab in the sign-in logs.
B. The What If tool, with the Register or join devices user action selected.
C. The Conditional Access insights and reporting workbook.
D. The Policy impact view for the new policy.

**Respuesta:** B

**Por qué es correcta:** **Report-only no soporta políticas con User Actions** (Register security information o Register or join devices). What If sí te deja elegir una user action como target y simular para un usuario sin molestar a nadie.

**Por qué las otras no:**
- A. Report-only no está disponible para user actions.
- C. El workbook muestra resultados de políticas en report-only o activas. No tienes esos datos para esta política.
- D. Policy impact también se alimenta de sign-ins reales de políticas activas o en report-only.

Detalle de configuración: si usas la user action Register or join devices, pon en No el device setting "Require Multifactor Authentication to register or join devices", o la política no se aplica bien.

**Fuente:** https://learn.microsoft.com/entra/identity/conditional-access/concept-conditional-access-report-only#overview, https://learn.microsoft.com/entra/identity/conditional-access/what-if-tool#how-it-works y https://learn.microsoft.com/entra/identity/conditional-access/concept-conditional-access-cloud-apps#user-actions

---

### Q21 · Implement session management · Select two

On devices that aren't compliant, users must not stay signed in after they close the browser. Users on compliant devices must not be affected. You create a Conditional Access policy that uses a filter for devices to exclude compliant devices.

Which two settings must the policy include? Each correct answer presents part of the solution.

A. Target resources: All resources.
B. Session: Persistent browser session set to Never persistent.
C. Target resources: Office 365 only.
D. Session: Sign-in frequency set to Every time.
E. In Company branding, set Show option to remain signed in to No.

**Respuesta:** A y B

**Por qué es correcta:** **Persistent browser session** es el control que decide si la sesión sobrevive al cerrar el navegador. Learn dice que **exige "All cloud apps"** (hoy All resources), porque todas las pestañas comparten el mismo session token.

**Por qué las otras no:**
- C. Con Office 365 solamente, el control no funciona como se espera.
- D. Every time pide reautenticación cuando la sesión se evalúa, no controla la persistencia. Learn pide usarlo poco para no causar fatiga de MFA.
- E. Branding es para todo el tenant, no distingue devices. Y si existen los dos, la política de CA le gana al "Stay signed in?".

**Fuente:** https://learn.microsoft.com/entra/identity/conditional-access/howto-conditional-access-session-lifetime#policy-2-persistent-browser-session y https://learn.microsoft.com/entra/identity/conditional-access/concept-session-lifetime#persistence-of-browsing-sessions

---

### Q22 · Implement continuous access evaluation · Yes/No series

Contoso has a Conditional Access policy that allows Exchange Online and SharePoint Online only from a named location named HQ-IPs. HQ-IPs contains all IPv4 and IPv6 egress ranges seen by Microsoft Entra ID and by the resources. Continuous access evaluation (CAE) isn't disabled. Users run the latest Outlook desktop client.

For each of the following statements, select Yes or No.

1. If an administrator disables a user account, the user loses access to Exchange Online in Outlook in near real time instead of waiting for the access token to expire.
2. If you replace HQ-IPs with a country or region location for the United States, CAE still enforces the location instantly when a user travels to another country.
3. If you add a user to a group that's excluded from a Conditional Access policy, Exchange Online applies the change immediately.

**Respuesta:** 1 = Yes, 2 = No, 3 = No

**Por qué es correcta:**
- 1 Yes. Deshabilitar o borrar la cuenta es un **evento crítico** de CAE. Exchange, SharePoint y Teams lo reciben casi en tiempo real (puede haber hasta 15 minutos de latencia).
- 2 No. CAE **solo entiende IP named locations**. Con country o region, o con MFA trusted IPs, Entra emite un token de una hora sin chequeo instantáneo de IP.
- 3 No. Cambios de **grupo o de política pueden tardar hasta un día** en los resource providers. Para aplicarlos ya, revoca las sesiones del usuario.

**Por qué las otras no:**
- Trampa de la 1: pensar que el access token siempre vive su hora completa. Con CAE no.
- Trampa de la 2: asumir que cualquier location sirve. Para enforcement instantáneo: IP ranges, IPv4 e IPv6.
- Trampa de la 3: meter "cambio de grupo" en la lista de eventos críticos. La lista es: cuenta deshabilitada o borrada, password cambiado o reseteado, MFA habilitado, revoke de refresh tokens y high user risk.

**Fuente:** https://learn.microsoft.com/entra/identity/conditional-access/concept-continuous-access-evaluation#critical-event-evaluation, https://learn.microsoft.com/entra/identity/conditional-access/concept-continuous-access-evaluation#supported-location-policies y https://learn.microsoft.com/entra/identity/conditional-access/concept-continuous-access-evaluation#group-membership-and-policy-update-effective-time

---

### Q23 · Configure authentication context · Drag/order

The SharePoint Online site named Legal-Confidential must require a compliant device and phishing-resistant MFA. Other SharePoint sites must not be affected. Contoso already has the Microsoft Purview licensing required, and sensitivity labels for groups and sites are enabled.

Which four actions should you perform in sequence? (Two actions aren't used.)

A. In Conditional Access > Authentication context, create an authentication context named Sensitive sites and select Publish to apps.
B. Create a Conditional Access policy whose target resource is the Sensitive sites authentication context, with grant controls Require device to be marked as compliant and Require authentication strength (Phishing-resistant MFA). Turn the policy on.
C. In Microsoft Purview, edit a sensitivity label for groups and sites, select Use Microsoft Entra Conditional Access to protect labeled SharePoint sites, and choose the Sensitive sites authentication context.
D. Apply the sensitivity label to the Legal-Confidential site.
E. Create a Conditional Access policy that targets https://contoso.sharepoint.com/sites/Legal-Confidential as a cloud app.
F. Create a named location for the Legal department office.

**Respuesta:** A, B, C, D (en ese orden)

**Por qué es correcta:** Es el orden de la guía de SharePoint: **crear el authentication context (con Publish to apps), crear la política que lo usa como target, ligar el context a la etiqueta y aplicar la etiqueta al sitio**. La alternativa sin etiqueta es Set-SPOSite con -ConditionalAccessPolicy AuthenticationContext (pide Microsoft 365 E5 o SharePoint Advanced Management).

**Por qué las otras no:**
- E. CA no puede apuntar a la URL de un sitio. Para granularidad dentro de una app existe el authentication context.
- F. La ubicación no es parte del requisito.
- Orden: si no marcas **Publish to apps**, el context no aparece para Purview ni para las apps. Hasta 99 contexts (c1 a c99). Las apps que no soportan authentication context reciben acceso denegado.

**Fuente:** https://learn.microsoft.com/sharepoint/authentication-context-example#set-up-an-authentication-context y https://learn.microsoft.com/entra/identity/conditional-access/concept-conditional-access-cloud-apps#configure-authentication-contexts

---

### Q24 · Configure authentication context · Multiple choice

Users who are eligible in Privileged Identity Management (PIM) for the Exchange Administrator role must use phishing-resistant MFA from a compliant device at the moment they activate the role. The requirement must apply at activation, not at every sign-in.

What should you do?

A. In the PIM role settings for Exchange Administrator, enable On activation, require multifactor authentication.
B. Create an authentication context and a Conditional Access policy that targets it, scoped to all users or the eligible users, with grant controls for a compliant device and the Phishing-resistant MFA strength. Then, in the PIM role settings, select On activation, require Microsoft Entra Conditional Access authentication context and choose that context.
C. Create a Conditional Access policy that includes the Exchange Administrator directory role and targets the authentication context used by PIM.
D. Add a protected action to the permission that assigns directory roles.

**Respuesta:** B

**Por qué es correcta:** PIM puede pedir un **authentication context** al activar. La política de CA que usa ese context define los requisitos (strength phishing-resistant y compliant device). Learn recomienda **crear y encender la política antes** de configurar el context en PIM.

**Por qué las otras no:**
- A. Solo pide MFA, y puede no pedir nada si el usuario ya hizo MFA en la sesión. No cubre phishing-resistant ni device.
- C. Learn dice que **no combines** el authentication context con el directory role en la misma política: durante la activación el usuario **todavía no tiene el rol**, así que la política no aplica.
- D. Protected actions protege permisos como administrar CA, named locations o cross-tenant settings. No es el mecanismo para activar roles en PIM.

**Fuente:** https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings#on-activation-require-microsoft-entra-conditional-access-authentication-context

---

### Q25 · Implement protected actions · Yes/No series

Contoso creates and publishes an authentication context named c5 Protected CA changes. It creates a Conditional Access policy that targets c5, requires the built-in Phishing-resistant MFA strength, excludes the emergency access accounts, and leaves the policy in Report-only while testing. A Security Administrator then adds protected actions for microsoft.directory/conditionalAccessPolicies/basic/update and microsoft.directory/conditionalAccessPolicies/delete by using c5.

For each of the following statements, select Yes or No.

1. The Security Administrator role has enough permissions to add the protected actions.
2. While the c5 policy is in Report-only, an administrator who completes phishing-resistant MFA can edit Conditional Access policies without issues.
3. An administrator who uses Azure PowerShell can delete a Conditional Access policy after satisfying the step-up prompt.

**Respuesta:** 1 = Yes, 2 = No, 3 = No

**Por qué es correcta:**
- 1 Yes. Para agregar o quitar protected actions se necesita **Conditional Access Administrator o Security Administrator**, más licencia P1.
- 2 No. La política que usa el context **tiene que estar On**. Si está en Off o Report-only, Learn documenta el síntoma "Policy is never satisfied": el admin entra en un ciclo de reautenticación. Para salir existe https://aka.ms/MSALProtectedActions.
- 3 No. **Azure PowerShell no soporta step-up** para protected actions y falla. Microsoft Graph PowerShell y Graph Explorer sí.

**Por qué las otras no:**
- Trampa de la 1: creer que solo Global Admin o Privileged Role Admin lo configuran.
- Trampa de la 2: tratar report-only como "casi On". Para protected actions no sirve.
- Trampa de la 3: confundir Azure PowerShell (ARM) con Microsoft Graph PowerShell.

**Fuente:** https://learn.microsoft.com/entra/identity/role-based-access-control/protected-actions-add#step-2-add-protected-actions, https://learn.microsoft.com/entra/identity/role-based-access-control/protected-actions-add#symptom---policy-is-never-satisfied y https://learn.microsoft.com/entra/identity/role-based-access-control/protected-actions-overview#what-happens-with-protected-actions-and-applications

---

### Q26 · Create a Conditional Access policy from a template · Multiple choice

Carlos, a Conditional Access Administrator, creates a policy from the template Require phishing-resistant multifactor authentication for administrators. Contoso has two cloud-only emergency access accounts that hold the Global Administrator role and don't have phishing-resistant methods.

What should Carlos do before he sets the policy to On?

A. Nothing. Templates automatically exclude emergency access accounts.
B. Edit the policy and exclude the two emergency access accounts, because the template excludes only the user who created the policy.
C. Change the policy state from Off to Report-only, because templates create policies in the Off state.
D. Export the template JSON, add the exclusions, and create the policy again with Upload policy file, because template policies can't be edited.

**Respuesta:** B

**Por qué es correcta:** Learn es explícito: las políticas creadas desde template **solo excluyen al usuario que las crea**. Las demás exclusiones (break-glass) se agregan editando la política después.

**Por qué las otras no:**
- A. No hay exclusión automática de break-glass.
- C. Los templates crean la política **en Report-only por default**, no en Off.
- D. Las políticas de template se editan como cualquier otra. Exportar e importar JSON existe, pero no es necesario.

**Fuente:** https://learn.microsoft.com/entra/identity/conditional-access/concept-conditional-access-policy-common#template-categories y https://learn.microsoft.com/entra/identity/conditional-access/concept-conditional-access-policy-common#user-exclusions

---

### Case study 1: Adatum Corporation (usar para Q27 y Q28)

Adatum Corporation has 4,000 users. Every user has a Microsoft 365 E3 license (which includes Microsoft Entra ID P1) and the Microsoft 365 E5 Compliance add-on. Adatum doesn't have Microsoft Entra ID P2. Security defaults are disabled, and Adatum has 30 Conditional Access policies. There are two cloud-only emergency access accounts.

Requirements:
- R1: Any creation, change, or deletion of a Conditional Access policy or a named location must require the administrator to use a FIDO2 security key at the moment of the change, regardless of which role grants the permission.
- R2: Access to the SharePoint site named Board must require a compliant device.
- R3: When Microsoft detects that a user's credentials were leaked, the user must be forced automatically to change the password at the next sign-in.
- R4: Users on unmanaged devices must get limited, browser-only access to Exchange Online.
- Administrative effort and cost must be minimized.

### Q27 · Implement protected actions · Case study (Multiple choice)

Refer to Case study 1. Which solution meets R1?

A. Create an authentication context and a Conditional Access policy (turned on) that targets it with a custom authentication strength that allows only passkeys (FIDO2) restricted to the approved security key AAGUIDs. Then, in Roles & admins > Protected actions, assign the context to the create, update, and delete permissions of Conditional Access policies and named locations.
B. Create a Conditional Access policy that includes the Conditional Access Administrator directory role, targets Microsoft Admin Portals, and requires the Phishing-resistant MFA strength.
C. Configure PIM for the Conditional Access Administrator role with On activation, require multifactor authentication.
D. Create a custom role without Conditional Access permissions and assign it to all administrators.

**Respuesta:** A

**Por qué es correcta:** **Protected actions** aplica CA **en el momento de la acción** y **sin importar el rol** que da el permiso. La lista de permisos soportados incluye CA policies y named locations. La strength custom con AAGUIDs asegura que sea una llave FIDO2; la built-in Phishing-resistant también aceptaría WHfB o CBA.

**Por qué las otras no:**
- B. Depende del rol (Security Admin o Global Admin también pueden editar CA) y se evalúa al sign-in, no al cambio.
- C. Solo pide MFA al activar, y no aplica a otros roles con el mismo permiso.
- D. Quitar permisos no es pedir una llave FIDO2 al hacer el cambio. Learn además dice que protected actions no se usa para bloquear por identidad.

**Fuente:** https://learn.microsoft.com/entra/identity/role-based-access-control/protected-actions-overview#what-permissions-can-be-used-with-protected-actions y https://learn.microsoft.com/entra/identity/authentication/concept-authentication-strength-advanced-options#configure-advanced-options-for-passkeys-fido2

---

### Q28 · Plan Conditional Access policies · Case study (Multiple choice)

Refer to Case study 1. Which requirement can't be met with Adatum's current licenses?

A. R1
B. R2
C. R3
D. R4

**Respuesta:** C

**Por qué es correcta:** Forzar el cambio de password automáticamente cuando hay riesgo es una **política de user risk**, y las políticas basadas en riesgo **piden Microsoft Entra ID P2**. La detección de leaked credentials sí llega con P1, pero automatizar la respuesta con CA no.

**Por qué las otras no:**
- A. Protected actions pide P1. Adatum lo tiene.
- B. Authentication context con CA es P1, y la sensitivity label de sitios la cubre el add-on E5 Compliance.
- D. App enforced restrictions es un session control de CA (P1).

**Fuente:** https://learn.microsoft.com/entra/id-protection/concept-identity-protection-policies y https://learn.microsoft.com/entra/identity/conditional-access/plan-conditional-access#prerequisites

---

## Subdominio 3: Manage risk by using Microsoft Entra ID Protection

### Q29 · Implement and manage user risk by using Microsoft Entra ID Protection or Conditional Access policies · Multiple choice

Contoso has Microsoft Entra ID P2. Some users sign in with passwords, and others are passwordless (Windows Hello for Business and passkeys). The legacy user risk policy in ID Protection is enabled with Require password change.

You need a user risk solution that lets both groups self-remediate when user risk is High and that follows Microsoft recommendations before the legacy risk policies are retired.

What should you do?

A. Keep the legacy ID Protection user risk policy and add Require multifactor authentication to it.
B. Create a Conditional Access policy for All users (excluding emergency access accounts) and All resources, with the condition User risk set to High and the grant control Require risk remediation. Then disable the legacy user risk policy.
C. Create a Conditional Access policy with the condition User risk set to High and the grant control Require multifactor authentication.
D. Create a Conditional Access policy with the conditions User risk High and Sign-in risk High and the grant control Require password change.

**Respuesta:** B

**Por qué es correcta:** **Require risk remediation** se adapta al método del usuario: con password pide un **secure password change**; en passwordless **revoca las sesiones** y pide sign-in otra vez. Al elegirlo se agregan solos **Require authentication strength** y **Sign-in frequency Every time**. Las políticas legacy de ID Protection se retiran el **1 de octubre de 2026**.

**Por qué las otras no:**
- A. La política legacy se retira y no ofrece este control.
- C. MFA remedia **sign-in risk**, no user risk.
- D. Learn pide **no combinar** user risk y sign-in risk en la misma política. Y password change no sirve para usuarios passwordless.

**Fuente:** https://learn.microsoft.com/entra/id-protection/concept-identity-protection-policies#require-risk-remediation-control y https://learn.microsoft.com/entra/id-protection/howto-identity-protection-configure-risk-policies#migrate-risk-policies-to-conditional-access

---

### Q30 · Implement and manage sign-in risk by using Microsoft Entra ID Protection or Conditional Access policies · Yes/No series

Contoso creates the following Conditional Access policy:

- Users: All users, excluding emergency access accounts
- Target resources: All resources
- Conditions: Sign-in risk set to Medium and High
- Grant: Require authentication strength (built-in Multifactor authentication)
- Session: Sign-in frequency set to Every time

For each of the following statements, select Yes or No.

1. A user who hasn't registered any MFA method and triggers a medium-risk sign-in is blocked and needs an administrator to intervene.
2. When a user completes MFA on a risky sign-in, the risk state of that sign-in changes to Remediated.
3. To reduce the number of policies, you should add the User risk High condition to this same policy.

**Respuesta:** 1 = Yes, 2 = Yes, 3 = No

**Por qué es correcta:**
- 1 Yes. Learn: el usuario **debe tener un método registrado** que satisfaga MFA antes de caer en la política. Si no puede cumplir el control, queda bloqueado y necesita al admin.
- 2 Yes. Al pasar MFA, el estado cambia de **"At risk" a "Remediated"** con el detalle "User passed multifactor authentication".
- 3 No. **Nunca combines sign-in risk y user risk** en la misma política. Crea una para cada uno.

**Por qué las otras no:**
- Trampa de la 1: pensar que el usuario se registra ahí mismo. Por eso existe la MFA registration policy o la registration campaign antes de activar riesgo.
- Trampa de la 3: querer "ahorrar" políticas. Las condiciones se suman con AND y el remedio de cada riesgo es distinto.

**Fuente:** https://learn.microsoft.com/entra/id-protection/concept-identity-protection-policies#sign-in-risk-based-conditional-access-policy, https://learn.microsoft.com/entra/id-protection/howto-identity-protection-remediate-unblock#self-remediation-of-sign-in-risk y https://learn.microsoft.com/entra/id-protection/howto-identity-protection-configure-risk-policies

---

### Q31 · Implement and manage user risk by using Microsoft Entra ID Protection or Conditional Access policies · Multiple choice

Contoso is a hybrid organization that uses password hash synchronization. Many users work on Microsoft Entra hybrid joined devices and change their passwords on-premises by pressing Ctrl+Alt+Del. When these users are flagged with user risk, the risk stays At risk after they change their password on-premises.

You need on-premises password changes to remediate user risk. What should you do?

A. Enable password writeback in Microsoft Entra Connect.
B. In ID Protection settings, select Allow on-premises password change to reset user risk.
C. Enable SSPR for all users.
D. Dismiss the user risk for all risky users every week.

**Respuesta:** B

**Por qué es correcta:** Con **PHS habilitado**, el setting **"Allow on-premises password change to reset user risk"** hace que un cambio de password on-prem remedie el user risk automáticamente. Es opt-in y lo configura como mínimo un Security Operator.

**Por qué las otras no:**
- A. Writeback va de la nube hacia AD. No hace que un cambio hecho en AD cuente como remedio.
- C. Un reset por SSPR en la nube sí remedia, pero estos usuarios cambian el password on-prem.
- D. Dismiss no cambia el password y deja la identidad igual de expuesta.

**Fuente:** https://learn.microsoft.com/entra/id-protection/howto-identity-protection-remediate-unblock#allow-on-premises-password-reset-to-remediate-user-risks

---

### Q32 · Implement and manage multifactor authentication registration by using authentication methods and registration campaigns · Multiple choice

Contoso users perform MFA with text messages (SMS). You create a registration campaign with the following settings: State Enabled, Authentication method Microsoft Authenticator, include All users, Days allowed to snooze 3, and Limited number of snoozes Enabled. After a week, no user has been prompted.

In the Microsoft Authenticator method policy, All users are targeted and Authentication mode is set to Passwordless.

What should you change?

A. Set Days allowed to snooze to 0.
B. Set the Authenticator Authentication mode to Any or Push.
C. Change the campaign state to Microsoft managed.
D. Enable the multifactor authentication registration policy in ID Protection.

**Respuesta:** B

**Por qué es correcta:** Prerrequisito de la campaign de Authenticator: los usuarios deben estar habilitados para Authenticator con **Authentication mode Any o Push**. Con **Passwordless no son elegibles** para el nudge.

**Por qué las otras no:**
- A. El snooze no arregla la elegibilidad.
- C. En Microsoft managed también se exige estar habilitado para Authenticator push.
- D. La MFA registration policy pide registrar MFA a quien no tiene nada. Estos usuarios ya tienen SMS.

Datos de la campaign: se configura como mínimo con Authentication Policy Administrator; snooze de 0 a 14 días; con snoozes limitados, después de 3 el registro es obligatorio; no hay nudge dentro de una sesión SSO.

**Fuente:** https://learn.microsoft.com/entra/identity/authentication/how-to-mfa-registration-campaign#prerequisites y https://learn.microsoft.com/entra/identity/authentication/how-to-mfa-registration-campaign#choose-a-campaign-state

---

### Q33 · Implement and manage multifactor authentication registration by using authentication methods and registration campaigns · Yes/No series

Contoso has Microsoft Entra ID P2. It enables the ID Protection multifactor authentication registration policy for all users and also runs a registration campaign in the Enabled state with Limited number of snoozes set to Enabled.

For each of the following statements, select Yes or No.

1. With the ID Protection MFA registration policy, users have 14 days to register, and after that they must register before they can complete sign-in.
2. A single registration campaign can nudge users to set up Microsoft Authenticator and a passkey at the same time.
3. With Limited number of snoozes enabled, a user can skip the campaign prompt three times before registration becomes required.

**Respuesta:** 1 = Yes, 2 = No, 3 = Yes

**Por qué es correcta:**
- 1 Yes. La política pide registro en el siguiente sign-in interactivo y da **14 días**. Después ya no se puede saltar.
- 2 No. La campaign apunta a **un método a la vez**: Authenticator o passkey, no los dos.
- 3 Yes. Con snoozes limitados, el usuario puede posponer **3 veces**; luego el registro es obligatorio.

**Por qué las otras no:**
- Trampa de la 1: confundir los 14 días de la MFA registration policy con el período de gracia de security defaults, que ya no existe desde julio de 2024.
- Trampa de la 2: la campaign nueva soporta passkeys, pero no en paralelo con Authenticator.
- Trampa de la 3: creer que se puede esconder el botón de snooze. No se puede; se limita a 3.

**Fuente:** https://learn.microsoft.com/entra/id-protection/howto-identity-protection-configure-mfa-policy#user-experience, https://learn.microsoft.com/entra/identity/authentication/how-to-mfa-registration-campaign#snooze-experience y https://learn.microsoft.com/entra/identity/authentication/how-to-mfa-registration-campaign#can-i-run-registration-campaigns-for-both-authenticator-and-passkeys-at-the-same-time

---

### Q34 · Monitor, investigate and remediate risky users and risky sign-ins · Select two

A security analyst must be able to dismiss user risk and generate temporary passwords for users directly from ID Protection > Risky users. The solution must follow the principle of least privilege.

Which two roles should you assign? Each correct answer presents part of the solution.

A. Security Reader
B. Security Operator
C. User Administrator
D. Security Administrator
E. Global Reader

**Respuesta:** B y C

**Por qué es correcta:** Learn lo pone en los prerrequisitos: **Security Operator** es el rol mínimo para **descartar user risk**, y **User Administrator** es el mínimo para **resetear passwords**. Para generar el password temporal desde ID Protection necesitas **los dos**: uno abre ID Protection y el otro permite el reset.

**Por qué las otras no:**
- A. Security Reader solo lee.
- D. Security Administrator sirve para crear o editar políticas de riesgo, pero no resetea passwords y da más de lo necesario.
- E. Global Reader es el mínimo para ver los reportes de riesgo, no para actuar.

**Fuente:** https://learn.microsoft.com/entra/id-protection/howto-identity-protection-remediate-unblock#prerequisites y https://learn.microsoft.com/entra/id-protection/howto-identity-protection-remediate-unblock#generate-a-temporary-password

---

### Q35 · Monitor, investigate and remediate risky users and risky sign-ins · Multiple choice

ID Protection flags an Atypical travel detection for Diego: one sign-in from Mexico City and, 20 minutes later, one from Frankfurt. Your investigation shows that the Frankfurt IP address is the egress IP of Contoso's sanctioned corporate VPN. Several users get similar detections every week.

What should you do?

A. Confirm the sign-in as compromised and reset Diego's password.
B. Confirm the sign-in as safe, and add the VPN egress IP range to named locations in Microsoft Entra ID and in Microsoft Defender for Cloud Apps.
C. Dismiss Diego's user risk and exclude Diego from the sign-in risk policy.
D. Turn off the Atypical travel detection in ID Protection settings.

**Respuesta:** B

**Por qué es correcta:** La guía de investigación de Learn para atypical travel dice: si el rango de IP es de una VPN autorizada, **confirma el sign-in como safe** y **agrega el rango de la VPN a named locations** en Entra y en Defender for Cloud Apps. Eso reduce falsos positivos futuros.

**Por qué las otras no:**
- A. No hay evidencia de compromiso. Confirmar compromised sube el riesgo sin razón.
- C. Excluir usuarios de la política debilita la protección y no arregla la causa (la VPN).
- D. No hay un switch documentado para apagar una detección. La vía es named locations y dar feedback (safe o compromised).

**Fuente:** https://learn.microsoft.com/entra/id-protection/howto-identity-protection-investigate-risk#atypical-travel-detections y https://learn.microsoft.com/entra/id-protection/howto-identity-protection-investigate-risk#mitigate-future-risks

---

### Q36 · Monitor, investigate and remediate risky users and risky sign-ins · Multiple choice

Contoso has Microsoft Entra ID P1 (no P2) and uses password hash synchronization. The Risky users report shows Adele with a Leaked credentials detection.

Which action remediates the user risk for this detection?

A. Dismiss Adele's user risk.
B. Reset Adele's password in Microsoft Entra ID, for example by generating a temporary password.
C. Require MFA at Adele's next sign-in.
D. Revoke Adele's sessions.

**Respuesta:** B

**Por qué es correcta:** Leaked credentials es una **detección nonpremium** (se ve completa con Free o P1) y **siempre es High**. Learn dice que **un reset de password en la nube remedia** el riesgo de esta detección, incluso para passwords on-prem, siempre que haya **PHS habilitado**. Con un password temporal el estado pasa a Remediated.

**Por qué las otras no:**
- A. Dismiss deja el estado en Dismissed, pero el password filtrado sigue siendo válido.
- C. MFA remedia sign-in risk, no un password filtrado.
- D. Revocar sesiones corta tokens, pero no cambia el password.

**Fuente:** https://learn.microsoft.com/entra/id-protection/concept-identity-protection-risks#leaked-credentials y https://learn.microsoft.com/entra/id-protection/howto-identity-protection-remediate-unblock#generate-a-temporary-password

---

### Q37 · Monitor, investigate, and remediate risky workload identities · Multiple choice

Contoso has Microsoft Entra ID P2 for all users. A single-tenant app registration named InvoiceSync authenticates with a client secret. You need to block sign-ins from the InvoiceSync service principal automatically whenever ID Protection flags it as high risk.

What do you need?

A. Nothing more than P2. Create a Conditional Access policy that targets the service principal with the service principal risk condition and Block access.
B. Workload Identities Premium licenses, and then a Conditional Access policy that targets the InvoiceSync service principal with the service principal risk condition set to High and the grant control Block access.
C. A Conditional Access policy that targets the service principal and requires MFA when risk is High.
D. A user risk-based Conditional Access policy that includes the owner of the app registration.

**Respuesta:** B

**Por qué es correcta:** Las detecciones de riesgo de workload identities llegan a todos (con detalle limitado sin licencia), pero **el control de acceso basado en riesgo pide Workload Identities Premium**. Y CA para workload identities solo aplica a **service principals single-tenant** registrados en tu tenant.

**Por qué las otras no:**
- A. P2 cubre usuarios, no workload identities.
- C. Una workload identity **no puede hacer MFA**. El control soportado es Block.
- D. El riesgo del dueño no es el riesgo del service principal.

Recuerda: **managed identities no están en scope** ni para las detecciones ni para CA, y tampoco las apps SaaS multitenant.

**Fuente:** https://learn.microsoft.com/entra/id-protection/concept-workload-identity-risk#prerequisites y https://learn.microsoft.com/entra/id-protection/concept-workload-identity-risk#enforce-access-controls-with-risk-based-conditional-access

---

### Q38 · Monitor, investigate, and remediate risky workload identities · Select two

The InvoiceSync service principal is confirmed compromised after its client secret was found in a public GitHub repository.

Which two actions should you perform to remediate the workload identity, according to Microsoft guidance? Each correct answer presents part of the solution.

A. Add a new credential, preferably an X.509 certificate, and remove all existing credentials from the application and the service principal.
B. Rotate the Azure Key Vault secrets that the service principal can access.
C. Require MFA for the service principal.
D. Reset the password of the application owner.
E. Dismiss the risk in the Risky workload identities report.

**Respuesta:** A y B

**Por qué es correcta:** Los pasos de remediación de Learn son: **inventariar credenciales**, **agregar una nueva** (se recomiendan certificados X.509), **quitar las comprometidas** (si crees que la cuenta está en riesgo, quita todas) y **rotar los secretos de Key Vault** a los que el service principal tiene acceso.

**Por qué las otras no:**
- C. Las workload identities no pueden hacer MFA.
- D. El dueño no es la credencial filtrada.
- E. Dismiss no invalida el secreto filtrado. Si quieres cortar ya los sign-ins, existe "Disable service principal".

**Fuente:** https://learn.microsoft.com/entra/id-protection/concept-workload-identity-risk#remediate-risky-workload-identities

---

## Subdominio 4: Implement Global Secure Access

### Q39 · Deploy Global Secure Access clients · Select two

Contoso has Microsoft Entra Internet Access licenses and deploys the Global Secure Access client for Windows by using Intune. The Internet Access traffic forwarding profile is enabled for all users.

- Device1: Windows 11, Microsoft Entra joined
- Device2: Windows 10 Enterprise LTSC 2021 (64-bit), Microsoft Entra hybrid joined
- Device3: Personal Windows 11 laptop, Microsoft Entra registered
- Device4: Azure Virtual Desktop multi-session host
- Device5: Windows 365 Cloud PC

On which two devices will Internet Access traffic NOT be tunneled by the client? Each correct answer presents part of the solution.

A. Device1
B. Device2
C. Device3
D. Device4
E. Device5

**Respuesta:** C y D

**Por qué es correcta:** Según los prerrequisitos del cliente para Windows: en devices **Microsoft Entra registered solo se soporta Private Access** (preview), y **Azure Virtual Desktop multi-session no está soportado**.

**Por qué las otras no:**
- A. Entra joined con Windows 11 es el caso base.
- B. Windows 10 LTSC 2021 o posterior de 64 bits está soportado, y hybrid joined también.
- E. Windows 365 está soportado (igual que AVD single-session).

Datos extra: instalar pide admin local; se puede instalar silencioso con /quiet o como Win32 app en Intune; Internet Access no soporta QUIC ni DNS over HTTPS, así que hay que deshabilitarlos en los navegadores; con RestrictNonPrivilegedUsers el usuario no puede apagar el cliente.

**Fuente:** https://learn.microsoft.com/entra/global-secure-access/how-to-install-windows-client#prerequisites

---

### Q40 · Deploy and manage Private Access · Drag/order

Contoso wants to replace its VPN. Remote users must reach on-premises file servers (TCP 445) and Remote Desktop hosts (TCP 3389) through Microsoft Entra Private Access by using Quick Access. The Global Secure Access client is already deployed.

Which four actions should you perform in sequence? (Two actions aren't used.)

A. Install a Microsoft Entra private network connector on an on-premises server and add it to a connector group.
B. In Global Secure Access > Applications > Quick Access, enter a name, select the connector group, and add application segments with the FQDNs or IP ranges and ports 445 and 3389.
C. Assign users or groups directly to the Quick Access enterprise application.
D. Enable the Private Access traffic forwarding profile.
E. Enable the Microsoft traffic forwarding profile.
F. Publish the file servers as Application Proxy apps with an external URL.

**Respuesta:** A, B, C, D (en ese orden)

**Por qué es correcta:** Es el resumen de Learn: **connector group con al menos un conector activo**, configurar **Quick Access** (crea una enterprise app nueva), **asignar usuarios y grupos**, ligar CA (opcional aquí) y **habilitar el Private Access profile**. Roles: Global Secure Access Administrator y Application Administrator.

**Por qué las otras no:**
- E. El Microsoft profile es para tráfico de Microsoft 365, no para recursos privados.
- F. Application Proxy publica apps web con URL externa. Private Access cubre cualquier puerto y protocolo sin URL externa.
- Ojo en C: la asignación debe ser **directa o por un grupo asignado; nested groups no se soportan**. Y Quick Access acepta hasta 500 application segments.

**Fuente:** https://learn.microsoft.com/entra/global-secure-access/how-to-configure-quick-access#high-level-steps y https://learn.microsoft.com/entra/global-secure-access/how-to-configure-quick-access#assign-users-and-groups

---

### Q41 · Deploy and manage Private Access · Multiple choice

Contoso uses Quick Access for its file servers, with a Conditional Access policy that requires MFA. A new ERP server at 10.20.5.20 (TCP 443) must be reachable only by the Finance group, and access must require a compliant device and MFA. The existing Quick Access policy for file servers must not change.

What should you do?

A. Add 10.20.5.20:443 to Quick Access and add Require device to be marked as compliant to the Conditional Access policy linked to Quick Access.
B. Create a Global Secure Access application (per-app access) for 10.20.5.20:443, assign the Finance group, and link a Conditional Access policy that requires a compliant device and MFA to that application.
C. Create a named location for 10.20.5.20 and a Conditional Access policy that blocks all other locations.
D. Add the Finance group as a nested member of the group that's assigned to Quick Access.

**Respuesta:** B

**Por qué es correcta:** Learn: una **Global Secure Access app (per-app access)** es para cuando necesitas **políticas de CA distintas para un subconjunto de recursos o de usuarios**. Quick Access es el bloque principal; per-app es el paso de segmentación en el camino Zero Trust.

**Por qué las otras no:**
- A. Cambia la política de todo Quick Access y afecta a los file servers. Además, cualquier usuario asignado a Quick Access llegaría al ERP.
- C. Named locations evalúan la IP de origen del usuario, no el destino privado.
- D. Nested groups no se soportan en la asignación, y no resuelve el requisito de política distinta.

**Fuente:** https://learn.microsoft.com/entra/global-secure-access/concept-private-access#global-secure-access-app y https://learn.microsoft.com/entra/global-secure-access/how-to-configure-quick-access#overview

---

### Q42 · Deploy and manage Internet Access · Select two

Contoso must block the Gambling web category for members of the Sales group only. The Internet Access traffic forwarding profile is enabled and the Global Secure Access client is deployed. You already created a web content filtering policy with a Block rule for the Gambling category.

Which two additional configurations are required? Each correct answer presents part of the solution.

A. A security profile that links the web content filtering policy.
B. A Conditional Access policy for the Sales group that targets All internet resources with Global Secure Access and uses the session control Use Global Secure Access security profile.
C. Linking the web content filtering policy to the baseline security profile.
D. Enabling the Microsoft traffic forwarding profile.
E. A named location for the Sales office.

**Respuesta:** A y B

**Por qué es correcta:** El flujo de Learn: filtering policy, **security profile** que la agrupa y **política de CA** que entrega ese security profile a los usuarios. CA es el mecanismo que hace la política **consciente del usuario**: target "All internet resources with Global Secure Access" y sesión "Use Global Secure Access security profile".

**Por qué las otras no:**
- C. El baseline profile **aplica a todo el tráfico** (incluidas remote networks) sin CA. Bloquearía a todos, no solo a Sales.
- D. El Microsoft profile es para tráfico de Microsoft 365; no filtra categorías de internet.
- E. No hace falta ubicación para este requisito.

Datos que caen: un security profile nuevo tarda de 60 a 90 minutos (viaja en el access token); un bloqueo HTTPS se ve como "Connection Reset"; sin TLS inspection solo aplican reglas por SNI.

**Fuente:** https://learn.microsoft.com/entra/global-secure-access/how-to-configure-web-content-filtering#high-level-steps, https://learn.microsoft.com/entra/global-secure-access/how-to-configure-web-content-filtering#create-a-security-profile y https://learn.microsoft.com/entra/global-secure-access/how-to-configure-web-content-filtering#create-and-link-conditional-access-policy

---

### Case study 2: Fabrikam Logistics (usar para Q43 y Q44)

Fabrikam Logistics has 3,000 employees. All employees have Microsoft Entra ID P1, and 600 remote employees also have Microsoft Entra Suite. Windows devices are Microsoft Entra joined and run the Global Secure Access client. The Seattle warehouse connects to Global Secure Access through a remote network (branch router). The Microsoft traffic forwarding profile is enabled.

Requirements:
- R1: Stolen tokens replayed from outside Fabrikam's Global Secure Access connections must be rejected for Microsoft 365 and other Microsoft Entra integrated apps. Administrators must not maintain lists of egress IP addresses.
- R2: Users on corporate devices must not be able to sign in to any other Microsoft Entra tenant, except the partner tenant contoso.com.
- R3: Sign-in logs must show each user's real public IP address instead of the proxy egress IP address.
- Administrative effort must be minimized.

### Q43 · Deploy and manage Internet Access for Microsoft 365 · Case study (Multiple choice)

Refer to Case study 2. Which solution meets R1?

A. Enable Conditional Access signaling in Global Secure Access (Session management > Adaptive access). Then create a Conditional Access policy for All resources with the Network condition set to include Any location and exclude All Compliant Network locations, and the grant control Block access.
B. Create a named location that contains the Global Secure Access egress IP addresses, and block all other locations.
C. Enable source IP restoration and create a location-based Conditional Access policy with the office IP ranges.
D. Enable universal tenant restrictions.

**Respuesta:** A

**Por qué es correcta:** El **compliant network check** asegura que el usuario entra por Global Secure Access **de tu tenant**, sin mantener IPs. Si alguien repite un token robado fuera de esa red, Entra lo rechaza, y con apps que soportan CAE el access token también se rechaza casi en tiempo real. Se activa el signaling y aparece la location **All Compliant Network locations**.

**Por qué las otras no:**
- B. Mantener IPs es justo lo que el requisito prohíbe, y las IPs de salida del servicio no son exclusivas de Fabrikam.
- C. Source IP restoration sirve para logs y políticas por IP (eso resuelve R3), pero vuelve a depender de listas de IPs.
- D. Tenant restrictions controla a qué tenants se entra, no el replay de tokens.

Dato fino: si el cliente no logra conectar, el tráfico del Microsoft profile **se va directo en lugar de bloquearse**; por eso el compliant network check es la red de seguridad. Excluye Microsoft Intune y Microsoft Intune Enrollment para evitar una dependencia circular.

**Fuente:** https://learn.microsoft.com/entra/global-secure-access/how-to-compliant-network#enable-global-secure-access-signaling-for-conditional-access y https://learn.microsoft.com/entra/global-secure-access/how-to-compliant-network#protect-your-resources-behind-the-compliant-network

---

### Q44 · Deploy and manage Internet Access for Microsoft 365 · Case study (Multiple choice)

Refer to Case study 2. Which solution meets R2?

A. In cross-tenant access settings, configure the default tenant restrictions v2 policy to block external accounts and apps, add contoso.com in Organizational settings with tenant restrictions that allow it, and then turn on universal tenant restrictions in Global Secure Access (Settings > Session management).
B. Configure the default outbound B2B collaboration settings to block all organizations, and allow only contoso.com.
C. Configure the default inbound B2B collaboration settings to block all organizations, and allow only contoso.com.
D. Enable source IP restoration and block sign-ins from IP addresses that aren't Fabrikam's.

**Respuesta:** A

**Por qué es correcta:** **Tenant restrictions v2** decide qué tenants externos se pueden usar desde tus devices y tu red. **Universal tenant restrictions** usa Global Secure Access para etiquetar el tráfico de autenticación con esa política, en cualquier navegador y plataforma, y funciona tanto con el cliente como con remote networks. Viene con el Microsoft traffic profile (P1). Para activarlo se necesitan Global Secure Access Administrator y Security Administrator.

**Por qué las otras no:**
- B. Outbound controla a **tus propios usuarios** como guests en otros tenants. No impide que alguien use en tu device una cuenta de otro tenant.
- C. Inbound controla a externos que entran a **tus recursos**. Es la dirección contraria.
- D. Source IP restoration es para R3 (logs con la IP real), no para limitar tenants.

**Fuente:** https://learn.microsoft.com/entra/global-secure-access/how-to-universal-tenant-restrictions#enable-universal-tenant-restrictions y https://learn.microsoft.com/entra/external-id/tenant-restrictions-v2#tenant-restrictions-v2-overview
