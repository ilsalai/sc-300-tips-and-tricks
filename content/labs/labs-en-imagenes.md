# SC-300 Tips and Tricks: labs en imágenes

## Por qué imágenes y no tenant

Hacer los 10 labs en un tenant toma entre 4 y 5 horas, pide licencias P1, P2 y Governance, y varias cosas tardan en propagar (dynamic groups, licencias, políticas de Conditional Access). Para el examen lo que importa es **reconocer la pantalla, el nombre exacto del campo y el estado final**. Esta guía condensa cada lab oficial en pasos cortos, con capturas oficiales de Microsoft Learn al lado de cada paso. Si quieres practicar en tenant, usa esta guía como checklist.

- Índice oficial de labs: https://microsoftlearning.github.io/SC-300-Identity-and-Access-Administrator/
- Las capturas vienen de páginas de Microsoft Learn. A veces el ejemplo de Learn usa otros nombres (por ejemplo "MFA Pilot" en vez de "MFA_for_Delia"). La pantalla es la misma, cambia el valor que escribes.
- Los pasos son paráfrasis del lab oficial. Los nombres de campos, botones y valores se dejan en inglés, igual que en el portal.
- Todas las URLs de imagen se validaron (responden 200, image/png) el 2026-09-23.

## Resumen de los 10 labs

| # | Lab oficial | Licencia que necesita | Tiempo real estimado |
|---|---|---|---|
| 1 | Lab 01: Manage user roles | Free (la licencia Windows E3 del ejercicio 6 viene en el tenant de lab) | 30 min |
| 2 | Lab 03: Assign licenses by group membership | P1 (group-based licensing y dynamic groups) | 25 min + hasta 15 min de espera del dynamic group |
| 3 | Lab 04 + Lab 05: External collaboration + guest users | Free | 25 min (5 + 20) |
| 4 | Lab 08 + Lab 09: MFA + SSPR | P1 (Conditional Access y SSPR para usuarios cloud) | 35 min aprox. (Lab 08 no trae estimado oficial, Lab 09 son 15) |
| 5 | Lab 13: Conditional Access policy | P1 | 20 min |
| 6 | Lab 14: User risk y sign-in risk policies | P2 | 10 min |
| 7 | Lab 19 + Lab 21: Register app + admin consent | Free (el custom role del ejercicio 2 necesita P1) | 45 min (30 + 15) |
| 8 | Lab 22: Catalog en entitlement management | Governance (algunas capacidades funcionan con P2) | 15 min |
| 9 | Lab 25: Access reviews | Governance (algunas capacidades funcionan con P2) | 5 min |
| 10 | Lab 26: PIM para Microsoft Entra roles | P2 o Governance | 30 min |

Nota de licencias: el Lab 22 oficial dice "P1, P2, EMS E3 o EMS E5", pero la documentación actual de Learn dice que entitlement management y access reviews requieren **Microsoft Entra ID Governance** (o Entra Suite), con algunas capacidades en P2. Para el examen, quédate con lo que dice Learn.

---

## Lab 1: Manage user roles (Lab 01)

**Skill del outline:** M1 > Configure and manage a Microsoft Entra tenant (built-in roles). M1 > Create, configure, and manage identities (users, bulk operations con admin center y PowerShell, licenses).

**Objetivo en una línea:** existe el usuario Chris Green (creado, borrado y restaurado), ya no tiene el rol Application administrator, hay usuarios creados por bulk create y PowerShell, y Raul Razo tiene la licencia Windows 10/11 Enterprise E3.

**Ruta en el portal:** Entra ID > Users > All users (crear, bulk, borrar, restaurar) y Entra ID > Roles & admins (asignar y quitar roles).

**Pasos (con imagen):**

