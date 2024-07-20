# Bibliotecas
import random

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
]
dificultad_media = {
    "cirugia": "Intervención médica que implica operar el cuerpo para tratar enfermedades o lesione",
    "naufragio": "Hundimiento o destrucción de una embarcación en el mar.",
    "sinfonia": "Composición musical para orquesta, generalmente estructurada en varios movimientos y de carácter instrumental.",
}
dificultad_alta = {
    "otorrinolaringologo": "Médico especializado en el diagnóstico y tratamiento de enfermedades relacionadas con el oído, la nariz y la garganta.",
    "ornitorrinco": "Mamífero semiacuático agente.",
    "hipopotomonstrosesquipedaliofobia": "El temor irracional a las palabras largas o complejas",
}

abecedario = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


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

    def rayas_para_palabra(self, la_palabra):
        rayas = len(la_palabra)
        self.palabra_vacia = "_ " * rayas
        return self.palabra_vacia.strip()

    def letra_pertenece_palabra(self, letra):
        if letra in self.palabra_a_adivinar:
            self.letras_adivinadas += letra
            return True
        else:
            return False

    def adivina_palabra(self, palabra):
        return self.palabra_a_adivinar == palabra

    def intento(self, letra):
        self.letras_arriesgada.append(letra)
        print(letra)
        if self.letra_pertenece_palabra(letra):
            self.mostrar_letra_correcta(letra)
            return True
        else:
            self.vidas_restantes -= 1
            return False

    def mostrar_letra_correcta(self, letra):
        letras_adivinadas = ""
        for l in self.palabra_a_adivinar:
            if l == letra or l in self.letras_arriesgada:
                letras_adivinadas += l
            else:
                letras_adivinadas += "_"
        self.palabra_a_mostrar = letras_adivinadas

    def letras_usadas(self, letra):
        if letra in self.letras_adivinadas:
            return True
        else:
            return False

    def se_termino_el_juego(self):
        if self.vidas_restantes == 0 or (
            "".join(self.palabra_a_mostrar) == self.palabra_a_adivinar
        ):
            self.partida_concluida = True
        return self.partida_concluida

    def iniciar_juego(self, nivel_dificultad=None, palabra=None):
        self.vidas = 5
        self.letras_adivinadas = []
        self.se_termino_el_juego = False
        self.letras_arriesgada = []
        if palabra is None:
            self.palabra_a_adivinar = self.generar_palabra(nivel_dificultad)
        else:
            self.palabra_a_adivinar[0] = palabra
            self.palabra_a_mostrar = ["_" for _ in self.palabra_a_adivinar[0]]
        self.pista = self.palabra_a_adivinar[1]
        self.dificultad = nivel_dificultad
        self.vidas_restantes = 5

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
