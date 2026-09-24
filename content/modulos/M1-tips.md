# M1 Tips and tricks: Implement and manage user identities (20 a 25%)

Bloque en vivo de 15 minutos. 12 trampas, más o menos 1 minuto cada una, y 3 minutos para preguntas.
Cada trampa trae: la frase que dice el presenter, la regla, las palabras de la pregunta que delatan la respuesta y el link al párrafo exacto en Learn.
Las preguntas del banco que practican cada trampa van al final de cada bloque.

---

## Trampa 1. AU normal vs restricted management AU

Frase clave: **"El AU normal recorta al admin; el restricted AU blinda al objeto."**

Regla:
- AU normal: limita lo que hace quien recibe el rol con scope, pero los admins de tenant siguen mandando. Meter un grupo al AU no mete a sus miembros y los AUs no se anidan.
- Restricted AU: ni el Global Admin modifica esos objetos sin una asignación en ese scope. Se elige solo al crear el AU y no acepta Microsoft 365 groups.

Palabras que delatan: "even Global Administrators", "only the ExecSupport team", "protect executive accounts", "without removing tenant-level role assignments", "members of the group".

Link: https://learn.microsoft.com/entra/identity/role-based-access-control/admin-units-restricted-management#who-can-modify-objects

Practica: Q3, Q4, Q6

---

## Trampa 2. Custom roles

Frase clave: **"Custom role: menú cerrado, P1 por usuario y cero clonar built-ins."**

Regla:
- Solo lleva permisos habilitados para custom (app registrations, enterprise apps, consent, devices, users, groups) y cada usuario asignado necesita Microsoft Entra ID P1.
- Se asigna a tenant, a una app registration, o a un AU si trae permisos de users, groups o devices. Solo puedes clonar desde otro custom role.

Palabras que delatan: "only for the Payroll-API app registration", "update credentials of a specific app", "least privilege", "clone".

Link: https://learn.microsoft.com/entra/identity/role-based-access-control/custom-create#create-a-custom-role

Practica: Q2

---

## Trampa 3. Effective permissions: quién resetea a quién

Frase clave: **"Helpdesk no resetea a los de arriba, y el Global Admin no ve Azure hasta que se eleva."**

Regla:
- La matriz manda: Password Admin resetea poco, Helpdesk un poco más, User Admin más, y a los miembros de un role-assignable group solo los tocan Privileged Authentication Admin y Global Admin.
- Entra roles y Azure RBAC son sistemas separados. El GA se eleva con "Access management for Azure resources" y recibe User Access Administrator en el root scope.

Palabras que delatan: "must not be able to reset passwords for User Administrators", "member of a role-assignable group", "can't see any subscriptions", "assign Azure roles in every subscription".

Link: https://learn.microsoft.com/entra/identity/role-based-access-control/privileged-roles-permissions#who-can-reset-passwords

Practica: Q1, Q7, Q8

---

## Trampa 4. Dynamic groups y device identity

Frase clave: **"-and pega más fuerte que -or. Y en devices: AzureAD es joined, ServerAD es hybrid, Workplace es registered."**

Regla:
- Una regla es de users o de devices, nunca ambos. M365 groups solo aceptan users, el rule builder solo sirve para users, y `user.objectId -ne null` incluye guests.
- "Users may join devices" y el límite de 50 devices no aplican a hybrid join. Deshabilitar un device revoca su PRT.

Palabras que delatan: "only member users", "exclude guests", "Sales or Marketing", "hybrid joined Windows devices", "personal devices", "Group Policy and imaging".

Link: https://learn.microsoft.com/entra/identity/users/groups-dynamic-membership#operator-precedence

Practica: Q15, Q16, Q19

---

## Trampa 5. Group-based licensing

Frase clave: **"Primero agrega al grupo nuevo, confirma, y luego quita del viejo."**

Regla:
- Sin UsageLocation no hay licencia directa. En licencias por grupo, el usuario sin ubicación hereda la del tenant. Los grupos anidados no reparten licencia al segundo nivel.
- E1 y E3 juntos chocan por Exchange Online Plan 1 y Plan 2. El error es conflicting service plans, no falta de licencias.

