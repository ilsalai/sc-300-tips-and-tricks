# Notas del presentador · Sesión 5 · Labs, estrategia y simulacro

Una entrada por slide: objetivo, frase clave, trampa favorita del examen, qué preguntas del banco la practican y tiempo. No es un guion para leer; es lo que hay que entender para transmitirlo con tus palabras.

## 1. Labs, estrategia y simulacro

Objetivo: abrir la última sesión con energía y dejar claro que hoy no hay módulo nuevo: hoy se practica cómo aprobar. Frase clave: "Ya estudiaron los cuatro módulos; hoy aprendemos a leer el examen, a reconocer las pantallas de los labs y a medirnos con un simulacro". Recordar que los labs se ven en imágenes con capturas oficiales de Learn, no en tenant. Tiempo: 30 segundos.

## 2. Última sesión: de estudiar a aprobar

Objetivo: fijar expectativas en 30 segundos. Hoy no hay Kahoot: el simulacro de 30 preguntas lo hacen por su cuenta y lo revisamos en el debrief. Frase clave: "El examen mide lectura de escenario, no memoria; hoy entrenamos la lectura". Tiempo: 30 segundos.

## 3. Lo que sí sabemos del examen

Objetivo: los números que sí importan, en un minuto. Frase clave: "700 de 1000, cuatro dominios casi parejos; ninguno se puede regalar". M2 es el que más pesa: el "at a glance" del study guide dice 25 a 30%, el detalle del outline dice 20 a 25%; trátenlo como el más grande. El practice assessment es gratis y el sandbox enseña la interfaz y los tipos de pregunta antes del día. Preview features pueden salir solo si son de uso común; la regla es GA. Tiempo: 2 minutos.

## 4. Seis reglas para leer cada pregunta

Objetivo: seis reflejos de lectura que eliminan distractores aunque no recuerden el detalle. Frase clave: "El examen te da tres datos y te pregunta por el cuarto; los tres datos son pistas, no contexto". Minimize administrative effort: la respuesta es la más automática (dynamic group, group-based licensing, access package, PIM for Groups). Least privilege: el rol más chico que alcance, nunca Global Admin. "Users must" o "must be prompted" es Conditional Access; "users at risk" es ID Protection. Preview no suele salir, GA es la regla. Nunca respondas con lo que harías en tu trabajo. Trampa favorita: elegir Global Administrator "porque funciona". Practican: M1 Q1, Q2 (least privilege), M1 Q12 y Q13 (minimize effort). Tiempo: 3 minutos.

## 5. Cada formato se ataca distinto

Objetivo: una táctica por formato. Frase clave: "Las preguntas antes que el caso, y ninguna vale más de 2 minutos". Case studies: leer primero las preguntas y luego el caso, marcando requisitos técnicos y de negocio. Yes/No en serie: cada frase se evalúa sola y no se puede regresar, así que no intenten que las tres respuestas "cuadren". Drag and drop y hot area: el orden importa, es la secuencia lógica del portal; por eso vemos los labs en imágenes. Labs: hacer primero lo que se sabe y dejar lo largo al final; se califica el estado final, no los pasos. Trampa favorita: quemar 6 minutos en una sola opción múltiple. Practican: M2 Q10 y M4 Q17 (drag/order), M2 Q19 y M4 Q22 (Yes/No). Tiempo: 3 minutos.

## 6. Los labs se califican por estado final, no por pasos

Objetivo: cambiar el ritmo y fijar la regla de los labs. Frase clave: "Los labs se califican por estado final, no por pasos: si llegas al mismo estado por otro camino, cuenta". Por eso en cada slide de lab la h2 es el objetivo en una línea: el estado final. En el examen, hacer primero lo que se sabe y dejar lo largo al final. Las licencias son las que pide Learn hoy: entitlement management y access reviews piden Microsoft Entra ID Governance (algunas capacidades con P2), aunque el lab viejo diga P1. Los 10 labs se eligieron del repo oficial MicrosoftLearning/SC-300 porque cubren las habilidades que más pegan. Tiempo: 1 minuto, luego 2 minutos por lab.

## 7. Roles, bulk create y usuarios borrados

Objetivo: reconocer Add assignments y Bulk create. Estado final: Chris Green existe (creado, borrado y restaurado) y ya no tiene Application administrator; hay usuarios de bulk create y de PowerShell (New-MgUser); Raul Razo tiene Windows 10/11 Enterprise E3. Frase clave: "Application Administrator deja crear enterprise apps propias sin ser Global Admin: el rol más chico que alcance". Trampa favorita: Usage location vacío bloquea la licencia; un usuario borrado vive 30 días en Deleted users con sus licencias y grupos. Bulk create: no tocar la fila version:v1.0 ni los encabezados. Practican: M1 Q1, Q2, Q11, Q12. Tiempo: 2 minutos.

