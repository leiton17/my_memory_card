from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel,
                             QRadioButton, QHBoxLayout, QPushButton,
                             QGroupBox, QButtonGroup, QStackedWidget, QFrame)
from random import shuffle, randint

app = QApplication([])

app.setStyleSheet("""
    QWidget {
        background-color: #1a1a2e;
        color: #e0e0f0;
        font-family: 'Segoe UI', sans-serif;
    }

    /* ── QUIZ ─────────────────────────────── */
    QLabel#pregunta {
        font-size: 14pt;
        font-weight: bold;
        color: #ffffff;
        padding: 14px 16px;
        background-color: #16213e;
        border-left: 5px solid #e94560;
        border-radius: 8px;
    }
    QGroupBox {
        font-size: 10pt;
        font-weight: bold;
        color: #a0a0c0;
        border: 2px solid #2a2a4a;
        border-radius: 10px;
        margin-top: 14px;
        padding: 10px;
        background-color: #16213e;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 14px;
        padding: 0 6px;
        color: #e94560;
    }
    QRadioButton {
        font-size: 12pt;
        color: #c8c8e8;
        padding: 8px 6px;
        spacing: 10px;
    }
    QRadioButton::indicator {
        width: 18px; height: 18px;
        border-radius: 9px;
        border: 2px solid #4a4a7a;
        background-color: #1a1a2e;
    }
    QRadioButton::indicator:checked {
        background-color: #e94560;
        border: 2px solid #e94560;
    }
    QRadioButton:hover { color: #ffffff; }
    QRadioButton:disabled { color: #555577; }

    /* ── BOTONES GENERALES ────────────────── */
    QPushButton {
        font-size: 12pt;
        font-weight: bold;
        color: #ffffff;
        background-color: #e94560;
        border: none;
        border-radius: 10px;
        padding: 10px 18px;
        min-height: 42px;
    }
    QPushButton:hover { background-color: #ff6b81; }
    QPushButton:pressed { background-color: #c73652; }
    QPushButton:disabled { background-color: #444466; color: #888899; }

    QPushButton#btn_verde { background-color: #2ecc71; }
    QPushButton#btn_verde:hover { background-color: #45e082; }
    QPushButton#btn_verde:pressed { background-color: #27ae60; }
    QPushButton#btn_verde:disabled { background-color: #444466; color: #888899; }

    QPushButton#btn_azul { background-color: #3b82f6; }
    QPushButton#btn_azul:hover { background-color: #60a5fa; }
    QPushButton#btn_azul:pressed { background-color: #2563eb; }

    QPushButton#btn_morado { background-color: #8b5cf6; }
    QPushButton#btn_morado:hover { background-color: #a78bfa; }
    QPushButton#btn_morado:pressed { background-color: #7c3aed; }

    QPushButton#btn_amarillo {
        background-color: #f59e0b;
        color: #1a1a2e;
    }
    QPushButton#btn_amarillo:hover { background-color: #fbbf24; }
    QPushButton#btn_amarillo:pressed { background-color: #d97706; }

    QPushButton#btn_gris { background-color: #374151; }
    QPushButton#btn_gris:hover { background-color: #4b5563; }

    /* ── MENÚ PRINCIPAL ───────────────────── */
    QLabel#menu_titulo {
        font-size: 30pt;
        font-weight: bold;
        color: #f5c518;
        qproperty-alignment: AlignCenter;
    }
    QLabel#menu_sub {
        font-size: 12pt;
        color: #a0a0c0;
        qproperty-alignment: AlignCenter;
    }
    QPushButton#btn_jugar {
        font-size: 16pt;
        font-weight: bold;
        background-color: #e94560;
        border-radius: 14px;
        min-height: 56px;
    }
    QPushButton#btn_jugar:hover { background-color: #ff6b81; }
    QPushButton#btn_tienda_menu {
        font-size: 14pt;
        font-weight: bold;
        background-color: #f59e0b;
        color: #1a1a2e;
        border-radius: 14px;
        min-height: 48px;
    }
    QPushButton#btn_tienda_menu:hover { background-color: #fbbf24; }

    /* ── TIENDA ───────────────────────────── */
    QLabel#tienda_titulo {
        font-size: 24pt;
        font-weight: bold;
        color: #f5c518;
        qproperty-alignment: AlignCenter;
    }
    QLabel#tienda_monedas {
        font-size: 14pt;
        font-weight: bold;
        color: #fbbf24;
        qproperty-alignment: AlignCenter;
    }
    QFrame#card {
        background-color: #16213e;
        border: 2px solid #2a2a4a;
        border-radius: 14px;
    }
    QLabel#card_emoji  { font-size: 28pt; qproperty-alignment: AlignCenter; }
    QLabel#card_nombre { font-size: 12pt; font-weight: bold; color: #ffffff; qproperty-alignment: AlignCenter; }
    QLabel#card_desc   { font-size: 9pt;  color: #a0a0c0; qproperty-alignment: AlignCenter; }
    QLabel#card_owned  { font-size: 10pt; color: #2ecc71; font-weight: bold; qproperty-alignment: AlignCenter; }

    /* ── PANTALLAS FINALES ────────────────── */
    QLabel#felicidades_titulo { font-size: 26pt; font-weight: bold; color: #f5c518; qproperty-alignment: AlignCenter; }
    QLabel#felicidades_emoji  { font-size: 52pt; qproperty-alignment: AlignCenter; }
    QLabel#felicidades_sub    { font-size: 13pt; color: #c8c8e8; qproperty-alignment: AlignCenter; }
    QLabel#felicidades_score  { font-size: 15pt; font-weight: bold; color: #2ecc71; qproperty-alignment: AlignCenter; }
    QLabel#master_titulo      { font-size: 24pt; font-weight: bold; color: #a855f7; qproperty-alignment: AlignCenter; }
    QLabel#master_emoji       { font-size: 52pt; qproperty-alignment: AlignCenter; }
    QLabel#master_sub         { font-size: 13pt; color: #c8c8e8; qproperty-alignment: AlignCenter; }
    QLabel#gracias_titulo     { font-size: 26pt; font-weight: bold; color: #e94560; qproperty-alignment: AlignCenter; }
    QLabel#gracias_sub        { font-size: 13pt; color: #c8c8e8; qproperty-alignment: AlignCenter; }
    QLabel#gracias_emoji      { font-size: 52pt; qproperty-alignment: AlignCenter; }
    QLabel#contador           { font-size: 10pt; color: #a0a0c0; }
    QLabel#monedas_hud        { font-size: 11pt; font-weight: bold; color: #fbbf24; }
    QLabel#cronometro_label   { font-size: 18pt; font-weight: bold; color: #e94560; qproperty-alignment: AlignCenter; }
    QLabel#pista_label        { font-size: 11pt; color: #fbbf24; padding: 4px; qproperty-alignment: AlignCenter; }
""")