Palabras que delatan: "must not lose access", "error although licenses are available", "nested group", "Set-MgUserLicense fails".

Link: https://learn.microsoft.com/microsoft-365/admin/manage/manage-group-licenses#move-users-between-licensed-groups

Practica: Q12, Q17, Q18

---

## Trampa 6. UserType no es dónde se autentica

Frase clave: **"UserType es el nivel de permiso; Identities dice dónde se autentica."**

Regla:
- Member o Guest solo define la relación con la organización. Cambiar a Member no vuelve interna la cuenta; para eso existe Convert to internal user.
- Si el guest cambió de empresa o de correo, usa reset redemption status: conserva object ID, grupos y apps. Helpdesk Administrator basta.

Palabras que delatan: "keep group memberships and app assignments", "moved to another company", "sign in with a new email", "external member".

Link: https://learn.microsoft.com/entra/external-id/user-properties#user-type

Practica: Q24

---

## Trampa 7. Invitar guests: settings, listas y bulk

Frase clave: **"Guest Inviter brinca el candado de 'solo admins', pero no el de 'nadie'."**

Regla:
- Es allow list o block list, nunca las dos, y no saca a los guests que ya redimieron (una invitación pendiente sí falla).
- Bulk create no invita. Bulk invite pide Email address to invite y Redirection url. `New-MgInvitation` sin `-SendInvitationMessage` no manda correo.

Palabras que delatan: "only users assigned to specific admin roles", "one non-admin must invite", "block gmail.com", "existing guests", "land on My Apps".

Link: https://learn.microsoft.com/entra/external-id/allow-deny-list#important-considerations

Practica: Q11, Q21, Q22, Q23

---

## Trampa 8. Cross-tenant access settings

Frase clave: **"Trust MFA siempre es inbound y se configura en el tenant de recursos."**

Regla:
- Organizational settings le ganan a default settings. Trust settings y scoping por usuario o app requieren P1 en el tenant que configuras.
- B2B collaboration viene permitido por default y B2B direct connect viene bloqueado. Direct connect es para Teams shared channels.

Palabras que delatan: "already completed MFA in their home tenant", "only for Fabrikam", "all other partners must keep", "shared channels".

Link: https://learn.microsoft.com/entra/external-id/cross-tenant-access-overview#organizational-settings

Practica: Q25

---

## Trampa 9. Cross-tenant synchronization

Frase clave: **"El source empuja; el target solo abre la puerta."**

Regla:
- Configuración, scope y mappings viven en el source (P1 solo ahí). El target activa "Allow user synchronization into this tenant", y ambos marcan automatic redemption.
- Crea external members por default, sincroniza solo internal members, corre cada 40 minutos y no sirve para migrar usuarios entre tenants.

Palabras que delatan: "multitenant organization", "no invitation emails or consent prompts", "removed automatically when they leave", "member-level access", "source tenant has not enabled automatic user consent".

Link: https://learn.microsoft.com/entra/identity/multi-tenant-organizations/cross-tenant-synchronization-overview#properties

Practica: Q26, Q27, Q29, Q30

---

## Trampa 10. PHS es el paracaídas

Frase clave: **"PHS es el paracaídas, pero no se abre solo."**

Regla:
- PTA valida contra AD en el momento del sign-in (disabled, lockout, logon hours) y pide mínimo 3 agentes en producción. Federación depende de AD FS.
- Habilita PHS siempre: da leaked credentials y es el respaldo, pero cambiar el método de sign-in en Entra Connect es manual.

Palabras que delatan: "on-premises outage", "ransomware", "enforce logon hours at sign-in", "leaked credentials", "without deploying new infrastructure".

Link: https://learn.microsoft.com/entra/identity/hybrid/connect/choose-ad-authn#detailed-considerations

Practica: Q31, Q32, Q33, Q39

---

## Trampa 11. Seamless SSO y staged rollout

Frase clave: **"Seamless SSO solo baila con PHS o PTA; con AD FS ni entra a la pista."**

