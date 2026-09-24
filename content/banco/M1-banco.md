# M1 Banco de preguntas: Implement and manage user identities (20 a 25%)

40 preguntas originales, escritas para SC-300 Tips and Tricks con base en Microsoft Learn. No vienen de dumps ni de preguntas filtradas. Las preguntas y opciones están en inglés (el idioma del examen) y las explicaciones en español.

Cómo usarlo:
- Contesta primero sin ver la respuesta. Luego lee el "por qué las otras no": ahí está el valor.
- En las series Yes/No, **cada afirmación se evalúa sola**. En el examen real no puedes regresar a ellas.
- En drag/order solo cuentan las acciones que sí van, en el orden correcto.

| Subdominio | Preguntas |
|---|---|
| Configure and manage a Microsoft Entra tenant | Q1 a Q10 |
| Create, configure, and manage identities | Q11 a Q20 |
| External users and tenants | Q21 a Q30 (Q29 y Q30 son el case study 1) |
| Hybrid identity | Q31 a Q40 (Q39 y Q40 son el case study 2) |

| Formato | Cantidad | Preguntas |
|---|---|---|
| Multiple choice (una respuesta) | 22 | Q1, Q2, Q4, Q5, Q7, Q11, Q12, Q13, Q15, Q18, Q20, Q21, Q25, Q27, Q28, Q29, Q30, Q31, Q33, Q35, Q37, Q39 |
| Yes/No series | 9 | Q3, Q8, Q10, Q14, Q19, Q22, Q24, Q32, Q36 |
| Drag/order | 4 | Q6, Q17, Q26, Q38 |
| Select two | 5 | Q9, Q16, Q23, Q34, Q40 |
| Case study (dentro de los formatos anteriores) | 2 casos, 4 preguntas | Q29 y Q30, Q39 y Q40 |

---

## Subdominio 1: Configure and manage a Microsoft Entra tenant

### Q1 · Configure and manage built-in and custom Microsoft Entra roles · Multiple choice

Contoso has 20,000 users. The service desk team must be able to reset passwords for users who have no administrative role and for other service desk members who hold the Helpdesk Administrator role. The team must NOT be able to reset passwords for users who hold the User Administrator role.

You need to assign a Microsoft Entra built-in role to the team. The solution must follow the principle of least privilege.

Which role should you assign?

A. Password Administrator
B. Helpdesk Administrator
C. User Administrator
D. Authentication Administrator

**Respuesta:** B

**Por qué es correcta:** En la matriz "Who can reset passwords", el Helpdesk Administrator puede resetear a usuarios sin rol y a otros Helpdesk Administrators, pero no a User Administrators. Cumple el requisito exacto y es el rol más chico que alcanza.

**Por qué las otras no:**
- A. Password Administrator solo resetea a non-admins, Directory Readers, Guest Inviter y otros Password Admins. **No puede resetear a un Helpdesk Administrator.**
- C. User Administrator sí resetea Helpdesk Admins, pero también a otros User Admins y administra usuarios y grupos completos. Rompe el requisito y no es least privilege.
- D. Authentication Administrator suena a "passwords", pero en la matriz no puede resetear a un Helpdesk Administrator. Su foco son los métodos de autenticación.

**Fuente:** https://learn.microsoft.com/entra/identity/role-based-access-control/privileged-roles-permissions#who-can-reset-passwords

---

### Q2 · Configure and manage built-in and custom Microsoft Entra roles · Multiple choice

Contoso has an app registration named Payroll-API. Five developers must be able to update only the credentials (secrets and certificates) and the basic properties of Payroll-API. They must not be able to modify any other app registration. You must use Microsoft Entra role-based access control, and the solution must follow the principle of least privilege.

What should you do?

A. Assign the Application Administrator built-in role at tenant scope.
B. Create a custom role that contains `microsoft.directory/applications/credentials/update` and `microsoft.directory/applications/basic/update`, and assign it at the scope of the Payroll-API app registration.
C. Clone the Cloud Application Administrator built-in role, remove the permissions you don't need, and assign the clone at tenant scope.
D. Assign the Application Developer built-in role at tenant scope.

**Respuesta:** B

**Por qué es correcta:** Un custom role son dos pasos: la definición (lista de permisos) y la asignación con scope. Learn usa justo esos dos permisos como ejemplo y dice que el custom role se puede asignar a nivel directorio o a nivel de una app registration. Ojo: cada usuario con custom role necesita **licencia Microsoft Entra ID P1**.

**Por qué las otras no:**
- A. Application Administrator a nivel tenant les da control sobre todas las apps. Demasiado privilegio.
- C. **No puedes clonar un rol built-in**, solo un custom role. Además, el scope de tenant les daría acceso a todas las app registrations.
- D. Application Developer sirve para que alguien pueda crear app registrations cuando ese permiso está apagado para usuarios. No da permisos sobre Payroll-API.

**Fuente:** https://learn.microsoft.com/entra/identity/role-based-access-control/custom-create#create-a-custom-role

---

### Q3 · Recommend when to use administrative units · Yes/No series

Contoso creates an administrative unit named Seattle-AU. An administrator adds the security group SEA-Sales to Seattle-AU. The 40 members of SEA-Sales are NOT added individually to the administrative unit. Anna is assigned the User Administrator role scoped to Seattle-AU.

For each of the following statements, select Yes or No.

1. Anna can change the name of the SEA-Sales group.
2. Anna can reset the password of a member of SEA-Sales.
3. Anna can create an administrative unit named Seattle-Downtown inside Seattle-AU to delegate a smaller area.

**Respuesta:** 1 = Yes, 2 = No, 3 = No

**Por qué es correcta:**
- 1 Yes. Un User Administrator con scope de AU puede cambiar el nombre y la membresía de un grupo que está dentro del AU.
- 2 No. Meter el grupo al AU mete **al grupo, no a sus miembros**. Para resetear passwords, los usuarios tienen que estar agregados directo al AU.
- 3 No. **Los AUs no se pueden anidar.** Además, crear AUs lo hace un Privileged Role Administrator, no un User Admin con scope.

**Por qué las otras no:**
- La trampa de la 2 es pensar que el AU "hereda" a los miembros del grupo.
- La trampa de la 3 es pensar en AUs como OUs de Active Directory, que sí se anidan.

**Fuente:** https://learn.microsoft.com/entra/identity/role-based-access-control/administrative-units#groups y https://learn.microsoft.com/entra/identity/role-based-access-control/administrative-units#constraints

---

### Q4 · Configure and manage administrative units · Multiple choice

Contoso must protect the CEO and CFO user accounts. The requirements are:

- Tenant-level Helpdesk Administrators and User Administrators must not be able to reset their passwords or change their properties.
- Only the ExecSupport team can manage the two accounts.
- Global Administrators must not be able to modify the accounts unless they explicitly assign themselves a role for that purpose, and that action must be auditable.
- You must not remove any existing tenant-level role assignments.

What should you do?

A. Create an administrative unit, add the two accounts, and assign ExecSupport the Helpdesk Administrator role scoped to the administrative unit.
B. Create a restricted management administrative unit, add the two accounts, and assign ExecSupport the required roles scoped to that administrative unit.
C. Add the two accounts to a role-assignable group so that only Privileged Authentication Administrators can reset their passwords.
D. Enable Privileged Identity Management for the Helpdesk Administrator and User Administrator roles and require approval for activation.

**Respuesta:** B

**Por qué es correcta:** Un restricted management AU bloquea cambios de cualquier admin con scope de tenant, **incluido el Global Admin**, salvo que tenga una asignación explícita en el scope de ese AU. El GA puede asignarse a sí mismo y eso queda en los audit logs. No hay que quitar roles a nadie.

**Por qué las otras no:**
- A. Un AU normal limita lo que hace el admin con scope, pero **no protege al objeto** de los admins de tenant. El Helpdesk de tenant sigue pudiendo resetear.
- C. El role-assignable group frena al Helpdesk, pero los Privileged Authentication Admins y GAs de tenant siguen pudiendo. No limita la gestión a ExecSupport.
- D. PIM controla cuándo y cómo se activa un rol, no sobre qué cuentas actúa.