# ══════════════════════════════════════════════════════════
# ESTADO GLOBAL
# ══════════════════════════════════════════════════════════
estado = {
    "monedas": 20,
    "total_correct": 0,
    "total_questions": 0,
    "ayudas": {
        "saltar":    {"cant": 0, "precio": 8,  "emoji": "⏭️",  "nombre": "Saltar",    "desc": "Salta la pregunta sin perder"},
        "pista":     {"cant": 0, "precio": 10, "emoji": "💡",  "nombre": "Pista",     "desc": "Elimina 2 respuestas incorrectas"},
        "reversa":   {"cant": 0, "precio": 12, "emoji": "🔄",  "nombre": "Reversa",   "desc": "Si fallas, no pierdes la racha"},
        "cronometro":{"cant": 0, "precio": 15, "emoji": "⏱️",  "nombre": "Revivir",   "desc": "5 seg para cambiar tu respuesta"},
    },
    "reversa_activa": False,
    "cronometro_activo": False,
}

preguntas_respondidas = set()

TOTAL_PREGUNTAS = 65

# ══════════════════════════════════════════════════════════
# PREGUNTAS
# ══════════════════════════════════════════════════════════
class Question():
    def __init__(self, question, right_answer, w1, w2, w3):
        self.question = question
        self.right_answer = right_answer
        self.wrong_answer1 = w1
        self.wrong_answer2 = w2
        self.wrong_answer3 = w3