## 8. La licencia llega sola por el grupo

Objetivo: ver que la licencia se hereda del grupo y que el dynamic group se llena solo. Estado final: sg-SC300-O365 tiene Office 365 E3 y Delia Dennis la recibe por herencia; existe el grupo Microsoft 365 Northwest Sales; existe SC300-myDynamicGroup con la regla user.objectId -ne null y más de 30 miembros. Frase clave: "Minimize administrative effort en licencias es group-based licensing con un dynamic group". Trampa favorita: nested groups no heredan licencia, solo miembros directos; y el conflicto de service plans deja la licencia en error (se revisa en Errors and issues). El rule builder solo soporta 5 expresiones; lo largo va en Edit. Practican: M1 Q12, Q13, Q15, Q17, Q18. Tiempo: 2 minutos.

## 9. Guests con el acceso más restringido

Objetivo: ubicar los settings de externos y los tres caminos para invitar. Estado final: guest self-service sign up via user flows en Yes, Email one-time passcode en Yes, Guest user access en most restrictive, invitaciones para member users y admin roles, y guests invitados uno por uno, en bulk y por PowerShell. Frase clave: "Most restrictive: el guest solo ve su propio objeto". Trampa favorita: con "Only users assigned to specific admin roles" solo invitan User Administrator y Guest Inviter. Tampoco se invitan emails de grupo ni direcciones con +. Un partner sin cuenta Microsoft ni Entra redime con Email one-time passcode. Practican: M1 Q21, Q22, Q23, Q24. Tiempo: 2 minutos.

## 10. MFA por CA y SSPR para un piloto

Objetivo: MFA para un piloto con CA y SSPR para un grupo. Estado final: la política MFA_for_Delia en On pide MFA para Office 365; Adele Vance tiene per-user MFA en Enabled; SSPR en Selected con SSPRTesters y Allan Deyoung registrado y probado; GradyA, fuera del grupo, no puede resetear. Frase clave: "MFA para un grupo piloto sin tocar al resto es Conditional Access, no security defaults ni per-user MFA". Trampa favorita: security defaults activos impiden usar CA; y no se mezcla per-user MFA con CA, Learn lo desaconseja. En el portal SSPR Selected acepta un solo grupo, y los admins siempre usan la política de dos métodos, por eso se prueba con un usuario sin rol. Practican: M2 Q6, Q7, Q8. Tiempo: 2 minutos.

## 11. Bloquear Sway y probarlo con What If

Objetivo: construir, apagar y diagnosticar una política. Estado final: existe Block Sway for DebraB con Block access y al final queda en Off; existe Sign in frequency para Grady Archie en Office 365, 30 Days, en Report-only. Frase clave: "What If te dice qué políticas aplican y cuál condición falló; pide identity, target resource, device platform y client app". Trampa favorita: una política en Off no sale en What If. Report-only no aplica nada, solo registra, y Remember MFA on trusted devices choca con Sign-in frequency. Security defaults activos bloquean CA. Practican: M2 Q13, Q19, Q20, Q21. Tiempo: 2 minutos.

## 12. Dos políticas de riesgo, nunca una

Objetivo: las dos políticas de riesgo hechas en Conditional Access, cada una con su cura. Estado final: User Risk Remediation (All users menos MOD Administrator, All resources, user risk High, Require risk remediation, On) y Sign-in Risk Policy (sign-in risk High, Require multifactor authentication, On). Frase clave: "User risk se cura con Require risk remediation; sign-in risk se cura con MFA; nunca en la misma política". Trampa favorita: Require risk remediation agrega solo Require authentication strength y Sign-in frequency Every time, y el usuario necesita MFA registrado antes o queda bloqueado. Siempre excluir break-glass (en el lab, MOD Administrator). Las risk policies legacy de ID Protection se retiran el 1 de octubre de 2026. Practican: M2 Q29, Q30, Q31. Tiempo: 2 minutos.

## 13. Registrar, exponer una API, consentir

Objetivo: el ciclo de una app, de registrarla a darle consent a nivel tenant. Estado final: Demo app con redirect URI Web https://localhost, client secret SC300 lab secret, Application ID URI api://DemoAppAPI con Employees.Read.All (Admins and users) y Employees.Write.All (Admins only), el custom role My custom app role, y admin consent otorgado. Frase clave: "Un permiso que solo un admin puede aprobar es Who can consent: Admins only". Trampa favorita: el Value del secret solo se ve una vez; y Grant admin consent desde App registrations puede revocar permisos dados antes a nivel tenant. Quién consiente: Privileged Role Administrator para todo; Cloud Application Administrator y Application Administrator para todo menos app roles de Microsoft Graph. Custom roles piden P1. Practican: M3 Q16, Q17, Q21, Q23, Q25, Q27, Q30. Tiempo: 2 minutos.