1. Entra ID > Users > All users > **+ New user** > **Create new user**. User principal name: `ChrisG`, Display name: `Chris Green`, marca **Auto-generate password**, copia el password, luego **Review + create** > **Create**.
   ![Página All users en Entra](https://learn.microsoft.com/en-us/entra/fundamentals/media/how-to-create-delete-users/all-users-page.png)  Fuente: https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users
   ![Menú New user > Create new user](https://learn.microsoft.com/en-us/entra/fundamentals/media/how-to-create-delete-users/create-new-user-menu.png)  Fuente: https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users
   ![Pestaña Basics del nuevo usuario](https://learn.microsoft.com/en-us/entra/fundamentals/media/how-to-create-delete-users/create-new-user-basics-tab.png)  Fuente: https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users
2. En ventana InPrivate entra como Chris Green, cambia el password y abre **Enterprise applications**. Confirma que **+ Create your own application** NO está disponible. Cierra sesión.
   Sin captura oficial, candidato a captura en tenant.
3. Como admin: Users > Chris Green > **Assigned roles** > **+ Add assignments** > **Application administrator** > **Next** > Assignment type **Active** > justificación "Needed for lab" > **Assign** > **Refresh**.
   ![Panel Add assignments para un rol](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/media/manage-roles-portal/add-assignments.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal
4. Otra vez InPrivate como Chris: Enterprise applications > **+ New application**. Ahora **+ Create your own application** sí aparece y el botón **Create** está activo.
   Sin captura oficial, candidato a captura en tenant.
5. Quitar el rol: **Roles and administrators** > **Application administrator** > busca a Chris Green > **Remove** > **Yes**.
   ![Página Roles and administrators](https://learn.microsoft.com/en-us/entra/media/common/entra-roles-admins.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/manage-roles-portal
6. Bulk create: Users > All users > **Bulk operations** > **Bulk create** > **Download** el template, edita `SC300BulkUser.csv` con tu dominio, súbelo y **Submit**. Revisa el estado en Bulk operation results.
   ![Página Bulk create user con botón de carga](https://learn.microsoft.com/en-us/entra/identity/users/media/users-bulk-add/upload-button.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-add
   ![Bulk operation results](https://learn.microsoft.com/en-us/entra/identity/users/media/users-bulk-add/bulk-center.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/users/users-bulk-add
7. PowerShell (7.2+): `Install-Module Microsoft.Graph -Scope CurrentUser`, `Connect-MgGraph -Scopes "User.ReadWrite.All"`, arma el PasswordProfile y corre `New-MgUser` con DisplayName, MailNickname, UsageLocation, UserPrincipalName, etc.
   Sin captura oficial, candidato a captura en tenant (consola).
8. Borrar y restaurar: All users > check en Chris Green > **Delete** > **Yes**. Luego **Deleted users** > Chris Green > **Restore user** > **OK**.
   ![Usuario seleccionado con botón Delete](https://learn.microsoft.com/en-us/entra/fundamentals/media/how-to-create-delete-users/delete-existing-user.png)  Fuente: https://learn.microsoft.com/en-us/entra/fundamentals/how-to-create-delete-users
   Paso de Restore: sin captura oficial, candidato a captura en tenant.
9. Licencia a Raul Razo: confirma que tiene **Usage location** y "No license assignments found". En admin.microsoft.com > **Billing** > **Licenses** > **Windows 10/11 Enterprise E3** > **+ Assign licenses** > Raul Razo. Verifica en Entra > Users > Raul Razo > **Licenses**.
   Sin captura oficial, candidato a captura en tenant.

**Trampas del lab:**
- Probar como el usuario sin InPrivate: la sesión de admin se mezcla y "parece" que el rol ya funciona.
- El rol puede tardar unos minutos en reflejarse. Si Create your own application no aparece, cierra sesión y vuelve a entrar.
- Bulk create: no borres ni cambies la fila `version:v1.0` ni los encabezados, y el UPN debe usar un dominio verificado de tu tenant.
- Sin **Usage location** no se puede asignar licencia. Un usuario borrado queda 30 días en Deleted users y después se borra para siempre.

**Cómo lo preguntaría el examen:**
- Un desarrollador necesita crear enterprise apps propias sin ser Global Administrator. ¿Qué rol de menor privilegio le asignas?
- Debes crear 500 usuarios desde un CSV con el mínimo esfuerzo administrativo. ¿Qué herramienta usas?
- Un usuario se borró hace 10 días por error. ¿Cómo lo recuperas con sus licencias y grupos?

---

## Lab 2: Assign licenses by group membership (Lab 03)

**Skill del outline:** M1 > Create, configure, and manage identities (groups, dynamic groups, assign, modify, and report on licenses).

**Objetivo en una línea:** el grupo de seguridad `sg-SC300-O365` tiene Office 365 E3 y Delia Dennis la recibe por herencia; existe el grupo Microsoft 365 `Northwest Sales`; existe el grupo dinámico `SC300-myDynamicGroup` con regla `user.objectId -ne null` y más de 30 miembros.

**Ruta en el portal:** Entra ID > Groups > All groups > New group. Licencias: Microsoft 365 admin center > Billing > Licenses.

**Pasos (con imagen):**

1. Confirma que Delia Dennis (InPrivate, m365.cloud.microsoft/apps) ve el aviso de que no tiene licencia.
   Sin captura oficial, candidato a captura en tenant.
2. Groups > All groups > **New group**. Group type **Security**, Group name `sg-SC300-O365`, Membership type **Assigned**, Owner tu admin, Members **Delia Dennis** > **Select** > **Create**.
   ![Página Groups con New group](https://learn.microsoft.com/en-us/entra/fundamentals/media/how-to-manage-groups/new-group.png)  Fuente: https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups
   ![Seleccionar miembros al crear el grupo](https://learn.microsoft.com/en-us/entra/fundamentals/media/how-to-manage-groups/add-members.png)  Fuente: https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups
3. En admin.microsoft.com > **Billing** > **Licenses** > **Office 365 E3** > **Assign licenses** > busca `sg-SC300-O365` > **Assign licenses**. La captura de abajo es la vista equivalente de asignar licencias a grupos desde Entra admin center.
   ![Asignar licencias a grupos desde Entra admin center](https://learn.microsoft.com/intune/solutions/education/tutorial-school-deployment/media/setup-entra-id/entra-assign-licenses.png)  Fuente: https://learn.microsoft.com/intune/solutions/education/tutorial-school-deployment/setup-entra-id
   Vista de Microsoft 365 admin center: sin captura oficial, candidato a captura en tenant.
4. En Entra > Groups > `sg-SC300-O365` > **Licenses** confirma Office 365 E3 (puede tardar minutos). Delia vuelve a entrar y ya ve las apps sin aviso.
   Sin captura oficial, candidato a captura en tenant.
5. New group: Group type **Microsoft 365**, name `Northwest Sales`, Membership **Assigned**, Members **Alex Wilber** y **Bianca Pisani**. Es la misma pantalla del paso 2.
6. New group: Group type **Security**, name `SC300-myDynamicGroup`, Membership type **Dynamic User** > **Add dynamic query** > **Edit** > regla `user.objectId -ne null` > **OK** > **Save** > **Create**.
   ![Crear grupo nuevo para regla dinámica](https://learn.microsoft.com/en-us/entra/identity/users/media/groups-create-rule/create-new-group.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/users/groups-create-rule
   ![Rule builder de dynamic group](https://learn.microsoft.com/en-us/entra/identity/users/media/groups-create-rule/add-dynamic-group-rule.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/users/groups-create-rule
7. Espera hasta 15 min, filtra por "SC300", abre el grupo y revisa **Members** (30+) y el estado de procesamiento. Prueba reglas alternas: `(user.objectId -ne null) and (user.userType -eq "Guest")` o `-eq "Member"`.
   ![Estado de procesamiento del dynamic group](https://learn.microsoft.com/en-us/entra/identity/users/media/groups-create-rule/group-status.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/users/groups-create-rule

**Trampas del lab:**
- Group-based licensing no soporta **nested groups**: solo reciben licencia los miembros directos del grupo.
- Usuarios sin Usage location heredan la del tenant en group-based licensing; si hay conflicto de service plans, la licencia queda en error (revisa Errors & issues).
- El grupo dinámico tarda en poblarse (hasta 15 min en el lab) y necesita P1. El **Group type** no se puede cambiar después de crear el grupo.
- La regla se escribe en el text box con **Edit**; el rule builder solo soporta 5 expresiones.

**Cómo lo preguntaría el examen:**
- Todos los usuarios del departamento Sales deben recibir Microsoft 365 E5 automáticamente al entrar y perderla al salir, con el mínimo esfuerzo. ¿Qué configuras?
- Asignaste una licencia a un grupo padre y los usuarios de un grupo anidado no la reciben. ¿Por qué?
- Un usuario aparece con error de licencia en un grupo con licencias. ¿Dónde revisas y qué causas son típicas?

---

## Lab 3: External collaboration settings + guest users (Lab 04 + Lab 05)

**Skill del outline:** M1 > External users and tenants (manage External collaboration settings, invite external users individually or in bulk).

**Objetivo en una línea:** guest self-service sign up via user flows en **Yes**, Email one-time passcode en **Yes**, guest user access en el nivel **most restrictive**, invitaciones permitidas a member users y roles admin, y existen guests invitados uno por uno, en bulk y por PowerShell.

**Ruta en el portal:** Entra ID > External Identities > External collaboration settings, Entra ID > External Identities > All identity providers, y Entra ID > Users > All users (Invite external user, Bulk invite).

**Pasos (con imagen):**

1. **Enable guest self-service sign up via user flows** en **Yes** > **Save**. (El lab llega por Users > User settings > Manage external user collaboration settings, que abre la misma página.)
   ![Setting de self-service sign up via user flows](https://learn.microsoft.com/en-us/entra/external-id/media/external-collaboration-settings-configure/self-service-sign-up-setting.png)  Fuente: https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure
2. External Identities > **All identity providers** > **Email one-time passcode** > **Configured** > deja **Yes** > **Save**.
   ![Toggle de Email one-time passcode](https://learn.microsoft.com/en-us/entra/external-id/media/one-time-passcode/email-one-time-passcode-toggle.png)  Fuente: https://learn.microsoft.com/en-us/entra/external-id/one-time-passcode
3. External collaboration settings > **Guest user access**: elige "Guest user access is restricted to properties and memberships of their own directory objects (most restrictive)".
   ![Opciones de Guest user access](https://learn.microsoft.com/en-us/entra/external-id/media/external-collaboration-settings-configure/guest-user-access.png)  Fuente: https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure
4. **Guest invite settings**: elige "Member users and users assigned to specific admin roles can invite guest users including guests with member permissions".
   ![Opciones de Guest invite settings](https://learn.microsoft.com/en-us/entra/external-id/media/external-collaboration-settings-configure/guest-invite-settings.png)  Fuente: https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure
5. **Collaboration restrictions**: deja el default (permitir invitaciones a cualquier dominio) > **Save**.
   ![Collaboration restrictions](https://learn.microsoft.com/en-us/entra/external-id/media/external-collaboration-settings-configure/collaboration-restrictions.png)  Fuente: https://learn.microsoft.com/en-us/entra/external-id/external-collaboration-settings-configure
6. Users > All users > **+ New user** > **Invite external user**. Email `sc300externaluser1@sc300email.com`, revisa en **Properties** que User type sea **Guest** > **Review + invite** > **Invite**.
   ![Menú Invite external user](https://learn.microsoft.com/en-us/entra/external-id/media/quickstart-add-users-portal/invite-external-user-menu.png)  Fuente: https://learn.microsoft.com/en-us/entra/external-id/b2b-quickstart-add-guest-users-portal
   ![Pestaña Basics de Invite external user](https://learn.microsoft.com/en-us/entra/external-id/media/quickstart-add-users-portal/invite-external-user-basics-tab.png)  Fuente: https://learn.microsoft.com/en-us/entra/external-id/b2b-quickstart-add-guest-users-portal
   ![Guest nuevo en el directorio](https://learn.microsoft.com/en-us/entra/external-id/media/quickstart-add-users-portal/new-guest-user-directory.png)  Fuente: https://learn.microsoft.com/en-us/entra/external-id/b2b-quickstart-add-guest-users-portal
7. Bulk: **Bulk operations** > **Bulk invite** > **Download** el CSV, llena **Email address to invite** y **Redirection url**, súbelo, espera la validación > **Submit** > revisa Bulk operation results.
   ![Botón Bulk invite](https://learn.microsoft.com/en-us/entra/external-id/media/tutorial-bulk-invite/bulk-invite-button.png)  Fuente: https://learn.microsoft.com/en-us/entra/external-id/tutorial-bulk-invite
   ![CSV de bulk invite con guests](https://learn.microsoft.com/en-us/entra/external-id/media/tutorial-bulk-invite/bulk-invite-csv.png)  Fuente: https://learn.microsoft.com/en-us/entra/external-id/tutorial-bulk-invite
   ![Resultados de la operación bulk](https://learn.microsoft.com/en-us/entra/external-id/media/tutorial-bulk-invite/bulk-operation-results.png)  Fuente: https://learn.microsoft.com/en-us/entra/external-id/tutorial-bulk-invite
8. PowerShell: `Connect-MgGraph -Scopes "User.ReadWrite.All"`, arma `$params` con InvitedUserEmailAddress e InviteRedirectUrl, corre `New-MgInvitation -BodyParameter $params` y verifica el guest en el portal.
   Sin captura oficial, candidato a captura en tenant (consola).

**Trampas del lab:**
- Buscar los settings en el lugar viejo. Hoy viven en **External Identities > External collaboration settings**; Email OTP está en **All identity providers**.
- No se pueden invitar emails de grupo ni direcciones con `+`.
- Bulk invite: no toques las dos primeras filas del CSV y no uses comas en el mensaje personalizado.
- Si eliges "Only users assigned to specific admin roles", solo User Administrator y **Guest Inviter** pueden invitar.

**Cómo lo preguntaría el examen:**
- Los guests no deben ver otros usuarios ni grupos del directorio, solo su propio perfil. ¿Qué nivel de Guest user access eliges?
- Solo un grupo pequeño de empleados, sin ser admins, debe poder invitar guests. ¿Qué setting y qué rol usas?
- Un partner sin cuenta Microsoft ni Entra debe poder redimir la invitación. ¿Qué identity provider habilitas?

---

## Lab 4: MFA + SSPR (Lab 08 + Lab 09)

**Skill del outline:** M2 > User authentication (tenant-wide MFA settings, configure and deploy SSPR). M2 > Conditional Access (grant controls).

**Objetivo en una línea:** existe la CA policy `MFA_for_Delia` en **On** que pide MFA para Office 365; Adele Vance tiene per-user MFA **Enabled**; SSPR está en **Selected** con el grupo `SSPRTesters` y Allan Deyoung registrado y probado.

**Ruta en el portal:** Entra ID > Multifactor authentication, Entra ID > Conditional Access, Entra ID > Users > All users > Per-user MFA, Entra ID > Password reset.

**Pasos (con imagen):**

1. Busca "multifactor" > **Multifactor authentication** > Getting started > **Additional cloud-based multifactor authentication settings**. Revisa trusted IPs, verification options y remember MFA (portal legacy).
   Sin captura oficial, candidato a captura en tenant.
2. Conditional Access > **+ New policy**, name `MFA_for_Delia`.
   ![Conditional Access, crear nueva política](https://learn.microsoft.com/en-us/entra/identity/authentication/media/tutorial-enable-azure-mfa/tutorial-enable-azure-mfa-conditional-access-menu-new-policy.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa
3. Users: **Select users and groups** > **Delia Dennis**. Target resources: **Resources (formerly cloud apps)** > **Office 365**. Network: Configure **Yes** > **Any network or location**.
   ![Seleccionar users and groups en la política](https://learn.microsoft.com/en-us/entra/identity/authentication/media/tutorial-enable-azure-mfa/tutorial-enable-azure-mfa-conditional-access-menu-select-users-groups.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa
4. Grant: **Grant access** > **Require multifactor authentication** con "Require all the selected controls". **Enable policy** en **On** > **Create**.
   ![Grant, Grant access](https://learn.microsoft.com/en-us/entra/identity/authentication/media/tutorial-enable-azure-mfa/tutorial-enable-azure-mfa-conditional-access-menu-grant-access.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa
   ![Require multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/media/tutorial-enable-azure-mfa/tutorial-enable-azure-mfa-conditional-access-select-require-mfa.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa
   ![Enable policy en On](https://learn.microsoft.com/en-us/entra/identity/authentication/media/tutorial-enable-azure-mfa/tutorial-enable-azure-mfa-conditional-access-enable-policy-on.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa
5. Prueba: InPrivate a office.com como DeliaD. Aparece "More information required" y registra MFA.
   ![Prompt More information required](https://learn.microsoft.com/en-us/entra/identity/authentication/media/tutorial-enable-azure-mfa/tutorial-enable-azure-mfa-browser-prompt-more-info.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa
6. Per-user MFA: Users > All users > **Per-user MFA** > check **Adele Vance** > **Enable MFA** > **Enable** > **Close**.
   ![Enable MFA en per-user MFA](https://learn.microsoft.com/en-us/entra/identity/authentication/media/howto-mfa-userstates/new-enable.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-userstates
   ![User MFA settings y estados](https://learn.microsoft.com/en-us/entra/identity/authentication/media/howto-mfa-userstates/user-states.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-userstates
7. SSPR, grupo: Groups > New group, **Security**, `SSPRTesters`, descripción "Testers of SSPR rollout", **Assigned**, miembros Alex Wilber, Allan Deyoung, Bianca Pisani > **Create**.
   ![Página Groups con New group](https://learn.microsoft.com/en-us/entra/fundamentals/media/how-to-manage-groups/new-group.png)  Fuente: https://learn.microsoft.com/en-us/entra/fundamentals/how-to-manage-groups
8. **Password reset** > **Properties** > "Self service password reset enabled" en **Selected** > cambia SSPRSecurityGroupUsers por **SSPRTesters** > **Save**. Revisa Authentication methods, Registration, Notifications y Customization.
   ![SSPR en Selected con un grupo](https://learn.microsoft.com/en-us/entra/identity/authentication/media/tutorial-enable-sspr/enable-sspr-for-group-cropped.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-sspr
9. Registro: InPrivate a `https://aka.ms/ssprsetup` como AllanD, "More information required" > **Next** > registra Microsoft Authenticator con el QR > **Done**. Es el mismo tipo de prompt del paso 5.
10. Prueba: InPrivate a portal.azure.com como AllanD > **Forgot my password** > captcha > código de Authenticator > nuevo password > **Finish**.
    ![Página Get back into your account](https://learn.microsoft.com/en-us/entra/identity/authentication/media/tutorial-enable-sspr/password-reset-page.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-sspr
11. Control negativo: GradyA (no está en SSPRTesters) intenta **Forgot my password** y no puede.
    Sin captura oficial, candidato a captura en tenant.

**Trampas del lab:**
- Si **Security defaults** está activo, no puedes usar Conditional Access. Hay que apagarlo primero.
- No mezcles per-user MFA con políticas de CA. Learn lo desaconseja; per-user MFA es para tenants sin CA.
- En el portal SSPR solo acepta **un grupo**. Los admins siempre tienen SSPR con 2 métodos, así que prueba con un usuario no admin.
- El lab pide tener **Phone** como método de autenticación; sin registro previo, el usuario no puede resetear.

**Cómo lo preguntaría el examen:**
- Debes pedir MFA solo a un grupo piloto al entrar a Office 365, sin afectar al resto. ¿Qué usas: security defaults, per-user MFA o Conditional Access?
- Quieres habilitar SSPR para un piloto de 50 usuarios antes de ir a todo el tenant. ¿Qué opción eliges en Properties?
- Un usuario tiene per-user MFA en Enabled y todavía entra con apps legacy sin MFA. ¿Qué estado explica esto?

---

## Lab 5: Implement and test a Conditional Access policy (Lab 13)

**Skill del outline:** M2 > Conditional Access (assignments, controls, test and troubleshoot, session management).

**Objetivo en una línea:** existe `Block Sway for DebraB` (block access a Sway, al final queda en **Off**) y existe `Sign in frequency` para Grady Archie con Office 365, 30 **Days**, en **Report-only**.

**Ruta en el portal:** Entra ID > Conditional Access > Policies (y **What If** en la barra superior).

**Pasos (con imagen):**

1. InPrivate a office.com como DebraB, abre Apps > **Sway** y confirma que tiene acceso.
   Sin captura oficial, candidato a captura en tenant.
2. Conditional Access > **+ Create new policy**, name `Block Sway for DebraB`. Users or agents: **Select users and groups** > DebraB. Target resources: **Resources (formerly cloud apps)** > **Select resources** > **Sway**.
   ![Conditional Access, crear nueva política](https://learn.microsoft.com/en-us/entra/identity/authentication/media/tutorial-enable-azure-mfa/tutorial-enable-azure-mfa-conditional-access-menu-new-policy.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa
3. Access controls > **Grant** > **Block access** > **Select**. Enable policy **On** > **Create**.
   ![Panel Grant de una política de Conditional Access](https://learn.microsoft.com/en-us/entra/identity/conditional-access/media/concept-conditional-access-grant/conditional-access-grant.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-grant
4. InPrivate a `https://sway.cloud.microsoft` como DebraB: el acceso sale bloqueado. Si entra solo, cierra sesión, espera 1 minuto y repite.
   Sin captura oficial, candidato a captura en tenant (mensaje de bloqueo).
5. Vuelve a la política y ponla en **Off** > **Save**. Es el mismo toggle Enable policy del Lab 4, paso 4.
6. **What If**: Identity type **Users**, user **DebraB**, target **Cloud apps** > **Sway**, Device platform **Windows**, Client app **Browser** > **What If**. Lee "Policies that will apply" y "Policies that will not apply".
   ![Botón What If en Policies](https://learn.microsoft.com/en-us/entra/identity/conditional-access/media/what-if-tool/portal-showing-location-of-what-if-tool.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool
   ![Condiciones de What If](https://learn.microsoft.com/en-us/entra/identity/conditional-access/media/what-if-tool/supply-conditions-to-evaluate-in-the-what-if-tool.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool
   ![Resultado de What If](https://learn.microsoft.com/en-us/entra/identity/conditional-access/media/what-if-tool/conditional-access-what-if-evaluation-result-example.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/conditional-access/what-if-tool
7. Nueva política `Sign in frequency`: user **Grady Archie**, resources **Office 365**, Session > **Sign-in frequency** = `30` **Days**, Enable policy **Report-only** > **Create**.
   ![Session control Sign-in frequency](https://learn.microsoft.com/en-us/entra/identity/conditional-access/media/howto-conditional-access-session-lifetime/conditional-access-policy-session-sign-in-frequency.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/conditional-access/howto-conditional-access-session-lifetime

**Trampas del lab:**
- **Security defaults** activos bloquean el uso de CA. Apágalos antes.
- La sesión ya abierta no se re-evalúa al instante: cierra sesión, espera y vuelve a probar.
- What If solo evalúa políticas en **On** o **Report-only**, y pide identity, target resource, device platform y client app. Una política en Off no sale.
- Report-only no aplica nada; solo registra. Y "remember MFA on trusted devices" choca con Sign-in frequency.

**Cómo lo preguntaría el examen:**
- Debes bloquear una sola app para un solo usuario y confirmar el efecto antes de aplicarlo. ¿Qué modo y qué herramienta usas?
- Un usuario dice que una política no le aplica. ¿Qué herramienta te muestra qué políticas aplican y cuál condición falló?
- Los usuarios deben volver a autenticarse cada 30 días en Office 365. ¿Qué control de sesión configuras?

---

## Lab 6: User risk y sign-in risk policies (Lab 14)

**Skill del outline:** M2 > ID Protection (implement and manage user risk y sign-in risk con Conditional Access).

**Objetivo en una línea:** existen `User Risk Remediation` (All users menos MOD Administrator, All resources, user risk **High**, **Require risk remediation**, On) y `Sign-in Risk Policy` (sign-in risk **High**, **Require multifactor authentication**, On).

**Ruta en el portal:** Entra ID > Conditional Access > + Create new policy > Conditions > User risk / Sign-in risk.

**Pasos (con imagen):**

1. **+ Create new policy**, name `User Risk Remediation`. Users: **All users**, Exclude **MOD Administrator**. Target resources: **All resources (formerly 'All cloud apps')**.
2. Conditions > **User risk** > Configure **Yes** > **High** > **Done**.
   ![Condición User risk en una política](https://learn.microsoft.com/en-us/entra/identity/authentication/media/howto-mfa-mfasettings/risk-based-conditional-access.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/howto-mfa-mfasettings
3. Grant > **Grant access** > **Require risk remediation** ("Require all the selected controls"). Enable policy **On** > **Create**.
   Sin captura oficial, candidato a captura en tenant (Grant con Require risk remediation).
4. Segunda política `Sign-in Risk Policy`: All users, excluye MOD Administrator, All resources. Conditions > **Sign-in risk** > **Yes** > **High** > **Done**.
   ![Política con condiciones de riesgo](https://learn.microsoft.com/en-us/entra/id-protection/media/howto-identity-protection-configure-risk-policies/sign-in-risk-conditions.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-protection/howto-identity-protection-configure-risk-policies
5. Grant > **Grant access** > **Require multifactor authentication** > **Select**. Enable policy **On** > **Create**.
   ![Require multifactor authentication](https://learn.microsoft.com/en-us/entra/identity/authentication/media/tutorial-enable-azure-mfa/tutorial-enable-azure-mfa-conditional-access-select-require-mfa.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/authentication/tutorial-enable-azure-mfa

**Trampas del lab:**
- Las condiciones de riesgo necesitan **P2** (o Entra Suite). Sin P2 no aparecen o no aplican.
- No combines user risk y sign-in risk en la misma política. Van en políticas separadas.
- **Require risk remediation** agrega solo "Require authentication strength" y **Sign-in frequency: Every time**. Además, los usuarios deben tener MFA registrado antes; si no, quedan bloqueados.
- Excluye siempre la cuenta break-glass (en el lab, MOD Administrator). Ojo: las risk policies legacy de ID Protection se retiran el **1 de octubre de 2026**; lo vigente es hacerlas en Conditional Access.

**Cómo lo preguntaría el examen:**
- Cuando un usuario tenga riesgo alto, debe remediar solo y el evento de riesgo debe cerrarse. ¿Qué condición y qué grant control usas?
- Un inicio de sesión con riesgo medio o alto debe pedir una prueba fuerte de identidad, sin bloquear. ¿Qué configuras?
- Tu tenant tiene las risk policies antiguas en ID Protection. ¿Qué haces antes de su retiro?

---

## Lab 7: Register an application + tenant-wide admin consent (Lab 19 + Lab 21)

**Skill del outline:** M3 > App registrations (create, configure app authentication, API permissions y scopes). M3 > Enterprise applications (user y admin consent). M1 > custom roles.

**Objetivo en una línea:** existe `Demo app` con redirect URI Web `https://localhost`, un client secret `SC300 lab secret`, Application ID URI `api://DemoAppAPI` con scopes `Employees.Read.All` y `Employees.Write.All`, existe el custom role `My custom app role`, y la app tiene **admin consent** otorgado a nivel tenant.

**Ruta en el portal:** Entra ID > App registrations, Entra ID > Roles & admins > New custom role, Entra ID > Enterprise apps > Demo app > Security > Permissions.

**Pasos (con imagen):**

1. App registrations > **+ New registration** > name `Demo app`, valores por defecto, sin redirect URI > **Register**.
   Sin captura oficial, candidato a captura en tenant (la página de Learn "Register an application" no trae captura del formulario).
2. Demo app > **Authentication** > **+ Add Redirect URI** > plataforma **Web** > `https://localhost` > **Configure**.
   Sin captura oficial, candidato a captura en tenant.
3. **Certificates & secrets** > **+ New client secret** > descripción `SC300 lab secret`, duración **90 days (3 months)** > **Add**. Copia el **Value** ya, solo se ve una vez.
   ![Client secrets en Certificates & secrets](https://learn.microsoft.com/en-us/entra/identity-platform/media/quickstart-register-app/add-client-secret.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials
4. **Expose an API** > Application ID URI `api://DemoAppAPI` > **Save and continue** > **+ Add a scope**: `Employees.Read.All`, Who can consent **Admins and users**, llena los display names y descriptions, State **Enabled** > **Add scope**.
   ![Pane Expose an API con Add a scope](https://learn.microsoft.com/en-us/entra/identity-platform/media/quickstart-configure-app-expose-web-apis/portal-02-expose-api.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-expose-web-apis
5. Segundo scope `Employees.Write.All`, Who can consent **Admins only**, user consent vacío, **Enabled** > **Add scope**. Al final ves los dos scopes.
   ![Expose an API con dos scopes](https://learn.microsoft.com/en-us/entra/identity-platform/media/quickstart-configure-app-expose-web-apis/portal-03-scopes-list.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-expose-web-apis
6. Roles & admins > **+ New custom role** > name `My custom app role` > **Next** > busca "credentials" y marca `microsoft.directory/servicePrincipals/managePasswordSingleSignOnCredentials` y `microsoft.directory/servicePrincipals/synchronizationCredentials/manage` > **Next** > **Create**. (La captura de Learn muestra otros permisos de ejemplo, la pantalla es la misma.)
   ![Pestaña Basics del custom role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/media/custom-create/basics-tab.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-create
   ![Pestaña Permissions del custom role](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/media/custom-create/permissions-tab.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-create
7. Admin consent desde App registrations: **All applications** > Demo app, copia Application (client) ID y Directory (tenant) ID > **API permissions** > **Grant admin consent** > **Yes**.
   Sin captura oficial, candidato a captura en tenant.
8. Admin consent desde Enterprise apps: Demo app > **Security** > **Permissions** > **Grant admin consent** > inicia sesión como admin > **Accept**.
   ![Permissions con Grant admin consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/media/grant-tenant-wide-admin-consent/grant-tenant-wide-admin-consent.png)  Fuente: https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent

**Trampas del lab:**
- El client secret **Value** solo se muestra una vez. Si no lo copias, creas otro.
- Grant admin consent desde App registrations puede **revocar** permisos otorgados antes a nivel tenant (el lab lo advierte).
- Quién puede dar consent: Privileged Role Administrator para cualquier permiso; Cloud Application Administrator y Application Administrator para todo menos Microsoft Graph app roles (application permissions).
- Custom roles necesitan **P1** y solo aceptan permisos habilitados para custom roles. El Lab 21 necesita que Demo app del Lab 19 ya exista.

**Cómo lo preguntaría el examen:**
- Una API interna debe exponer un permiso de escritura que solo un admin pueda aprobar. ¿Qué valor pones en Who can consent?
- Los usuarios no pueden dar consent a una app y ves "Need admin approval". ¿Qué rol de menor privilegio otorga consent para permisos delegados?
- Un equipo solo debe gestionar credenciales de las apps, no crearlas ni borrarlas. ¿Qué creas y con qué scope lo asignas?

---

## Lab 8: Catalog en entitlement management (Lab 22)

**Skill del outline:** M4 > Entitlement management (create and configure catalogs). M4 > Access reviews (review de guests).

**Objetivo en una línea:** existe el catalog `Marketing` (Enabled **Yes**, Enabled for external users **No**) con Retail, Box, Salesforce y el sitio Brand como recursos, Adele Vance es catalog owner, y existe un access review de guests en todos los grupos Microsoft 365.

**Ruta en el portal:** ID Governance > Entitlement management > Catalogs. ID Governance > Access reviews.

**Pasos (con imagen):**

1. ID Governance > **Catalogs** > **+ New catalog**: Name `Marketing`, Description "For marketing department users", **Enabled** Yes, **Enabled for external users** No > **Create**.
   ![Lista de catalogs](https://learn.microsoft.com/en-us/entra/id-governance/media/entitlement-management-catalog-create/catalogs.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create
   ![Pane New catalog](https://learn.microsoft.com/en-us/entra/id-governance/media/entitlement-management-shared/new-catalog.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create
2. Marketing > **Resources** > **+ Add resources**: Groups and Teams **Retail**, Applications **Box** y **Salesforce**, SharePoint sites **Brand** > **Add**.
   ![Add resources to a catalog](https://learn.microsoft.com/en-us/entra/id-governance/media/entitlement-management-catalog-create/catalog-add-resources.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create
3. **Roles and administrators** > **+ Add catalog owner** > **Adele Vance** > **Select**.
   ![Roles and administrators del catalog](https://learn.microsoft.com/en-us/entra/id-governance/media/entitlement-management-shared/catalog-roles-administrators.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create
4. **Overview** > **Edit** > Enabled **Yes** > **Save**.
   ![Editar catalog](https://learn.microsoft.com/en-us/entra/id-governance/media/entitlement-management-shared/catalog-edit.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-catalog-create
5. ID Governance > **Access reviews** > **+ New access review** > **Teams + Groups** > Review scope **All Microsoft 365 groups with guest users** > Scope **Guest users only**.
   ![Select what to review](https://learn.microsoft.com/en-us/entra/id-governance/media/create-access-review/select-what-review.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/create-access-review
   ![Opciones de Teams + Groups](https://learn.microsoft.com/en-us/entra/id-governance/media/create-access-review/teams-groups.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/create-access-review
6. **Next: Reviews** > reviewers **Group owner(s)**, Duration **3**, recurrence y start date. En settings marca **Auto apply results to resource** e **If reviewers don't respond** = **Remove access** > **Review + create** > **Create**.
   ![Upon completion settings](https://learn.microsoft.com/en-us/entra/id-governance/media/create-access-review/upon-completion-settings-new.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/create-access-review
7. Catalog Marketing > Overview > **Delete** > en el diálogo elige **No** (se conserva para el siguiente lab).
   Sin captura oficial, candidato a captura en tenant.

**Trampas del lab:**
- Licencia: Learn pide **Microsoft Entra ID Governance** (algunas capacidades con P2), aunque el lab viejo diga P1.
- Rol: hoy se usa **Identity Governance Administrator**; User Administrator ya no puede crear catalogs ni gestionar access packages de catalogs ajenos.
- Solo sirven grupos creados en la nube. Grupos sincronizados de AD on-prem y distribution groups de Exchange no se pueden agregar. La búsqueda de sitios SharePoint distingue mayúsculas.
- No puedes borrar un catalog que tenga access packages. Y Auto apply + Remove access puede quitar acceso a todos si nadie revisa.

**Cómo lo preguntaría el examen:**
- Un gerente de Marketing debe administrar los recursos de su área sin ser admin global. ¿Qué rol de entitlement management le das?
- Quieres agrupar un grupo, dos apps y un sitio SharePoint para luego crear access packages. ¿Qué objeto creas primero?
- Debes revisar cada trimestre a todos los guests en grupos de Microsoft 365, con los owners como revisores. ¿Qué scope eliges?

---

## Lab 9: Access reviews (Lab 25)

**Skill del outline:** M4 > Access reviews (plan, create and configure access reviews).

**Objetivo en una línea:** existe el access review `SC300 Access Review Test` sobre el grupo **Sales and Marketing**, scope All users, revisor **Alex Wilber**, recurrencia **Annually**.

**Ruta en el portal:** ID Governance > Access reviews > + New access review.

**Pasos (con imagen):**

1. ID Governance > **Access reviews** > **+ New access review**.
   ![Pane de Access reviews](https://learn.microsoft.com/en-us/entra/id-governance/media/create-access-review/access-reviews.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/create-access-review
2. En los templates, **Select** en el tile de revisión de recursos (Review access to a resource type).
   ![Templates de access review](https://learn.microsoft.com/en-us/entra/id-governance/media/catalog-access-reviews/access-review-templates.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/create-access-review
3. Select what to review **Teams + Groups** > Review scope **Select Teams + groups** > **+ Select group(s)** > **Sales and Marketing** > Scope **All users** > **Next: Reviews**. Misma pantalla que el Lab 8, paso 5.
4. Specify reviewers **Selected user(s) or group(s)** > **+ Select reviewers** > **Alex Wilber**.
   ![Pestaña Reviews con reviewers](https://learn.microsoft.com/en-us/entra/id-governance/media/create-access-review/new-access-review.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/create-access-review
5. Duration y Start date por defecto, Review recurrence **Annually** > **Next: Settings**.
   ![Recurrencia del review](https://learn.microsoft.com/en-us/entra/id-governance/media/create-access-review/frequency.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/create-access-review
6. En Settings deja los defaults (Upon completion, decision helpers, advanced) > **Next: Review + Create**. Misma pantalla de Upon completion del Lab 8, paso 6.
7. Name `SC300 Access Review Test` > **Create**.
   ![Pestaña Review + Create](https://learn.microsoft.com/en-us/entra/id-governance/media/create-access-review/create-review.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/create-access-review

**Trampas del lab:**
- Licencia **Governance** para miembros que revisan o son revisados (algunas capacidades con P2).
- Si seleccionas varios grupos, se crean varios access reviews, uno por grupo.
- El start time puede variar unas horas. Los revisores reciben email al iniciar; un guest revisor debe aceptar antes la invitación al tenant.
- "Group owner(s)" solo existe para reviews de grupos; con Managers of users o Group owner(s) puedes poner **fallback reviewers**.

**Cómo lo preguntaría el examen:**
- Cada año el dueño del negocio debe confirmar quién sigue en un grupo sensible y los rechazados deben salir solos. ¿Qué dos settings activas?
- Quieres que los usuarios sin sign-in en 30 días salgan recomendados para deny. ¿Qué opción de decision helpers usas?
- Los owners de grupos deben poder crear sus propios reviews. ¿Dónde lo habilitas?

---

## Lab 10: PIM para Microsoft Entra roles (Lab 26)

**Skill del outline:** M4 > Privileged access (PIM para Entra roles: settings y assignments, request y approval).

**Objetivo en una línea:** el rol **Compliance Administrator** pide **approval** para activarse (aprobador: tu admin); Miriam Graham fue **Eligible**, lo activó con justificación, y al final la asignación se quitó.

**Ruta en el portal:** ID Governance > Privileged Identity Management > Microsoft Entra roles (Roles, Settings, Assignments, My roles).

**Pasos (con imagen):**

1. PIM > **Microsoft Entra roles** > **Settings** (o Roles > rol > Role settings) > busca "compliance" > **Compliance Administrator**.
   ![Lista de roles en PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/media/pim-how-to-change-default-settings/role-settings.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings
2. **Edit** > marca **Require approval to activate** > **Select approvers** > tu admin > **Update**.
   ![Role settings con Edit](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/media/pim-how-to-change-default-settings/role-settings-edit.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings
   Checkbox Require approval to activate y Select approvers: sin captura oficial, candidato a captura en tenant.
3. **Roles** > **+ Add assignments** > Select role **Compliance Administrator** > member **Miriam Graham** > **Next** > en Settings revisa Assignment type (**Eligible** o **Active**) > **Assign**.
   ![Roles con Add assignments](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/media/pim-how-to-add-role-to-user/roles-list.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user
   ![Seleccionar rol en la asignación](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/media/pim-how-to-add-role-to-user/select-role.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user
   ![Membership settings con fechas](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/media/pim-how-to-add-role-to-user/start-and-end-dates.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user
4. InPrivate como MiriamG: Users > Miriam Graham > **Assigned roles** > pestaña **Eligible assignments** muestra Compliance Administrator.
   Sin captura oficial, candidato a captura en tenant.
5. Miriam: PIM > **My roles** > Compliance Administrator > **Activate** > **Additional verification required** (MFA) > justificación "This is my justification for activating this role" > **Activate**.
   ![My roles en PIM](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/media/pim-how-to-activate-role/my-roles.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-activate-role
   ![Link Activate en eligible roles](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/media/pim-how-to-activate-role/activate-link.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-activate-role
   ![Pane Activate con duración y scope](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/media/pim-how-to-activate-role/activate-page.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-activate-role
6. Scope restringido: como admin, Roles > **+ Add assignments** > **User administrator** > revisa **Scope type** (Directory o Administrative unit) > **Cancel**.
   ![Selección de scope en la asignación](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/media/pim-how-to-add-role-to-user/add-scope.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user
7. **Assignments** > Compliance Administrator > columna Action: **Update** (revisa Membership settings) y luego **Remove** > **Yes**.
   ![Update o Remove de una asignación](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/media/pim-how-to-add-role-to-user/remove-update-assignments.png)  Fuente: https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user

**Trampas del lab:**
- Con **Require approval to activate**, la activación de Miriam queda **pendiente** hasta que el aprobador la apruebe. No es un error.
- **Eligible** necesita activación; **Active** da el permiso de inmediato. Una asignación no se puede quitar en los primeros 5 minutos.
- Miriam debe poder hacer MFA; si no tiene método registrado, se atora en Additional verification required.
- Riesgo de lockout: approval requerido, sin aprobadores y todos los admins solo eligible. Por eso existen las cuentas break-glass.

**Cómo lo preguntaría el examen:**
- Los admins de Compliance deben tener el rol solo cuando lo necesitan, con MFA y aprobación de seguridad. ¿Qué tipo de asignación y qué settings configuras?
- Un Helpdesk admin solo debe resetear passwords de una sucursal. ¿Qué scope usas al asignar el rol?
- Un usuario dice que activó su rol pero no tiene permisos. ¿Qué revisas primero en My requests?

---

## Faltan por capturar

Pasos sin captura oficial en Microsoft Learn. El presentador puede capturarlos en su tenant.

| ID | Lab | Paso que falta |
|---|---|---|
| L1-P2 | Lab 1 (Lab 01) | Chris Green en Enterprise applications sin **Create your own application** |
| L1-P4 | Lab 1 (Lab 01) | Chris Green con **Create your own application** y **Create** disponibles |
| L1-P7 | Lab 1 (Lab 01) | Consola PowerShell con `Connect-MgGraph` y `New-MgUser` |
| L1-P8 | Lab 1 (Lab 01) | **Deleted users** > **Restore user** |
| L1-P9 | Lab 1 (Lab 01) | Microsoft 365 admin center, asignar Windows 10/11 Enterprise E3 a Raul Razo y verlo en Licenses |
| L2-P1 | Lab 2 (Lab 03) | Delia Dennis sin licencia en m365.cloud.microsoft/apps |
| L2-P3 | Lab 2 (Lab 03) | Microsoft 365 admin center, Billing > Licenses > Office 365 E3 > Assign licenses al grupo |
| L2-P4 | Lab 2 (Lab 03) | Grupo sg-SC300-O365 > Licenses con Office 365 E3 |
| L3-P8 | Lab 3 (Lab 05) | Consola PowerShell con `New-MgInvitation` |
| L4-P1 | Lab 4 (Lab 08) | Additional cloud-based multifactor authentication settings (service settings legacy) |
| L4-P11 | Lab 4 (Lab 09) | GradyA intentando Forgot my password sin estar en SSPRTesters |
| L5-P1 | Lab 5 (Lab 13) | DebraB abriendo Sway antes de la política |
| L5-P4 | Lab 5 (Lab 13) | Mensaje de acceso bloqueado en sway.cloud.microsoft |
| L6-P3 | Lab 6 (Lab 14) | Grant con **Require risk remediation** (y los controles que agrega solo) |
| L7-P1 | Lab 7 (Lab 19) | Formulario **New registration** de Demo app |
| L7-P2 | Lab 7 (Lab 19) | Authentication > Add Redirect URI > Web `https://localhost` |
| L7-P7 | Lab 7 (Lab 21) | App registrations > API permissions > **Grant admin consent** |
| L8-P7 | Lab 8 (Lab 22) | Delete del catalog y diálogo (responder **No**) |
| L10-P2 | Lab 10 (Lab 26) | Edit role setting con **Require approval to activate** y **Select approvers** |
| L10-P4 | Lab 10 (Lab 26) | Miriam Graham > Assigned roles > **Eligible assignments** |
