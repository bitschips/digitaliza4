#!/usr/bin/env python3
"""Genera PDF imprimible y presentación PPTX desde Temario_Digitalizacion_4ESO.md."""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

ROOT = Path(__file__).resolve().parents[1]
STEM = "Temario_Digitalizacion_4ESO"
md = (ROOT / (STEM + ".md")).read_text(encoding="utf-8")
sections = []
current_topic = None
for line in md.splitlines():
    m = re.match(r"^## Bloque (\d+)\. (.+)$", line)
    if m:
        sections.append([f"BLOQUE {m.group(1)}", m.group(2), []])
        continue
    m = re.match(r"^### Tema (\d+)\. (.+)$", line)
    if m:
        current_topic = [int(m.group(1)), m.group(2), []]
        sections[-1][2].append(current_topic)
        continue
    if line.startswith("- ") and current_topic:
        current_topic[2].append(line[2:])

assert len(sections) == 4 and sum(len(sec[2]) for sec in sections) == 18

# Índice imprimible en A4.
navy = colors.HexColor("#132a45")
blue = colors.HexColor("#1d5c8d")
muted = colors.HexColor("#5a6978")
ink = colors.HexColor("#23334b")
P = ParagraphStyle("P", fontName="Helvetica-Bold", fontSize=18, leading=21, textColor=navy, spaceAfter=5)
SUB = ParagraphStyle("SUB", fontName="Helvetica", fontSize=8.4, leading=11, textColor=muted, spaceAfter=9)
BH = ParagraphStyle("BH", fontName="Helvetica-Bold", fontSize=11, leading=13, textColor=blue, spaceBefore=9, spaceAfter=2, keepWithNext=True)
BT = ParagraphStyle("BT", fontName="Helvetica", fontSize=8.2, leading=10, textColor=muted, spaceAfter=6, keepWithNext=True)
TH = ParagraphStyle("TH", fontName="Helvetica-Bold", fontSize=9.3, leading=11, textColor=navy, spaceBefore=3, spaceAfter=2, keepWithNext=True)
BL = ParagraphStyle("BL", fontName="Helvetica", fontSize=8.35, leading=10.4, textColor=ink, leftIndent=9, firstLineIndent=-6, spaceAfter=1)
NOTE = ParagraphStyle("NOTE", fontName="Helvetica-Oblique", fontSize=7.5, leading=9.5, textColor=muted, spaceBefore=6)

