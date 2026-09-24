# M4 Banco de preguntas: Plan and automate identity governance (20 a 25%)

40 preguntas originales, escritas para SC-300 Tips and Tricks con base en Microsoft Learn (revisado en septiembre 2026). No vienen de dumps ni de preguntas filtradas. Las preguntas y opciones están en inglés (el idioma del examen) y las explicaciones en español.

Cómo usarlo:
- Contesta primero sin ver la respuesta. Luego lee el "por qué las otras no": ahí está el valor.
- En las series Yes/No, **cada afirmación se evalúa sola**.
- En drag/order solo cuentan las acciones que sí van, en el orden correcto.
- En select two, necesitas las dos respuestas para sumar el punto.
- Las queries KQL están completas y corren tal cual en un Log Analytics workspace que ya recibe los logs de Entra.

| Subdominio | Preguntas |
|---|---|
| Plan and implement entitlement management | Q1 a Q12 (Q11 y Q12 son el case study 1) |
| Plan, implement, and manage access reviews | Q13 a Q20 |
| Plan and implement privileged access | Q21 a Q32 (Q31 y Q32 son el case study 2) |
| Monitor identity activity by using logs, workbooks, and reports | Q33 a Q40 |

| Formato | Cantidad | Preguntas |
|---|---|---|
| Multiple choice (una respuesta) | 23 | Q1, Q3, Q4, Q6, Q8, Q11, Q13, Q15, Q16, Q18, Q19, Q21, Q23, Q25, Q26, Q29, Q31, Q32, Q33, Q37, Q38, Q39, Q40 |
| Yes/No series | 7 | Q2, Q5, Q9, Q14, Q22, Q28, Q34 |
| Drag/order | 4 | Q10, Q17, Q24, Q36 |
| Select two | 6 | Q7, Q12, Q20, Q27, Q30, Q35 |
| Case study (dentro de los formatos anteriores) | 2 casos, 4 preguntas | Q11 y Q12, Q31 y Q32 |
| Con query KQL completa | 4 | Q29, Q32, Q37, Q38 |

---

## Subdominio 1: Plan and implement entitlement management

### Q1 · Plan entitlements · Multiple choice

Contoso already uses a dynamic membership group and group-based licensing so that every employee gets a Microsoft 365 license on day one. A new requirement arrives: employees from Finance sometimes need access to the Legal SharePoint Online site and the Legal contracts app for 30 days. The Legal manager must approve each request, and users from a partner organization must also be able to ask for the same access.

What should you use?

A. A second dynamic membership group with a rule based on the department attribute
B. An access package in Microsoft Entra entitlement management
C. PIM for Groups on the Legal security group
D. Self-service group management with owner approval on the Legal group

**Respuesta:** B

**Por qué es correcta:** Learn dice que los access packages son lo indicado cuando el acceso es **por tiempo limitado, necesita aprobación y también lo piden personas de una organización socia**. Un access package junta el sitio y la app en un solo paquete, con expiración de 30 días y aprobador.

**Por qué las otras no:**
- A: un grupo dinámico es para acceso "de nacimiento" por atributo. No tiene aprobación, no expira a los 30 días y no trae externos.
- C: PIM for Groups es JIT para accesos privilegiados. No invita externos ni junta un sitio y una app en un paquete.
- D: self-service de grupos solo cubre un grupo, sin expiración y sin flujo para partners.

**Fuente:** https://learn.microsoft.com/entra/id-governance/entitlement-management-overview#when-should-i-use-access-packages

---

### Q2 · Create and configure catalogs (delegation roles) · Yes/No series

In the Marketing catalog of Contoso:
- Mamta is a catalog owner.
- Jessica is an access package manager.
- Nuno is an access package assignment manager.

None of them hold a Microsoft Entra directory role.

For each of the following statements, select Yes or No.

1. Jessica can create a new access package that uses resources already in the Marketing catalog.
2. Jessica can add a new SharePoint Online site to the Marketing catalog.
3. Nuno can directly assign a user to an existing access package in the catalog and reprocess a request that failed.

**Respuesta:** 1 = Yes, 2 = No, 3 = Yes

**Por qué es correcta:**
- 1 Yes. El access package manager **crea access packages con recursos que ya están en el catalog** y maneja sus policies.
- 2 No. Agregar recursos al catalog es trabajo del catalog owner (o de un admin), y además hace falta permiso sobre el recurso. Para un sitio de SharePoint, ser SharePoint Administrator o admin del sitio.
- 3 Yes. El access package assignment manager puede asignar y quitar usuarios, ver requests y hacer reprocess. **No crea ni edita access packages.**

**Por qué las otras no:**
- Trampa de la 1: creer que solo el catalog owner crea paquetes. El access package manager también.
- Trampa de la 2: confundir "crear paquetes" con "agregar recursos al catalog".
- Trampa de la 3: pensar que el assignment manager solo ve. Sí asigna, quita y reprocesa.

**Fuente:** https://learn.microsoft.com/entra/id-governance/entitlement-management-delegate#entitlement-management-roles

---

### Q3 · Create and configure catalogs (adding resources) · Multiple choice

Pat is a user with no Microsoft Entra directory role. Pat is the catalog owner of the Research catalog. Pat needs to add the security group SG-Lab to the catalog, but SG-Lab doesn't appear in the resource picker.

You need to let Pat add SG-Lab by granting the least privilege.

What should you do?

A. Assign Pat the Identity Governance Administrator role.
B. Assign Pat the Groups Administrator role.
C. Add Pat as an owner of SG-Lab.
D. Add Pat as an access package manager of the Research catalog.

**Respuesta:** C

**Por qué es correcta:** Para agregar un recurso al catalog hacen falta **dos cosas: ser catalog owner y tener permiso sobre el recurso**. La tabla de Learn dice que un usuario normal que es catalog owner puede agregar un grupo "only if group owner". Ser owner de ese único grupo es lo más acotado.

**Por qué las otras no:**
- A: trampa clásica. En la tabla de Learn, Identity Governance Administrator puede agregar **apps**, pero no security groups ni Microsoft 365 groups.
- B: Groups Administrator más catalog owner sí funciona, pero es un rol de todo el tenant. No es least privilege.
- D: el access package manager usa recursos que ya están en el catalog. No agrega recursos.

**Fuente:** https://learn.microsoft.com/entra/id-governance/entitlement-management-delegate#required-roles-to-add-resources-to-a-catalog

---

### Q4 · Create and configure access packages (policy audience) · Multiple choice

You are creating the Project Falcon access package. Requirements:
- Member users of Contoso (not guests) can request it, with approval from their manager.
- Users from Fabrikam, an existing connected organization, can request it, with approval from the Fabrikam external sponsor.

What is the minimum number of policies the access package needs?

A. One
B. Two
C. Three
D. Four

**Respuesta:** B

**Por qué es correcta:** Learn lo dice claro: **una sola policy no puede asignar identidades internas y externas** al mismo access package. Necesitas una policy "For users, service principals, and agent identities in your directory" (All members excluding guests, manager como approver) y otra "For users not in your directory" (Specific connected organizations, external sponsor como approver).

**Por qué las otras no:**
- A: una policy tiene un solo público. No mezcla "in your directory" con "not in your directory".
- C: tres sería si además quisieras asignación automática o solo directa por admin. No se pide.
- D: no hay cuatro públicos distintos en el escenario.

