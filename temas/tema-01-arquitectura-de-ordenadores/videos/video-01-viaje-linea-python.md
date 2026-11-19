# Vídeo 01. El viaje de una línea de código por el ordenador

**Tema:** 1. Arquitectura de ordenadores · Digitalización 4.º ESO  
**Estado:** Guion e idea preparados; vídeo no generado  
**Duración orientativa:** 60-90 segundos  
**Actualización:** 19/11/2026

[Volver al índice de vídeos](README.md) · [Actividad práctica relacionada](../actividades/actividad-01-hola-mundo-python.md)

## Objetivo didáctico

Visualizar cómo colaboran almacenamiento, RAM, CPU, sistema operativo y pantalla cuando se ejecuta un programa Python simple, y relacionar la CPU con sus transistores.

## Ejemplo que aparece en pantalla

```python
print("Hola mundo")
```

## Guion por escenas

1. **El alumno escribe y guarda (0-15 s).** Primer plano de un editor de texto. El alumnado escribe la línea y guarda el archivo `hola.py` en el SSD. Voz: «El archivo queda guardado aunque apaguemos el ordenador».
2. **Pulsa Ejecutar (15-30 s).** Una animación distingue archivo, sistema operativo e intérprete de Python. El sistema operativo carga en RAM el intérprete y los datos necesarios, y accede al programa. Voz: «La RAM permite trabajar rápidamente con lo que se está ejecutando».
3. **Trabaja la CPU (30-50 s).** Acercamiento visual a la CPU; el intérprete interpreta/ejecuta las instrucciones de Python mediante instrucciones de máquina procesadas por la CPU. Zoom a circuitos lógicos construidos con transistores. Voz: «La CPU no entiende directamente el texto Python: ejecuta instrucciones de máquina del intérprete».
4. **Se muestra el resultado (50-65 s).** El texto `Hola mundo` aparece en la terminal. El sistema de gráficos y, cuando corresponda, la GPU, ayudan a representar la ventana en el monitor. Voz: «El resultado llega a la ventana que vemos en la pantalla».
5. **Resumen (65-90 s).** Esquema visual: archivo en SSD → RAM/intérprete → CPU/transistores → salida en terminal/pantalla. Mensaje final: «Hardware y software colaboran para ejecutar una sola línea».

## Indicaciones para generar el vídeo con IA

Animación didáctica 2D, estilo infografía clara, componentes identificados con rótulos grandes, movimiento lento de flechas y partículas para representar el flujo de información; relación visual entre código, datos y hardware sin mostrar componentes que se desplacen físicamente. Público de 14-16 años. Narración en español, subtítulos legibles, fondo sencillo, sin marcas comerciales ni interfaces inventadas.

**Precauciones de exactitud:** no afirmar que el archivo Python se transforma directamente en instrucciones de CPU; el intérprete participa en la ejecución. No atribuir la ejecución del código Python a la GPU; su papel, cuando existe, corresponde a la representación gráfica. El sistema operativo gestiona procesos y memoria. El esquema es una simplificación pedagógica, no una traza literal de cada acceso.

## Actividad complementaria

[Crear, guardar y ejecutar `hola.py`](../actividades/actividad-01-hola-mundo-python.md). Después, identificar en un esquema las funciones del SSD, RAM, CPU y pantalla.

## Pendiente para producción

- Elegir generador de vídeo y formato de salida.
- Generar voz, escenas y subtítulos; revisar la exactitud técnica.
- Guardar o enlazar el vídeo final y cambiar su estado a **revisado** o **publicado** solo tras comprobarlo.