Lista_preguntas = []
# Historia
Lista_preguntas.append(Question("¿En que año empezo la primera Guerra Mundial?","1914","1918","1939","1945"))
Lista_preguntas.append(Question("¿En que año termino la primera Guerra Mundial?","1918","1914","1920","1922"))
Lista_preguntas.append(Question("¿En que año empezo la segunda Guerra Mundial?","1939","1935","1941","1943"))
Lista_preguntas.append(Question("¿En que año termino la segunda Guerra Mundial?","1945","1943","1947","1950"))
Lista_preguntas.append(Question("¿En que año se descubrio America?","1492","1490","1495","1500"))
Lista_preguntas.append(Question("¿En que año se hundio el Titanic?","1912","2001","1918","1920"))
Lista_preguntas.append(Question("¿En que año cayo el Muro de Berlin?","1989","1985","1991","1993"))
Lista_preguntas.append(Question("¿En que año ocurrio la Revolucion Francesa?","1789","1776","1800","1812"))
Lista_preguntas.append(Question("¿En que año llego el hombre a la luna?","1969","1959","1979","1989"))
Lista_preguntas.append(Question("¿Quien fue el primer presidente de los Estados Unidos?","George Washington","Abraham Lincoln","Thomas Jefferson","Benjamin Franklin"))
Lista_preguntas.append(Question("¿En que año se firmo la Declaracion de Independencia de EE.UU?","1776","1783","1770","1800"))
Lista_preguntas.append(Question("¿Quien fue Napoleon Bonaparte?","Emperador de Francia","Rey de España","Zar de Rusia","Papa de Roma"))
Lista_preguntas.append(Question("¿En que continente se origino el Imperio Romano?","Europa","Asia","Africa","America"))
Lista_preguntas.append(Question("¿Cual fue la primera civilizacion de la historia?","Sumeria","Egipto","Grecia","China"))
Lista_preguntas.append(Question("¿Donde se construyeron las piramides mas famosas?","Egipto","Mexico","Peru","China"))
# Ciencia
Lista_preguntas.append(Question("¿Quien creo la primera computadora moderna?","Konrad Zuse","Arquímedes","Alfred Nobel","Isaac Newton"))
Lista_preguntas.append(Question("¿En que año se creo el primer iPhone?","2007","2004","2008","2006"))
Lista_preguntas.append(Question("¿En que año se creo Minecraft?","2009","2010","2011","2012"))
Lista_preguntas.append(Question("¿Cuantos elementos hay en la tabla periodica?","118","100","150","200"))
Lista_preguntas.append(Question("¿Cual es el planeta mas grande del sistema solar?","Jupiter","Saturno","Urano","Neptuno"))
Lista_preguntas.append(Question("¿Cual es el planeta mas cercano al Sol?","Mercurio","Venus","Tierra","Marte"))
Lista_preguntas.append(Question("¿Cuantos planetas tiene el sistema solar?","8","9","7","10"))
Lista_preguntas.append(Question("¿Quien formulo la teoria de la relatividad?","Albert Einstein","Isaac Newton","Nikola Tesla","Stephen Hawking"))
Lista_preguntas.append(Question("¿Quien invento el telefono?","Alexander Graham Bell","Thomas Edison","Nikola Tesla","Benjamin Franklin"))
Lista_preguntas.append(Question("¿Quien invento la bombilla electrica?","Thomas Edison","Nikola Tesla","Benjamin Franklin","James Watt"))
Lista_preguntas.append(Question("¿Cual es el hueso mas largo del cuerpo humano?","Femur","Tibia","Humero","Radio"))
Lista_preguntas.append(Question("¿Cuantos huesos tiene el cuerpo humano adulto?","206","208","200","212"))
Lista_preguntas.append(Question("¿Cual es el organo mas grande del cuerpo humano?","La piel","El higado","El cerebro","El corazon"))
Lista_preguntas.append(Question("¿A que velocidad viaja la luz?","300,000 km/s","150,000 km/s","500,000 km/s","1,000,000 km/s"))
Lista_preguntas.append(Question("¿Cual es el gas mas abundante en la atmosfera?","Nitrogeno","Oxigeno","Dioxido de carbono","Argon"))
Lista_preguntas.append(Question("¿Que planeta es conocido como el planeta rojo?","Marte","Jupiter","Saturno","Venus"))
Lista_preguntas.append(Question("¿Quien fue el primer humano en el espacio?","Yuri Gagarin","Neil Armstrong","Buzz Aldrin","Alan Shepard"))
Lista_preguntas.append(Question("¿En que año se lanzo el primer satelite artificial?","1957","1961","1969","1950"))
Lista_preguntas.append(Question("¿Cual es la formula quimica del agua?","H2O","CO2","O2","H2SO4"))
Lista_preguntas.append(Question("¿Cuantos cromosomas tiene una celula humana normal?","46","23","48","44"))
# Geografia
Lista_preguntas.append(Question("¿Cual es el pais mas grande del mundo?","Rusia","Canada","China","Estados Unidos"))
Lista_preguntas.append(Question("¿Cual es el rio mas largo del mundo?","Nilo","Amazonas","Yangtze","Misisipi"))
Lista_preguntas.append(Question("¿Cual es el oceano mas grande del mundo?","Pacifico","Atlantico","Indico","Artico"))
Lista_preguntas.append(Question("¿Cual es la montaña mas alta del mundo?","Everest","K2","Kangchenjunga","Aconcagua"))
Lista_preguntas.append(Question("¿Cual es el desierto mas grande del mundo?","Antartico","Sahara","Gobi","Atacama"))
Lista_preguntas.append(Question("¿Cuantos continentes hay en el mundo?","7","5","6","8"))
Lista_preguntas.append(Question("¿Cual es la capital de Francia?","Paris","Lyon","Marsella","Burdeos"))
Lista_preguntas.append(Question("¿Cual es la capital de Japon?","Tokio","Osaka","Kioto","Hiroshima"))
Lista_preguntas.append(Question("¿Cual es el pais mas pequeño del mundo?","Vaticano","Monaco","San Marino","Liechtenstein"))
Lista_preguntas.append(Question("¿En que pais se encuentra la Torre Eiffel?","Francia","Italia","España","Belgica"))
Lista_preguntas.append(Question("¿Cual es el lago mas profundo del mundo?","Baikal","Titicaca","Victoria","Superior"))
Lista_preguntas.append(Question("¿En que continente esta Brasil?","America del Sur","America del Norte","Africa","Europa"))
# Cultura
Lista_preguntas.append(Question("¿En que año murio Albert Einstein?","1955","1945","1965","1975"))
Lista_preguntas.append(Question("¿En que año murio Pablo Escobar?","1993","1989","1995","2000"))
Lista_preguntas.append(Question("¿En que año murio Michael Jackson?","2009","2005","2010","2012"))
Lista_preguntas.append(Question("¿Quien escribio Don Quijote de la Mancha?","Miguel de Cervantes","Federico Garcia Lorca","Pablo Neruda","Gabriel Garcia Marquez"))
Lista_preguntas.append(Question("¿Quien pinto la Mona Lisa?","Leonardo da Vinci","Miguel Angel","Rafael","Picasso"))
Lista_preguntas.append(Question("¿Quien compuso la Quinta Sinfonia?","Beethoven","Mozart","Bach","Chopin"))
Lista_preguntas.append(Question("¿En que año se estreno la primera pelicula de Star Wars?","1977","1975","1980","1983"))
Lista_preguntas.append(Question("¿Cuantos jugadores hay en un equipo de futbol?","11","9","10","12"))
Lista_preguntas.append(Question("¿Cada cuantos años se celebra el Mundial de Futbol?","4","2","3","5"))
Lista_preguntas.append(Question("¿Quien escribio Harry Potter?","J.K. Rowling","J.R.R. Tolkien","C.S. Lewis","Roald Dahl"))
Lista_preguntas.append(Question("¿De que material esta hecha la Estatua de la Libertad?","Cobre","Oro","Hierro","Bronce"))
Lista_preguntas.append(Question("¿En que ciudad esta la Sagrada Familia?","Barcelona","Madrid","Valencia","Sevilla"))
Lista_preguntas.append(Question("¿Cuantos colores tiene el arcoiris?","7","5","6","8"))
Lista_preguntas.append(Question("¿Cual es el animal terrestre mas rapido?","Guepardo","Leon","Caballo","Antilope"))
Lista_preguntas.append(Question("¿Cual es el animal mas grande del mundo?","Ballena azul","Elefante africano","Tiburon ballena","Jirafa"))

