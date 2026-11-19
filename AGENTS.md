# AGENTS.md — Normas y procedimientos del proyecto Digitalización 4.º ESO

> **Versión de estas normas:** 1.3.0  
> **Última actualización:** 19/11/2026  
> **Estado:** Documento vivo; revisar y ampliar cuando cambie el procedimiento.

## 1. Propósito y alcance

Este archivo recoge las decisiones de organización, preferencias y procedimientos para mantener y ampliar el repositorio `bitschips/digitalizaci-n-4`.

**Instrucción para asistentes, colaboradores y automatizaciones:** leer este archivo antes de crear, modificar, reorganizar o publicar contenidos. Aplicar sus reglas a todos los temas, respetando las peticiones nuevas y explícitas del profesor. Si una nueva decisión cambia estas normas, actualizar este mismo documento y su versión.

Este repositorio reúne materiales de **Digitalización de 4.º de ESO de la Comunitat Valenciana (GVA)**, inicialmente organizados en 4 bloques y 18 temas. Los títulos son una **propuesta didáctica**, no una numeración oficial de la Generalitat.

La finalidad es mantener los contenidos **editables, reutilizables y preparados para generar presentaciones**.

## 2. Principios generales

1. **El Markdown es la fuente principal de contenido**: desarrollar, revisar y actualizar cada tema en su archivo `.md`.
2. **Un único índice**: el archivo raíz `README.md` contiene los bloques y **solo los títulos de los temas**, con enlace al `.md` correspondiente cuando este exista. No duplicar allí los apartados del tema ni crear un segundo índice.
3. **Cada tema es independiente**: su contenido, sus presentaciones, sus actividades y sus ideas de vídeos están en su propia carpeta.
4. **Cambios mínimos**: no modificar temas o presentaciones no afectados por la tarea.
5. **Materiales para alumnado de 4.º ESO**: lenguaje claro, progresivo, correcto y didáctico; definiciones comprensibles, ejemplos reales y pequeñas actividades.
6. **Ampliación progresiva**: empezar con un documento útil y mejorarlo sin perder contenidos revisados anteriormente.
7. **No crear materiales duplicados ni archivos innecesarios**. No generar PDF ni una presentación general del índice, salvo petición explícita.
8. Se autoriza **GitHub Actions exclusivamente para mantener sincronizadas las presentaciones HTML/PPTX con sus temas Markdown**. No activar GitHub Pages ni servicios externos adicionales sin autorización.

## 3. Estructura del repositorio

```text
digitalizaci-n-4/
├── README.md
├── AGENTS.md                         # Normas y métodos de trabajo
└── temas/
    ├── tema-01-arquitectura-de-ordenadores/
    │   ├── tema-01.md                # Fuente del tema
    │   ├── presentaciones/
    │   │   ├── tema-01.html          # Presentación navegable
    │   │   └── tema-01-arquitectura-de-ordenadores.pptx
    │   └── actividades/
    ├── tema-02-sistemas-operativos/
    │   ├── presentaciones/
    │   └── actividades/
    └── ... hasta tema-18
```

- Actualmente existen las **18 carpetas de temas**, cada una con `presentaciones/` y `actividades/`.
- **Solo el Tema 1** tiene por ahora un archivo de contenido `tema-01.md` y presentaciones HTML/PPTX. No dar por creados los documentos de los demás temas.
- Las carpetas todavía vacías pueden contener un archivo `.gitkeep`, porque Git no registra directorios vacíos.
- Para temas nuevos, seguir el patrón `temas/tema-NN-nombre-en-minusculas-sin-acentos/tema-NN.md`.
- Los archivos auxiliares de generación, si más adelante son necesarios, deberían ser **reutilizables y comunes** a todos los temas, preferentemente en `scripts/`, en lugar de duplicar uno por tema.
- No eliminar, renombrar ni reorganizar contenido existente sin comprobar primero sus enlaces y dependencias.

## 4. Índice principal y enlaces

### README.md

- Conservar los **4 bloques curriculares y 18 títulos**.
- Cuando un tema tenga contenido, enlazar su título directamente a su Markdown, usando una ruta relativa. Ejemplo:

  `### [Tema 1. Arquitectura de ordenadores](temas/tema-01-arquitectura-de-ordenadores/tema-01.md)`

