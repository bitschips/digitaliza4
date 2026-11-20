# Imágenes del Tema 2. Sistemas operativos

Ilustraciones SVG originales para el contenido didáctico de Digitalización, 4.º ESO.

| Archivo | Concepto | Apartado |
|---|---|---|
| [escritorio-sistema-operativo.svg](escritorio-sistema-operativo.svg) | Funciones del escritorio y del sistema | 1 |
| [comparacion-sistemas-operativos.svg](comparacion-sistemas-operativos.svg) | Sistemas en ordenadores y móviles | 4 |
| [distribuciones-linux.svg](distribuciones-linux.svg) | Linux Mint, Debian, Alpine y LliureX | 8 |
| [usb-live-linux.svg](usb-live-linux.svg) | Iniciar Linux en modo Live | 10 |
| [recuperacion-archivos-linux.svg](recuperacion-archivos-linux.svg) | Recuperar archivos con un USB Live | 10 |

Son **ilustraciones didácticas**, no capturas exactas de aplicaciones ni pantallas reales. Las referencias a los sistemas y sus menús son simplificadas.

## Integración en presentaciones

Las cinco imágenes se enlazan con comentarios `<!-- IMAGEN: ... -->` en [tema-02.md](../tema-02.md). Cada comentario produce una diapositiva independiente en HTML y PowerPoint mediante `scripts/generar_presentaciones.py`. El generador convierte internamente los SVG a imágenes de mapa de bits para PowerPoint mediante CairoSVG; el HTML utiliza directamente los SVG vectoriales.

No insertar nuevas imágenes en bloques excluidos de presentación salvo instrucción expresa. Mantener nombres descriptivos, rutas relativas y proporción 16:9.