# ══════════════════════════════════════════════════════════
# VENTANA PRINCIPAL
# ══════════════════════════════════════════════════════════
my_window = QWidget()
my_window.setWindowTitle("🧠 Tarjeta de Memoria")
my_window.resize(680, 640)

stack = QStackedWidget()

# ══════════════════════════════════════════════════════════
# PÁGINA 0 — MENÚ PRINCIPAL
# ══════════════════════════════════════════════════════════
pagina_menu = QWidget()

lbl_emoji_menu = QLabel("🧠")
lbl_emoji_menu.setAlignment(Qt.AlignCenter)
lbl_emoji_menu.setStyleSheet("font-size: 56pt;")

lbl_titulo_menu = QLabel("Tarjeta de Memoria")
lbl_titulo_menu.setObjectName("menu_titulo")

lbl_sub_menu = QLabel("Pon a prueba tus conocimientos")
lbl_sub_menu.setObjectName("menu_sub")

monedas_menu_label = QLabel("🪙 20 monedas")
monedas_menu_label.setObjectName("tienda_monedas")

btn_jugar = QPushButton("▶  Jugar")
btn_jugar.setObjectName("btn_jugar")

btn_tienda_menu = QPushButton("🛒  Tienda de Ayudas")
btn_tienda_menu.setObjectName("btn_tienda_menu")

sep = QFrame()
sep.setFrameShape(QFrame.HLine)
sep.setStyleSheet("color: #2a2a4a;")

layout_menu = QVBoxLayout()
layout_menu.setContentsMargins(60, 40, 60, 40)
layout_menu.setSpacing(16)
layout_menu.addStretch()
layout_menu.addWidget(lbl_emoji_menu)
layout_menu.addWidget(lbl_titulo_menu)
layout_menu.addWidget(lbl_sub_menu)
layout_menu.addWidget(monedas_menu_label)
layout_menu.addSpacing(10)
layout_menu.addWidget(sep)
layout_menu.addSpacing(10)
layout_menu.addWidget(btn_jugar)
layout_menu.addWidget(btn_tienda_menu)
layout_menu.addStretch()
pagina_menu.setLayout(layout_menu)

# ══════════════════════════════════════════════════════════
# PÁGINA 1 — QUIZ
# ══════════════════════════════════════════════════════════
pagina_quiz = QWidget()