Regla:
- Necesita device domain-joined en la red, la URL autologon en la Intranet zone por GPO y rollover de la key de AZUREADSSOACC cada 30 días. En Windows 10 o posterior, el SSO va por PRT.
- Staged rollout prueba PHS o PTA antes del cutover con grupos cloud (sin nested ni dinámicos, máximo 10 por feature). No convierte el dominio: eso es `Update-MgDomain -AuthenticationType "Managed"`.

Palabras que delatan: "domain-joined Windows 8.1", "still prompted for a password", "pilot group before converting the domain", "federated with AD FS".

Link: https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-staged-rollout#unsupported-scenarios

Practica: Q34, Q38

---

## Trampa 12. Connect Sync vs Cloud Sync

Frase clave: **"Forest desconectado o varios agentes activos: Cloud Sync. Hybrid join, PTA o reglas complejas: Connect Sync."**

Regla:
- Connect Sync es Active-Passive: staging mode importa y sincroniza, pero no exporta ni hace PHS. Trae el agente de Connect Health, que pide P1 (1 licencia para el primer agente y 25 por cada agente extra).
- Cloud Sync sincroniza cada 2 minutos, recomienda 3 agentes activos y llega a 150K objetos por dominio. Ojo: la tabla actual de Learn marca Exchange hybrid como soportado en los dos.

Palabras que delatan: "merger or acquisition", "no network connectivity between forests", "Microsoft Entra hybrid join", "more than 150,000 objects", "standby server", "health alerts".

Link: https://learn.microsoft.com/entra/identity/hybrid/cloud-sync/connect-to-cloud-sync-decision-guide#comparison-between-microsoft-entra-connect-and-cloud-sync

Practica: Q35, Q36, Q37, Q40

---

## Objetivo de la sesión

El presenter no tiene que recitar límites ni números. Tiene que entender que casi todas las preguntas de M1 se resuelven con tres preguntas: **el alcance** (quién puede hacer qué y sobre quién: AU, restricted AU, custom role, matriz de reset), **la dirección** (en qué tenant y en qué lado se configura: inbound vs outbound, source vs target, member vs guest) y **la dependencia de on-prem** (qué deja de funcionar si se cae AD: PTA y federación sí, PHS no). Si el presenter puede tomar cualquier pregunta del banco, señalar las dos o tres palabras que la delatan y explicar con sus palabras por qué cada distractor falla, la sesión cumplió. Los números (50 devices, 500 deletes, 40 minutos, 150K objetos) se quedan en la guía para consulta, no se memorizan en vivo.

---

## Orden sugerido de slides (10)

| # | Título | Para qué sirve |
|---|---|---|
| 1 | M1 en un vistazo | Mostrar los 4 subdominios, el peso de 20 a 25% y las tres preguntas mágicas: alcance, dirección y dependencia de on-prem. |
| 2 | Delegar sin regalar el tenant | Comparar AU, restricted AU y custom role en una sola tabla (trampas 1 y 2). |
| 3 | ¿Quién resetea a quién? | Enseñar la escalera de reset y por qué el Global Admin no ve Azure sin elevarse (trampa 3). |
| 4 | Grupos y devices que se llenan solos | Leer reglas dinámicas en voz alta, cazar el error de precedencia y memorizar AzureAD, ServerAD y Workplace (trampa 4). |
| 5 | Licencias por grupo sin sustos | Usage location, conflicto E1 con E3 y el orden correcto para mover usuarios (trampa 5). |
| 6 | Guest, member, external, internal | Separar permiso de autenticación, reset redemption e invitaciones en bulk (trampas 6 y 7). |
| 7 | Cross-tenant: quién abre y quién empuja | Dibujar dos tenants con flechas: trust inbound en recursos, sync push desde el source (trampas 8 y 9). |
| 8 | Si se cae on-prem | Árbol de decisión PHS, PTA y federación, con el paracaídas manual (trampa 10). |
| 9 | De AD FS a la nube | Seamless SSO, staged rollout y el cutover del dominio en orden (trampa 11). |
| 10 | Connect Sync vs Cloud Sync | Tabla de decisión, staging mode y Connect Health como cierre antes del Kahoot (trampa 12). |