- No introducir en el índice principal descripciones largas ni listados de contenidos de cada tema.
- No enlazar temas a archivos que todavía no existan.

### Enlaces dentro del tema

Al principio de cada `tema-NN.md`, incluir el enlace **Volver al índice general** y una sección **Materiales del tema**, con enlaces diferenciados:

- **Presentación HTML — abrir en el navegador**: cuando exista, enlazar al visor HTML disponible.
- **Presentación PPTX — descargar**: cuando exista, enlazar al archivo editable.
- **Actividades**: enlazar a la carpeta de actividades, o a una actividad individual si se solicita.

Evitar enlaces redundantes como **Presentación** y **Carpeta de presentaciones** cuando llevan a la misma ubicación. Usar simplemente **Actividades**, no **Carpeta de actividades**.

### Preferencia: enlaces en pestaña nueva

**El profesor prefiere que todos los enlaces se abran en una pestaña nueva.**

- En páginas HTML propias usar `target="_blank" rel="noopener noreferrer"` para enlaces de navegación.
- **Limitación:** en el Markdown renderizado por GitHub no se puede forzar de forma fiable la apertura en una nueva pestaña. Mantener enlaces Markdown compatibles y no prometer un comportamiento que GitHub controla. Para abrirlos manualmente en nueva pestaña: Ctrl/Cmd + clic o menú del navegador.
- Comprobar los destinos y utilizar URLs públicas correctas, sin suponer que un servicio externo está disponible.

## 5. Contenido de cada tema Markdown

Crear cada tema como documento de trabajo ampliable, con estructura coherente:

1. Título, curso y estado del material.
2. Enlace de vuelta al índice y apartado **Materiales del tema**.
3. Objetivos de aprendizaje.
4. Contenidos principales desarrollados con secciones numeradas.
5. Definiciones, explicaciones breves, ejemplos reales, comparativas y esquemas cuando ayuden a comprender.
6. Actividades prácticas, preferentemente realizables en el aula.
7. Preguntas de repaso y/o autoevaluación.
8. Glosario breve de conceptos.
9. **Control de versiones al final del archivo.**

No es obligatorio que todos los temas tengan exactamente el mismo número de secciones, diapositivas o ejercicios. Mantener la estructura flexible y adaptar la profundidad al alumnado.

Cuando se aborden afirmaciones técnicas o normativas que cambian con el tiempo, verificarlas antes de publicarlas. No confundir la organización didáctica de este repositorio con el índice oficial del currículo.

### Pie de control de versiones obligatorio

Añadir siempre al final del contenido un bloque como este:

```markdown
---

## Control de versiones

- **Versión del contenido:** 1.0.0
- **Última actualización:** 19/11/2026
- **Estado:** Borrador ampliable
```

Usar fechas en formato `DD/MM/AAAA` (zona horaria de referencia: **Europe/Madrid**). Actualizar la fecha cuando se cambie el contenido didáctico.

Convención orientativa de versión `MAJOR.MINOR.PATCH`:
- **PATCH** (1.0.1): correcciones menores sin cambios sustanciales.
- **MINOR** (1.1.0): nuevos ejemplos, actividades o apartados.
- **MAJOR** (2.0.0): reorganización o revisión importante del tema.

La versión identifica una edición humana del material. No sustituye la comprobación automática de cambios.

## 6. Presentaciones: HTML y PPTX

Se mantendrán **dos versiones de cada presentación**, en `presentaciones/`:

| Formato | Finalidad | Ubicación |
|---|---|---|
| `.html` | Ver diapositivas directamente en el navegador | `presentaciones/tema-NN.html` |
| `.pptx` | Descargar, editar y presentar desde PowerPoint/LibreOffice | `presentaciones/tema-NN-nombre-del-tema.pptx` |