# HUD superior
hud = QHBoxLayout()
contador_label = QLabel("✅ 0 correctas")
contador_label.setObjectName("contador")
monedas_hud = QLabel("🪙 20")
monedas_hud.setObjectName("monedas_hud")
hud.addWidget(contador_label)
hud.addStretch()
hud.addWidget(monedas_hud)

# Cronómetro
cronometro_label = QLabel("")
cronometro_label.setObjectName("cronometro_label")
cronometro_label.hide()

# Pista
pista_label = QLabel("")
pista_label.setObjectName("pista_label")
pista_label.hide()

pregunta = QLabel("Aqui va la pregunta")
pregunta.setObjectName("pregunta")
pregunta.setWordWrap(True)

grupo_preguntas = QGroupBox("Opciones de respuesta")
QRB1 = QRadioButton("R1"); QRB2 = QRadioButton("R2")
QRB3 = QRadioButton("R3"); QRB4 = QRadioButton("R4")
radioGroup = QButtonGroup()
for rb in [QRB1, QRB2, QRB3, QRB4]:
    radioGroup.addButton(rb)

lg1 = QHBoxLayout(); lg2 = QVBoxLayout(); lg3 = QVBoxLayout()
lg2.setSpacing(6); lg3.setSpacing(6)
lg2.addWidget(QRB1); lg2.addWidget(QRB2)
lg3.addWidget(QRB3); lg3.addWidget(QRB4)
lg1.addLayout(lg2); lg1.addLayout(lg3)
grupo_preguntas.setLayout(lg1)

# Botones de ayuda en quiz
ayudas_layout = QHBoxLayout()
ayudas_layout.setSpacing(8)

btn_usar_saltar    = QPushButton("⏭️ Saltar")
btn_usar_pista     = QPushButton("💡 Pista")
btn_usar_reversa   = QPushButton("🔄 Reversa")
btn_usar_crono     = QPushButton("⏱️ Revivir")
btn_tienda_quiz    = QPushButton("🛒")

for b in [btn_usar_saltar, btn_usar_pista, btn_usar_reversa, btn_usar_crono]:
    b.setStyleSheet("font-size: 9pt; min-height: 32px; padding: 4px 8px; border-radius: 8px; background-color: #2a2a4a; color: #c8c8e8;")
btn_tienda_quiz.setStyleSheet("font-size: 10pt; min-height: 32px; padding: 4px 10px; border-radius: 8px; background-color: #f59e0b; color: #1a1a2e; font-weight: bold;")

ayudas_layout.addWidget(btn_usar_saltar)
ayudas_layout.addWidget(btn_usar_pista)
ayudas_layout.addWidget(btn_usar_reversa)
ayudas_layout.addWidget(btn_usar_crono)
ayudas_layout.addStretch()
ayudas_layout.addWidget(btn_tienda_quiz)

boton_respuesta = QPushButton("Responder")

grupo_respuestas = QGroupBox("Resultado")
respuesta_correcta_lbl = QLabel("—")
respuesta_correcta_lbl.setObjectName("respuesta_correcta")
respuesta_correcta_lbl.setAlignment(Qt.AlignCenter)
al = QVBoxLayout(); al.addWidget(respuesta_correcta_lbl)
grupo_respuestas.setLayout(al)

layout_quiz = QVBoxLayout()
layout_quiz.setContentsMargins(18, 16, 18, 16)
layout_quiz.setSpacing(10)
layout_quiz.addLayout(hud)
layout_quiz.addWidget(cronometro_label)
layout_quiz.addWidget(pista_label)
layout_quiz.addWidget(pregunta)
layout_quiz.addWidget(grupo_preguntas)
layout_quiz.addWidget(grupo_respuestas)
grupo_respuestas.hide()
layout_quiz.addLayout(ayudas_layout)
layout_quiz.addWidget(boton_respuesta)
pagina_quiz.setLayout(layout_quiz)

# ══════════════════════════════════════════════════════════
# PÁGINA 2 — TIENDA
# ══════════════════════════════════════════════════════════
pagina_tienda = QWidget()

lbl_tienda_titulo = QLabel("🛒  Tienda de Ayudas")
lbl_tienda_titulo.setObjectName("tienda_titulo")

tienda_monedas_label = QLabel("🪙 20 monedas disponibles")
tienda_monedas_label.setObjectName("tienda_monedas")

# Cards de ayudas
def make_card(key, info):
    frame = QFrame()
    frame.setObjectName("card")
    v = QVBoxLayout()
    v.setSpacing(4)
    v.setContentsMargins(12, 12, 12, 12)

    em = QLabel(info["emoji"]); em.setObjectName("card_emoji")
    nm = QLabel(info["nombre"]); nm.setObjectName("card_nombre")
    dc = QLabel(info["desc"]); dc.setObjectName("card_desc"); dc.setWordWrap(True)
    pr = QLabel(f"💰 {info['precio']} monedas")
    pr.setStyleSheet("font-size: 10pt; color: #fbbf24; font-weight: bold; qproperty-alignment: AlignCenter;")
    ow = QLabel(f"Tienes: {info['cant']}")
    ow.setObjectName("card_owned")

    btn = QPushButton(f"Comprar  ({info['precio']} 🪙)")
    btn.setObjectName("btn_amarillo")

    v.addWidget(em); v.addWidget(nm); v.addWidget(dc)
    v.addWidget(pr); v.addWidget(ow); v.addWidget(btn)
    frame.setLayout(v)
    return frame, ow, btn

