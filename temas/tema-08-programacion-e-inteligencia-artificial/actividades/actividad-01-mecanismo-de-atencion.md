# Actividad 1. ¿Cómo relaciona las palabras una inteligencia artificial?

**Materia:** Digitalización · 4.º ESO  
**Duración orientativa:** 25–30 minutos  
**Modalidad:** Individual y puesta en común  
**Material:** Vídeo explicativo del mecanismo de atención facilitado por el profesor y cuaderno o documento digital.

## Objetivos
- Descubrir que los modelos de lenguaje procesan unidades de texto mediante representaciones numéricas.
- Comprender, de forma intuitiva, cómo el mecanismo de **atención** relaciona diferentes palabras de una oración.
- Reconocer las ambigüedades del lenguaje y explicar por qué una IA puede equivocarse.

## 1. Observa el vídeo
Tras ver el vídeo, responde:
1. ¿Por qué una IA necesita relacionar unas palabras con otras?
2. ¿Qué significa que una palabra preste más «atención» a otra?
3. ¿La IA comprende la frase exactamente igual que una persona? Explica tu respuesta.

## 2. Conviértete en un mecanismo de atención
Lee cada oración y decide a qué se refiere la expresión destacada. Justifica tu decisión indicando qué palabras del contexto te han ayudado.

**A.** «María dejó la mochila en el suelo porque **pesaba mucho**». ¿Qué pesaba mucho: María, la mochila o el suelo?

**B.** «Pedro guardó el ordenador en la caja porque **estaba roto**». ¿Qué estaba roto: el ordenador o la caja? ¿Podemos saberlo con total seguridad?

**C.** «Ana puso el helado en la nevera porque **se estaba derritiendo**». ¿Qué se estaba derritiendo: el helado o la nevera?

## 3. Representa las relaciones
Elige una frase del ejercicio anterior. Rodea la expresión que debemos interpretar y dibuja flechas hacia las palabras que crees relevantes. Dibuja una flecha más gruesa hacia la palabra que consideres más relacionada. **Este dibujo es una analogía**, no un cálculo real realizado por una IA.

## 4. Un ejemplo que puede confundir a la IA
«Laura vio a Marta con unos prismáticos».

1. Escribe dos interpretaciones diferentes de la oración.
2. Añade una oración de contexto que permita distinguir quién tenía los prismáticos.
3. Explica por qué la IA no debería afirmar con seguridad una única interpretación sin contexto suficiente.

## 5. Explicación científica simplificada
Los modelos de lenguaje dividen el texto en **tokens**, convierten estos tokens en números y emplean mecanismos matemáticos como la **atención** para combinar información relevante de distintas posiciones del texto. En la atención de tipo *query-key-value*, **Q** representa lo que se busca, **K** ayuda a medir la relación y **V** aporta la información que se combina. La analogía de flechas simplifica mucho el proceso: no equivale a decir que el modelo identifica siempre un referente único ni que entiende como una persona.

## Entrega
Un documento con las respuestas de las partes 1, 2 y 4 y un dibujo de flechas de la parte 3.

## Evaluación (10 puntos)
- Interpretación y justificación de las tres frases: **3 puntos**.
- Representación de relaciones mediante flechas: **2 puntos**.
- Dos interpretaciones y contexto para la frase de los prismáticos: **2 puntos**.
- Explicación sencilla de tokens y atención: **2 puntos**.
- Claridad y presentación: **1 punto**.

## Orientaciones para el profesorado
- A: la mochila; C: el helado. 
- B: «el ordenador» es una interpretación probable, pero «la caja» también es gramatical y semánticamente posible.
- En «Laura vio a Marta con unos prismáticos», Laura podría haber usado los prismáticos para ver a Marta, o Marta podría llevarlos.
- Insistir en que la atención no es una prueba infalible de comprensión ni se limita a resolver pronombres.