**Fuente:** https://learn.microsoft.com/entra/identity/role-based-access-control/admin-units-restricted-management#who-can-modify-objects

---

### Q5 · Configure tenant properties, user settings, group settings, and device settings · Multiple choice

Contoso wants to stop all standard users from creating app registrations. Five developers must still be able to register new applications. The solution must follow the principle of least privilege.

What should you do?

A. Set "Users can register applications" to No, and assign the five developers the Application Developer role.
B. Set "Restrict access to Microsoft Entra admin center" to Yes, and assign the five developers the Global Reader role.
C. Set "Users can register applications" to No, and assign the five developers the Cloud Application Administrator role.
D. Keep the default user settings and create a Conditional Access policy that blocks the Windows Azure Service Management API for users who aren't developers.

**Respuesta:** A

**Por qué es correcta:** Learn lo dice literal: con "Users can register applications" en No, los usuarios ya no crean app registrations, y **devuelves el permiso a personas específicas con el rol Application Developer**.

**Por qué las otras no:**
- B. "Restrict access to Microsoft Entra admin center" **no es un control de seguridad**. No bloquea PowerShell ni Graph. Y Global Reader es solo lectura.
- C. Cloud Application Administrator funciona, pero da control sobre todas las apps. No es least privilege.
- D. Conditional Access controla el acceso a apps. No cambia el permiso por default de registrar aplicaciones.

**Fuente:** https://learn.microsoft.com/entra/fundamentals/users-default-permissions#restrict-member-users-default-permissions

---

### Q6 · Configure and manage administrative units · Drag/order

Contoso has a regional office in Lima. The role-assignable group LIM-Helpdesk must be able to reset passwords only for users who work in Lima. The users aren't in any administrative unit yet. When the role assignment is created, the scope must already contain the Lima users. You sign in as a Privileged Role Administrator.