class IndexDoc(BaseDocTemplate):
    def __init__(self, name):
        super().__init__(str(name), pagesize=A4, leftMargin=19*mm, rightMargin=19*mm, topMargin=21*mm, bottomMargin=17*mm)
        width = A4[0]-38*mm
        gap=10*mm
        fr1=Frame(19*mm, 18*mm, (width-gap)/2, A4[1]-40*mm, id="L", leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        fr2=Frame(19*mm+(width-gap)/2+gap, 18*mm, (width-gap)/2, A4[1]-40*mm, id="R", leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
        self.addPageTemplates(PageTemplate(id="index", frames=[fr1,fr2],onPage=self.draw_page))
    def draw_page(self,c,doc):
        c.saveState()
        w,h=A4
        c.setFillColor(navy); c.rect(0,h-9*mm,w,9*mm,stroke=0,fill=1)
        c.setFont("Helvetica-Bold",8); c.setFillColor(colors.white)
        c.drawString(19*mm,h-6.2*mm,"DIGITALIZACIÓN  ·  4.º ESO")
        c.setStrokeColor(colors.HexColor("#dce6ee")); c.line(19*mm,14*mm,w-19*mm,14*mm)
        c.setFont("Helvetica",7.5); c.setFillColor(muted)
        c.drawString(19*mm,10*mm,"Propuesta de índice didáctico · Comunitat Valenciana · 2026-2027")
        c.drawRightString(w-19*mm,10*mm,str(doc.page))
        c.restoreState()

story=[Paragraph("Digitalización — 4.º ESO",P),Paragraph("Comunitat Valenciana · GVA · Curso 2026-2027",SUB)]
for label,desc,topics in sections:
    story.extend([Paragraph(escape(label),BH),Paragraph(escape(desc),BT)])
    for num,name,bullets in topics:
        story.append(Paragraph(f"Tema {num}. {escape(name)}",TH))
        story.extend([Paragraph("•  "+escape(b),BL) for b in bullets])
story.extend([
    Paragraph("Nota: los 18 temas son una propuesta didáctica resumida; no son una numeración oficial de la GVA.",NOTE),
    Paragraph("Referencia: Decreto 107/2022 y modificaciones posteriores. Currículo de Digitalización (GVA).",NOTE)
])
IndexDoc(ROOT/(STEM+".pdf")).build(story)

# PowerPoint 16:9, con siete diapositivas.
prs=Presentation()
prs.slide_width=Inches(13.333); prs.slide_height=Inches(7.5)
NAVY=RGBColor(18,39,61); MID=RGBColor(25,82,119); TEAL=RGBColor(30,132,142)
WHITE=RGBColor(255,255,255); PALE=RGBColor(244,247,250); MUTED=RGBColor(84,104,123)
LINE=RGBColor(221,231,238)

def rect(s,x,y,w,h,fill,rounding=False):
    q=s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rounding else MSO_SHAPE.RECTANGLE,Inches(x),Inches(y),Inches(w),Inches(h))
    q.fill.solid();q.fill.fore_color.rgb=fill;q.line.fill.background()
def txt(s,value,x,y,w,h,size=17,bold=False,color=NAVY):
    q=s.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h))
    tf=q.text_frame; tf.clear(); tf.word_wrap=True
    tf.margin_left=tf.margin_right=0;tf.margin_top=tf.margin_bottom=Inches(0.025)
    p=tf.paragraphs[0];p.text=value;p.font.name="Aptos";p.font.size=Pt(size);p.font.bold=bold;p.font.color.rgb=color
    return q
def slide(label,title,sub,num):
    s=prs.slides.add_slide(prs.slide_layouts[6])
    rect(s,0,0,13.333,7.5,PALE);rect(s,0,0,0.18,7.5,TEAL)
    txt(s,label.upper(),0.65,0.36,11.5,0.28,12,True,TEAL)
    txt(s,title,0.65,0.78,12.1,0.55,29,True)
    txt(s,sub,0.68,1.38,11.7,0.5,14,False,MUTED)
    rect(s,0.67,7.12,12,0.015,LINE)
    txt(s,"DIGITALIZACIÓN · 4.º ESO",0.7,7.18,7,0.2,9,True,MUTED)
    txt(s,f"{num} / 7",12.05,7.17,0.6,0.2,9,True,MUTED)
    return s
def card(s,x,y,w,h,topic):
    n,title,bullets=topic
    rect(s,x,y,w,h,WHITE,True);rect(s,x,y,0.055,h,TEAL)
    txt(s,f"TEMA {n:02d}",x+0.22,y+0.18,w-0.45,0.28,11,True,TEAL)
    txt(s,title,x+0.22,y+0.47,w-0.44,0.44,15,True)
    size=11.5 if len(bullets)>=5 else 11.9
    for i,b in enumerate(bullets):
        txt(s,"• "+b,x+0.26,y+0.98+i*0.29,w-0.55,0.36,size,False,MID)
def note(s,x,y,heading,body):
    rect(s,x,y,5.85,2.33,RGBColor(221,239,242),True)
    txt(s,heading,x+0.31,y+0.36,5.06,0.35,13,True,TEAL)
    txt(s,body,x+0.31,y+0.93,5.06,0.95,19,True)