cards_widgets = {}  # key -> (frame, owned_label, buy_btn)

cards_row1 = QHBoxLayout(); cards_row1.setSpacing(12)
cards_row2 = QHBoxLayout(); cards_row2.setSpacing(12)

keys = list(estado["ayudas"].keys())
for i, key in enumerate(keys):
    frame, ow, btn = make_card(key, estado["ayudas"][key])
    cards_widgets[key] = (frame, ow, btn)
    if i < 2:
        cards_row1.addWidget(frame)
    else:
        cards_row2.addWidget(frame)

btn_volver_tienda = QPushButton("← Volver")
btn_volver_tienda.setObjectName("btn_gris")

layout_tienda = QVBoxLayout()
layout_tienda.setContentsMargins(20, 20, 20, 20)
layout_tienda.setSpacing(14)
layout_tienda.addWidget(lbl_tienda_titulo)
layout_tienda.addWidget(tienda_monedas_label)
layout_tienda.addLayout(cards_row1)
layout_tienda.addLayout(cards_row2)
layout_tienda.addStretch()
layout_tienda.addWidget(btn_volver_tienda)
pagina_tienda.setLayout(layout_tienda)

# ══════════════════════════════════════════════════════════
# PÁGINAS FINALES
# ══════════════════════════════════════════════════════════
def make_final_page(emoji_txt, titulo_txt, titulo_obj, sub_txt, sub_obj, score_obj=None, btns=[]):
    page = QWidget()
    em = QLabel(emoji_txt); em.setObjectName("felicidades_emoji" if "Felicidades" in titulo_txt or "pasado" in titulo_txt else "gracias_emoji"); em.setAlignment(Qt.AlignCenter)
    ti = QLabel(titulo_txt); ti.setObjectName(titulo_obj); ti.setAlignment(Qt.AlignCenter)
    su = QLabel(sub_txt); su.setObjectName(sub_obj); su.setAlignment(Qt.AlignCenter); su.setWordWrap(True)
    lv = QVBoxLayout(); lv.setContentsMargins(40,40,40,40); lv.setSpacing(14)
    lv.addStretch(); lv.addWidget(em); lv.addWidget(ti); lv.addWidget(su)
    sc = None
    if score_obj:
        sc = QLabel(""); sc.setObjectName(score_obj); sc.setAlignment(Qt.AlignCenter)
        lv.addWidget(sc)
    bh = QHBoxLayout(); bh.setSpacing(12)
    for b in btns: bh.addWidget(b)
    lv.addSpacing(8); lv.addLayout(bh); lv.addStretch()
    page.setLayout(lv)
    return page, sc

# Página 3 — Felicidades (cada 10)
btn_si  = QPushButton("✅  Sí, continuar"); btn_si.setObjectName("btn_verde")
btn_no  = QPushButton("❌  No, salir")
pag_fel, score_label = make_final_page("🏆","¡Felicidades!","felicidades_titulo",
    "¡Lograste 10 respuestas correctas!\n¿Deseas continuar jugando?",
    "felicidades_sub","felicidades_score",[btn_si,btn_no])

# Página 4 — Gracias
pag_grac, _ = make_final_page("👋","¡Gracias por jugar!","gracias_titulo",
    "Esperamos verte de nuevo pronto. 😊","gracias_sub",btns=[])

# Página 5 — Master
btn_reiniciar = QPushButton("🔄  Jugar de nuevo"); btn_reiniciar.setObjectName("btn_verde")
pag_master, _ = make_final_page("😱","¡LO HAS LOGRADO!","master_titulo",
    f"¡Te has pasado el juego!\nRespondiste bien las {TOTAL_PREGUNTAS} preguntas.\n¡Eres un genio! 🧠",
    "master_sub", btns=[btn_reiniciar])

# Armar stack
# 0=menu 1=quiz 2=tienda 3=felicidades 4=gracias 5=master
for p in [pagina_menu, pagina_quiz, pagina_tienda, pag_fel, pag_grac, pag_master]:
    stack.addWidget(p)

layout_main = QVBoxLayout()
layout_main.setContentsMargins(0,0,0,0)
layout_main.addWidget(stack)
my_window.setLayout(layout_main)

# ══════════════════════════════════════════════════════════
# LÓGICA
# ══════════════════════════════════════════════════════════
answers      = [QRB1, QRB2, QRB3, QRB4]
current_idx  = [0]
crono_timer  = QTimer()
crono_secs   = [0]
origen_tienda = [0]   # desde qué página se abrió la tienda