Which four actions should you perform in sequence? (Two actions aren't used.)

A. Select Add assignments and select the LIM-Helpdesk group.
B. Create an administrative unit named Lima-AU.
C. From Roles & admins, assign the Helpdesk Administrator role to LIM-Helpdesk with Directory scope.
D. Inside Lima-AU, open Roles and administrators and select Helpdesk Administrator.
E. Add the Lima users to Lima-AU (manually, by CSV, or with a dynamic membership rule based on a user attribute).
F. Create a custom role by cloning Helpdesk Administrator and restrict it to Lima.

**Respuesta:** B, E, D, A

**Por qué es correcta:** Es el flujo de Learn: creas el AU, metes a los usuarios, entras al AU, abres Roles and administrators, eliges el rol y haces Add assignments. Un **role-assignable group sí puede recibir un rol con scope de AU**.

**Por qué las otras no:**
- C. Scope de Directory significa todo el tenant. Podrían resetear a cualquier non-admin de Contoso.
- F. No se puede clonar un built-in. Y el recorte por región se hace con el AU, no con el rol.
- Orden: si asignas el rol antes de meter a los usuarios, el scope estaría vacío cuando se crea la asignación y no cumple el requisito.

**Fuente:** https://learn.microsoft.com/entra/identity/role-based-access-control/manage-roles-portal#assign-roles-with-administrative-unit-scope

---

### Q7 · Evaluate effective permissions for Microsoft Entra roles · Multiple choice

Megan is a Global Administrator in Contoso's Microsoft Entra tenant. She signs in to the Azure portal and can't see any of the company's Azure subscriptions or virtual machines. For an audit, Megan must be able to assign Azure roles in every subscription and management group linked to the tenant, and then remove that access when she finishes.

What should Megan do first?

A. Assign herself the Privileged Role Administrator role in Microsoft Entra ID.
B. In Microsoft Entra ID > Properties, set Access management for Azure resources to Yes.
C. Add herself to a role-assignable group that has the Global Administrator role.
D. Create a Microsoft Entra custom role that includes Azure RBAC permissions.

**Respuesta:** B

**Por qué es correcta:** Entra roles y Azure RBAC son **sistemas separados**. Un GA no ve Azure por default, pero puede elevarse: el toggle le da User Access Administrator en el root scope (/), sobre todas las suscripciones y management groups. Es un setting por usuario y al terminar se regresa a No.

**Por qué las otras no:**
- A. Privileged Role Administrator administra roles de Entra, no roles de Azure.
- C. Ya es GA. Tener el mismo rol vía grupo no cambia su acceso a Azure.
- D. Los permisos de Entra y los de Azure no se mezclan en custom roles.

**Fuente:** https://learn.microsoft.com/azure/role-based-access-control/elevate-access-global-admin#how-does-elevated-access-work

---

### Q8 · Evaluate effective permissions for Microsoft Entra roles · Yes/No series

Tom holds the Helpdesk Administrator role at tenant scope. Consider these users:

- Lina holds the User Administrator role.
- Omar has no administrative role, but he is a member of a role-assignable group.
- Sara holds the Password Administrator role.

For each of the following statements, select Yes or No.

1. Tom can reset Lina's password.
2. Tom can reset Omar's password.
3. Tom can reset Sara's password.

**Respuesta:** 1 = No, 2 = No, 3 = Yes

**Por qué es correcta:**
- 1 No. Un Helpdesk Administrator no puede resetear a un User Administrator. Ese rol está "arriba" en la matriz.
- 2 No. Los miembros y owners de un role-assignable group **solo los resetea un Privileged Authentication Administrator o un Global Admin**, aunque no tengan rol propio.
- 3 Yes. El Helpdesk Administrator sí puede resetear a un Password Administrator.

**Por qué las otras no:**
- La trampa de la 2 es pensar "Omar no tiene rol, entonces es un usuario normal". Estar en un role-assignable group lo protege.
- La trampa de la 3 es pensar que cualquier rol admin está fuera del alcance del Helpdesk.

**Fuente:** https://learn.microsoft.com/entra/identity/role-based-access-control/privileged-roles-permissions#who-can-reset-passwords y https://learn.microsoft.com/entra/identity/role-based-access-control/groups-concept#how-are-role-assignable-groups-protected

---

### Q9 · Configure and manage domains in Microsoft Entra ID and Microsoft 365 · Select two

Contoso's tenant was created as contoso.onmicrosoft.com. You added contoso.com as a custom domain, but it shows as Unverified. New users created in the Microsoft Entra admin center must get contoso.com as the default domain suffix.

Which two actions should you perform? Each correct answer presents part of the solution.

A. At the DNS registrar, create the TXT (or MX) record shown in the admin center for contoso.com, and then select Verify.
B. After verification, select contoso.com and select Make primary.
C. Rename contoso.onmicrosoft.com to contoso.com.
D. Delete the contoso.onmicrosoft.com domain so that contoso.com becomes the only domain.
E. Configure contoso.com as a federated domain before you make it primary.

**Respuesta:** A y B

**Por qué es correcta:** Primero pruebas que el dominio es tuyo con el registro TXT o MX y Verify. Luego Make primary, porque **el primary es el dominio por default al crear usuarios**. Cambiar el primary no cambia el UPN de los usuarios que ya existen.

**Por qué las otras no:**
- C. **El dominio inicial onmicrosoft.com no se puede cambiar.**
- D. Tampoco se puede borrar el dominio inicial.
- E. Solo puede ser primary un dominio verificado que no esté federado.

**Fuente:** https://learn.microsoft.com/entra/fundamentals/add-custom-domain#add-your-dns-information-to-the-domain-registrar y https://learn.microsoft.com/entra/identity/users/domains-manage#set-the-primary-domain-name-for-your-microsoft-entra-organization

---

### Q10 · Configure Company branding settings · Yes/No series

Contoso configured company branding: a default sign-in experience with a banner logo, a background image, and sign-in page text, plus a customization for the Spanish browser language. Contoso employees use https://myapps.microsoft.com. Guest users from Fabrikam (another Microsoft Entra tenant) access Contoso resources through B2B collaboration.

For each of the following statements, select Yes or No.

1. Users whose browser language is Spanish see the Spanish customization instead of the default branding for the elements that were customized.
2. An employee who opens https://myapps.microsoft.com sees Contoso's branding on the first screen, before typing a username.
3. When Fabrikam guests perform a cross-tenant sign-in, they see the branding of their home tenant.

**Respuesta:** 1 = Yes, 2 = No, 3 = Yes

**Por qué es correcta:**
- 1 Yes. La customización por idioma del navegador **sobrescribe el branding default** en los elementos que cambiaste.
- 2 No. En apps multitenant como My Apps, el branding sale **después de escribir el correo** y dar Next. Para verlo desde el inicio se usa un hint como `https://myapps.microsoft.com/?whr=contoso.com`.
- 3 Yes. En B2B, el usuario ve el branding de su home tenant.

**Por qué las otras no:**
- La trampa de la 2 es pensar que el branding siempre sale en la primera pantalla.
- La trampa de la 3 es pensar que el guest ve el branding del tenant que lo invitó.

**Fuente:** https://learn.microsoft.com/entra/fundamentals/how-to-customize-branding#software-as-a-service-saas-and-multitenant-applications y https://learn.microsoft.com/entra/fundamentals/how-to-customize-branding#b2b-scenarios

---

## Subdominio 2: Create, configure, and manage Microsoft Entra identities

### Q11 · Automate bulk operations by using the Microsoft Entra admin center and PowerShell · Multiple choice

HR sends Contoso a spreadsheet with 450 new employees. You plan to use Bulk create in the Microsoft Entra admin center and you download the CSV template.

Which columns must have a value for every user for the upload to succeed?

A. Name, User name, Initial password, and Block sign in (Yes/No)
B. Name, User name, Usage location, and Department
C. Email address to invite and Redirection url
D. User name, Initial password, Usage location, and Manager

**Respuesta:** A

**Por qué es correcta:** En la plantilla de Bulk create **solo las primeras cuatro columnas son obligatorias**. El bulk create hace usuarios internos con el password del CSV y **no manda correos de invitación**. Deja intactas la fila de versión y los encabezados.

**Por qué las otras no:**
- B. Usage location y Department son opcionales en la plantilla. Usage location importa después para licencias directas, pero no para crear.
- C. Esas son las columnas de Bulk invite, que es para guests.
- D. Usage location y Manager no son obligatorios para crear el usuario.

**Fuente:** https://learn.microsoft.com/entra/identity/users/users-bulk-add#example-csv-file

---

### Q12 · Assign, modify, and report on licenses · Multiple choice

A PowerShell script creates 200 users with `New-MgUser` from a CSV file, and then runs `Set-MgUserLicense` to assign Microsoft 365 E5 directly to each user. The users are created, but the license assignment fails for all of them. The CSV contains UserPrincipalName, DisplayName, MailNickname, and Department.

What should you add to the `New-MgUser` command to fix the issue?

A. `-UsageLocation` with a two-letter ISO country code
B. `-Country` with the full country name
C. `-PreferredDataLocation`
D. `-UserType "Member"`

**Respuesta:** A

**Por qué es correcta:** Learn dice que **no puedes asignar una licencia a un usuario que no tiene UsageLocation** (código ISO 3166-1 alpha-2, por ejemplo US o MX). Dato extra: en group-based licensing, si el usuario no tiene ubicación, hereda la del tenant.

**Por qué las otras no:**
- B. Country es un dato de perfil. El requisito para licenciar es UsageLocation.
- C. PreferredDataLocation no tiene que ver con asignar licencias.
- D. UserType define la relación con la organización. No bloquea la licencia.

**Fuente:** https://learn.microsoft.com/microsoft-365/enterprise/create-user-accounts-with-microsoft-365-powershell#create-multiple-user-accounts y https://learn.microsoft.com/microsoft-365/admin/manage/manage-group-licenses

---

### Q13 · Create, configure, and manage groups · Multiple choice

Contoso uses Microsoft Entra ID Free. Users must be able to request membership to security groups from the My Groups portal, and group owners must approve or deny the requests. In Groups > General, "Owners can manage group membership requests in My Groups" is Yes and "Restrict user ability to access groups features in My Groups" is No. Users still can't request to join groups that require owner approval.

What should you do?

A. Purchase and assign Microsoft Entra ID P1 or P2 licenses.
B. Set "Users can create security groups in Azure portals, API or PowerShell" to Yes.
C. Convert the security groups to dynamic membership groups.
D. Make the security groups role-assignable.

**Respuesta:** A

**Por qué es correcta:** Learn: pedir unirse a un grupo y que el owner apruebe **requiere Microsoft Entra ID P1 o P2**. Sin P1, los usuarios manejan sus grupos pero no pueden crear grupos con aprobación ni pedir unirse.

**Por qué las otras no:**
- B. Ese setting controla quién crea grupos, no las solicitudes de membresía.
- C. En un grupo dinámico no se agregan miembros a mano ni por solicitud. La regla manda.
- D. Role-assignable es para asignar roles de Entra. Complica más la gestión y no habilita solicitudes.

**Fuente:** https://learn.microsoft.com/entra/identity/users/groups-self-service-management#make-a-group-available-for-user-self-service

---

### Q14 · Create, configure, and manage groups · Yes/No series

Contoso has Microsoft Entra ID P1. You configure a group expiration policy with a lifetime of 180 days, applied to All groups, and an alternate notification email for groups without owners.

For each of the following statements, select Yes or No.

1. A cloud security group that nobody has used for 200 days is deleted by this policy.
2. A Microsoft 365 group whose members regularly visit its Teams channel is renewed automatically, without any owner action.
3. If a Microsoft 365 group expires and is deleted, it can be restored within 30 days.

**Respuesta:** 1 = No, 2 = Yes, 3 = Yes

**Por qué es correcta:**
- 1 No. **La expiration policy solo aplica a Microsoft 365 groups.** "All" significa todos los M365 groups.
- 2 Yes. Hay renovación automática por actividad (Outlook, SharePoint, Teams, Viva Engage). Visitar un canal de Teams cuenta.
- 3 Yes. Un M365 group borrado se puede restaurar dentro de 30 días, y ese plazo no se cambia.

**Por qué las otras no:**
- La trampa de la 1 es leer "All" como "todos los grupos del tenant".
- En la 2, mucha gente cree que el owner siempre tiene que renovar a mano.

**Fuente:** https://learn.microsoft.com/entra/identity/users/groups-lifecycle#overview y https://learn.microsoft.com/entra/identity/users/groups-lifecycle#activity-based-automatic-renewal

---

### Q15 · Create, configure, and manage groups · Multiple choice

You need a dynamic membership security group that contains only member users (no guests) from the Sales or Marketing departments.

Which membership rule should you use?

A. `(user.department -in ["Sales","Marketing"]) -and (user.userType -eq "Member")`
B. `(user.department -eq "Sales") -or (user.department -eq "Marketing") -and (user.userType -eq "Member")`
C. `(user.department -in ["Sales","Marketing"]) -and (user.objectId -ne null)`
D. `(device.department -in ["Sales","Marketing"]) -and (user.userType -eq "Member")`

**Respuesta:** A

**Por qué es correcta:** `-in` compara contra una lista entre corchetes, y `-and (user.userType -eq "Member")` saca a los guests.

**Por qué las otras no:**
- B. **`-and` tiene más precedencia que `-or`**. Se evalúa como Sales OR (Marketing AND Member), así que entran los guests de Sales. Se arregla con paréntesis.
- C. `user.objectId -ne null` es la regla de "todos los usuarios" e incluye members y guests B2B.
- D. `device.` es para reglas de dispositivos. Una regla no puede mezclar users y devices.

**Fuente:** https://learn.microsoft.com/entra/identity/users/groups-dynamic-membership#operator-precedence y https://learn.microsoft.com/entra/identity/users/groups-dynamic-membership#create-a-rule-for-all-users

---

### Q16 · Manage device join and device registration in Microsoft Entra ID · Select two

You need a group that automatically contains all Windows devices that are Microsoft Entra hybrid joined. The group must update by itself when new hybrid joined Windows devices appear.

Which two actions should you perform? Each correct answer presents part of the solution.

A. Create a security group with the membership type set to Dynamic Device.
B. Build the rule in the rule builder by adding two expressions.
C. In the rule syntax text box, enter `(device.deviceOSType -eq "Windows") -and (device.deviceTrustType -eq "ServerAD")`.
D. Create a Microsoft 365 group with the membership type set to Dynamic Device.
E. In the rule syntax text box, enter `(device.deviceOSType -eq "Windows") -and (device.deviceTrustType -eq "AzureAD")`.

**Respuesta:** A y C

**Por qué es correcta:** Los devices solo van en security groups. En `deviceTrustType`, **AzureAD = joined, ServerAD = hybrid joined, Workplace = registered**. Hybrid joined es ServerAD.

**Por qué las otras no:**
- B. El rule builder solo sirve para reglas de usuarios. **Las reglas de devices se escriben en el text box.**
- D. Los Microsoft 365 groups solo aceptan usuarios.
- E. AzureAD son los equipos Microsoft Entra joined, no los hybrid.

**Fuente:** https://learn.microsoft.com/entra/identity/users/groups-dynamic-membership#rules-for-devices y https://learn.microsoft.com/entra/identity/users/groups-dynamic-membership#rule-builder-in-the-azure-portal

---

### Q17 · Assign, modify, and report on licenses · Drag/order

Contoso uses group-based licensing. The group LIC-E3 assigns Microsoft 365 E3 and the group LIC-E5 assigns Microsoft 365 E5. Pedro is moving to a role that needs E5. He must not lose access to licensed services at any point during the change.

Which three actions should you perform in sequence? (Two actions aren't used.)

A. Remove Pedro from LIC-E3.
B. Add Pedro to LIC-E5.
C. On Pedro's Licenses page, confirm that the E5 license is applied.
D. Assign E5 to Pedro directly, and then remove the direct assignment.
E. Remove Pedro from LIC-E3 and wait for the next license processing cycle before adding him to LIC-E5.

**Respuesta:** B, C, A

**Por qué es correcta:** Learn lo pide en ese orden: **primero agregas al grupo destino, confirmas que ya tiene la licencia nueva y al final lo quitas del grupo original**. Así no hay hueco sin licencia.

**Por qué las otras no:**
- D. Es trabajo manual extra y no es el flujo documentado.
- E. Si lo quitas primero, queda sin licencia hasta que se procese el grupo nuevo. En tenants grandes eso puede tardar.

**Fuente:** https://learn.microsoft.com/microsoft-365/admin/manage/manage-group-licenses#move-users-between-licensed-groups

---

### Q18 · Assign, modify, and report on licenses · Multiple choice

At Contoso, the group G-Frontline assigns Office 365 E1. You add Julia, who is a member of G-Frontline, to the group G-Knowledge, which assigns Office 365 E3. The admin center shows an error for Julia's E3 assignment from G-Knowledge. There are 150 unassigned E3 licenses, and Julia has a usage location.

What is the most likely cause of the error?

A. Conflicting service plans: Exchange Online (Plan 2) in E3 can't be assigned together with Exchange Online (Plan 1) in E1.
B. The E3 subscription doesn't have enough licenses.
C. G-Knowledge is nested inside G-Frontline, and group-based licensing doesn't support nested groups.
D. Julia's usage location doesn't allow Office 365 E3.

**Respuesta:** A

**Por qué es correcta:** Learn pone este caso como ejemplo: E1 y E3 juntos fallan porque **Exchange Online Plan 1 y Plan 2 son mutuamente excluyentes**. En group-based licensing sale como conflicto de service plans. En PowerShell sale como MutuallyExclusiveViolation. Se arregla sacándola de G-Frontline o apagando el plan en conflicto.

**Por qué las otras no:**
- B. El escenario dice que hay 150 licencias libres.
- C. Nada indica anidamiento. Y con grupos anidados el efecto es que los miembros de segundo nivel no reciben licencia, no un conflicto.
- D. Julia tiene usage location. Sería otro tipo de error.

**Fuente:** https://learn.microsoft.com/entra/identity/users/licensing-service-plan-reference#service-plans-that-cannot-be-assigned-at-the-same-time

---

### Q19 · Manage device join and device registration in Microsoft Entra ID · Yes/No series

Contoso has these device settings:

- Users may join devices to Microsoft Entra ID: Selected (group IT-Joiners)
- Require multifactor authentication to register or join devices with Microsoft Entra ID: No (a Conditional Access policy for the "Register or join devices" user action requires MFA)
- Maximum number of devices: 50

Contoso also uses Microsoft Entra Connect to make domain-joined Windows 11 PCs Microsoft Entra hybrid joined.

For each of the following statements, select Yes or No.

1. A domain-joined Windows 11 PC used by someone who isn't in IT-Joiners can still become Microsoft Entra hybrid joined.
2. A user who already has 50 Microsoft Entra registered devices can register one more personal phone.
3. If you disable a device in Microsoft Entra ID, the device's Primary Refresh Token (PRT) is revoked.

**Respuesta:** 1 = Yes, 2 = No, 3 = Yes

**Por qué es correcta:**
- 1 Yes. **"Users may join devices" no aplica a hybrid join**, solo a Microsoft Entra join en Windows 10 o posterior, macOS y Linux.
- 2 No. El límite cuenta devices joined o registered. Llegando a 50, tiene que borrar uno antes de agregar otro.
- 3 Yes. Deshabilitar un device revoca el PRT y los refresh tokens del equipo.

**Por qué las otras no:**
- La trampa de la 1 es pensar que el setting de join controla todos los tipos de join.
- La 2 prueba que el límite es duro. Además, ese límite no aplica a hybrid joined.

**Fuente:** https://learn.microsoft.com/entra/identity/devices/manage-device-identities#configure-device-settings y https://learn.microsoft.com/entra/identity/devices/manage-device-identities#enable-or-disable-a-microsoft-entra-device

---

### Q20 · Manage custom security attributes · Multiple choice

You are a Global Administrator at Contoso. The Attribute Definition Administrator created an attribute set named HR that contains an attribute named CostCenter. Five HR analysts must assign CostCenter values to users. They must not be able to assign attributes from other attribute sets or define new attributes. The solution must follow the principle of least privilege.

Which role should you assign to the five analysts?

A. Attribute Assignment Administrator, scoped to the HR attribute set
B. Attribute Definition Administrator, at tenant scope
C. User Administrator, at tenant scope
D. Attribute Assignment Reader, scoped to the HR attribute set

**Respuesta:** A

**Por qué es correcta:** Attribute Assignment Administrator es el rol mínimo para **asignar valores** de custom security attributes. Se puede asignar a nivel tenant o **a nivel de un attribute set**, y así se queda solo en HR.

**Por qué las otras no:**
- B. Definition Admin define atributos, no asigna valores. Y con scope de tenant ve todo.
- C. **Global Admin y los otros roles admin no tienen permisos de custom security attributes por default.** User Administrator no sirve.
- D. Reader solo lee, no asigna.

**Fuente:** https://learn.microsoft.com/entra/fundamentals/custom-security-attributes-overview#custom-security-attribute-roles

---

## Subdominio 3: Implement and manage identities for external users and tenants

### Q21 · Manage External collaboration settings in Microsoft Entra ID · Multiple choice

Contoso's policy says regular employees must not invite guest users, while administrators who hold specific roles can. Carla, a marketing coordinator with no administrative role, must be able to invite guests. The solution must follow the principle of least privilege.

What should you do?

A. Set Guest invite settings to "Only users assigned to specific admin roles can invite guest users," and assign Carla the Guest Inviter role.
B. Set Guest invite settings to "Member users and users assigned to specific admin roles can invite guest users including guests with member permissions."
C. Set Guest invite settings to "Only users assigned to specific admin roles can invite guest users," and assign Carla the User Administrator role.
D. Set Guest invite settings to "No one in the organization can invite guest users including admins," and assign Carla the Guest Inviter role.

**Respuesta:** A

**Por qué es correcta:** Con "Only users assigned to specific admin roles" solo invitan User Admins y Guest Inviters. **Guest Inviter sí puede invitar aunque ese setting esté activo**, y es el rol más chico para eso.

**Por qué las otras no:**
- B. Deja invitar a todos los members. Rompe la política.
- C. User Administrator funciona, pero es mucho más privilegio.
- D. "No one... including admins" bloquea a todos, incluido el Guest Inviter.

**Fuente:** https://learn.microsoft.com/entra/external-id/external-collaboration-settings-configure#to-configure-guest-invite-settings y https://learn.microsoft.com/entra/external-id/external-collaboration-settings-configure#assign-the-guest-inviter-role-to-a-user

---

### Q22 · Manage External collaboration settings in Microsoft Entra ID · Yes/No series

Contoso sets Collaboration restrictions to "Deny invitations to the specified domains" and adds gmail.com and outlook.com.

For each of the following statements, select Yes or No.

1. A gmail.com guest who redeemed an invitation last month can still access Contoso resources.
2. A gmail.com user whose invitation is still pending can redeem it after the policy is saved.
3. Contoso can also add an allow list that contains fabrikam.com to the same policy.

**Respuesta:** 1 = Yes, 2 = No, 3 = No

**Por qué es correcta:**
- 1 Yes. **La lista no aplica a usuarios que ya redimieron.** Se aplica de ahí en adelante.
- 2 No. Si la invitación estaba pendiente y bloqueas el dominio, la redención falla.
- 3 No. **Es allow list o block list, nunca las dos.** Y hay una sola política por organización.

**Por qué las otras no:**
- La trampa de la 1 es pensar que el block list "corre" a los guests existentes. Para eso tienes que quitarlos o bloquearlos aparte.
- La trampa de la 3 es querer combinar listas.

**Fuente:** https://learn.microsoft.com/entra/external-id/allow-deny-list#important-considerations

---

### Q23 · Invite external users, individually or in bulk · Select two

Contoso must invite 250 partner users as B2B guests with the least administrative effort. After redeeming the invitation, the guests must land on the My Apps portal.

Which two actions should you perform? Each correct answer presents part of the solution.

A. In Users, select Bulk operations > Bulk invite and download the CSV template.
B. In each row, set Email address to invite, and set Redirection url to https://myapplications.microsoft.com.
C. Use Bulk create and set the user type to Guest in the CSV.
D. Run `New-MgInvitation` for each address without the `-SendInvitationMessage` parameter, so that the default invitation email is sent.
E. Remove the version row from the CSV template before you upload it.

**Respuesta:** A y B

**Por qué es correcta:** Bulk invite es el camino de menor esfuerzo. Las columnas obligatorias son **Email address to invite y Redirection url**, y para caer en My Apps pones https://myapplications.microsoft.com (o myapps).

**Por qué las otras no:**
- C. **Bulk create hace usuarios internos con password y no manda invitaciones.**
- D. En `New-MgInvitation`, si no pones `-SendInvitationMessage`, **no se manda correo**. El default es no enviar.
- E. La fila de versión y los encabezados no se tocan o el archivo no se procesa.

**Fuente:** https://learn.microsoft.com/entra/external-id/tutorial-bulk-invite#invite-guest-users-in-bulk y https://learn.microsoft.com/entra/external-id/b2b-quickstart-invite-powershell#send-an-invitation

---

### Q24 · Manage external user accounts in Microsoft Entra ID · Yes/No series

Ana (ana@fabrikam.com) was invited to Contoso as a B2B guest two years ago. She belongs to five Contoso groups and has access to three apps. Ana now works for Litware, and her Fabrikam account was deleted. She must keep the same access in Contoso by using her new ana@litware.com account.

For each of the following statements, select Yes or No.

1. If you reset Ana's redemption status and invite ana@litware.com, her object ID, group memberships, and app assignments are kept.
2. If you change Ana's UserType from Guest to Member, she authenticates with Contoso credentials instead of an external account.
3. The Helpdesk Administrator role is enough to reset Ana's redemption status.

**Respuesta:** 1 = Yes, 2 = No, 3 = Yes

**Por qué es correcta:**
- 1 Yes. Reset redemption status existe justo para esto: **conserva object ID, grupos y app assignments** y deja que se autentique con otra cuenta. El UPN no cambia.
- 2 No. **UserType solo indica la relación con la organización, no dónde se autentica.** Para que sea interno de verdad se usa "Convert to internal user".
- 3 Yes. Learn marca a Helpdesk Administrator como el rol de menor privilegio para esto (también sirve User Administrator).

**Por qué las otras no:**
- La trampa de la 1 es la solución vieja: borrar al guest y reinvitar, que pierde todo.
- La trampa de la 2 es confundir Member con "cuenta interna".

**Fuente:** https://learn.microsoft.com/entra/external-id/reset-redemption-status#required-microsoft-entra-roles y https://learn.microsoft.com/entra/external-id/user-properties#user-type

---

### Q25 · Implement Cross-tenant access settings · Multiple choice

Contoso has a Conditional Access policy that requires MFA for all guest users. Users from Fabrikam (a Microsoft Entra tenant) already complete MFA in their home tenant and complain about a second MFA prompt in Contoso. Users from all other partner organizations must keep completing MFA in Contoso. Contoso has Microsoft Entra ID P1.

What should you do?

A. In Contoso's cross-tenant access default settings, configure the inbound trust settings to trust MFA from Microsoft Entra tenants.
B. In Contoso's cross-tenant access settings, add Fabrikam under Organizational settings and configure its inbound trust settings to trust MFA.
C. In Contoso's cross-tenant access settings, add Fabrikam under Organizational settings and configure its outbound settings to trust MFA.
D. Exclude guest users from the Conditional Access policy.

**Respuesta:** B

**Por qué es correcta:** Los trust settings son **inbound y viven en el tenant de recursos** (Contoso). Para que solo aplique a Fabrikam, lo agregas en Organizational settings, que **tienen prioridad sobre los default**. La política de MFA sigue aplicando, pero acepta el MFA que ya hizo en casa. Configurar trust requiere P1.

**Por qué las otras no:**
- A. El default aplica a todas las organizaciones externas. Rompe el requisito.
- C. Outbound controla a dónde van tus usuarios. El trust no vive ahí.
- D. Quita el MFA a todos los guests.

**Fuente:** https://learn.microsoft.com/entra/external-id/cross-tenant-access-overview#manage-external-access-with-inbound-and-outbound-settings y https://learn.microsoft.com/entra/external-id/cross-tenant-access-overview#organizational-settings

---

### Q26 · Implement and manage cross-tenant synchronization · Drag/order

Contoso (source tenant) must synchronize its internal users into Fabrikam (target tenant). Both tenants are in the Azure commercial cloud.

Which five actions should you perform in the sequence documented by Microsoft? (Two actions aren't used.)

A. In Fabrikam, add Contoso under Organizational settings and select Allow user synchronization into this tenant.
B. In Fabrikam, in the inbound trust settings for Contoso, select Automatically redeem invitations with the tenant.
C. In Contoso, add Fabrikam under Organizational settings and, in the outbound trust settings, select Automatically redeem invitations with the tenant.
D. In Contoso, create a cross-tenant synchronization configuration, enter Fabrikam's tenant ID, and select Test connection.
E. In Contoso, assign users or groups to the configuration, and then start provisioning.
F. In Fabrikam, create the cross-tenant synchronization configuration and the scoping filters.
G. In Fabrikam, send B2B invitations to the Contoso users by using Bulk invite.

**Respuesta:** A, B, C, D, E

**Por qué es correcta:** El target solo **abre la puerta** (inbound: allow sync + automatic redemption). **El source empuja todo lo demás**: automatic redemption outbound, crea la configuración, prueba la conexión, define el scope y arranca el provisioning. El Test connection falla si falta el automatic redemption en cualquiera de los dos lados.

**Por qué las otras no:**
- F. **Es push desde el source, no pull desde el target.** La configuración, el scope y los mappings viven en el source.
- G. La sincronización sustituye las invitaciones. Los usuarios sincronizados no reciben correo ni consent prompt.

**Fuente:** https://learn.microsoft.com/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure#step-4-automatically-redeem-invitations-in-the-source-tenant y https://learn.microsoft.com/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-overview#properties

---

### Q27 · Implement and manage cross-tenant synchronization · Multiple choice

In Contoso (source tenant), you create a cross-tenant synchronization configuration for Fabrikam. When you select Test connection, it fails with this message: "Error code: AzureActiveDirectoryCrossTenantSyncPolicyCheckFailure. Details: The source tenant has not enabled automatic user consent with the target tenant."

What should you do?

A. In Contoso, in the outbound trust settings for Fabrikam, select Automatically redeem invitations with the tenant.
B. In Fabrikam, select Allow user synchronization into this tenant for Contoso.
C. In Fabrikam, assign the Contoso administrator the Hybrid Identity Administrator role.
D. In Contoso, enable outbound B2B direct connect for Fabrikam.

**Respuesta:** A

**Por qué es correcta:** El mensaje dice "the source tenant" y "automatic user consent". Falta el **automatic redemption outbound en el source**.

**Por qué las otras no:**
- B. Ese setting vive en el target. El mensaje que apunta al target es otro ("The target tenant has not enabled inbound synchronization"). Este error nombra al source, así que lee bien cuál tenant menciona.
- C. Cada admin trabaja en su propio tenant. No hace falta un rol en el otro.
- D. B2B direct connect es para Teams shared channels. No tiene que ver con la sincronización.

**Fuente:** https://learn.microsoft.com/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure#symptom---test-connection-fails-with-azureactivedirectorycrosstenantsyncpolicycheckfailure

---

### Q28 · Configure external identity providers, including protocols such as SAML and WS-Fed · Multiple choice

Contoso wants users from the partner Tailwind Traders to redeem B2B invitations with their own corporate credentials. Tailwind uses a third-party SAML 2.0 identity provider, not Microsoft Entra ID. Tailwind users have email addresses in tailwindtraders.com. The IdP passive authentication endpoint is https://login.tailwind-idp.net/saml2.

What must happen for the federation to work?

A. Tailwind must add a DNS TXT record to tailwindtraders.com with the value `DirectFedAuthUrl=https://login.tailwind-idp.net/saml2`.
B. Contoso must add and verify tailwindtraders.com as a custom domain in its own tenant.
C. Tailwind must configure its IdP to send the NameID claim in transient format.
D. Contoso must add Tailwind under cross-tenant access Organizational settings and trust its MFA.

**Respuesta:** A

**Por qué es correcta:** El endpoint (tailwind-idp.net) no es el dominio tailwindtraders.com ni un host dentro de él. En ese caso **el partner agrega un TXT DirectFedAuthUrl** en su DNS. Del lado de Contoso, el IdP se agrega en All identity providers > Custom > SAML/WS-Fed y conviene poner la metadata URL para que el certificado se renueve solo.

**Por qué las otras no:**
- B. El dominio del partner no debe estar verificado en el tenant de Contoso. Es un dominio de Tailwind.
- C. SAML requiere **NameID persistent** y el claim de emailaddress.
- D. Cross-tenant access settings son para organizaciones que usan Microsoft Entra ID. Tailwind no lo usa.

**Fuente:** https://learn.microsoft.com/entra/external-id/direct-federation#step-1-determine-if-the-partner-needs-to-update-their-dns-text-records y https://learn.microsoft.com/entra/external-id/direct-federation#to-configure-a-saml-20-identity-provider

---

### Case study 1: Northwind Group (usar para Q29 y Q30)

Northwind Group owns three Microsoft Entra tenants in the Azure commercial cloud: NW-HQ, NW-Retail, and NW-Labs. All employees are homed in NW-HQ, which has Microsoft Entra ID P1 licenses for every user. NW-Retail and NW-Labs have no premium licenses.

Business requirements:
- HQ employees must get accounts in NW-Retail and NW-Labs automatically, with member-level access, and without invitation emails or consent prompts.
- When an employee leaves HQ or moves out of scope, the account in the other tenants must be removed automatically.
- NW-Retail and NW-Labs administrators must be able to stop the synchronization at any time.
- Administrative effort must be minimized.

Technical note: after an old hardening project, NW-Labs has Guest invite settings set to "No one in the organization can invite guest users including admins (most restrictive)."

### Q29 · Implement and manage cross-tenant synchronization · Case study (Multiple choice)

Refer to Case study 1. Which solution meets the requirements for NW-Retail?

A. In NW-HQ, configure cross-tenant synchronization to NW-Retail, enable automatic redemption in both tenants, and keep the default userType mapping of Member.
B. In NW-Retail, configure cross-tenant synchronization that pulls users from NW-HQ.
C. In NW-Retail, bulk invite the HQ users every week with a CSV export from NW-HQ, and set their UserType to Member.
D. Configure B2B direct connect between NW-HQ and NW-Retail.

**Respuesta:** A

**Por qué es correcta:** Cross-tenant sync crea, actualiza y **borra (soft delete) automáticamente** a los usuarios cuando salen del scope. Con automatic redemption en ambos lados no hay correo ni consent prompt. **Por default se crean como external member** (userType Member). La licencia P1 solo se necesita en el source (NW-HQ), y el target puede frenar la sync cuando quiera quitando el inbound.

**Por qué las otras no:**
- B. No existe el pull. **Es push desde el source.**
- C. Mucho esfuerzo manual, manda invitaciones y no borra solo.
- D. B2B direct connect no crea cuentas en el directorio. Se usa para Teams shared channels.

**Fuente:** https://learn.microsoft.com/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-overview#properties y https://learn.microsoft.com/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure#step-9-review-attribute-mappings

---

### Q30 · Implement and manage cross-tenant synchronization · Case study (Multiple choice)

Refer to Case study 1. You configure synchronization from NW-HQ to NW-Labs the same way as for NW-Retail. Test connection succeeds, but the provisioning logs show that users fail with AzureActiveDirectoryForbidden: "Guest invitations not allowed for your company."

What should you do?

A. In NW-Labs, change Guest invite settings to a less restrictive option.
B. In NW-Labs, assign the Guest Inviter role to the synchronization service principal.
C. In NW-HQ, enable automatic redemption in the outbound settings for NW-Labs.
D. Purchase Microsoft Entra ID P1 licenses for NW-Labs.

**Respuesta:** A

**Por qué es correcta:** Learn documenta este error exacto. Aparece cuando el target tiene Guest invite settings en la opción más restrictiva. **La solución es relajar ese setting en el target.**

**Por qué las otras no:**
- B. No es la solución documentada. Con "No one... including admins" nadie puede invitar.
- C. Si el Test connection pasó, el automatic redemption ya está bien.
- D. **El target no necesita licencias** para cross-tenant sync.

**Fuente:** https://learn.microsoft.com/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-configure#symptom---users-fail-to-provision-with-error-azureactivedirectoryforbidden

---

## Subdominio 4: Implement and manage hybrid identity

### Q31 · Implement and manage pass-through authentication · Multiple choice

Contoso uses pass-through authentication with three authentication agents: one on the Microsoft Entra Connect Sync server, which runs as a VM in Azure, and two on on-premises servers. Password hash synchronization was enabled months ago as well. A ransomware attack takes all on-premises domain controllers and both on-premises agent servers offline. Users can't sign in to Microsoft 365. You must restore cloud sign-in as fast as possible.

What should you do?

A. Nothing. Microsoft Entra ID automatically fails over to password hash synchronization.
B. On the Microsoft Entra Connect server, change the user sign-in method to password hash synchronization.
C. Enable seamless single sign-on.
D. Install two more pass-through authentication agents on new servers in Azure.

**Respuesta:** B

**Por qué es correcta:** PHS sirve de respaldo para PTA, pero **el failover no es automático**. Tienes que cambiar el método de sign-in manualmente en Microsoft Entra Connect. Por eso Learn recomienda tener PHS habilitado antes de que pase algo.

**Por qué las otras no:**
- A. Es la trampa principal: PHS no se activa solo.
- C. Seamless SSO solo evita que el usuario escriba el password. No autentica si PTA está caído.
- D. Los agentes nuevos también validan contra los DCs, y los DCs están caídos.

**Fuente:** https://learn.microsoft.com/entra/identity/hybrid/connect/choose-ad-authn#detailed-considerations

---

### Q32 · Implement and manage password hash synchronization · Yes/No series

Contoso uses password hash synchronization through Microsoft Entra Connect Sync with default settings. CloudPasswordPolicyForPasswordSyncedUsersEnabled isn't enabled.

For each of the following statements, select Yes or No.

1. Password hash synchronization runs every 2 minutes, independently of the 30-minute object sync cycle.
2. A user whose on-premises password has expired can still sign in to Microsoft 365 with that password.
3. An Active Directory account that reaches its accountExpires date is automatically blocked from signing in to Microsoft Entra ID.

**Respuesta:** 1 = Yes, 2 = Yes, 3 = No

**Por qué es correcta:**
- 1 Yes. PHS corre **cada 2 minutos y esa frecuencia no se puede cambiar**. Los demás atributos van en el ciclo de 30 minutos.
- 2 Yes. Por default el password en la nube queda como **Never Expire**. El usuario puede seguir entrando con el password vencido hasta que lo cambie on-prem.
- 3 No. **accountExpires no se sincroniza.** Learn sugiere un script que deshabilite la cuenta en AD cuando expire.

**Por qué las otras no:**
- La trampa de la 2 es pensar que la expiración de AD se respeta en la nube. Para eso existe CloudPasswordPolicyForPasswordSyncedUsersEnabled.
- La trampa de la 3 es confundir "cuenta expirada" con "cuenta deshabilitada".

**Fuente:** https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-password-hash-synchronization#password-expiration-policy y https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-password-hash-synchronization#account-expiration

---

### Q33 · Implement and manage pass-through authentication · Multiple choice

Contoso enabled pass-through authentication. The only authentication agent runs on the Microsoft Entra Connect server. For production, sign-ins must continue if that server fails.

What should you do?

A. Install standalone authentication agents on at least two additional servers, close to the domain controllers.
B. Install a second authentication agent on the Microsoft Entra Connect server.
C. Deploy a second Microsoft Entra Connect Sync server in staging mode and rely on it for sign-in failover.
D. Publish the agents behind an inbound load balancer in the perimeter network.

**Respuesta:** A

**Por qué es correcta:** Learn recomienda **mínimo 3 authentication agents en producción**, en servidores distintos al de Connect y cerca de los DCs.

**Por qué las otras no:**
- B. **Solo cabe un agente por servidor.**
- C. Staging mode es para disaster recovery de la sincronización. No es el método documentado de HA para PTA.
- D. Los agentes solo hacen conexiones de salida (443 y 80), así que no necesitan DMZ ni publicarse hacia adentro. Además, varios agentes dan alta disponibilidad, no load balancing.

**Fuente:** https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-pta-quick-start#step-4-ensure-high-availability y https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-pta-faq#can-i-install-two-or-more-pass-through-authentication-agents-on-the-same-server

---

### Q34 · Implement and manage seamless single sign-on (SSO) · Select two

Contoso uses password hash synchronization and just enabled Seamless SSO in Microsoft Entra Connect. Users on domain-joined Windows 8.1 devices inside the corporate network are still prompted for a password in Microsoft Edge.

Which two actions should you perform? Each correct answer presents part of the solution.

A. Use Group Policy to add https://autologon.microsoftazuread-sso.com to the users' Intranet zone (Site to Zone Assignment List, value 1).
B. Use Group Policy to enable "Allow updates to status bar via script" for the Intranet zone.
C. Convert the contoso.com domain to federated.
D. Assign Microsoft Entra ID P1 licenses to the users.
E. Add https://autologon.microsoftazuread-sso.com to the Restricted sites zone (value 4).

**Respuesta:** A y B

**Por qué es correcta:** El navegador no manda el ticket de Kerberos a un endpoint en la nube **si la URL no está en la Intranet zone**. Learn pide las dos políticas de GPO: la URL autologon con valor 1 y "Allow updates to status bar via script".

**Por qué las otras no:**
- C. **Seamless SSO solo funciona con PHS o PTA, no con AD FS.**
- D. Seamless SSO es gratis.
- E. El valor 4 es Restricted zone y hace que Seamless SSO falle siempre. Se usa a propósito para kioscos compartidos.

**Fuente:** https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-sso-quick-start#roll-out-the-feature

---

### Q35 · Implement and manage Microsoft Entra Cloud Sync · Multiple choice

Contoso acquired Fabrikam. Fabrikam's Active Directory forest has no network connectivity or trust with Contoso's forest, and it won't be connected for at least a year. Contoso already syncs its own forest with Microsoft Entra Connect Sync. About 8,000 Fabrikam users must appear in Contoso's Microsoft Entra tenant. The solution must be highly available and must minimize on-premises infrastructure.

What should you do?

A. Install Microsoft Entra Cloud Sync provisioning agents on three servers in Fabrikam's forest, and create a Cloud Sync configuration for fabrikam.com.
B. Add an Active Directory connector for fabrikam.com to the existing Microsoft Entra Connect Sync server.
C. Install a second Microsoft Entra Connect Sync server in Fabrikam's forest in active mode.
D. Configure cross-tenant synchronization from Fabrikam's tenant to Contoso's tenant.

**Respuesta:** A

**Por qué es correcta:** **Forests desconectados son escenario de Cloud Sync**, y Connect Sync no los soporta. Cloud Sync usa agentes ligeros, recomienda 3 agentes activos para HA y puede convivir con Connect Sync (forest existente con Connect, forest nuevo con Cloud Sync). Cada objeto debe estar en el scope de una sola herramienta.

**Por qué las otras no:**
- B. El conector de Connect Sync necesita conectividad con el forest. No hay.
- C. Connect Sync es Active-Passive. **Solo un servidor activo** por tenant.
- D. Cross-tenant sync mueve usuarios entre tenants de Entra, no desde un AD on-prem.

**Fuente:** https://learn.microsoft.com/entra/identity/hybrid/cloud-sync/connect-to-cloud-sync-decision-guide#comparison-between-microsoft-entra-connect-and-cloud-sync y https://learn.microsoft.com/entra/identity/hybrid/cloud-sync/plan-cloud-sync-topologies#active-directory-to-microsoft-entra-id-supported-topologies

---

### Q36 · Implement and manage Microsoft Entra Cloud Sync · Yes/No series

Contoso is evaluating whether to replace Microsoft Entra Connect Sync with Cloud Sync. The environment has one forest and one domain with 90,000 objects. Also, 3,000 Windows 11 PCs are Microsoft Entra hybrid joined through Microsoft Entra Connect. Contoso uses password hash synchronization and OU-based filtering only.

For each of the following statements, select Yes or No.

1. Cloud Sync can synchronize the computer objects needed for Microsoft Entra hybrid join of those PCs.
2. Cloud Sync supports password hash synchronization.
3. Cloud Sync can run several active agents at the same time, with automatic failover.

**Respuesta:** 1 = No, 2 = Yes, 3 = Yes

**Por qué es correcta:**
- 1 No. **Device synchronization para hybrid join es solo de Connect Sync.** Es el bloqueador típico para migrar.
- 2 Yes. PHS tiene paridad total en las dos herramientas.
- 3 Yes. Múltiples agentes activos con failover automático es una ventaja clave de Cloud Sync. Connect Sync es Active-Passive.

**Por qué las otras no:**
- La trampa de la 1 es pensar que Cloud Sync ya hace todo lo de Connect Sync.
- Ojo: 90,000 objetos entra en el límite de 150,000 por dominio de Cloud Sync, así que el tamaño no es el problema aquí.

**Fuente:** https://learn.microsoft.com/entra/identity/hybrid/cloud-sync/connect-to-cloud-sync-decision-guide#comparison-between-microsoft-entra-connect-and-cloud-sync y https://learn.microsoft.com/entra/identity/hybrid/common-scenarios#supported-sync-scenarios

---

### Q37 · Implement and manage Microsoft Entra Connect Sync · Multiple choice

Contoso has two Microsoft Entra Connect Sync servers. SYNC1 is active. SYNC2 is in staging mode, has its scheduler enabled, and has synchronized recently. SYNC1's hardware fails permanently. You must resume exports to Microsoft Entra ID as fast as possible.

What should you do?

A. On SYNC2, run the Microsoft Entra Connect wizard, select Configure staging mode, clear the staging mode checkbox, and start synchronization.
B. On SYNC2, run `Start-ADSyncSyncCycle -PolicyType Initial`.
C. Install Microsoft Entra Connect on a new server by using express settings.
D. On SYNC2, enable password writeback so that it takes over from SYNC1.

**Respuesta:** A

**Por qué es correcta:** Un servidor en staging mode **importa y sincroniza, pero no exporta ni hace password sync ni writeback**. Para que tome el control, quitas el staging mode en el wizard. Antes, asegúrate de que SYNC1 no vuelva a encender. **Solo puede haber un servidor activo.**

**Por qué las otras no:**
- B. Un ciclo completo en staging sigue sin exportar.
- C. Reconstruir es más lento. Para eso tienes el standby listo.
- D. Password writeback no activa las exportaciones. En staging mode, PHS y writeback están apagados hasta que sales de staging.

**Fuente:** https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-sync-staging-server#staging-mode y https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-sync-staging-server#change-current-staging-sync-server-to-active-mode

---

### Q38 · Migrate from AD FS to other authentication and authorization mechanisms · Drag/order

Contoso's domain contoso.com is federated with AD FS. Microsoft Entra Connect Sync is installed. Contoso wants to move to password hash synchronization, test with a pilot group first, and decommission the Microsoft 365 relying party trust at the end.

Which five actions should you perform in sequence? (Two actions aren't used.)

A. Enable password hash synchronization in Microsoft Entra Connect, without changing the sign-in method yet.
B. Create a cloud security group and add the pilot users.
C. Enable staged rollout for password hash sync and add the pilot group.
D. Convert contoso.com from federated to managed by running `Update-MgDomain -DomainId contoso.com -AuthenticationType "Managed"`.
E. After Microsoft Entra Connect Health shows no more authentication requests on AD FS, remove the Microsoft 365 relying party trust.
F. Add a dynamic membership group that contains all users to staged rollout.
G. Convert the domain to managed first, and then enable staged rollout to test.

**Respuesta:** A, B, C, D, E

**Por qué es correcta:** Primero la prework de PHS, luego el grupo piloto (Learn recomienda **grupos cloud**), luego staged rollout para probar, luego el cutover del dominio a Managed y al final quitar el relying party trust cuando Connect Health confirme que ya no hay tráfico. Después del cutover también apagas staged rollout.

**Por qué las otras no:**
- F. **Staged rollout no soporta grupos dinámicos ni anidados**, y hay un máximo de 10 grupos por feature.
- G. Staged rollout es para probar antes del cutover. **No convierte dominios** y no tiene sentido después.

**Fuente:** https://learn.microsoft.com/entra/identity/hybrid/connect/migrate-from-federation-to-cloud-authentication#convert-domains-from-federated-to-managed y https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-staged-rollout#unsupported-scenarios

---

### Case study 2: Litware, Inc. (usar para Q39 y Q40)

Litware, Inc. has one Active Directory forest (litware.com) with 12,000 users in two datacenters. The domain is federated with AD FS (two AD FS servers and two Web Application Proxy servers). Microsoft Entra Connect Sync runs on LIT-SYNC1. Every user has Microsoft 365 E3, which includes Microsoft Entra ID P1.

Requirements:
- Decommission AD FS within six months.
- At sign-in time, Microsoft Entra ID must enforce on-premises account states (disabled, locked out) and the allowed logon hours.
- If the on-premises authentication infrastructure fails, administrators must be able to switch users to a cloud sign-in method without deploying new infrastructure.
- The security team requires the leaked credentials detection of Microsoft Entra ID Protection.
- Before the relying party trust is removed, the identity operations team must see which applications still authenticate through AD FS, and the mailbox IdentityOps@litware.com must receive Connect Health alerts.

### Q39 · Implement and manage pass-through authentication · Case study (Multiple choice)

Refer to Case study 2. Which sign-in configuration should Litware implement after AD FS?

A. Pass-through authentication with at least three authentication agents, and password hash synchronization enabled as well
B. Password hash synchronization only, with Seamless SSO
C. Keep AD FS federation and enable password hash synchronization
D. Pass-through authentication only, with at least three authentication agents

**Respuesta:** A

**Por qué es correcta:** **PTA aplica en el momento del sign-in** el estado de la cuenta en AD (disabled, locked out, logon hours). PHS encima da leaked credentials y queda como respaldo para cambiar manualmente si falla on-prem. Learn recomienda habilitar PHS sin importar el método principal.

**Por qué las otras no:**
- B. Con solo PHS, Entra no revisa en vivo el estado de AD ni los logon hours.
- C. El requisito es quitar AD FS.
- D. Sin PHS no hay leaked credentials ni respaldo para cambiar el método de sign-in.

**Fuente:** https://learn.microsoft.com/entra/identity/hybrid/connect/choose-ad-authn#detailed-considerations y https://learn.microsoft.com/entra/identity/hybrid/connect/choose-ad-authn#recommendations

---

### Q40 · Implement and manage Microsoft Entra Connect Health · Case study (Select two)

Refer to Case study 2. Which two actions should you perform to meet the monitoring requirements? Each correct answer presents part of the solution.

A. Install the Microsoft Entra Connect Health agent for AD FS on the AD FS and Web Application Proxy servers, and enable AD FS auditing.
B. In Connect Health notification settings, add IdentityOps@litware.com as a custom notification email.
C. Manually install the Connect Health agent for sync on LIT-SYNC1.
D. Purchase Microsoft Entra ID P2 licenses, because Connect Health requires P2.
E. Install the Connect Health agent for AD DS on all domain controllers.

**Respuesta:** A y B

**Por qué es correcta:** El agente de AD FS va en los AD FS y en los WAP. **Usage analytics necesita el AD FS auditing habilitado**, porque no viene prendido por default. Con esos agentes también se ve qué apps siguen usando AD FS. Las notificaciones por correo vienen activas por default, y para que lleguen al buzón de IdentityOps se agrega en Custom notification emails.

**Por qué las otras no:**
- C. **El agente de sync se instala solo** con la versión actual de Microsoft Entra Connect.
- D. Connect Health pide P1 (1 licencia para el primer agente y 25 por cada agente extra). Litware ya tiene P1 con Microsoft 365 E3.
- E. No se pidió monitorear AD DS.

**Fuente:** https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-health-adfs#install-the-agent-for-ad-fs y https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-health-operations#enable-email-notifications