## 14. Un catalog con dueño y recursos

Objetivo: el catalog como contenedor de recursos y de delegación. Estado final: catalog Marketing con Enabled Yes y Enabled for external users No, con el grupo Retail, las apps Box y Salesforce y el sitio Brand como recursos, Adele Vance como catalog owner, y un access review de guests en todos los grupos Microsoft 365 con Group owner(s) como revisores. Frase clave: "Primero el catalog, luego los access packages; el catalog owner administra su área sin ser admin". Trampa favorita: licencia Microsoft Entra ID Governance (algunas capacidades con P2) aunque el lab viejo diga P1; User Administrator ya no crea catalogs, el rol es Identity Governance Administrator. Grupos sincronizados de AD y distribution groups no se agregan; la búsqueda de sitios distingue mayúsculas. Auto apply con Remove access puede sacar a todos si nadie revisa. Practican: M4 Q1, Q2, Q3. Tiempo: 2 minutos.

## 15. Un access review anual con revisor

Objetivo: las cuatro pestañas de un access review. Estado final: existe SC300 Access Review Test sobre el grupo Sales and Marketing, scope All users, revisor Alex Wilber y recurrencia Annually. Frase clave: "Que el dueño confirme cada año y que los rechazados salgan solos: Auto apply results to resource más If reviewers don't respond". Enseñar la segunda captura: Upon completion es donde vive el examen (Auto apply, Remove access, decision helpers como no sign-in en 30 días). Trampa favorita: seleccionar varios grupos crea un review por grupo; Group owner(s) solo existe para grupos y con Managers o Group owner(s) se ponen fallback reviewers. Licencia Governance para quien revisa o es revisado. Un guest revisor debe aceptar antes la invitación. Practican: M4 Q13 a Q20. Tiempo: 2 minutos.

## 16. Eligible, con approval y activación

Objetivo: el ciclo completo de PIM: settings, asignación eligible, activación y retiro. Estado final: Compliance Administrator pide approval para activarse con tu admin como aprobador; Miriam Graham fue Eligible, lo activó con MFA y justificación, y al final la asignación se quitó. Frase clave: "Solo cuando lo necesitan, con MFA y aprobación: Eligible más Require approval to activate". Trampa favorita: con approval la activación queda pendiente hasta que alguien apruebe, no es un error; y una asignación no se puede quitar en sus primeros 5 minutos. Si Miriam no tiene MFA registrado se atora en Additional verification required. Riesgo de lockout: approval sin aprobadores y todos los admins solo eligible; para eso existen las break-glass. Un Helpdesk admin de una sucursal: Scope type Administrative unit. Practican: M4 Q21, Q22, Q23, Q30, Q31. Tiempo: 2 minutos.

## 17. 30 preguntas

Objetivo: dejar el simulacro armado para que lo hagan solos. Son 30 preguntas del banco que no salieron en los Kahoot: 8 de M1, 8 de M2, 7 de M3 y 7 de M4, casi todas de opción múltiple, con 2 Yes/No series, 2 select two y 1 drag and drop, como el examen. Reglas: 45 minutos con reloj, sin apuntes ni portal, y una sola pasada con "marcar para revisar". Calificación: un punto por pregunta completa; en Yes/No, select two y drag and drop es todo o nada. 21 de 30 es la meta. Lo que fallen, lo anotan por dominio y lo traen al debrief. Frase clave: "El simulacro no es para sacar 30; es para saber qué dominio te cuesta antes de que te cueste en el examen". Tiempo: 5 minutos.

## 18. El debrief reemplaza a los dumps

Objetivo: que cada quien que presente llene el debrief el mismo día y lo comparta en el canal. Frase clave: "El debrief reemplaza a los dumps: temas sí, preguntas no". Qué se anota: resultado y score por dominio (el score report lo da), qué dominio se sintió más pesado, qué tipos de escenario costaron por tema, qué labs salieron por tarea y no por pasos, y qué hubiera estudiado más. Por qué: acumula señal legítima sobre el peso real de cada tema y es el input para ajustar los tips and tricks de cada cohort. Trampa favorita: copiar preguntas literales; eso viola el acuerdo del examen y no ayuda a nadie. Tiempo: 5 minutos.

## 19. Gracias. Ahora, a agendar

Cierre del curso. Dejar el slide abierto mientras anotan. Tres cosas: agendar el examen esta semana, hacer el practice assessment una vez más después del simulacro, y abrir un issue de debrief en el repositorio. Preguntar quién presenta este mes. Frase clave: "Ya tienen todo: la guía, el banco, los labs y el simulacro; lo que falta es la fecha". Todos los links del deck son clicables, incluido el lab oficial en el pie de cada slide de lab. Gracias. Tiempo: 5 minutos con preguntas.