def actualizar_hud():
    m = estado["monedas"]
    c = estado["total_correct"]
    q = estado["total_questions"]
    monedas_hud.setText(f"🪙 {m}")
    contador_label.setText(f"✅ {c} correctas  |  ❓ {q} respondidas")
    monedas_menu_label.setText(f"🪙 {m} monedas")
    tienda_monedas_label.setText(f"🪙 {m} monedas disponibles")
    # Actualizar owned labels en tienda
    for key, (frame, ow, btn) in cards_widgets.items():
        ow.setText(f"Tienes: {estado['ayudas'][key]['cant']}")
        btn.setEnabled(estado["monedas"] >= estado["ayudas"][key]["precio"])
    # Actualizar botones de ayuda en quiz
    btn_usar_saltar.setText(f"⏭️ Saltar ({estado['ayudas']['saltar']['cant']})")
    btn_usar_pista.setText(f"💡 Pista ({estado['ayudas']['pista']['cant']})")
    btn_usar_reversa.setText(f"🔄 Reversa ({estado['ayudas']['reversa']['cant']})")
    btn_usar_crono.setText(f"⏱️ Revivir ({estado['ayudas']['cronometro']['cant']})")
    btn_usar_saltar.setEnabled(estado["ayudas"]["saltar"]["cant"] > 0)
    btn_usar_pista.setEnabled(estado["ayudas"]["pista"]["cant"] > 0)
    btn_usar_reversa.setEnabled(estado["ayudas"]["reversa"]["cant"] > 0)
    btn_usar_crono.setEnabled(False)  # solo se activa tras fallar

def mostrar_respuesta_panel():
    grupo_preguntas.hide()
    grupo_respuestas.show()
    boton_respuesta.setText("Siguiente Pregunta")

def mostrar_pregunta_panel():
    grupo_preguntas.show()
    grupo_respuestas.hide()
    pista_label.hide()
    cronometro_label.hide()
    boton_respuesta.setText("Responder")
    estado["reversa_activa"] = False
    estado["cronometro_activo"] = False
    btn_usar_crono.setEnabled(False)
    radioGroup.setExclusive(False)
    for b in radioGroup.buttons(): b.setChecked(False)
    radioGroup.setExclusive(True)
    for b in radioGroup.buttons(): b.setEnabled(True)

def ask(idx):
    current_idx[0] = idx
    q = Lista_preguntas[idx]
    estado["total_questions"] += 1
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_answer1)
    answers[2].setText(q.wrong_answer2)
    answers[3].setText(q.wrong_answer3)
    pregunta.setText(q.question)
    respuesta_correcta_lbl.setText(q.right_answer)
    mostrar_pregunta_panel()
    actualizar_hud()

def next_question():
    grupo_respuestas.setStyleSheet("")
    ask(randint(0, TOTAL_PREGUNTAS - 1))

def marcar_resultado(es_correcto):
    if es_correcto:
        grupo_respuestas.setTitle("✅  ¡Correcto!")
        grupo_respuestas.setStyleSheet("QGroupBox{border:2px solid #2ecc71;} QGroupBox::title{color:#2ecc71;}")
    else:
        grupo_respuestas.setTitle("❌  Incorrecto")
        grupo_respuestas.setStyleSheet("QGroupBox{border:2px solid #e94560;} QGroupBox::title{color:#e94560;}")

def check_answer():
    es_correcto = answers[0].isChecked()

    if not es_correcto and estado["reversa_activa"]:
        # Reversa: absorbe el fallo
        estado["reversa_activa"] = False
        grupo_respuestas.setTitle("🔄  ¡Reversa activada! Fallo absorbido")
        grupo_respuestas.setStyleSheet("QGroupBox{border:2px solid #8b5cf6;} QGroupBox::title{color:#8b5cf6;}")
        respuesta_correcta_lbl.setText(f"Respuesta correcta: {Lista_preguntas[current_idx[0]].right_answer}")
        mostrar_respuesta_panel()
        return

    if not es_correcto and estado["ayudas"]["cronometro"]["cant"] > 0 and not estado["cronometro_activo"]:
        # Ofrecer cronómetro de revivir
        btn_usar_crono.setEnabled(True)

    if es_correcto:
        estado["total_correct"] += 1
        estado["monedas"] += 3   # +3 monedas por correcta
        preguntas_respondidas.add(current_idx[0])
        marcar_resultado(True)
    else:
        marcar_resultado(False)

    mostrar_respuesta_panel()
    actualizar_hud()

    if len(preguntas_respondidas) == TOTAL_PREGUNTAS:
        boton_respuesta.setText("¡Ver resultado final!")
    elif estado["total_correct"] > 0 and estado["total_correct"] % 10 == 0:
        boton_respuesta.setText("Ver resultado")

