# Actividad de ampliación 1. Recuperar archivos de un Windows que no arranca usando un USB Live de Linux

**Materia:** Digitalización · 4.º ESO · Tema 2. Sistemas operativos  
**Modalidad:** Práctica guiada por el docente, por parejas  
**Duración estimada:** 1–2 sesiones  
**Estado:** Propuesta de ampliación

[Volver al Tema 2](../tema-02.md) · [Índice de actividades](README.md)

## Situación-problema

Un ordenador de prácticas tiene Windows instalado, pero no llega al escritorio. El objetivo **no es reparar Windows a cualquier precio**, sino comprobar si los archivos personales siguen accesibles y realizar una **copia de recuperación** arrancando un sistema Linux desde un USB, sin instalar Linux ni borrar Windows.

## Objetivos

- Diferenciar un fallo de arranque de Windows de un fallo físico del disco.
- Comprender el arranque desde USB y el modo *Live*.
- Identificar una partición de datos y copiar archivos a otro dispositivo.
- Documentar pruebas y límites de recuperación sin poner en peligro la información.

## Materiales

- Equipo de pruebas autorizado por el centro, preferiblemente con **datos ficticios** preparados por el docente.
- USB arrancable con una distribución con entorno Live, como Linux Mint, preparado siguiendo el apartado 10 del tema.
- Segunda memoria USB o disco externo para guardar la copia (no utilizar el propio USB Live como destino salvo que esté expresamente preparado para ello).
- Archivos ficticios de ejemplo: `Documentos/actividad.txt`, `Fotos/prueba.jpg`.
- Permiso y supervisión del docente para acceder al equipo y a sus datos.

> **Seguridad de los datos:** no hacer la práctica sobre un ordenador de otra persona ni consultar archivos privados. No formatear, reinstalar, reparar particiones, ejecutar comandos de escritura ni cambiar el arranque del disco sin autorización. Si hay indicios de avería física (ruidos extraños, desconexiones, errores repetidos), detener la prueba y consultar a un profesional. Si hay cifrado BitLocker u otro cifrado, necesitarás la **clave de recuperación legítima**; no intentar eludirlo.

## Procedimiento paso a paso

1. **Preparación del escenario.** El profesor simula un Windows que no termina de arrancar en un equipo de laboratorio o plantea el caso mediante imágenes/capturas. El alumnado anota qué mensajes aparecen y qué hipótesis tiene.
2. **Comprobar el medio.** Identificar cuál es el USB Live y cuál el USB de destino para la copia. Recordar que crear el USB de arranque normalmente borra el contenido previo de ese USB.
3. **Arrancar Linux Live.** Conectar el USB Live, reiniciar y abrir el menú de arranque UEFI/BIOS, si el equipo lo permite. Seleccionar el USB y la opción **Probar Linux** o equivalente, **sin instalar**.
4. **Identificar las unidades.** Abrir el gestor gráfico de archivos o la utilidad **Discos**. Observar tamaños y etiquetas para distinguir el dispositivo interno, el USB Live y el dispositivo de copia. No elegir opciones de formateo o reparación.
5. **Comprobar acceso.** Si el volumen de Windows aparece y se puede abrir de forma segura, localizar solamente la carpeta de pruebas autorizada. En un Windows típico puede estar bajo `Users/Alumno/Documents`; la ubicación real depende del sistema y usuario.
6. **Copiar los archivos.** Conectar el segundo USB, crear en él una carpeta `Rescate-Tema2` y **copiar** los archivos de prueba desde la unidad de Windows. Nunca mover ni borrar los originales. Si la unidad no monta o solicita reparar, detenerse y consultar al docente.
7. **Verificar la copia.** Abrir desde el USB de destino el archivo de texto y comprobar que la imagen se visualiza correctamente. Comparar número de archivos y tamaños.
8. **Cerrar con seguridad.** Expulsar las unidades externas desde el sistema cuando sea posible, apagar Linux y retirar el USB Live siguiendo las indicaciones del equipo.
9. **Registrar conclusiones.** Distinguir entre **rescatar datos**, **reparar Windows** y **reinstalar Windows**: son operaciones distintas y la primera no garantiza las otras.

## Preguntas para el alumnado

1. ¿Por qué se puede acceder a los archivos de un ordenador aunque Windows no arranque?
2. ¿Qué diferencia hay entre **iniciar Linux en modo Live** e instalar Linux?
3. ¿Por qué conviene copiar los archivos a **otra unidad**, en lugar de moverlos?
4. ¿Qué ocurriría si el disco está físicamente averiado o cifrado?
5. ¿Qué precauciones adoptarías si los archivos fueran personales y no datos de prueba?
6. ¿Cómo verificarías que la recuperación se ha realizado correctamente?

## Entrega

Documento breve con: diagnóstico inicial, esquema de los tres dispositivos (disco interno, USB Live, USB de copia), cuatro capturas autorizadas de la práctica y respuestas a las seis preguntas. No incluir datos privados.

## Criterios de logro

- Identifica correctamente los dispositivos y evita sobrescribirlos.
- Arranca o describe correctamente un sistema Live sin instalarlo.
- Realiza y verifica la copia de archivos ficticios o explica el bloqueo encontrado.
- Diferencia recuperación de datos, reparación del sistema y reinstalación.
- Respeta las normas de seguridad, privacidad y supervisión.

## Alternativa sin equipos disponibles

El profesor muestra capturas del arranque Live y tres unidades simuladas. El alumnado ordena los pasos, decide dónde buscar el archivo y señala **qué acciones serían peligrosas**. Se evalúa el procedimiento, sin necesidad de provocar un fallo real en Windows.

---

**Fecha:** 20/11/2026 · **Versión:** 1.0.0
