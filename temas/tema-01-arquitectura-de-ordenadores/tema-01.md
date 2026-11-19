# Tema 1. Arquitectura de ordenadores

**Materia:** Digitalización · 4.º ESO · Comunitat Valenciana  
**Estado:** Borrador didáctico ampliable

[Volver al índice general](../../README.md)

## Materiales del tema

- [Presentación HTML — abrir en el navegador](https://htmlpreview.github.io/?https://github.com/bitschips/digitalizaci-n-4/blob/main/temas/tema-01-arquitectura-de-ordenadores/presentaciones/tema-01.html)
- [Presentación PPTX — descargar](presentaciones/tema-01-arquitectura-de-ordenadores.pptx)
- [Actividades](actividades/)

## Objetivos de aprendizaje

Al finalizar este tema, el alumnado debería poder:

- Explicar cómo representa un ordenador la información en formato digital.
- Identificar los componentes principales de un ordenador y su función.
- Distinguir hardware, software y periféricos.
- Relacionar características de los equipos con su rendimiento y uso.
- Reconocer semejanzas y diferencias entre ordenadores y dispositivos móviles.

## 1. Representación digital de la información

Los ordenadores procesan información mediante señales digitales que se representan con dos valores: **0 y 1**. Cada valor se denomina **bit**. Un conjunto de ocho bits forma un **byte**, una unidad habitual para expresar el tamaño de los datos.

Los mismos bits pueden representar distintos tipos de información dependiendo de las reglas de codificación que se utilicen:

- **Texto:** las letras y los símbolos se convierten en números mediante códigos como ASCII o Unicode.
- **Imágenes:** se representan con píxeles; cada píxel almacena información sobre su color.
- **Sonido:** se digitaliza tomando muestras de una señal de audio.
- **Vídeo:** combina una sucesión de imágenes con sonido.

**Ejemplo:** el número binario `01000001` corresponde a la letra «A» en ASCII. Una fotografía también se guarda como datos binarios, aunque su representación es más compleja.

**Unidades frecuentes:** bit (b), byte (B), megabyte (MB), gigabyte (GB) y terabyte (TB). Conviene distinguir la capacidad de almacenamiento de la velocidad de transferencia.

## 2. Hardware y componentes de un ordenador

El **hardware** es el conjunto de componentes físicos de un dispositivo. El **software** es el conjunto de programas e instrucciones que permiten utilizarlo.

| Componente | Función principal | Ejemplo de uso |
|---|---|---|
| Procesador (CPU) | Ejecuta instrucciones y realiza operaciones | Abrir un programa y efectuar cálculos |
| Memoria RAM | Guarda temporalmente datos de los programas en uso | Trabajar con varias aplicaciones abiertas |
| Almacenamiento (SSD/HDD) | Conserva archivos y programas aunque se apague el equipo | Guardar documentos y fotografías |
| Placa base | Conecta y permite comunicar los componentes | Conectar CPU, RAM y unidades de almacenamiento |
| Procesador gráfico (GPU) | Acelera el procesamiento de gráficos y otros cálculos | Videojuegos, edición y determinadas tareas de IA |
| Fuente de alimentación | Proporciona energía eléctrica al equipo | Alimentar los componentes de un PC |

Los **periféricos de entrada** permiten introducir información (teclado, ratón, micrófono), los **de salida** muestran resultados (monitor, altavoces) y algunos permiten ambas operaciones (pantalla táctil, memoria USB).

### 2.1. ¿Cómo trabajan juntos?

Al abrir una aplicación, sus datos pasan normalmente del almacenamiento a la memoria RAM. La CPU ejecuta sus instrucciones y, cuando es necesario mostrar imágenes, interviene la GPU. El sistema operativo coordina el uso de estos recursos.

**Idea clave:** la RAM es temporal; el almacenamiento conserva los archivos. No cumplen la misma función.


### 2.2. El transistor: la pieza básica de las CPU y GPU

Un **transistor** es un componente electrónico diminuto fabricado con material semiconductor, normalmente **silicio**. Se puede utilizar como un **interruptor electrónico** que deja pasar o interrumpe una corriente según la señal que recibe. Esta idea sirve para explicar, de forma sencilla, cómo funcionan los circuitos digitales.

- **0 y 1:** los circuitos representan estos valores mediante niveles eléctricos. *Un transistor no equivale por sí solo a un bit*: se combinan muchos transistores para construir circuitos más complejos.
- **Puertas lógicas:** al combinar transistores obtenemos circuitos que realizan operaciones como AND, OR y NOT.
- **CPU y GPU:** integran enormes cantidades de transistores para realizar cálculos, almacenar información temporal y controlar distintas operaciones.

**Ejemplo para clase:** imagina muchos interruptores minúsculos que se conectan entre sí. Con ellos se pueden construir circuitos capaces de sumar números y tomar decisiones sencillas.

#### Evolución del número de transistores en procesadores y SoC

| Año | Procesador | Transistores aproximados | Tipo |
|---|---|---:|---|
| 1971 | Intel 4004 | 2.300 | CPU |
| 1978 | Intel 8086 | 29.000 | CPU |
| 1993 | Intel Pentium | 3,1 millones | CPU |
| 2000 | Intel Pentium 4 | 42 millones | CPU |
| 2006 | Intel Core 2 Duo | 291 millones | CPU |
| 2020 | Apple M1 | 16.000 millones | SoC |
| 2024 | Apple M4 | 28.000 millones | SoC |

**Importante:** los Apple M1 y M4 son **sistemas en chip (SoC)**. El recuento incluye CPU, GPU y otros componentes integrados; por tanto, no es exactamente comparable con los procesadores Intel clásicos.

#### Evolución de los chips gráficos y de IA de NVIDIA

| Año | Chip NVIDIA | Transistores aproximados | Uso destacado |
|---|---|---:|---|
| 1999 | GeForce 256 | 23 millones | Gráficos 3D |
| 2006 | GeForce 8800 GTX | 681 millones | Videojuegos y gráficos |
| 2016 | GeForce GTX 1080 | 7.200 millones | Gráficos y realidad virtual |
| 2022 | GeForce RTX 4090 | 76.300 millones | Gráficos y cálculos de IA |
| 2024 | NVIDIA Blackwell B200 | 208.000 millones | Aceleración de inteligencia artificial |

En Blackwell B200 se contabilizan los transistores de **dos bloques de silicio (dies)** conectados para funcionar como una GPU. No es un único bloque monolítico.

Este crecimiento recuerda a la **ley de Moore**, una observación histórica sobre el aumento de transistores en los chips. No es una ley física que garantice duplicaciones indefinidas. Además, **más transistores no significa necesariamente más velocidad**: también influyen el diseño, el consumo energético, la memoria y la refrigeración.

**Actividad rápida:** ¿cuántas veces más transistores tiene el Intel 8086 que el 4004? ¿Por qué no sería justo comparar directamente el Apple M4 con el Intel 4004 o el NVIDIA B200?

**Fuentes de los datos históricos:** [Intel, historia del 4004](https://www.intel.com/pressroom/archive/releases/2001/20011115corp_a.htm), [Intel, 8086](https://www.intel.com/pressroom/archive/releases/2003/20030609corp.htm), [Intel, referencia de microprocesadores](https://www.intel.com/pressroom/kits/quickreffam.htm), [Intel, Core 2 Duo](https://www.intel.com/pressroom/archive/releases/2006/20060727comp.htm), [Apple M1](https://www.apple.com/uk/newsroom/2020/11/apple-unleashes-m1/), [Apple M4](https://www.apple.com/newsroom/2024/05/apple-introduces-m4-chip/), [NVIDIA, GeForce 256](https://download.nvidia.com/developer/cg/Cg_Tutorial/Chapter_1.pdf), [NVIDIA, GTX 1080](https://www.nvidia.com/en-us/geforce/news/geforce-gtx-1080-gaming-perfected/), [NVIDIA, RTX 4090](https://images.nvidia.com/aem-dam/Solutions/Data-Center/l4/nvidia-ada-gpu-architecture-whitepaper-V2.02.pdf), [NVIDIA Blackwell](https://investor.nvidia.com/news/press-release-details/2024/NVIDIA-Blackwell-Platform-Arrives-to-Power-a-New-Era-of-Computing/). El valor de la GeForce 8800 GTX procede de una tabla histórica en los [foros técnicos de NVIDIA](https://forums.developer.nvidia.com/t/gpu-vs-cpu-comparison-over-the-last-years/13097).

## 3. Montaje, configuración y rendimiento

Montar un ordenador implica elegir componentes compatibles, conectarlos correctamente y comprobar su funcionamiento. En un PC de sobremesa se pueden identificar la placa base, la CPU, los módulos de RAM, la unidad SSD y las conexiones de alimentación.

**Precaución:** antes de abrir un equipo es necesario apagarlo, desconectarlo de la corriente y seguir las normas de seguridad. No se debe abrir una fuente de alimentación.

La **configuración** comprende tareas como conectar periféricos, reconocer dispositivos, revisar las especificaciones e instalar el sistema operativo y los controladores cuando sea necesario.

El rendimiento depende de varios factores, no de una única cifra:

- **CPU:** arquitectura, número de núcleos, frecuencia y tipo de tarea.
- **RAM:** capacidad suficiente para ejecutar las aplicaciones previstas.
- **SSD:** velocidad de lectura y escritura y espacio disponible.
- **GPU:** importante para gráficos, vídeo, juegos y determinados cálculos.
- **Refrigeración:** evita que el equipo reduzca su velocidad por exceso de temperatura.

**Ejemplo:** sustituir un disco duro mecánico por un SSD puede acelerar mucho el arranque del sistema, pero no convierte automáticamente el procesador en uno más potente.

## 4. Dispositivos móviles

Un teléfono móvil y una tableta también son ordenadores: incorporan procesador, memoria, almacenamiento, pantalla, sistema operativo y conexiones de red.

En muchos móviles, varios componentes se integran en un único **sistema en chip (SoC)**. Además, estos dispositivos suelen incorporar batería, cámaras y sensores, como acelerómetro, giroscopio, GPS y lector de huellas.

| Aspecto | Ordenador de sobremesa | Teléfono móvil |
|---|---|---|
| Alimentación | Habitualmente conectado a la red eléctrica | Batería recargable |
| Componentes | A menudo más accesibles y ampliables | Muy integrados; poco ampliables |
| Interacción | Teclado, ratón y monitor | Pantalla táctil y sensores |
| Usos | Trabajo, creación de contenido, cálculo | Comunicación, fotografía, navegación, aplicaciones |

Las diferencias no son absolutas: existen portátiles, tabletas con teclado y móviles muy potentes.

## 5. Actividades propuestas

1. **Identificación:** elabora un esquema sencillo de un ordenador e identifica CPU, RAM, SSD, placa base y periféricos.
2. **Investigación:** consulta las especificaciones de un ordenador del aula e indica su procesador, memoria RAM, almacenamiento y sistema operativo.
3. **Comparación:** compara un ordenador con un teléfono móvil. ¿Qué componentes tienen en común? ¿Qué diferencias encuentras?
4. **Razonamiento:** explica por qué aumentar la capacidad de almacenamiento no equivale a aumentar la memoria RAM.
5. **Representación digital:** investiga cómo se representa la letra «A» en binario y explica qué significa que una imagen esté formada por píxeles.

## 6. Preguntas de repaso

- ¿Qué diferencia existe entre bit y byte?
- ¿Por qué un ordenador puede representar texto, imágenes y sonido mediante bits?
- ¿Qué diferencia hay entre hardware y software?
- ¿Qué papel desempeñan CPU, RAM y SSD cuando se ejecuta una aplicación?
- ¿Qué es un periférico? Escribe un ejemplo de entrada y otro de salida.
- ¿Qué significa SoC y por qué se utiliza en dispositivos móviles?
- ¿Por qué el rendimiento de un equipo no depende únicamente de la frecuencia del procesador?

## 7. Glosario básico

- **Bit:** unidad mínima de información digital; puede valer 0 o 1.
- **Byte:** conjunto de ocho bits.
- **CPU:** unidad que ejecuta instrucciones.
- **RAM:** memoria de trabajo temporal.
- **SSD:** dispositivo de almacenamiento persistente basado en memoria flash.
- **GPU:** procesador especializado en gráficos y cálculos paralelos.
- **Periférico:** dispositivo que permite introducir, mostrar o intercambiar información.
- **SoC:** chip que integra varios componentes de un sistema informático.

<!-- PRESENTACION:EXCLUIR -->

## 8. Ampliación: ideas para profundizar

Los siguientes contenidos son **propuestas complementarias, fuera del temario básico**. Se podrán desarrollar progresivamente mediante explicaciones visuales, vídeos cortos y, cuando proceda, actividades prácticas.

1. **¿Qué ocurre cuando encendemos un ordenador?** Seguir el proceso de arranque: firmware BIOS/UEFI, carga del sistema operativo desde el almacenamiento a la RAM y trabajo inicial de la CPU.
2. **¿Por qué un móvil puede ser tan potente como un ordenador?** Comparar CPU, SoC, núcleos, consumo de energía y refrigeración; analizar por qué la mayoría de los móviles no utilizan ventilador.
3. **¿En qué se diferencian CPU, GPU y NPU?** Explicar de forma sencilla el procesamiento general, los cálculos paralelos y la aceleración especializada de tareas de inteligencia artificial.
4. **El viaje de una línea de código por el ordenador.** Usar `print("Hola mundo")` para visualizar cómo intervienen SSD, RAM, intérprete de Python, CPU, transistores y salida en pantalla. [Idea y guion del vídeo](videos/video-01-viaje-linea-python.md) · [Actividad práctica: crear y ejecutar `hola.py`](actividades/actividad-01-hola-mundo-python.md).
5. **¿Por qué los ordenadores son cada vez más rápidos?** Partir de la evolución histórica de los transistores para introducir la ley de Moore, la fabricación a escala nanométrica, los procesadores multinúcleo y los límites térmicos y energéticos. Aclarar que más transistores no implica necesariamente más velocidad.

Estas ideas son **ampliaciones opcionales**; no sustituyen los objetivos y contenidos de los apartados anteriores. Se podrán desarrollar como futuros materiales en [Vídeos: índice de ideas](videos/README.md) y [Actividades](actividades/README.md).

<!-- PRESENTACION:FIN_EXCLUSION -->

---

> **Nota docente:** documento ampliable. Las tablas históricas incluyen chips de distinta arquitectura, época y categoría; deben interpretarse como ilustración del crecimiento tecnológico, no como una comparación directa de rendimiento. Cada apartado se mantiene separado para facilitar su adaptación a una presentación PowerPoint.

---

## Control de versiones

- **Versión del contenido:** 1.2.1
- **Última actualización:** 19/11/2026
- **Estado:** Borrador ampliable
