# Actividad 3. Tu primer programa: condiciones y bucles

**Digitalización · 4.º ESO**  
**Duración:** 40–50 minutos · **Modalidad:** individual o parejas  
**Herramienta:** Python 3 en un entorno de clase autorizado.

[Volver al tema 8](../tema-08.md)

## Objetivo
Crear un programa sencillo con una variable, una condición y un bucle, y comprobar que funciona con diferentes datos.

## Reto
Un programa pide la temperatura de **tres días**. Para cada temperatura indica si hace frío (menos de 10 °C) o no. Después muestra cuántos días fueron fríos.

## Código inicial
```python
dias_frios = 0

for dia in range(1, 4):
    temperatura = float(input(f"Temperatura del día {dia} (°C): "))
    if temperatura < 10:
        print("Hace frío")
        dias_frios += 1
    else:
        print("No hace frío")

print("Días fríos:", dias_frios)
```

## Tareas
1. Copia el código, ejecútalo y explica qué almacenan las variables `temperatura` y `dias_frios`.
2. Identifica la **condición** y el **bucle**. ¿Cuántas veces se repite?
3. Comprueba estos datos: **5, 12 y 9 °C**. ¿Qué resultado debería mostrar? Compara tu predicción con la ejecución.
4. Cambia el programa para evaluar **cinco días** en lugar de tres.
5. Cambia el límite de frío de 10 °C a 15 °C y explica qué líneas has modificado.
6. Explica qué ocurre si el usuario introduce texto en lugar de un número. No es necesario resolver ese error, pero sí reconocerlo.

## Entrega
Código completo y capturas o transcripción de dos ejecuciones, con una explicación breve de las modificaciones.

## Evaluación (10 puntos)
- Comprensión de variables, condición y bucle: **3 puntos**.
- Programa ejecutado y pruebas: **3 puntos**.
- Modificaciones solicitadas: **3 puntos**.
- Explicación de errores y claridad: **1 punto**.

**Importante:** este ejemplo es **programación con reglas explícitas**, no un modelo de aprendizaje automático.