- Ambos formatos se crearán **a partir del contenido revisado del `.md` del tema**; no generar información incompatible o contradictoria entre ellos.
- Dar preferencia a diapositivas **claras y visuales**, con una idea principal por diapositiva, ejemplos y repaso; evitar trasladar párrafos largos sin adaptar.
- Incluir portada, desarrollo progresivo, ejemplos y alguna actividad o repaso cuando proceda.
- **Tema 1:** existe una presentación inicial de **16 diapositivas**, pero ese número no es una regla general.
- HTML: navegación anterior/siguiente, teclado, diseño adaptable a móvil y pantalla completa cuando sea posible; evitar dependencias externas innecesarias.
- PPTX: archivo editable y descargable; conservarlo en el repositorio.
- **Mostrar en cada presentación el número de versión y la fecha**; preferiblemente también en el pie o portada. En HTML añadir además metadatos legibles por máquinas (por ejemplo, `content-version`, `updated-date` y una huella del contenido). En PPTX registrar también esos datos en las propiedades del archivo cuando sea posible.
- No crear versiones PDF salvo solicitud explícita.

### Visualización HTML sin GitHub Pages

**No activar GitHub Pages por ahora.** Se ha decidido seguir con el repositorio GitHub normal:

- PPTX: enlace de GitHub para descargar.
- HTML: enlace a la versión HTML usando el visor externo `htmlpreview.github.io`, mientras funcione.

Ejemplo de visor para el Tema 1:

`https://htmlpreview.github.io/?https://github.com/bitschips/digitalizaci-n-4/blob/main/temas/tema-01-arquitectura-de-ordenadores/presentaciones/tema-01.html`

Alojar un HTML **como archivo en GitHub** no equivale a publicarlo como sitio web nativo; la vista de diapositivas se obtiene aquí mediante un visor externo. Si el visor deja de funcionar, buscar una alternativa y comentarla antes de cambiar la arquitectura.

## 7. Automatización incremental con GitHub Actions

**Sistema activo y comprobado:** cuando cambie el contenido de un tema, regenerar **solo las presentaciones desactualizadas**, no todo el repositorio.

- **Workflow:** `.github/workflows/actualizar-presentaciones.yml`.
- **Generador reutilizable:** `scripts/generar_presentaciones.py` (Python, `markdown`, `beautifulsoup4`, `python-pptx`).
- **Manifest por tema:** `temas/tema-NN-.../presentaciones/manifest.json`, con SHA-256, versión del contenido, fecha, versión del generador, número de diapositivas y nombres de salidas.
- **Activación:** en cada push que afecte a `temas/**/tema-*.md`, imágenes admitidas, generador, o el propio workflow; también admite ejecución manual.
- **Sin IA externa:** la Action transforma el Markdown en diapositivas por reglas predefinidas. Para una transformación editorial distinta o visuales elaborados, el profesor puede solicitar una mejora del generador o un diseño específico.
- **Última prueba:** el Tema 1 pasó automáticamente de v1.0.0 (21 diapositivas) a v1.1.0 (28 diapositivas) tras añadir el contenido de transistores.

El procedimiento que se debe conservar en las futuras revisiones es:

1. **Evento de entrada:** cambios en archivos `tema-NN.md`, recursos de los temas, plantillas o generadores; opcionalmente ejecución manual (`workflow_dispatch`).
2. **Identificar temas afectados** por las rutas modificadas. No actualizar presentaciones de temas que no hayan cambiado.
3. **Comparar una huella digital de las fuentes** de cada tema con la huella registrada en la última generación. Usar SHA-256 de contenido normalizado o un mecanismo equivalente.
4. **Evitar falsos positivos:** calcular la huella sobre el contenido pedagógico y los recursos efectivos (imágenes, plantillas, generador y configuración), excluyendo elementos que no afectan a las diapositivas, como enlaces de descarga o el propio bloque de control de versiones cuando proceda.
5. **Comprobar versiones:** registrar en los archivos generados la versión y fecha del tema. La versión debe ser coherente, pero **no depender solo del incremento manual de versión**, ya que podría olvidarse.
6. **Regenerar ambos formatos** (HTML y PPTX) únicamente para cada tema afectado y solo si es necesario. Si se modifica un generador común, regenerar los temas a los que afecte ese cambio.
7. **Validar** la generación antes de publicar: archivos existentes, formatos legibles, enlaces, número de diapositivas razonable y coincidencia con la versión de la fuente.
8. **Publicar cambios** mediante un commit únicamente si hay archivos de salida diferentes, evitando commits vacíos y bucles de GitHub Actions.
9. **Registrar los resultados** de la ejecución: temas actualizados, omitidos y fallidos. Si falla un tema, no indicar que su presentación está actualizada.
10. **No desplegar GitHub Pages** como parte de este proceso.

