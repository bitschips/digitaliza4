# Tema 2. Sistemas operativos

**Materia:** Digitalización · 4.º ESO · Comunitat Valenciana  
**Estado:** Contenido aprobado · material ampliable  
**Fecha:** 20/11/2026

[Volver al índice general](../../README.md)

## Materiales del tema

- [Presentación HTML — abrir en el navegador](https://htmlpreview.github.io/?https://github.com/bitschips/digitaliza4/blob/main/temas/tema-02-sistemas-operativos/presentaciones/tema-02.html)
- [Presentación PPTX — descargar](presentaciones/tema-02-sistemas-operativos.pptx)
- [Actividades](actividades/)

## Objetivos de aprendizaje

Al finalizar el tema podrás explicar para qué sirve un sistema operativo, identificar sus principales funciones, comparar Windows, macOS, GNU/Linux, Android e iOS, comprender las diferencias entre software libre y propietario, reconocer distribuciones Linux y practicar la preparación de un USB de arranque Live para diagnosticar y recuperar archivos de un equipo.

## 1. ¿Qué es un sistema operativo?

Un **sistema operativo (SO)** es el software básico que permite utilizar un ordenador, móvil o tableta y coordina el hardware con los programas y las personas. Al encender un equipo, el firmware inicia el proceso de arranque, que carga el sistema operativo; después podemos abrir aplicaciones, manejar archivos y utilizar dispositivos.

**Ejemplo:** cuando guardas un documento, el procesador ejecuta instrucciones, la RAM mantiene datos temporales y el sistema operativo organiza su almacenamiento en el SSD.

### Funciones principales

- **Gestionar procesos:** reparte tiempo de procesador entre los programas.
- **Gestionar memoria:** asigna RAM a las aplicaciones.
- **Gestionar archivos:** crea, organiza, busca y protege carpetas y documentos.
- **Controlar dispositivos:** se comunica con pantalla, teclado, impresora o Wi-Fi mediante controladores y otros componentes.
- **Facilitar la interacción:** proporciona un escritorio gráfico, aplicaciones y/o terminal.
- **Proteger el sistema:** controla usuarios, permisos, actualizaciones y acceso a recursos.

No hay que confundir **sistema operativo** con **aplicación**: Windows o Linux gestionan el equipo; un navegador o un procesador de textos realizan tareas concretas sobre el sistema.

<!-- IMAGEN: img/escritorio-sistema-operativo.svg | TITULO: El escritorio de un sistema operativo | POSICION: DESPUES -->

## 2. Breve historia y evolución

| Época | Evolución | Idea clave |
|---|---|---|
| Años 50–60 | Sistemas por lotes en grandes ordenadores | Ejecutaban trabajos sin interacción continua con el usuario. |
| Años 60–70 | Tiempo compartido; nacimiento de Unix | Varios usuarios y programas podían compartir un ordenador. |
| Años 80 | Ordenadores personales, MS-DOS y primeros entornos gráficos populares | Se extendió la informática doméstica. |
| Años 90 | Windows, GNU/Linux y evolución de Mac OS | Se consolidaron distintos modelos de sistema. |
| Años 2000 | macOS basado en Unix, popularización de Linux en servidores | Mayor importancia de Internet y las redes. |
| Años 2010–2020 | Android, iOS, nube, virtualización y contenedores | El sistema operativo está también en móviles y centros de datos. |

**Reflexión:** hoy podemos utilizar simultáneamente un sistema en el móvil, otro en el portátil y otro en el servidor que guarda nuestros archivos.

## 3. Tipos de sistemas operativos

- **De escritorio:** diseñados principalmente para ordenadores personales, como Windows, macOS y distribuciones de GNU/Linux.
- **Móviles:** optimizados para pantallas táctiles, batería y sensores, como Android e iOS.
- **De servidor:** orientados a ofrecer servicios en red con estabilidad, seguridad y administración remota.
- **Integrados o embebidos:** funcionan en routers, electrodomésticos, vehículos u otros dispositivos.
- **De tiempo real:** se diseñan para responder dentro de límites temporales definidos, importantes en determinados controles industriales.

Un mismo sistema o familia puede servir para varias categorías.

## 4. Principales sistemas operativos: comparación

| Sistema | Uso habitual | Licencia y coste básico | Aspecto importante |
|---|---|---|---|
| Windows | PC personales, empresas, videojuegos | Propietario; normalmente requiere licencia de pago, a menudo incluida en el precio del equipo | Amplia compatibilidad comercial |
| macOS | Ordenadores Apple | Propietario; incluido para equipos Apple compatibles | Integración con hardware Apple |
| GNU/Linux (Debian, Mint, etc.) | PC, servidores, educación | Muchas distribuciones son gratuitas y de código abierto; otras venden suscripciones o soporte | Se puede elegir entre distintas distribuciones |
| Android | Móviles, tabletas y otros equipos | Base de código abierto (AOSP), con componentes y servicios que pueden ser propietarios; normalmente incluido en el dispositivo | Gran variedad de fabricantes |
| iOS | iPhone | Propietario; incluido en iPhone compatible | Ecosistema de Apple |

**Importante:** «gratuito» describe el precio, mientras que **«software libre»** se refiere a libertades de uso, estudio, modificación y distribución según su licencia. Un software libre puede ofrecerse con servicios de pago; un programa gratuito puede ser propietario.

### 4.1. El coste real de un sistema operativo

Para comparar costes hay que distinguir **precio de la licencia**, **coste del equipo**, **mantenimiento**, **soporte profesional** y **formación**. Windows suele comercializarse con licencia, pero también puede venir preinstalado y pagado indirectamente dentro del precio del ordenador. Muchas distribuciones de Linux se pueden descargar, instalar y usar sin pagar licencia. **Red Hat Enterprise Linux**, en determinados usos, se ofrece mediante suscripciones comerciales que incluyen servicios y soporte.

**Ejemplo orientativo sin precios fijos:** instalar Linux Mint en un ordenador compatible puede no tener coste de licencia. Comprar un PC con Windows puede incluir el importe de su licencia. Una empresa puede decidir pagar una suscripción de Linux empresarial para recibir soporte especializado.

**Actividad breve:** ¿qué opción elegirías para diez ordenadores antiguos de un aula y por qué? Razona el coste total, no solo la descarga.

<!-- IMAGEN: img/comparacion-sistemas-operativos.svg | TITULO: Sistemas operativos en distintos dispositivos | POSICION: DESPUES -->

## 5. Cómo funciona un sistema operativo

El **núcleo o kernel** es una parte central del sistema: coordina operaciones de bajo nivel y recursos como procesos, memoria y dispositivos. Los programas utilizan servicios del sistema para realizar tareas que no deberían ejecutar directamente sobre el hardware.

- **Proceso:** programa en ejecución; por ejemplo, dos navegadores o un editor.
- **Multitarea:** el sistema intercala o ejecuta trabajo de varias aplicaciones.
- **Memoria RAM:** mantiene los datos de trabajo; el sistema asigna y protege espacios de memoria.
- **Controladores (drivers):** permiten que el sistema interactúe con determinados dispositivos.
- **Usuarios y permisos:** limitan qué archivos y operaciones puede utilizar cada cuenta.

**Ejemplo:** si abres varias pestañas y el equipo se ralentiza, pueden estar compitiendo por RAM, CPU o almacenamiento. No significa automáticamente que haya un virus.

## 6. Interfaz gráfica y terminal

La **interfaz gráfica (GUI)** utiliza ventanas, iconos, menús y puntero. La **línea de comandos (CLI)** permite escribir instrucciones en una terminal. Ambas son formas de interactuar con el sistema, no sistemas operativos distintos.

Ejemplos básicos para Linux (en una carpeta de prueba):

```bash
pwd          # muestra el directorio actual
ls           # lista archivos y carpetas
mkdir prueba # crea una carpeta
cd prueba    # entra en ella
```

El alumnado debe realizar estos comandos en una cuenta de prácticas y comprender qué hacen antes de ejecutarlos. No introducir comandos destructivos ni usar privilegios de administrador sin supervisión.

## 7. Archivos, carpetas, rutas y permisos

Un **archivo** almacena información; una **carpeta o directorio** permite organizar archivos. La **ruta** indica su ubicación. Una **extensión**, como `.txt`, `.jpg` o `.py`, suele ayudar a reconocer el formato, aunque no garantiza por sí sola el tipo real de archivo.

- Ruta típica en Windows: `C:\\Usuarios\\Alumno\\Documentos`.
- Ruta típica en Linux: `/home/alumno/Documentos`.
- La cuenta de usuario y los permisos determinan quién puede leer, modificar o ejecutar determinados archivos.
- Los sistemas de archivos, como NTFS, ext4 o FAT32, organizan cómo se almacenan los datos en los dispositivos.

**Actividad:** crear una estructura con carpetas `Digitalizacion/Tema2/Practicas`, guardar un archivo de texto y localizar su ruta.

## 8. Distribuciones GNU/Linux

**Linux** es el nombre del núcleo. Una **distribución GNU/Linux** reúne ese núcleo con utilidades, programas, sistema de instalación, actualizaciones y, en muchos casos, un escritorio. No todas las distribuciones incluyen los mismos componentes ni requieren los mismos recursos.

| Distribución | Enfoque principal | Ligereza | Coste de uso / soporte | Descarga oficial |
|---|---|---|---|---|
| **Linux Mint** | Escritorio sencillo para quien empieza | Edición Xfce relativamente ligera; Cinnamon suele requerir más recursos | Uso gratuito; donaciones voluntarias | [linuxmint.com/download.php](https://linuxmint.com/download.php) |
| **Alpine Linux** | Sistema minimalista, contenedores y servidores | Muy ligera en configuraciones mínimas; no es un escritorio completo listo para principiantes | Gratuito y de código abierto | [alpinelinux.org/downloads](https://alpinelinux.org/downloads/) |
| **Debian** | Escritorio y servidor; gran variedad de paquetes | Depende del escritorio instalado; puede ser muy ligera | Gratuito; soporte de terceros opcional | [debian.org/distrib](https://www.debian.org/distrib/) |
| **Red Hat Enterprise Linux (RHEL)** | Empresas y servidores profesionales | Depende de la configuración | Suscripciones comerciales; existen condiciones de acceso sin coste para determinados desarrolladores y usos | [redhat.com](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) |
| **LliureX** | Entorno educativo valenciano | Depende del equipo y edición | Descarga y utilización gratuitas | [lliurex.net](https://portal.edu.gva.es/lliurex/) |

**Aclaraciones:** Linux Mint no es necesariamente la distribución más ligera: Alpine es más minimalista, pero más compleja para principiantes. Debian con un entorno ligero también puede ser adecuada para ordenadores modestos. LliureX es la distribución educativa de la Comunitat Valenciana. Los requisitos de RAM, CPU y espacio dependen de la versión y deben consultarse en sus páginas oficiales antes de una instalación.

### 8.1. Elegir una distribución según el equipo

- Para **empezar con un PC doméstico o de clase**: Linux Mint o LliureX, si cumplen los requisitos.
- Para **un equipo antiguo**: una distribución con escritorio ligero (por ejemplo Mint Xfce o Debian con Xfce/LXQt), comprobando RAM y compatibilidad.
- Para **servidores y proyectos técnicos**: Debian, Alpine o Red Hat según necesidades de administración y soporte.
- Para **un centro educativo valenciano**: investigar el papel de LliureX y sus recursos educativos.

**No confundir:** poder descargar gratis una imagen ISO no garantiza que todos los servicios profesionales de una distribución sean gratuitos.

<!-- IMAGEN: img/distribuciones-linux.svg | TITULO: Distribuciones GNU/Linux | POSICION: DESPUES -->

## 9. Descarga e instalación de sistemas operativos

Una **imagen ISO** es un archivo que contiene una imagen de un soporte de instalación o arranque. Se debe descargar desde la **web oficial**, seleccionar la versión y arquitectura compatibles, leer los requisitos y, cuando sea posible, verificar la suma de comprobación (SHA-256) publicada.

En una instalación normal, el asistente puede crear o modificar particiones y **borrar archivos**. Por eso no se debe instalar un sistema sobre un ordenador que contenga datos importantes sin autorización y copia de seguridad. Para practicar, se puede usar una máquina virtual o arrancar un USB en modo Live.

## 10. Crear un USB de arranque desde Linux y utilizarlo en modo Live

**Objetivo:** arrancar temporalmente un ordenador con Linux desde una memoria USB, sin instalarlo, para conocer el sistema o intentar acceder a archivos de un ordenador cuyo sistema habitual no arranca.

**Material:** ordenador Linux operativo, una memoria USB de capacidad suficiente y una imagen ISO de una distribución que ofrezca modo Live. **Atención: preparar el USB suele borrar todo su contenido.**

1. Descargar la ISO desde la página oficial de Linux Mint u otra distribución con modo Live.
2. Conectar una memoria USB vacía o con archivos ya respaldados.
3. Abrir una herramienta gráfica adecuada en Linux, por ejemplo **Discos de GNOME** (opción de restaurar imagen de disco, cuando esté disponible) o **KDE ISO Image Writer**. Seleccionar la ISO y comprobar cuidadosamente el USB de destino.
4. Grabar la imagen. No copiar simplemente el archivo `.iso` al USB como si fuera un documento: hay que crear el medio arrancable con una herramienta apropiada.
5. Reiniciar el ordenador de prueba y abrir su **menú de arranque** (la tecla varía según fabricante; puede ser F12, Esc, F9 u otra).
6. Seleccionar el USB y elegir **Probar / Live** si el menú lo permite. No elegir instalar si solo se quiere probar.
7. Explorar el escritorio, el administrador de archivos y, si procede, una unidad interna accesible. Copiar los documentos recuperables a un almacenamiento externo distinto.

**Limitaciones y precauciones:** algunos equipos necesitan ajustes compatibles de UEFI/Secure Boot; un disco cifrado requerirá la clave; un soporte físicamente dañado puede ser ilegible; un USB Live no garantiza recuperar todos los ordenadores ni reparar cualquier avería. En equipos del aula, hacerlo siempre con permiso y supervisión. Evitar modificar particiones o escribir sobre un disco que pueda estar dañado antes de salvaguardar sus datos.

<!-- IMAGEN: img/usb-live-linux.svg | TITULO: Arranque desde un USB Live | POSICION: DESPUES -->

**Actividad de clase:** en un ordenador autorizado, preparar un USB Live, arrancar una sesión de prueba, identificar el sistema operativo y localizar una carpeta de ejemplo. Documentar en cuatro capturas los pasos y explicar por qué el sistema instalado permanece sin cambios cuando no se ejecuta el instalador ni se modifica el disco.

<!-- IMAGEN: img/recuperacion-archivos-linux.svg | TITULO: Recuperación de archivos de Windows con Linux Live | POSICION: DESPUES -->

## 11. Actualizaciones, mantenimiento y seguridad

Actualizar el sistema y sus aplicaciones corrige errores y vulnerabilidades. Conviene usar fuentes oficiales, realizar copias de seguridad, proteger las contraseñas, limitar los permisos de administrador y reconocer mensajes sospechosos. Un equipo sin actualizaciones de seguridad es más vulnerable, independientemente de que utilice Windows, Linux o macOS.

## 12. Actividades propuestas

1. **Identificar funciones:** relacionar seis acciones (imprimir, guardar, abrir aplicación, conectar Wi-Fi, cambiar usuario, ejecutar dos programas) con funciones del sistema operativo.
2. **Comparar costes:** elaborar una tabla de tres casos (PC con Windows, PC con Mint, servidor con RHEL) diferenciando licencia, soporte, hardware y mantenimiento.
3. **Investigar distribuciones:** elegir dos de Mint, Alpine, Debian, RHEL o LliureX y comparar público objetivo, requisitos, escritorio y licencia.
4. **Archivos y terminal:** crear, localizar y mostrar el contenido de una carpeta de pruebas desde la interfaz gráfica y el terminal.
5. **USB Live:** preparar un USB con una ISO oficial y practicar el arranque en un equipo autorizado, sin instalar ni modificar sus discos.

## 13. Preguntas de repaso

1. ¿Por qué el sistema operativo no es lo mismo que una aplicación?
2. ¿Qué función tienen el kernel, la RAM y los controladores?
3. ¿Qué diferencia existe entre interfaz gráfica y terminal?
4. ¿En qué se diferencian «gratuito», «libre» y «propietario»?
5. ¿Por qué una distribución Linux puede ser gratis y otra tener soporte de pago?
6. ¿Qué distribución elegirías para un ordenador antiguo y por qué?
7. ¿Qué es una ISO y por qué no basta normalmente con copiarla como archivo a una memoria USB?
8. ¿Qué permite hacer un sistema Live y qué limitaciones tiene?
9. ¿Por qué es importante realizar una copia de seguridad antes de instalar un sistema operativo?

## 14. Glosario

- **Sistema operativo:** software base que coordina recursos y permite ejecutar aplicaciones.
- **Kernel o núcleo:** componente central del sistema operativo.
- **Proceso:** programa en ejecución.
- **Controlador:** componente de software que facilita la comunicación con un dispositivo.
- **GUI / CLI:** interfaz gráfica / interfaz de línea de comandos.
- **Distribución:** conjunto de sistema, herramientas y aplicaciones preparado para su instalación o uso.
- **Software libre:** software que respeta ciertas libertades de uso, estudio, modificación y redistribución.
- **Software propietario:** software cuyo uso, modificación o distribución están restringidos por su licencia.
- **ISO:** archivo con una imagen de medio de instalación o arranque.
- **USB Live:** memoria arrancable que permite iniciar un sistema sin instalarlo en el disco interno.
- **UEFI:** firmware moderno que ayuda a iniciar el ordenador.
- **Partición:** división lógica de un dispositivo de almacenamiento.


<!-- PRESENTACION:EXCLUIR -->

## 15. Ampliación opcional: casos reales de uso y mantenimiento cotidiano

Este apartado complementa el temario básico y **no se incorpora automáticamente a las presentaciones**. Conecta el funcionamiento de los sistemas operativos con situaciones que pueden surgir en casa o en el aula.

### 15.1. ¿Qué ocurre al encender un ordenador?

1. Al pulsar el botón de encendido, el equipo comienza a alimentar sus componentes.
2. El firmware **UEFI/BIOS** comprueba e inicializa parte del hardware y localiza un dispositivo de arranque.
3. Un **gestor de arranque** inicia la carga del sistema operativo.
4. El **núcleo o kernel** comienza a gestionar memoria, procesos y dispositivos.
5. Se inician servicios y aparece la pantalla de inicio de sesión y, después, el escritorio.

**Relación con el Tema 1:** la CPU ejecuta instrucciones, el almacenamiento contiene el sistema y la RAM permite cargar los programas en funcionamiento.

### 15.2. Máquinas virtuales: dos sistemas operativos en un equipo

Una **máquina virtual** es un ordenador simulado mediante software. Herramientas como VirtualBox permiten, en equipos compatibles y con recursos suficientes, probar un sistema operativo invitado (por ejemplo, Debian) dentro de otro anfitrión (por ejemplo, Windows o Linux), sin reemplazar el sistema original.

**Ejemplo:** arrancar Debian en una ventana, practicar con carpetas y apagar la máquina virtual. Necesita RAM, CPU y almacenamiento propios asignados y un archivo ISO o disco virtual. No confundir una máquina virtual con arrancar un USB Live.

### 15.3. Dar una segunda vida a un ordenador antiguo

En un equipo con poca RAM o procesador modesto puede ser útil una distribución con entorno de escritorio ligero, como Debian con LXQt/Xfce o Linux Mint Xfce. **No todos los sistemas Linux consumen menos que Windows**: el resultado depende de la versión, el escritorio, los servicios, los controladores y las aplicaciones abiertas.

**Actividad propuesta:** anotar procesador, RAM y almacenamiento de un ordenador y comparar los requisitos oficiales de varias distribuciones. Hablar también del ahorro económico y de la reducción de residuos electrónicos por reutilización.

### 15.4. ¿Qué hacer cuando una aplicación se bloquea?

El sistema operativo gestiona procesos y puede ayudar a identificar un programa que no responde. En Windows puede utilizarse el **Administrador de tareas**; en Linux, el **Monitor del sistema** o herramientas equivalentes. Antes de finalizar una aplicación es conveniente intentar guardar el trabajo; cerrar a la fuerza puede hacer perder cambios sin guardar.

**Práctica:** abrir dos aplicaciones, consultar su consumo aproximado de CPU y memoria, y describir las diferencias sin forzar bloqueos reales.

### 15.5. Privacidad y permisos

Los sistemas operativos ofrecen configuraciones relacionadas con ubicación, cámara, micrófono, actualizaciones y datos de diagnóstico. Algunas funciones y servicios pueden recopilar información según las opciones activadas y las políticas del proveedor.

**Práctica:** revisar los permisos de una aplicación de ejemplo sin modificar cuentas ajenas ni compartir información personal.

### 15.6. Recuperar archivos cuando Windows no arranca

A veces **Windows deja de arrancar, pero los archivos siguen guardados en el disco**. Un USB con una distribución Linux en modo Live puede permitir acceder a ellos y copiarlos a otra unidad, siempre que el almacenamiento sea legible y se disponga de las credenciales o claves necesarias. **Rescatar archivos no equivale a reparar Windows.**

**Actividad práctica de ampliación:** [Recuperar archivos de un Windows que no arranca mediante un USB Live de Linux](actividades/actividad-01-recuperar-archivos-windows-usb-linux.md). Se realiza sobre equipos autorizados con archivos ficticios, sin reinstalar ni modificar particiones. Un disco cifrado o averiado puede requerir asistencia especializada.

<!-- PRESENTACION:FIN_EXCLUSION -->

---

## Control de versiones

- **Versión del contenido:** 1.2.1
- **Última actualización:** 20/11/2026
- **Estado:** Contenido aprobado y ampliable