**Fuente:** https://learn.microsoft.com/entra/id-governance/entitlement-management-access-package-request-policy#choose-between-one-or-multiple-policies

---

### Q5 · Create and configure access packages (lifecycle and extension) · Yes/No series

An access package policy has these Lifecycle settings:
- Access package assignments expire: Number of days, 90
- Allow users to extend access: Yes
- Require approval to grant extension: Yes

On the Requests tab, the policy requires approval from the requestor's manager.

For each of the following statements, select Yes or No.

1. Users receive an email 14 days before and again one day before their assignment expires, asking them to extend it.
2. An extension request is approved by using the same approval settings defined on the Requests tab.
3. A user who is no longer in the scope of the policy can still request an extension.

**Respuesta:** 1 = Yes, 2 = Yes, 3 = No

**Por qué es correcta:**
- 1 Yes. Con extensión permitida, el correo llega **14 días antes y un día antes** de que expire.
- 2 Yes. "Require approval to grant extension" usa **las mismas reglas de aprobación** de la pestaña Requests.
- 3 No. Learn pide que el usuario **siga dentro del scope de la policy** al pedir la extensión.

**Por qué las otras no:**
- Trampa de la 1: inventar otros números (7 días, 30 días).
- Trampa de la 2: creer que la extensión tiene su propio approver aparte.
- Trampa de la 3: pensar que la extensión es automática para quien ya tuvo acceso.

**Fuente:** https://learn.microsoft.com/entra/id-governance/entitlement-management-access-package-lifecycle-policy#specify-a-lifecycle

---

### Q6 · Manage access requests (multi-stage approval) · Multiple choice

An access package policy uses two-stage approval:
- Stage 1 approvers: Alice and Bob. Decision must be made in 5 days.
- Stage 2 approver: Carol. Decision must be made in 5 days.

A user submits a request. Alice approves it on day 1. Carol doesn't act during her stage.

What happens to the request?

