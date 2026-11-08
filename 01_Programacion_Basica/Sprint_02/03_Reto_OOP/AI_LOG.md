# AI_LOG · Práctica OOP 

Este registro no cuenta. Sirve para ver dónde vais solos y dónde os apoyáis. Si no habéis usado IA en una tarea, dejad el nivel en 0 también es un dato útil.
me apoye en la IA, mas que nada en las partes donde tengo que armar la logica del ejercicio. se que son las partes mas importantes, pero sino me apoyo no se como seguir y salir de ahi. me falta mas practica, y aprenderme mas elementos con los cuales apoyarme para no ir por el camino mas facil, perdon.

**Grupo:** (Ludmila

**Herramientas usadas:** (ChatGPT, Claude, Gemini, Copilot, autocompletado de VS Code... o ninguna) gemini. 

> El repositorio es público: no pongáis datos personales ni contraseñas en los prompts que copiéis aquí.

## Resumen por tarea

Niveles: **0** sin IA · **1** consulta puntual, el código es nuestro · **2** la IA escribe partes y las adaptamos · **3** casi todo lo escribe la IA. consulte cosas puntuales.

| Tarea | Quién la ha llevado | Nivel de IA (0-3) | Nº de prompts | ¿La podríais repetir sin IA? (sí / en parte / no) |
|si| en parte| en parte| si 
| 1. Constructor y validación | | | | |
| 2. `deposit` y `withdraw` | | | | |
| 3. `transfer` | | | | |
| 4. Pruebas propias | | | | |

## Registro de prompts

Copiad este bloque por cada prompt que haya influido en vuestro código.

### Tarea X · Prompt 1

- **Objetivo:** qué queríais resolver. el error en el metodo transferir y asegurar que las validaciones de cuentas de comprobacion y saldos funcionen correctamente
- **Prompt:** copiadlo tal cual.ayudame a revisar por que fallan las pruebas en el metodo transfer de la clase user y como estructurarlo con los parametros correctos
- **Respuesta relevante:** la parte que usasteis, resumida.sugerencia de ajustar el orden de los parametros a self , otro_usuario, amount y validar los tipos de datos, los valores negativos y el atributo checking_account antes de modificar los saldos.
- **Cambios:** qué modificasteis y por qué. organice el orden de los argumentos en la firma del metodo transferir y añadi las comprobaciones de isinstance y valueerror 
- **Comprobación:** cómo verificasteis que funcionaba. se volvieron a ejecutar las celdas de pruebas automaticas con ejecutar_pruebas() y todas pasaron de forma exitosa.
- **Decisión propia:** qué decidisteis vosotros.decidi mantener la conversion automatica de float a int utilizando int() para cumplir de forma estricta con las notas adicionales del ejercicio.