### Ejemplo de decisión de actualización

| Tema | Contenido actual | Presentación existente | Decisión |
|---|---|---|---|
| 01 | Versión 1.1.0, huella nueva | Versión 1.0.0 | Regenerar HTML y PPTX |
| 02 | Sin cambios detectados | Coincide con la fuente | Mantener archivos |
| 03 | Fuente creada, sin presentación | No existe | Crear presentación |

**Importante:** los números anteriores son ejemplos de funcionamiento, no el estado real de los temas 2 o 3.

Actualmente **ya se utiliza** `presentaciones/manifest.json` en cada tema desarrollado. Mantener esta estructura para que el generador incremental pueda comparar cambios sin depender solo de la versión manual.

## 7 bis. SINCRONIZACIÓN AUTOMÁTICA OBLIGATORIA (prioridad alta)

**Regla central: una petición de «añade/corrige/modifica este punto en el Tema N» incluye implícitamente actualizar sus presentaciones HTML y PPTX. El docente NO tiene que solicitar «actualiza la presentación».** Aplica incluso si el cambio se dicta por voz o es una sola línea.

### Cuando la modificación se hace hablando con ChatGPT

1. Leer `AGENTS.md` y localizar `tema-NN.md` y sus recursos existentes.
2. Incorporar la idea en la sección apropiada, manteniendo el nivel didáctico y los contenidos anteriores.
3. Incrementar la versión del tema y actualizar su fecha; si el cambio es pequeño, incrementar PATCH; si añade un apartado, MINOR.
4. Guardar y comprobar el Markdown. **No dar por finalizado el encargo mientras no se haya iniciado/completado correctamente la sincronización de HTML/PPTX**, según permita el acceso al repositorio.
5. Si está configurado el flujo de GitHub Actions, el guardado del Markdown debe dispararlo automáticamente. Verificar su resultado y sus archivos en GitHub si es posible. Si falla o está pendiente, informarlo claramente; no afirmar que ya están actualizadas.
6. Si el flujo no está disponible, regenerar ambas presentaciones durante la misma tarea cuando se disponga de herramientas. Si no es técnicamente posible, explicar con precisión qué queda pendiente. **No pedir al profesor que recuerde indicar «actualiza la presentación».**
7. Evitar generar presentaciones nuevas si solo se han cambiado los enlaces, el historial o la metadata sin afectar al contenido.

### Cuando el docente modifica un Markdown directamente en GitHub

1. Un workflow de `push` para `temas/**/tema-*.md` ejecuta el generador incremental.
2. Se calcula una huella SHA-256 del **contenido pedagógico** (excluyendo cabecera de enlaces y bloque de versiones), más el generador o las plantillas que afecten a las diapositivas.
3. Si la huella coincide con la de la generación anterior y existen ambas salidas, **no hacer nada** en ese tema.
4. Si cambió o no existe alguna salida, actualizar **solo** HTML/PPTX de ese tema.
5. Si el cambio pedagógico no tiene una nueva versión declarada, el generador debe incrementar automáticamente al menos PATCH y actualizar la fecha del Markdown; si el docente ya incrementó la versión, conservarla.
6. Las presentaciones deben indicar la versión, fecha y huella de origen, y el generador debe guardar un manifiesto verificable para futuras comparaciones.
7. El commit automático debe incluir solo archivos realmente modificados, no activar de nuevo el mismo workflow, y dejar trazabilidad del resultado.
8. Si el generador tiene limitaciones para algún contenido (tablas complejas, imágenes, etc.), señalarlas y no afirmar que la presentación refleja exactamente el tema cuando no sea cierto.

**El índice principal `README.md` solo se modifica si aparece un tema nuevo o cambia su ruta; no se reescribe por cada edición didáctica.**

---

## 8. Flujo de trabajo para crear o actualizar un tema