A. It's approved, because stage 1 already approved it.
B. It expires (it's automatically denied), and the user must submit a new request.
C. It's forwarded to Global Administrators for a decision.
D. It returns to Bob, because he didn't respond in stage 1.

**Respuesta:** B

**Por qué es correcta:** En multi-stage, **basta un approver por stage** para pasar al siguiente, y cada stage tiene su plazo. Si nadie decide a tiempo, la solicitud **se deniega sola** (estado Expired) y el usuario tiene que pedir otra vez.

**Por qué las otras no:**
- A: un stage aprobado no aprueba los siguientes. Todos los stages deben aprobar.
- C: no existe un forward automático a Global Administrators. Solo hay alternate approvers si los configuras.
- D: Alice ya resolvió el stage 1. Bob no vuelve a entrar.

**Fuente:** https://learn.microsoft.com/entra/id-governance/entitlement-management-access-package-approval-policy#multi-stage-approval

---

### Q7 · Manage access requests (alternate approvers) · Select two

An access package uses single-stage approval with a specific approver. When that approver doesn't act, pending requests must go to the IT-Backup group before they time out.

Which two settings should you configure? Each correct answer presents part of the solution.

A. Set "If no action taken, forward to alternate approvers?" to Yes and add IT-Backup as alternate approvers.
B. Set "Forward to alternate approver(s) after how many days", and keep the request decision time-out at four days or more.
C. Add IT-Backup as a fallback approver.
D. Set "Require approver justification" to Yes.
E. Set "Users can request specific timeline" to Yes.

**Respuesta:** A y B

**Por qué es correcta:** Los **alternate approvers** reciben la solicitud cuando el approver principal no actúa, según el número de días que definas. Learn agrega dos reglas: el forward solo pasa un día después de creada la solicitud, y el **time-out debe ser de al menos cuatro días**.

**Por qué las otras no:**
- C: fallback approver es para cuando **no se encuentra el manager** del usuario. No es para cuando el approver no responde.
- D: la justificación del approver no mueve la solicitud a nadie.
- E: esto deja al usuario pedir fechas de inicio y fin. No tiene que ver con aprobación.

**Fuente:** https://learn.microsoft.com/entra/id-governance/entitlement-management-access-package-approval-policy#alternate-approvers

---

### Q8 · Manage the lifecycle of external users · Multiple choice

The entitlement management setting "Lifecycle of external users" is configured as follows:
- Block external user from signing in to this directory: Yes
- Remove external user: Yes
- Number of days before removing external user from this directory: 30

Ana, a partner user, was invited to Contoso when her access package request was approved. Later, a site owner also shared a SharePoint Online site directly with Ana. Today, Ana's only access package assignment expires.

What happens to Ana's guest account?

A. Nothing, because she still has access to a SharePoint Online site.
B. It's deleted immediately.
C. It's blocked from signing in now and removed after 30 days.
D. It stays active until the next access review of the SharePoint site.

**Respuesta:** C

**Por qué es correcta:** Al perder su **último** access package, el guest queda bloqueado y se borra a los 30 días. Learn aclara que el usuario **se borra aunque tenga otros accesos** que no vienen de access packages, como un sitio de SharePoint compartido después.

**Por qué las otras no:**
- A: trampa directa. El acceso directo al sitio no la salva, porque Ana entró por entitlement management.
- B: el borrado inmediato solo pasa si pones 0 días.
- D: una access review no controla este ciclo de vida.

**Fuente:** https://learn.microsoft.com/entra/id-governance/entitlement-management-external-users#manage-the-lifecycle-of-external-users

---

### Q9 · Implement and manage terms of use (ToU) · Yes/No series

A Conditional Access Administrator creates a terms of use named Contractor ToU with these settings:
- Require users to consent on every device: On
- Expire consents: Off
- Duration before re-acceptance required (days): 90
- Enforce with Conditional Access policy template: Create Conditional Access policy later

For each of the following statements, select Yes or No.

1. Users aren't prompted to accept Contractor ToU until a Conditional Access policy selects it as a grant control.
2. B2B guest users in scope must accept Contractor ToU on every device they use.
3. When a user's 90-day consent expires, the user is prompted to accept again only after their session expires.

**Respuesta:** 1 = Yes, 2 = No, 3 = Yes

**Por qué es correcta:**
- 1 Yes. Con "Create Conditional Access policy later", la ToU solo aparece en la lista de grant controls. **Sin una política de CA, nadie la ve.**
- 2 No. La ToU por device **no soporta usuarios B2B**. Además pide que el device esté registrado en Entra ID.
- 3 Yes. Learn marca como importante que, con Expire consents o con Duration before re-acceptance, el usuario vuelve a aceptar **solo cuando su sesión expira**.

**Por qué las otras no:**
- Trampa de la 1: creer que crear la ToU ya la hace cumplir.
- Trampa de la 2: olvidar las limitaciones de per-device (B2B y la app Intune Enrollment).
- Trampa de la 3: pensar que la re-aceptación corta la sesión en ese mismo momento.

**Fuente:** https://learn.microsoft.com/entra/identity/conditional-access/terms-of-use#per-device-terms-of-use y https://learn.microsoft.com/entra/identity/conditional-access/terms-of-use#add-terms-of-use

---

### Q10 · Implement and manage terms of use (ToU) · Drag/order

All members of the Contractors group must accept a new terms of use before they can open the Contoso Projects app.

Which four actions should you perform in sequence?

Actions:
- A. Create the terms of use document in PDF format.
- B. In Conditional Access > Terms of use, add new terms, upload the PDF, and choose "Create Conditional Access policy later".
- C. Create a Conditional Access policy that targets the Contractors group and the Contoso Projects app, and select the new terms under Grant.
- D. Set Enable policy to On and tell users in scope to sign out and sign back in.
- E. Enable email one-time passcode for the tenant.
- F. Add the terms of use to the Contractors access package policy.

**Respuesta:** A, B, C, D

**Por qué es correcta:** La ToU es un **PDF** que subes en Terms of use. Si eliges "Create Conditional Access policy later", la ToU queda disponible como grant control. Luego creas la **política de CA** con el grupo y la app, y la activas. Learn avisa que los usuarios en scope deben cerrar sesión y volver a entrar para cumplir la nueva política.

**Por qué las otras no:**
- E: email one-time passcode es para externos sin cuenta de Entra. No tiene nada que ver con aceptar una ToU.
- F: las policies de access package no tienen un campo de ToU. La ToU se hace cumplir con Conditional Access.

**Fuente:** https://learn.microsoft.com/entra/identity/conditional-access/terms-of-use#add-terms-of-use

---

### Case study 1: Woodgrove Bank (Q11 y Q12)

Woodgrove Bank has Microsoft Entra ID Governance licenses. It plans to share the Partner Portal access package with two partners:
- Tailspin Toys uses Microsoft Entra ID (tenant tailspintoys.com).
- Northwind Traders doesn't use Microsoft Entra ID. Its users have email addresses that end in @northwindtraders.com.

Current configuration:
- Two connected organizations exist: one for the Tailspin Toys tenant and one for the northwindtraders.com domain (one-time passcode).
- The catalog that contains Partner Portal has Enabled for external users set to Yes.
- Email one-time passcode is enabled.
- The B2B external collaboration settings use an allowlist that contains only tailspintoys.com.

Requirements:
- Only users from the two partners can request Partner Portal.
- Each request must be approved first by a contact person from the partner, who is already a guest in Woodgrove, and then by Woodgrove's partner manager, Omar.
- Assignments expire after 180 days.
- When a partner user loses their last access package assignment, their guest account must be removed as soon as possible.

### Q11 · Configure and manage connected organizations · Multiple choice (case study 1)

Requests from Northwind Traders users are approved, but those users never get access, and no guest account is created for them.

What should you do?

A. Add northwindtraders.com to the B2B allowlist, or remove the allowlist.
B. Change the policy to All users (All connected organizations + any new external users).
C. Recreate the Northwind Traders connected organization with the Microsoft Entra ID authentication type.
D. Set Enabled for external users to Yes on the catalog.

**Respuesta:** A

**Por qué es correcta:** Cuando se aprueba la solicitud, entitlement management invita al usuario con B2B. **La B2B allow/block list tiene prioridad**: si el dominio no está permitido, el usuario no se invita y no recibe acceso hasta que actualices la lista.

**Por qué las otras no:**
- B: cambiar a "All users" no arregla nada, porque la allowlist sigue ganando. Además rompe el requisito de "solo los dos partners".
- C: Northwind no tiene tenant de Entra. Su tipo de autenticación correcto es one-time passcode por dominio.
- D: el catalog ya está en Yes, según el caso.

**Fuente:** https://learn.microsoft.com/entra/id-governance/entitlement-management-external-users#settings-for-external-users

---

### Q12 · Create and configure access packages and lifecycle of external users · Select two (case study 1)

Which two configurations meet the approval and lifecycle requirements of Woodgrove Bank? Each correct answer presents part of the solution.

A. In the policy for users not in your directory, configure two-stage approval: first approver External sponsor, second approver Omar as a specific approver.
B. In Control Configurations > Lifecycle of external users, set Remove external user to Yes and Number of days before removing external user from this directory to 0.
C. In the policy, set Manager as the first approver and add Omar as the fallback approver.
D. Create an access review of the access package with "Block user from signing in for 30 days, then remove user from the tenant".
E. Keep Number of days before removing external user from this directory at 30.

**Respuesta:** A y B

**Por qué es correcta:**
- A: para usuarios que no están en tu directorio puedes elegir **External sponsor** en el primer stage y un approver específico en el segundo. Los sponsors externos se definen en la connected organization.
- B: con **0 días**, la cuenta guest se borra en cuanto el usuario pierde su último access package. Eso es "lo antes posible".

**Por qué las otras no:**
- C: "Manager as approver" solo existe en policies para usuarios de tu directorio. Los externos no tienen manager en Woodgrove.
- D: una access review decide sobre el acceso. No es el mecanismo para borrar al guest cuando pierde su último paquete.
- E: 30 días es el default. No cumple "lo antes posible".

**Fuente:** https://learn.microsoft.com/entra/id-governance/entitlement-management-access-package-approval-policy#single-stage-approval y https://learn.microsoft.com/entra/id-governance/entitlement-management-external-users#manage-the-lifecycle-of-external-users

---

## Subdominio 2: Plan, implement, and manage access reviews

### Q13 · Plan for access reviews · Multiple choice

Auditors ask Contoso to review, every quarter, who holds eligible or active assignments to the Global Administrator role.

Where should you create this access review?

A. ID Governance > Access Reviews > Teams + Groups
B. Microsoft Entra Privileged Identity Management
C. Entitlement management, in the policy of an access package
D. Enterprise applications, in the properties of the Microsoft Graph app

**Respuesta:** B

**Por qué es correcta:** La tabla de Learn "Where do you create reviews?" dice que los **roles de Microsoft Entra y los roles de Azure se revisan desde PIM**. Para roles de Entra necesitas al menos Privileged Role Administrator.

**Por qué las otras no:**
- A: Teams + Groups revisa membresía de grupos, no asignaciones de roles.
- C: en entitlement management se revisan asignaciones de access packages.
- D: en Enterprise applications se revisa quién tiene asignada una app.

**Fuente:** https://learn.microsoft.com/entra/id-governance/access-reviews-overview#where-do-you-create-reviews

---

### Q14 · Create and configure access reviews · Yes/No series

You create an access review with these settings:
- Review: Teams + Groups, Select Teams + groups: Project-X
- Scope: Guest users only
- Reviewers: Group owner(s), fallback reviewer: Lee
- Auto apply results to resource: Enabled
- If reviewers don't respond: Remove access
- Action to apply on denied guest users: Block user from signing-in for 30 days, then remove user from the tenant

For each of the following statements, select Yes or No.

1. If Project-X has no owner when the review starts, Lee is asked to review.
2. A guest that no reviewer reviews is blocked from signing in to the tenant after the review ends.
3. An owner added to Project-X during the review becomes a reviewer of the current review instance.

**Respuesta:** 1 = Yes, 2 = Yes, 3 = No

**Por qué es correcta:**
- 1 Yes. El **fallback reviewer** entra cuando el usuario no tiene manager o el grupo no tiene owner.
- 2 Yes. "Remove access" cuenta como denegar, y la acción para guests aplica cuando se niegan **por un reviewer o por el setting If reviewers don't respond**. Con auto apply, el guest queda bloqueado y se borra a los 30 días.
- 3 No. Solo cuentan los owners **que existían cuando empezó la review**. Los cambios entran en la siguiente instancia.

**Por qué las otras no:**
- Trampa de la 1: creer que sin owner la review se queda sin reviewer.
- Trampa de la 2: pensar que la acción de guests solo aplica a denegaciones manuales.
- Trampa de la 3: olvidar que la review toma una foto al inicio.

**Fuente:** https://learn.microsoft.com/entra/id-governance/create-access-review#next-reviews y https://learn.microsoft.com/entra/id-governance/create-access-review#next-settings

---

### Q15 · Create and configure access reviews (if reviewers don't respond) · Multiple choice

You create a recurring review of the Sales-Apps group with the decision helper "No sign-in within 30 days" enabled and Auto apply results to resource enabled. Reviewers are the users' managers.

When a manager doesn't respond, users who haven't signed in during the last 30 days must lose access, and active users must keep access.

Which "If reviewers don't respond" option should you select?

A. No change
B. Remove access
C. Approve access
D. Take recommendations

**Respuesta:** D

**Por qué es correcta:** **Take recommendations** aplica lo que recomienda el sistema. Con el helper "No sign-in within 30 days", el sistema recomienda aprobar a quien entró en los últimos 30 días y **denegar a quien no entró**. Justo lo que se pide.

**Por qué las otras no:**
- A: deja a todos igual, incluidos los inactivos.
- B: quita el acceso a todos los no revisados, incluidos los activos. Learn avisa que con auto apply esto puede quitar todo el acceso al recurso.
- C: aprueba a todos, incluidos los inactivos.

**Fuente:** https://learn.microsoft.com/entra/id-governance/create-access-review#next-settings

---

### Q16 · Create and configure access reviews (multi-stage) · Multiple choice

You create a multi-stage access review of the Finance-DB app:
- Stage 1: Managers of users
- Stage 2: The Security team (selected users)

The Security team must double-check only the users that managers decided to keep.

Which option should you select in "Specify reviewees to go to next stage"?

A. Approved reviewees
B. Denied reviewees
C. Not reviewed reviewees
D. All

**Respuesta:** A

**Por qué es correcta:** Con **Approved reviewees**, solo los usuarios aprobados en el stage 1 pasan al stage 2. La decisión del stage 2 **sobrescribe** la del stage 1.

**Por qué las otras no:**
- B: mandaría a los usuarios que el manager quiso quitar.
- C: mandaría solo a los que nadie revisó.
- D: mandaría a todos, y el equipo de seguridad tendría más trabajo del que se pide.

**Fuente:** https://learn.microsoft.com/entra/id-governance/create-access-review#create-a-multi-stage-access-review

---

### Q17 · Create and configure access reviews · Drag/order

You need a recurring quarterly review of guest users in all Microsoft 365 groups. Group owners must review, Lee must review groups that have no owner, and denied guests must be removed automatically.

Which five actions should you perform in sequence?

Actions:
- A. Browse to ID Governance > Access Reviews and select New access review.
- B. Select Teams + Groups, then All Microsoft 365 groups with guest users.
- C. On the Reviews tab, select Group owner(s), add Lee as fallback reviewer, and set the recurrence to Quarterly.
- D. On the Settings tab, enable Auto apply results to resource and choose an "If reviewers don't respond" option.
- E. On Review + Create, name the review and select Create.
- F. On the Settings tab, set Action to apply on denied guest users to "Block user from signing-in for 30 days, then remove user from the tenant".
- G. In Access Reviews > Settings, set "Group owners can create and manage access reviews for groups they own" to Yes.

**Respuesta:** A, B, C, D, E

**Por qué es correcta:** Es el orden del asistente: Select what to review, Reviews, Settings y Review + Create. Con "All Microsoft 365 groups with guest users" el scope queda en **Guest users only** sin más opciones.

**Por qué las otras no:**
- F: trampa fuerte. Learn dice que "Action to apply on denied guest users" **no se puede configurar** en reviews de "All Microsoft 365 groups with guest users". Se usa el default: quitar la membresía.
- G: ese setting sirve para que los owners **creen** reviews. Aquí la crea un admin y los owners solo revisan.

**Fuente:** https://learn.microsoft.com/entra/id-governance/create-access-review#scope y https://learn.microsoft.com/entra/id-governance/create-access-review#next-settings

---

### Q18 · Monitor access review activity · Multiple choice

Auditors need a single CSV file with every decision taken in the last quarter across reviews of groups, applications, Microsoft Entra roles, and access packages. For each user, the file must show the reviewer, the system recommendation, and who applied the result.

What should you use?

A. ID Governance > Access Reviews > Review History > New report
B. The Download button on the Results page of each access review
C. The Microsoft Entra sign-in logs filtered by application
D. The Identity Secure Score history tab

**Respuesta:** A

**Por qué es correcta:** El reporte de **Review History** junta varias reviews en un rango de fechas y filtra por tipo y resultado. Trae columnas como ReviewerName, AccessRecommendation y AppliedByName. El CSV queda disponible **30 días**.

**Por qué las otras no:**
- B: Download en Results da el CSV de **una** review. No junta todas en un archivo.
- C: los sign-in logs muestran inicios de sesión, no decisiones de reviews.
- D: Secure Score no guarda decisiones de reviews.

**Fuente:** https://learn.microsoft.com/entra/id-governance/access-reviews-downloadable-review-history#how-to-create-a-review-history-report

---

### Q19 · Manually respond to access review activity · Multiple choice

A single-stage access review of the HR-Files group has two selected reviewers, Alice and Bob. Auto apply results to resource is enabled.

On day 2, Alice approves Dan. On day 5, before the review ends, Bob denies Dan.

What happens to Dan's membership?

A. Dan keeps his membership, because one approval is enough.
B. Dan is removed as soon as Bob submits his decision.
C. Dan is removed when the review period ends or when an administrator stops the review.
D. The review is flagged as a conflict and an administrator must decide.

**Respuesta:** C

**Por qué es correcta:** Con varios reviewers **se guarda la última respuesta enviada**, aquí la de Bob. Y un usuario denegado **no se quita al instante**: sale cuando termina la review o cuando un admin la detiene.

**Por qué las otras no:**
- A: en access reviews no hay regla de "basta una aprobación". Gana la última decisión.
- B: el deny no se aplica en el momento. Se aplica al final.
- D: no existe un estado de conflicto entre reviewers.

**Fuente:** https://learn.microsoft.com/entra/id-governance/perform-access-review#manually-review-access-for-one-or-more-users

---

### Q20 · Manually respond to access review activity (apply results) · Select two

An access review of several groups finished. Auto apply results to resource was disabled. Some denied users still have access.

Which two statements are true? Each correct answer presents a complete solution.

A. An administrator must open Review history, select the completed instance, and select Apply.
B. When you select Apply, denied members of a group synced from on-premises Active Directory are removed from the on-premises group.
C. Denied members of a dynamic membership group stay in the group, because the group rule controls membership.
D. Users marked as "Don't know" lose their access when the results are applied.
E. You can restart a stopped review to collect more decisions.

**Respuesta:** A y C

**Por qué es correcta:**
- A: sin auto apply, el admin va a **Review history** bajo Series, elige la instancia y hace **Apply**.
- C: las decisiones de una review **no cambian grupos dinámicos**. Mientras el usuario cumpla la regla, sigue siendo miembro.

**Por qué las otras no:**
- B: Apply no toca grupos que vienen de on-premises. Hay que descargar los resultados y hacer el cambio en AD.
- D: "Don't know" deja al usuario con su acceso.
- E: una review detenida con Stop no se puede reiniciar.

**Fuente:** https://learn.microsoft.com/entra/id-governance/complete-access-review#apply-the-changes

---

## Subdominio 3: Plan and implement privileged access

### Q21 · PIM for Microsoft Entra roles (assignments) · Multiple choice

Three helpdesk leads need the User Administrator role only when they run a bulk task during a six-month migration project. After the project ends, they must lose the ability to use the role without any manual cleanup.

Which assignment should you create in PIM?

A. Active, permanent
B. Eligible, permanent
C. Eligible, time-bound with an end date at the end of the project
D. Active, time-bound with an end date at the end of the project

**Respuesta:** C

**Por qué es correcta:** **Eligible** significa que activan el rol solo cuando lo necesitan (JIT). **Time-bound** con fecha de fin hace que la elegibilidad termine sola al acabar el proyecto.

**Por qué las otras no:**
- A: tendrían el rol siempre activo y para siempre.
- B: nunca vence. Alguien tendría que quitarla a mano.
- D: tendrían el rol activo los seis meses completos, sin JIT.

**Fuente:** https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-how-to-add-role-to-user#assign-a-role

---

### Q22 · PIM for Microsoft Entra roles (settings) · Yes/No series

The PIM role settings of the Exchange Administrator role are:
- Activation maximum duration (hours): 4
- On activation, require: Azure MFA
- Require justification on activation: Yes
- Require ticket information on activation: Yes
- Require approval to activate: Yes, no approvers selected

For each of the following statements, select Yes or No.

1. An eligible user can activate the role for six hours.
2. Active Privileged Role Administrators and Global Administrators can approve the activation requests.
3. PIM checks that the ticket number exists in the company's ticketing system before it activates the role.

**Respuesta:** 1 = No, 2 = Yes, 3 = No

**Por qué es correcta:**
- 1 No. El usuario elige una duración **dentro del máximo** configurado, aquí 4 horas. El slider va de 1 a 24.
- 2 Yes. En roles de Entra, **si no eliges approvers, los Privileged Role Administrators y Global Administrators activos son los approvers por default**.
- 3 No. El ticket es **solo informativo**. PIM no lo valida contra ningún sistema.

**Por qué las otras no:**
- Trampa de la 1: confundir el máximo que pone el admin con lo que pide el usuario.
- Trampa de la 2: aplicar la regla de Azure resources y PIM for Groups, donde **no hay approvers por default**.
- Trampa de la 3: creer que PIM se integra con ServiceNow para validar tickets.

**Fuente:** https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings#require-approval-to-activate y https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings#activation-maximum-duration

---

### Q23 · PIM request and approval process · Multiple choice

A user requests activation of the SharePoint Administrator role, which requires approval. The designated approvers don't respond.

How long do they have before the user must submit a new request?

A. 8 hours
B. The same time as the role's activation maximum duration
C. 24 hours, and this window isn't configurable
D. 7 days, configurable in the role settings

**Respuesta:** C

**Por qué es correcta:** Learn dice que los approvers delegados tienen **24 horas** para aprobar. Si no, el usuario debe mandar una nueva solicitud. **Esa ventana no se configura.**

**Por qué las otras no:**
- A: 8 horas no es la ventana de aprobación.
- B: la duración máxima de activación es cuánto dura el rol activo, no cuánto espera la aprobación.
- D: no hay un setting de días para la aprobación de roles de Entra.

**Fuente:** https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-approval-workflow#overview

---

### Q24 · PIM for Azure resources (settings and assignments) · Drag/order

The Prod subscription is already visible in PIM > Azure resources. Members of the DevOps group must get the Contributor role on Prod only when needed, and each activation must be approved by the Platform leads.

Which four actions should you perform in sequence?

Actions:
- A. Sign in as an Owner or User Access Administrator of the Prod subscription and open Prod in PIM > Azure resources.
- B. Open Settings, edit the Contributor role, set Require approval to activate, and select the Platform leads as approvers.
- C. Open Roles, select Add assignments, choose Contributor and the DevOps group, and set the assignment type to Eligible.
- D. A DevOps member activates Contributor from My roles > Azure resources, and a Platform lead approves the request.
- E. Configure the Contributor role settings on the root management group so that every subscription and resource group inherits them.
- F. Make the DevOps pipeline managed identity eligible for Contributor.

**Respuesta:** A, B, C, D

**Por qué es correcta:** Los settings de roles de Azure resources los cambia un **Owner o User Access Administrator** del recurso. Primero ajustas el setting del rol (aprobación y approvers), luego creas la asignación **Eligible** y, al final, el usuario activa y el approver aprueba.

**Por qué las otras no:**
- E: los role settings **no se heredan** de un nivel alto a uno bajo. Cada recurso y cada rol tiene los suyos.
- F: no se crean asignaciones eligible para aplicaciones, service principals ni managed identities, porque no pueden hacer los pasos de activación.

Nota: en la experiencia legacy primero hacías **Discover resources > Manage resource**, y eso asigna el service principal MS-PIM como User Access Administrator. La experiencia nueva maneja Azure resources sin onboarding.

**Fuente:** https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-resource-roles-configure-role-settings#overview y https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-resource-roles-assign-roles#assign-a-role

---

### Q25 · PIM for Azure resources (settings) · Multiple choice

In PIM, you configure the Owner role settings on the subscription Sub1 to require approval. Kim is eligible for the Owner role on the resource group RG1, which is inside Sub1. Kim activates Owner on RG1 without any approval.

Why?

A. Approval is supported only for Microsoft Entra roles.
B. Role settings configured on the subscription aren't inherited by the resource group.
C. The Owner role can't require approval in PIM.
D. RG1 wasn't discovered, so PIM ignores its settings.

**Respuesta:** B

**Por qué es correcta:** Learn: las role settings son **por rol y por recurso**, y lo que configuras en un nivel alto como Subscription **no se hereda** en un nivel más bajo como Resource Group. RG1 tiene su propia policy del rol Owner, sin aprobación.

**Por qué las otras no:**
- A: la aprobación existe en roles de Entra, Azure resources y PIM for Groups.
- C: Owner sí puede pedir aprobación. De hecho, Learn lo usa como ejemplo en el plan de PIM.
- D: los hijos de un recurso ya manejado entran en PIM. El problema no es el discovery.

**Fuente:** https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-resource-roles-configure-role-settings#overview

---

### Q26 · PIM for Groups · Multiple choice

SQL-Admins is a cloud security group that isn't role-assignable. Membership gives access to Azure SQL. You want members to activate their membership just-in-time with approval.

Which statement is true?

A. You must first convert SQL-Admins into a role-assignable group.
B. You can enable SQL-Admins in PIM for Groups, because the group doesn't have to be role-assignable.
C. PIM for Groups supports only Microsoft 365 groups.
D. You can enable PIM for Groups only if the group uses dynamic membership.

**Respuesta:** B

**Por qué es correcta:** Desde enero de 2023, **cualquier security group o Microsoft 365 group** puede entrar a PIM for Groups, sea role-assignable o no. Las excepciones son los grupos **dinámicos** y los **sincronizados desde on-premises**.

**Por qué las otras no:**
- A: ser role-assignable ya no es requisito. Además, un grupo existente no se convierte en role-assignable.
- C: funciona con security groups y con Microsoft 365 groups.
- D: al revés. Los grupos dinámicos **no** se pueden usar en PIM for Groups.

**Fuente:** https://learn.microsoft.com/entra/id-governance/privileged-identity-management/concept-pim-for-groups#relationship-between-role-assignable-groups-and-pim-for-groups

---

### Q27 · PIM for Groups and role-assignable groups · Select two

The group Tier1-Admins has an active assignment to a Microsoft Entra administrator role. Helpdesk engineers get eligible membership of Tier1-Admins through PIM for Groups.

Which two recommendations from Microsoft Learn should you follow? Each correct answer presents part of the solution.

A. Create Tier1-Admins as a role-assignable group, so that roles like Helpdesk Administrator can't reset the credentials of its members.
B. Require approval for activation of eligible member assignments.
C. Add the group Tier2-Admins as an active member of Tier1-Admins.
D. Use PIM for Groups instead of PIM for Microsoft Entra roles for Exchange Administrator, to avoid activation delays.
E. Configure a single policy that covers both membership and ownership of Tier1-Admins.

**Respuesta:** A y B

**Por qué es correcta:**
- A: en un grupo **role-assignable** nadie más cambia las credenciales de sus miembros y owners, **incluso los eligible que aún no activan**. Así un admin de menor nivel no resetea una contraseña para activar en nombre de otro.
- B: Learn recomienda **pedir aprobación** en las asignaciones eligible de grupos que elevan a roles de Entra.

**Por qué las otras no:**
- C: un grupo role-assignable **no puede tener grupos anidados como miembros activos**. Solo se permite como eligible.
- D: es al revés. Para SharePoint, Exchange o Purview, Learn recomienda **PIM for Microsoft Entra roles** para evitar demoras.
- E: cada grupo tiene **dos policies**, una para membership y otra para ownership.

**Fuente:** https://learn.microsoft.com/entra/id-governance/privileged-identity-management/concept-pim-for-groups#what-are-microsoft-entra-role-assignable-groups

---

### Q28 · Create and manage break-glass accounts · Yes/No series

Contoso configures two emergency access accounts, bg1@contoso.onmicrosoft.com and bg2@contoso.onmicrosoft.com:
- Both are cloud-only.
- Each one has a FIDO2 security key stored in a separate safe. Regular admins use Microsoft Authenticator.
- In PIM, both accounts are eligible for Global Administrator, and activation requires approval.
- Both accounts are excluded from every Conditional Access policy that blocks or restricts sign-in.

For each of the following statements, select Yes or No.

1. The Global Administrator assignment of the two accounts follows Microsoft recommendations.
2. The two accounts must also be excluded from Conditional Access policies in Report-only mode.
3. Using FIDO2 security keys for these accounts, while regular admins use Microsoft Authenticator, follows Microsoft recommendations.

**Respuesta:** 1 = No, 2 = No, 3 = Yes

**Por qué es correcta:**
- 1 No. Learn pide que el rol Global Administrator de las cuentas de emergencia sea **active permanent**, no eligible. Si la emergencia es justo que nadie puede aprobar, la cuenta no sirve.
- 2 No. Las políticas en **Report-only** no bloquean nada, así que no necesitan exclusión.
- 3 Yes. Learn pide un método fuerte (passkey FIDO2 o CBA) y **distinto** al que usan los admins normales.

**Por qué las otras no:**
- Trampa de la 1: pensar que "todo admin va eligible". Las break-glass son la excepción.
- Trampa de la 2: excluir de más. La regla es excluir de las políticas que bloquean o restringen.
- Trampa de la 3: el mito viejo de "break-glass sin MFA". Hoy se recomienda un método phishing-resistant que cumpla la MFA obligatoria.

**Fuente:** https://learn.microsoft.com/entra/identity/role-based-access-control/security-emergency-access#configuration-requirements y https://learn.microsoft.com/entra/identity/role-based-access-control/security-emergency-access#conditional-access-considerations

---

### Q29 · Create and manage break-glass accounts (monitoring) · Multiple choice (KQL)

Contoso sends Microsoft Entra sign-in logs to a Log Analytics workspace. You create an Azure Monitor alert rule with the signal Custom log search and the alert logic "Greater than 0". The alert must fire on **any** sign-in attempt, successful or failed, by the two emergency access accounts. Their object IDs are 00aa00aa-bb11-cc22-dd33-44ee44ee44ee and 11bb11bb-cc22-dd33-ee44-55ff55ff55ff.

Which query should you use in the alert rule?

A.
```kusto
SigninLogs
| where UserId == "00aa00aa-bb11-cc22-dd33-44ee44ee44ee" or UserId == "11bb11bb-cc22-dd33-ee44-55ff55ff55ff"
| project TimeGenerated, UserPrincipalName, UserId, IPAddress, ResultType, ResultDescription
```

B.
```kusto
SigninLogs
| where UserId in ("00aa00aa-bb11-cc22-dd33-44ee44ee44ee", "11bb11bb-cc22-dd33-ee44-55ff55ff55ff")
| where ResultType == "0"
| project TimeGenerated, UserPrincipalName, UserId, IPAddress
```

C.
```kusto
AuditLogs
| where OperationName has "Add member to role"
| where tostring(TargetResources) has "00aa00aa-bb11-cc22-dd33-44ee44ee44ee"
```

D.
```kusto
AADServicePrincipalSignInLogs
| where ServicePrincipalId in ("00aa00aa-bb11-cc22-dd33-44ee44ee44ee", "11bb11bb-cc22-dd33-ee44-55ff55ff55ff")
```

**Respuesta:** A

**Por qué es correcta:** Es la query que Learn usa para las cuentas de emergencia: filtra **SigninLogs** por el object ID (UserId) de cada cuenta y no filtra por resultado. Así cuenta los intentos buenos y los fallidos, y con umbral mayor que 0 la alerta salta en cualquier uso.

**Por qué las otras no:**
- B: ResultType "0" es solo éxito. Se pierden los intentos fallidos, que también hay que investigar.
- C: AuditLogs registra cambios, como agregar a un rol. No registra inicios de sesión.
- D: las cuentas break-glass son usuarios, no service principals. Esa tabla no tendrá nada de ellas.

**Fuente:** https://learn.microsoft.com/entra/identity/role-based-access-control/security-emergency-access#create-an-alert-rule

---

### Q30 · PIM request and approval process · Select two

Which two statements about approvals for Microsoft Entra roles in PIM are true? Each correct answer presents a complete solution.

A. An approver must hold a Microsoft Entra administrator role.
B. A request is resolved by the first approver who approves or denies it.
C. A user who is also an approver can approve their own activation request.
D. A service principal can approve activation requests through Microsoft Graph.
E. All approvers are notified when one approver responds to the request.

**Respuesta:** B y E

**Por qué es correcta:**
- B: en PIM **la primera decisión resuelve** la solicitud, sea approve o deny.
- E: cuando un approver responde, **todos los approvers reciben aviso**.

**Por qué las otras no:**
- A: Learn dice que el approver **no necesita tener ningún rol**.
- C: nadie aprueba su propia activación.
- D: los service principals **no pueden** aprobar solicitudes.

**Fuente:** https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-approval-workflow#workflow-notifications y https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-approval-workflow#approve-requests

---

### Case study 2: Litware (Q31 y Q32)

Litware Inc. has 40 administrators with eligible assignments to Microsoft Entra roles in PIM. Microsoft Entra sign-in and audit logs are sent to a Log Analytics workspace by using diagnostic settings.

Security requirements:
- R1: Activating the Security Administrator role must require a phishing-resistant authentication method at the moment of activation, even if the admin already completed MFA earlier in the same session.
- R2: For a single activation, auditors need every related audit event: request, approval, activation, and later deactivation. Some activations use approval and a scheduled start time.
- R3: PIM audit data must be kept for one year.

### Q31 · PIM for Microsoft Entra roles (settings) · Multiple choice (case study 2)

Which configuration meets R1?

A. In the Security Administrator role settings, select On activation, require Azure MFA.
B. Create a Conditional Access authentication context, create a Conditional Access policy for that context with a phishing-resistant authentication strength that targets all users, and select that authentication context in the Security Administrator role settings.
C. In the Security Administrator role settings, select Require multifactor authentication on active assignment.
D. Create a Conditional Access policy that targets the Security Administrator directory role and requires a phishing-resistant authentication strength.

**Respuesta:** B

**Por qué es correcta:** "On activation, require Microsoft Entra Conditional Access **authentication context**" junto con **authentication strengths** obliga a autenticar en la activación con el método que pides. La política de CA del contexto debe incluir a todos los usuarios o a los eligible.

**Por qué las otras no:**
- A: Learn avisa que con "require MFA" el usuario **puede no recibir el prompt** si ya hizo MFA antes en la sesión. No cumple "aunque ya haya hecho MFA".
- C: ese setting aplica al admin que **crea** una asignación active, no a la activación.
- D: durante la activación el usuario **todavía no tiene el rol**, así que una política dirigida al rol no aplica en ese momento.

**Fuente:** https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-how-to-change-default-settings#on-activation-require-multifactor-authentication

---

### Q32 · PIM audit history and reports · Multiple choice (KQL, case study 2)

You have the roleAssignmentRequestId of one activation. Which query returns all audit events for its full activation and deactivation cycle, as required by R2?

A.
```kusto
let requestCorrelation = "c0ffee00-1111-2222-3333-444455556666";
AuditLogs
| where CorrelationId == requestCorrelation
```

B.
```kusto
let roleAssignmentRequestId = "a1b2c3d4-0000-1111-2222-333344445555";
let relatedCorrelationIds = AuditLogs
    | where AdditionalDetails has roleAssignmentRequestId
    | summarize make_set(CorrelationId);
AuditLogs
| where AdditionalDetails has roleAssignmentRequestId
    or CorrelationId in (relatedCorrelationIds)
```

C.
```kusto
SigninLogs
| where CorrelationId == "a1b2c3d4-0000-1111-2222-333344445555"
```

D.
```kusto
AuditLogs
| where OperationName has "Add member to role"
| take 1
```

**Respuesta:** B

**Por qué es correcta:** En PIM, una activación con aprobación o con inicio programado se procesa en pasos asíncronos, y **el CorrelationId puede cambiar**. El que no cambia es **roleAssignmentRequestId**, que queda en AdditionalDetails, incluso en la desactivación. La query B junta ese ID con todos los CorrelationId relacionados.

**Por qué las otras no:**
- A: con un solo CorrelationId se pierden los pasos que tienen otro.
- C: SigninLogs no guarda eventos de PIM.
- D: trae un evento cualquiera de activación, no el ciclo completo de esa solicitud.

Para R3: el Resource audit de PIM guarda **30 días**. Para un año, se envían los AuditLogs con diagnostic settings a una storage account o a Log Analytics con la retención adecuada.

**Fuente:** https://learn.microsoft.com/entra/id-governance/privileged-identity-management/pim-how-to-use-audit-log#correlating-events-related-to-the-same-activation-cycle

---

## Subdominio 4: Monitor identity activity by using logs, workbooks, and reports

### Q33 · Review and analyze sign-in, audit, and provisioning logs (retention) · Multiple choice

Fabrikam used Microsoft Entra ID Free and never exported its logs. Today, Fabrikam buys Microsoft Entra ID P1. An investigator needs the sign-in logs from 20 days ago.

What can you tell the investigator?

A. The data isn't available. Only up to seven days of data from the Free period can be seen.
B. 30 days of data are available right away, because P1 keeps 30 days.
C. The data will appear within three days of the upgrade.
D. The data can be restored by opening a support request.

**Respuesta:** A

**Por qué es correcta:** Free guarda **7 días** de sign-ins y audit. Learn dice que el cambio de retención **no es retroactivo**: al pasar a P1 solo ves lo que seguía dentro de los 7 días. Lo que ya venció no vuelve, salvo que lo hubieras exportado.

**Por qué las otras no:**
- B: los 30 días de P1 cuentan hacia adelante, no hacia atrás.
- C: los "hasta tres días" aplican cuando **no había datos** y empiezan a aparecer después del upgrade. No recuperan datos vencidos.
- D: soporte no restaura logs que ya se borraron.

**Fuente:** https://learn.microsoft.com/entra/identity/monitoring-health/reference-reports-data-retention#activity-reports

---

### Q34 · Review and analyze sign-in, audit, and provisioning logs · Yes/No series

For each of the following statements, select Yes or No.

1. A client app that uses an OAuth 2.0 refresh token to get a new access token for a user is recorded in the non-interactive user sign-in logs.
2. A virtual machine that uses a managed identity to get a token for Azure Key Vault is recorded in the service principal sign-in logs.
3. The provisioning logs can show the status Skipped for a user that doesn't match a scoping filter.

**Respuesta:** 1 = Yes, 2 = No, 3 = Yes

**Por qué es correcta:**
- 1 Yes. Los **non-interactive** son sign-ins hechos a nombre del usuario, como renovar un token con un refresh token, sin que el usuario dé un factor.
- 2 No. Eso va en **managed identity sign-ins**, un log separado del de service principals.
- 3 Yes. Status puede ser Success, Failure, Skipped o Warning. **Skipped** sale, por ejemplo, cuando un scoping filter deja fuera al usuario.

**Por qué las otras no:**
- Trampa de la 1: creer que todo sign-in de usuario es interactive.
- Trampa de la 2: juntar service principal y managed identity en un solo log.
- Trampa de la 3: pensar que Skipped significa error.

**Fuente:** https://learn.microsoft.com/entra/identity/monitoring-health/concept-sign-ins#what-are-the-types-of-sign-in-logs y https://learn.microsoft.com/entra/identity/monitoring-health/concept-provisioning-logs#what-do-the-logs-show

---

### Q35 · Configure diagnostic settings · Select two

Contoso has two requirements for Microsoft Entra audit and sign-in logs:
- Keep them for two years, at low cost, for compliance. They will rarely be queried.
- Stream them in near real time to a third-party SIEM.

Which two destinations should you configure in diagnostic settings? Each correct answer presents part of the solution.

A. An Azure storage account
B. An event hub
C. A Log Analytics workspace
D. A Microsoft Entra workbook
E. The Identity Secure Score dashboard

**Respuesta:** A y B

**Por qué es correcta:** Learn: para guardar más de 30 días y consultar poco, **storage account**. Para un SIEM que no es de Microsoft, **event hub**. Puedes tener varias diagnostic settings con destinos distintos.

**Por qué las otras no:**
- C: Log Analytics es para consultar seguido con KQL, workbooks y alertas. Sirve, pero no es la opción barata para archivo ni el canal hacia un SIEM de terceros.
- D: un workbook lee de Log Analytics. No es un destino de diagnostic settings.
- E: Secure Score no recibe logs.

**Fuente:** https://learn.microsoft.com/entra/identity/monitoring-health/concept-log-monitoring-integration-options-considerations#integration-options

---

### Q36 · Configure diagnostic settings (Log Analytics) · Drag/order

You need to run KQL queries on Microsoft Entra sign-in and audit logs in the Microsoft Entra admin center.

Which four actions should you perform in sequence?

Actions:
- A. Create a Log Analytics workspace in an Azure subscription.
- B. Sign in to the Microsoft Entra admin center as a Security Administrator and browse to Entra ID > Monitoring & health > Diagnostic settings.
- C. Add a diagnostic setting, select the AuditLogs and SignInLogs categories, select Send to Log Analytics workspace, and save.
- D. Browse to Entra ID > Monitoring & health > Log Analytics and run the queries.
- E. Create a Microsoft Entra workbook so that data starts flowing to the workspace.
- F. Assign the Reports Reader role to the Log Analytics workspace.

**Respuesta:** A, B, C, D

**Por qué es correcta:** El destino **tiene que existir antes** de crear la diagnostic setting. La setting la crea un **Security Administrator**: eliges las categorías y el workspace. Luego consultas en Log Analytics. Learn avisa que los datos pueden tardar en aparecer.

**Por qué las otras no:**
- E: el workbook lee datos que ya están en el workspace. No los envía.
- F: Reports Reader es un rol de Entra para personas. No se asigna a un workspace.

**Fuente:** https://learn.microsoft.com/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs#send-logs-to-azure-monitor

---

### Q37 · Monitor Microsoft Entra ID by using KQL queries in Log Analytics · Multiple choice (KQL)

Provisioning logs are sent to Log Analytics. You need a list of error codes from failed provisioning operations in the last 24 hours, with how many times each one happened and when it was last seen.

Which query should you run?

A.
```kusto
AADProvisioningLogs
| where TimeGenerated > ago(1d)
| where ResultType == "Failure"
| summarize Occurrences = count(), LastSeen = max(TimeGenerated) by ResultSignature
| order by Occurrences desc
```

B.
```kusto
AADProvisioningLogs
| where TimeGenerated > ago(1d)
| where ResultType == "Skipped"
| summarize Occurrences = count(), LastSeen = max(TimeGenerated) by ResultSignature
| order by Occurrences desc
```

C.
```kusto
SigninLogs
| where TimeGenerated > ago(1d)
| where ResultType != "0"
| summarize Occurrences = count(), LastSeen = max(TimeGenerated) by ResultType
```

D.
```kusto
AuditLogs
| where TimeGenerated > ago(1d)
| where Result == "failure"
| summarize Occurrences = count() by OperationName
```

**Respuesta:** A

**Por qué es correcta:** Los eventos de provisioning viven en **AADProvisioningLogs**. Ahí ResultType puede ser Success, Failure o Skipped, y **ResultSignature** trae el código de error. La query A cuenta cada código y saca la fecha más reciente.

**Por qué las otras no:**
- B: Skipped no es un fallo. Suele ser un usuario fuera de scope.
- C: SigninLogs son inicios de sesión, no operaciones de provisioning.
- D: AuditLogs muestra cambios del directorio. Los detalles del provisioning a apps van en su propia tabla.

**Fuente:** https://learn.microsoft.com/azure/azure-monitor/reference/tables/aadprovisioninglogs#columns y https://learn.microsoft.com/entra/identity/monitoring-health/howto-analyze-activity-logs-log-analytics#query-activity-logs

---

### Q38 · Monitor Microsoft Entra ID by using KQL queries in Log Analytics · Multiple choice (KQL)

Contoso has one diagnostic setting that sends the AuditLogs and SignInLogs categories to a Log Analytics workspace. It has been working for two months. An analyst runs this query and gets no results:

```kusto
AADNonInteractiveUserSignInLogs
| where TimeGenerated > ago(1d)
| summarize CountPerIPAddress = count() by IPAddress
| order by CountPerIPAddress desc
| take 100
```

What should you do so the query returns data?

A. Edit the diagnostic setting and add the NonInteractiveUserSignInLogs category.
B. Upgrade the tenant from Microsoft Entra ID P1 to P2.
C. Add the ServicePrincipalSignInLogs category.
D. Change ago(1d) to ago(30d), because non-interactive sign-ins are written once a month.

**Respuesta:** A

**Por qué es correcta:** Cada categoría de la diagnostic setting llena **su propia tabla**. SignInLogs llena la tabla SigninLogs (interactive). La tabla **AADNonInteractiveUserSignInLogs** solo recibe datos si activas la categoría **NonInteractiveUserSignInLogs**.

**Por qué las otras no:**
- B: P1 ya alcanza para enviar logs a Log Analytics. La licencia no es el problema.
- C: ServicePrincipalSignInLogs llena otra tabla, la de apps y service principals.
- D: los sign-ins non-interactive se registran todo el tiempo. El rango de fechas no es el problema.

**Fuente:** https://learn.microsoft.com/entra/identity/monitoring-health/concept-diagnostic-settings-logs-options#activity-log-options

---

### Q39 · Analyze Microsoft Entra ID by using workbooks and reporting · Multiple choice

Contoso has Microsoft Entra ID P1. A Security Reader opens the Sign-ins workbook template in Entra ID > Monitoring & health > Workbooks, but every chart is empty. No diagnostic settings exist in the tenant.

What should you do first?

A. Configure a diagnostic setting that sends the sign-in logs to a Log Analytics workspace, and use that workspace in the workbook.
B. Assign Microsoft Entra ID P2 licenses to all users.
C. Archive the sign-in logs to a storage account.
D. Wait 24 hours for the Identity Secure Score to recalculate.

**Respuesta:** A

**Por qué es correcta:** Los workbooks de Entra piden **P1, un Log Analytics workspace y los logs enviados ahí**. Sin diagnostic setting, el workspace no tiene datos y los gráficos salen vacíos.

**Por qué las otras no:**
- B: P1 ya cumple el requisito de licencia de los workbooks.
- C: los workbooks no leen de una storage account.
- D: Secure Score no tiene nada que ver con los datos de un workbook.

**Fuente:** https://learn.microsoft.com/entra/identity/monitoring-health/howto-use-workbooks#prerequisites

---

### Q40 · Monitor and improve the security posture by using Identity Secure Score · Multiple choice

Contoso protects every user with a non-Microsoft MFA solution. The Identity Secure Score improvement action "Ensure all users can complete MFA" still shows as not done. You want the score to reflect that the risk is covered.

Which status should you set on the improvement action?

A. Planned
B. Risk accepted
C. Resolved through third party
D. To address

**Respuesta:** C

**Por qué es correcta:** Con **Resolved through third party** (o Resolved through alternate mitigation) **recibes los puntos** de la acción, porque ya la cubre otra herramienta. Learn aclara que Microsoft no puede ver si esa herramienta está completa.

**Por qué las otras no:**
- A: Planned solo dice que hay un plan. No da puntos.
- B: Risk accepted **no da puntos** y quita la acción de la lista.
- D: To address dice que la vas a atender en el futuro. No da puntos.

Dato extra: el score se recalcula **cada 24 horas**, así que el cambio no se ve en el momento.

**Fuente:** https://learn.microsoft.com/entra/identity/monitoring-health/concept-identity-secure-score#how-do-i-use-the-identity-secure-score
