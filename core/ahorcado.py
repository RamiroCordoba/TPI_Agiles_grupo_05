# Bibliotecas
import random
from dotenv import load_dotenv, find_dotenv
import os
# Main
dificultad_baja = [
    [
        "gato",
        "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes.",
    ],
    [
        "sol",
        "Estrella luminosa que está en el centro del sistema solar y da luz y calor a la Tierra.",
    ],
    [
        "luna",
        "Satélite natural de la Tierra que brilla en el cielo nocturno reflejando la luz del sol.",
    ],
    [
        "flor",
        "Parte de una planta que suele ser colorida y de la cual salen los frutos y semillas.",
    ],
    ["dubi", "Arquero de la seleccion Argentina 2024 dicho con dislexia"],
]
dificultad_media = [
    [
        "cirugia",
        "Intervención médica que implica operar el cuerpo para tratar enfermedades o lesiones",
    ],
    ["naufragio", "Hundimiento o destrucción de una embarcación en el mar."],
    [
        "sinfonia",
        "Composición musical para orquesta, generalmente estructurada en varios movimientos y de carácter instrumental.",
    ],
]

dificultad_alta = [
    [
        "otorrinolaringologo",
        "Médico especializado en el diagnóstico y tratamiento de enfermedades relacionadas con el oído, la nariz y la garganta.",
    ],
    ["ornitorrinco", "Mamífero semiacuático agente."],
    [
        "hipopotomonstrosesquipedaliofobia",
        "El temor irracional a las palabras largas o complejas",
    ],
]

def cargar_env():
    load_dotenv(find_dotenv())
    return os.getenv('Entorno')

class Ahorcado:
    def __init__(self):
        self.palabra_vacia = ""
        self.palabra_a_adivinar = ["", ""]
        self.vidas = 5
        self.vidas_restantes = 5
        self.letras_adivinadas = []
        self.letras_arriesgada = []
        self.palabra_a_mostrar = []
        self.partida_concluida = False
        self.dificultad = ""
        self.pista = ""
        self.img = ""
        self.long = 0
        self.pruebaenv = cargar_env()
        print(f"Valor de Entorno en el backend: {self.pruebaenv}")
    

    def rayas_para_palabra(self, la_palabra):
        rayas = len(la_palabra)
        self.palabra_vacia = "_ " * rayas
        return self.palabra_vacia.strip()

    def letra_pertenece_palabra(self, letra):
        if letra in self.palabra_a_adivinar[0]:
            self.letras_adivinadas.append(letra) 
            return True
        else:
            return False

    def adivina_palabra(self, palabra):
        return self.palabra_a_adivinar == palabra

    def intento(self, letra):
        if letra in self.letras_arriesgada:
            return False
        self.letras_arriesgada.append(letra)

        if self.letra_pertenece_palabra(letra):
            self.mostrar_letra_correcta(letra)
            return True
        else:
            self.vidas_restantes -= 1
            self.img=("static\img\ " +  str(self.vidas_restantes) + ".png").replace(" ","")
            self.fin_juego()
            return False

    def mostrar_letra_correcta(self, letra):
        letras_adivinadas = []
        for l in self.palabra_a_adivinar[0]:
            if l == letra or l in self.letras_arriesgada:
                letras_adivinadas.append(l)
            else:
                letras_adivinadas.append("_")
        self.palabra_a_mostrar = letras_adivinadas

    def letras_usadas(self, letra):
        if letra in self.letras_adivinadas:
            return True
        else:
            return False

    def se_termino_el_juego(self): 
        if self.vidas_restantes == 0 or ("".join(self.palabra_a_mostrar) == self.palabra_a_adivinar[0]):
            self.partida_concluida = True
            self.fin_juego()
        return self.partida_concluida

    def iniciar_juego(self, nivel_dificultad=None, palabra=None,pista=None):
        self.vidas = 5
        self.letras_adivinadas = []
        self.partida_concluida = False
        self.letras_arriesgada = []
        self.vidas_restantes = 5
        self.fin_juego()
        if palabra is None:
            self.palabra_a_adivinar = self.generar_palabra(nivel_dificultad)
        else:
            self.palabra_a_adivinar[0] = palabra
        self.long = len(self.palabra_a_adivinar[0])
        self.palabra_a_mostrar = ["_" for _ in self.palabra_a_adivinar[0]]
        if pista:
            self.pista = pista
        else:
            self.pista = self.palabra_a_adivinar[1]
        

    def letras_arriesgadas_en_el_juego(self, letra):
        if letra in self.letras_arriesgada:
            return True
        else:
            return False
        
    def generar_palabra(self, dificultad):
        if dificultad == "facil":
            return random.choice(dificultad_baja)
        elif dificultad == "media":
            return random.choice(dificultad_media)
        else:
            return random.choice(dificultad_alta)


    def dame_una_pista(self):
        return self.pista

    def fin_juego(self):
        if self.partida_concluida:
            if self.vidas_restantes == 0:
                url = 'img/0.png'
                self.img = url.replace(" ","")
            else:
                url = 'img/Winner.jpg'
                self.img = url.replace(" ","")
        else:
            self.img=("img/ " +  str(self.vidas_restantes) + ".png").replace(" ","")

    def intentoP(self, palabraA):
        self.partida_concluida = True
        self.palabra_vacia = str(palabraA)
        if "".join(palabraA) == self.palabra_a_adivinar[0]:
            self.palabra_a_mostrar = list(self.palabra_a_adivinar[0])
        else:
            self.vidas_restantes = 0
            self.palabra_a_mostrar = list(palabraA)
    """        print(self.palabra_a_mostrar)"""

    
    def reiniciar_juego(self):
        self.iniciar_juego() 