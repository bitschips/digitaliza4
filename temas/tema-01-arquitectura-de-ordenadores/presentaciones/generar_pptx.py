from pathlib import Path
import re
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

root=Path(__file__).resolve().parents[3]
source=root/'temas/tema-01-arquitectura-de-ordenadores/tema-01.md'
md=source.read_text(encoding='utf8')
def bullets(title):
    m=re.search(r'^## '+re.escape(title)+r'\s*\n(.*?)(?=^## |\Z)',md,re.M|re.S)
    return [re.sub(r'\*\*|\x60','',line[2:]) for line in m.group(1).splitlines() if line.startswith('- ')] if m else []
prs=Presentation()
prs.slide_width=Inches(13.333);prs.slide_height=Inches(7.5)
navy=RGBColor(16,35,56); teal=RGBColor(19,143,150); white=RGBColor(255,255,255); pale=RGBColor(242,247,250)
def add_text(s,t,x,y,w,h,sz=23,bold=False,color=None):
    sh=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h));f=sh.text_frame;f.clear();f.word_wrap=True
    p=f.paragraphs[0];p.text=t;p.font.name='Aptos';p.font.size=Pt(sz);p.font.bold=bold;p.font.color.rgb=color or navy
def add_box(s,x,y,w,h,color):
    sh=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h));sh.fill.solid();sh.fill.fore_color.rgb=color;sh.line.fill.background()
def slide(title,lines,compact=False):
    s=prs.slides.add_slide(prs.slide_layouts[6])
    add_box(s,0,0,13.33,7.5,pale)
    add_box(s,.2,.2,.13,7.05,teal)
    add_text(s,'DIGITALIZACIÓN · 4.º ESO',.8,.35,11,.35,12,True,teal)
    add_text(s,title,.8,.85,11.8,1,32,True)
    if len(lines)<=4:
        for i,line in enumerate(lines):
            add_box(s,.84,2.05+i*1.13,11.55,.94,white)
            add_text(s,line,1.05,2.26+i*1.13,11.1,.58,19 if compact else 21)
    else:
        for i,line in enumerate(lines[:7]):
            add_box(s,.84,1.95+i*.69,11.55,.59,white)
            add_text(s,line,1.03,2.07+i*.69,11.1,.42,17)
    add_text(s,str(len(prs.slides)).zfill(2),12,7.16,.6,.22,10,color=teal)
slide('Tema 1 · Arquitectura de ordenadores',['Bits y bytes · Componentes del equipo','Configuración y rendimiento','Dispositivos móviles · Actividades de repaso'])
slide('Objetivos de aprendizaje',bullets('Objetivos de aprendizaje'),True)
slide('El lenguaje binario',['Un bit tiene dos valores posibles: 0 y 1','Ocho bits forman un byte','Ejemplo: 01000001 representa «A» en ASCII'])
slide('La información digital',['Texto: letras codificadas con ASCII o Unicode','Imágenes: píxeles y sus colores','Sonido: muestras digitales','Vídeo: sucesión de imágenes y sonido'])
slide('Hardware y software',['Hardware: componentes físicos del dispositivo','Software: aplicaciones, sistema operativo e instrucciones','Ejemplos de hardware: CPU, RAM, SSD, teclado','Ejemplos de software: navegador, editor de texto'])
slide('Componentes esenciales',['CPU: ejecuta instrucciones','RAM: mantiene datos temporalmente','SSD o HDD: almacenamiento permanente','GPU: procesamiento gráfico','Placa base: conecta componentes','Fuente de alimentación: suministra energía'])
slide('¿Qué sucede al abrir un programa?',['1 · El programa está almacenado en el SSD','2 · Sus instrucciones y datos se cargan en RAM','3 · La CPU ejecuta las instrucciones','4 · La GPU puede ayudar a mostrar el resultado'])
slide('Periféricos',['Entrada: teclado, ratón y micrófono','Salida: monitor, altavoces e impresora','Entrada y salida: pantalla táctil y memoria USB'])
slide('Montaje y seguridad',['Elegir componentes compatibles','Apagar y desconectar el equipo antes de abrirlo','Usar herramientas adecuadas y supervisión','Nunca abrir la fuente de alimentación'])
slide('¿De qué depende el rendimiento?',['CPU: arquitectura, núcleos y carga de trabajo','RAM: capacidad para programas activos','SSD: velocidad de lectura y escritura','GPU: gráficos y ciertos cálculos','Refrigeración: mantener temperaturas adecuadas'])
slide('Ejemplo: HDD frente a SSD',['Cambiar el HDD por SSD puede acelerar el arranque','También reduce tiempos de apertura de aplicaciones','No aumenta la potencia de cálculo de la CPU'])
slide('Móviles: ordenadores de bolsillo',['CPU, RAM, almacenamiento y sistema operativo','SoC: integra varios componentes en un chip','Batería, sensores, cámaras y conexión inalámbrica'])
slide('PC frente a móvil',['PC: generalmente más ampliable','Móvil: portátil, táctil y con batería','Ambos procesan información digital','Existen equipos híbridos y excepciones'])
slide('Actividad práctica',['Identifica CPU, RAM y SSD de un equipo del aula','Compara sus características con las de un móvil','Explica qué mejorarías y por qué'])
slide('Preguntas de repaso',bullets('6. Preguntas de repaso'),True)
slide('Ideas clave',['Los datos se representan mediante bits','CPU, RAM y SSD cumplen funciones distintas','El rendimiento depende de todo el equipo','Un smartphone también es un ordenador'])
out=source.parent/'presentaciones/tema-01-arquitectura-de-ordenadores.pptx'
prs.save(out)
print(out)