s=prs.slides.add_slide(prs.slide_layouts[6]);rect(s,0,0,13.333,7.5,NAVY);rect(s,0,0,0.2,7.5,TEAL)
txt(s,"CURSO 2026–2027  ·  COMUNITAT VALENCIANA",0.85,1.05,11.5,0.34,15,True,RGBColor(111,211,212))
txt(s,"DIGITALIZACIÓN",0.85,1.77,11.6,0.9,48,True,WHITE)
txt(s,"4.º de Educación Secundaria Obligatoria",0.9,2.73,11.7,0.72,25,False,WHITE)
rect(s,0.9,4.12,11.5,0.035,RGBColor(62,115,145))
txt(s,"Índice resumido de contenidos",0.9,4.43,11.2,0.55,24,True,WHITE)
txt(s,"4 bloques curriculares   ·   18 temas",0.9,5.18,11.2,0.5,19,False,RGBColor(170,202,218))
txt(s,"Organización didáctica orientativa basada en el currículo GVA",0.9,6.66,11.5,0.28,11,False,RGBColor(180,204,219))

s=slide("Bloque 1","Dispositivos, sistemas y redes","Temas 1–4 · Fundamentos tecnológicos y mantenimiento",2)
for x,y,topic in [(0.67,2.02,sections[0][2][0]),(6.82,2.02,sections[0][2][1]),(0.67,4.49,sections[0][2][2]),(6.82,4.49,sections[0][2][3])]:
    card(s,x,y,5.85,2.34,topic)

s=slide("Bloque 2 · parte 1","Entorno digital de aprendizaje","Temas 5–7 · Información, organización y creación",3)
for x,y,topic in [(0.67,2.0,sections[1][2][0]),(6.82,2.0,sections[1][2][1]),(0.67,4.52,sections[1][2][2])]:
    card(s,x,y,5.85,2.33,topic)
note(s,6.82,4.52,"TRABAJAR CON INFORMACIÓN","Buscar · verificar · organizar · crear")

s=slide("Bloque 2 · parte 2","Creación, programación y colaboración","Temas 8–10 · Aplicaciones, inteligencia artificial y publicación",4)
for x,y,topic in [(0.67,2.0,sections[1][2][3]),(6.82,2.0,sections[1][2][4]),(0.67,4.56,sections[1][2][5])]:
    card(s,x,y,5.85,2.34,topic)
note(s,6.82,4.56,"APRENDER HACIENDO","Buscar · crear · programar · publicar")

s=slide("Bloque 3","Seguridad y bienestar digital","Temas 11–12 · Protección y hábitos saludables",5)
for x,topic in zip([0.67,6.82],sections[2][2]):
    card(s,x,2.15,5.85,3.8,topic)

s=slide("Bloque 4 · parte 1","Ciudadanía digital crítica","Temas 13–15 · Convivencia, información y servicios públicos",6)
for x,y,topic in [(0.67,2.0,sections[3][2][0]),(6.82,2.0,sections[3][2][1]),(0.67,4.52,sections[3][2][2])]:
    card(s,x,y,5.85,2.33,topic)
note(s,6.82,4.52,"CIUDADANÍA RESPONSABLE","Convivir · contrastar · participar")

s=slide("Bloque 4 · parte 2","Economía, ética y participación","Temas 16–18 · Comercio electrónico, IA y sociedad",7)
for x,y,topic in [(0.67,2.0,sections[3][2][3]),(6.82,2.0,sections[3][2][4]),(0.67,4.52,sections[3][2][5])]:
    card(s,x,y,5.85,2.33,topic)
rect(s,6.82,4.52,5.85,2.33,RGBColor(221,239,242),True)
txt(s,"REFERENCIA CURRICULAR",7.13,4.87,5.15,0.35,13,True,TEAL)
txt(s,"Decreto 107/2022 y modificaciones posteriores",7.13,5.32,5.1,0.78,17,True)
txt(s,"Los 18 temas son una propuesta didáctica, no una numeración oficial de la GVA.",7.13,6.13,5.08,0.5,11.5,False,MID)

prs.save(ROOT/(STEM+".pptx"))
print("Archivos generados")