1. Leer `AGENTS.md`, `README.md` y los archivos existentes del tema.
2. Aclarar qué contenido o actividad se desea ampliar o corregir. Si la instrucción es suficiente, actuar sin solicitar confirmaciones innecesarias.
3. Editar primero el archivo `tema-NN.md`, conservando enlaces y estructura.
4. Incrementar su versión de forma proporcionada y actualizar la fecha.
5. **Siempre que se modifica el contenido pedagógico, generar o actualizar automáticamente HTML y PPTX**, aunque no se solicite de manera expresa. Sincronizar versión, fecha y huella. Respetar pestañas nuevas en HTML.
6. Si se solicita actividad, guardarla en `actividades/` y añadir un enlace no redundante desde el tema.
7. Actualizar el enlace del `README.md` **solo cuando se cree el contenido de un tema que antes no existía** o cambie su ruta.
8. Comprobar las rutas y visualizar/verificar los resultados en la medida que permitan las herramientas.
9. Resumir exactamente qué se ha publicado, qué se ha conservado y qué queda pendiente. No afirmar que una publicación o Action ha funcionado sin verificarlo.

## 9. Estado de referencia (19/11/2026)

- `README.md`: índice principal simplificado, con título y enlace al contenido del Tema 1.
- Carpetas de **18 temas** y sus subcarpetas `presentaciones/` y `actividades/`: creadas.
- `tema-01.md`: ampliado con transistores y evolución histórica CPU/NVIDIA, versión **1.1.0**, con control de versión al final.
- `tema-01.html`: presentación HTML generada automáticamente, versión **1.1.0**.
- `tema-01-arquitectura-de-ordenadores.pptx`: presentación editable generada automáticamente, versión **1.1.0**.
- Los **temas 2–18 aún no tienen contenido de tema desarrollado**.
- El flujo común de regeneración incremental ya está activo: `.github/workflows/actualizar-presentaciones.yml`. La modificación del Tema 1 disparó la Action, que publicó ambas presentaciones en versión **1.1.0**.
- No se utiliza GitHub Pages.
- No generar de nuevo el antiguo PDF ni el PowerPoint del índice principal.

## 9 bis. Ideas de vídeos y actividades por tema

- Cada uno de los **18 temas** incorpora `videos/README.md` como índice vivo de propuestas de vídeos para comprender visualmente conceptos del tema.
- Cada idea se documenta por separado en `videos/video-NN-titulo.md`: objetivo didáctico, duración, conceptos, guion por escenas, narración, instrucciones para una futura herramienta de vídeo con IA, comprobación de exactitud, actividad asociada y estado.
- **Registrar una idea o un guion no significa que el vídeo esté generado.** Los vídeos se generarán más adelante con la herramienta que se elija; solo publicar enlaces a vídeos comprobados.
- Las actividades se documentan en `actividades/actividad-NN-titulo.md`, con pasos realizables en clase y criterios de logro; `actividades/README.md` recoge el índice del tema.
- Una misma propuesta puede tener guion audiovisual y actividad práctica, enlazados entre sí. Ejemplo de Tema 1: viaje de `print("Hola mundo")` por SSD, RAM, CPU/transistores y pantalla, junto a la creación y ejecución de `hola.py`.
- Al proponer nuevas actividades o vídeos por voz, crear el Markdown correspondiente y actualizar su índice **sin esperar que el docente pida expresamente crear el índice**.
- **No modificar `tema-NN.md` ni regenerar HTML/PPTX solo por incorporar propuestas de vídeo o actividades separadas**, salvo que el docente pida incorporar también esos contenidos a las diapositivas o al material principal.
- Mantener enlaces relativos Markdown para GitHub y `target="_blank" rel="noopener noreferrer"` en los enlaces de páginas HTML propias.

## 10. Cómo mejorar este documento

Cuando se apruebe una nueva preferencia, añadirla a su sección correspondiente, actualizar **Versión de estas normas** y **Última actualización**, y conservar una explicación breve del cambio.

### Historial de cambios

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0.0 | 19/11/2026 | Primer documento de normas: estructura de temas, enlaces, contenidos, HTML/PPTX, versiones y diseño de automatización incremental. |
| 1.1.0 | 19/11/2026 | Sincronización obligatoria de presentaciones al añadir o modificar contenidos, incluso por voz y sin petición adicional; autorización para GitHub Actions. |
| 1.2.0 | 19/11/2026 | Registrar el workflow incremental ya operativo, su generador, manifiestos de versiones y la prueba automática del Tema 1. |
| 1.3.0 | 19/11/2026 | Índices de ideas de vídeos para los 18 temas; guiones y actividades enlazados sin regeneración innecesaria de presentaciones. |