def click_OK():
    txt = boton_respuesta.text()
    if txt == "Responder":
        check_answer()
    elif txt == "¡Ver resultado final!":
        stack.setCurrentIndex(5)
    elif txt == "Ver resultado":
        if score_label:
            score_label.setText(f"🎯 {estado['total_correct']} correctas de {estado['total_questions']} intentos  |  🪙 {estado['monedas']} monedas")
        stack.setCurrentIndex(3)
    else:
        next_question()

# ── Ayudas ────────────────────────────────────────────────
def usar_saltar():
    if estado["ayudas"]["saltar"]["cant"] > 0 and boton_respuesta.text() == "Responder":
        estado["ayudas"]["saltar"]["cant"] -= 1
        estado["total_questions"] -= 1   # no cuenta como respondida
        next_question()

def usar_pista():
    if estado["ayudas"]["pista"]["cant"] > 0 and boton_respuesta.text() == "Responder":
        estado["ayudas"]["pista"]["cant"] -= 1
        # Deshabilitar 2 respuestas incorrectas (índices 1 y 2 son incorrectas)
        disabled = 0
        for b in answers[1:]:
            if disabled < 2:
                b.setEnabled(False)
                disabled += 1
        pista_label.setText("💡 Pista: se eliminaron 2 opciones incorrectas")
        pista_label.show()
        actualizar_hud()

def usar_reversa():
    if estado["ayudas"]["reversa"]["cant"] > 0 and boton_respuesta.text() == "Responder":
        estado["ayudas"]["reversa"]["cant"] -= 1
        estado["reversa_activa"] = True
        pista_label.setText("🔄 Reversa activa: tu próximo fallo será absorbido")
        pista_label.show()
        actualizar_hud()

def usar_cronometro():
    if estado["ayudas"]["cronometro"]["cant"] > 0 and not estado["cronometro_activo"]:
        estado["ayudas"]["cronometro"]["cant"] -= 1
        estado["cronometro_activo"] = True
        crono_secs[0] = 5
        cronometro_label.setText(f"⏱️ Tienes {crono_secs[0]} segundos para cambiar tu respuesta...")
        cronometro_label.show()
        # Rehabilitar botones para que pueda cambiar respuesta
        for b in radioGroup.buttons(): b.setEnabled(True)
        grupo_respuestas.hide()
        grupo_preguntas.show()
        boton_respuesta.setText("Confirmar respuesta")
        crono_timer.start(1000)
        actualizar_hud()

def tick_cronometro():
    crono_secs[0] -= 1
    if crono_secs[0] <= 0:
        crono_timer.stop()
        cronometro_label.hide()
        estado["cronometro_activo"] = False
        boton_respuesta.setText("Responder")
        check_answer()
    else:
        cronometro_label.setText(f"⏱️ Tienes {crono_secs[0]} segundos para cambiar tu respuesta...")

crono_timer.timeout.connect(tick_cronometro)

# ── Tienda: comprar ───────────────────────────────────────
def comprar(key):
    precio = estado["ayudas"][key]["precio"]
    if estado["monedas"] >= precio:
        estado["monedas"] -= precio
        estado["ayudas"][key]["cant"] += 1
        actualizar_hud()

for key, (frame, ow, btn) in cards_widgets.items():
    btn.clicked.connect(lambda checked, k=key: comprar(k))

# ── Navegación ────────────────────────────────────────────
def ir_tienda(desde):
    origen_tienda[0] = desde
    actualizar_hud()
    stack.setCurrentIndex(2)

def volver_desde_tienda():
    stack.setCurrentIndex(origen_tienda[0])
    actualizar_hud()

def click_si():
    stack.setCurrentIndex(1)
    next_question()

def click_no():
    stack.setCurrentIndex(4)

def click_reiniciar():
    estado["total_correct"] = 0
    estado["total_questions"] = 0
    preguntas_respondidas.clear()
    actualizar_hud()
    stack.setCurrentIndex(0)

btn_jugar.clicked.connect(lambda: (stack.setCurrentIndex(1), next_question() if estado["total_questions"] == 0 else None))
btn_tienda_menu.clicked.connect(lambda: ir_tienda(0))
btn_tienda_quiz.clicked.connect(lambda: ir_tienda(1))
btn_volver_tienda.clicked.connect(volver_desde_tienda)
boton_respuesta.clicked.connect(click_OK)
btn_usar_saltar.clicked.connect(usar_saltar)
btn_usar_pista.clicked.connect(usar_pista)
btn_usar_reversa.clicked.connect(usar_reversa)
btn_usar_crono.clicked.connect(usar_cronometro)
btn_si.clicked.connect(click_si)
btn_no.clicked.connect(click_no)
btn_reiniciar.clicked.connect(click_reiniciar)

actualizar_hud()
stack.setCurrentIndex(0)
my_window.show()
app.exec_()