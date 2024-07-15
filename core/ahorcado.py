# Bibliotecas
import random

# Main
dificultad_baja = [
    [
        "Gato",
        "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes.",
    ],
    [
        "Sol",
        "Estrella luminosa que está en el centro del sistema solar y da luz y calor a la Tierra.",
    ],
    [
        "Luna",
        "Satélite natural de la Tierra que brilla en el cielo nocturno reflejando la luz del sol.",
    ],
    [
        "Flor",
        "Parte de una planta que suele ser colorida y de la cual salen los frutos y semillas.",
    ],
]
dificultad_media = {
    "Cirugía": "Intervención médica que implica operar el cuerpo para tratar enfermedades o lesione",
    "Naufragio": "Hundimiento o destrucción de una embarcación en el mar.",
    "Sinfonía": "Composición musical para orquesta, generalmente estructurada en varios movimientos y de carácter instrumental.",
}
dificultad_alta = {
    "Otorrinolaringólogo": "Médico especializado en el diagnóstico y tratamiento de enfermedades relacionadas con el oído, la nariz y la garganta.",
    "Ornitorrinco": "Mamífero semiacuático agente.",
    "hipopotomonstrosesquipedaliofobia": "El temor irracional a las palabras largas o complejas",
}

abecedario = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
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
            self.palabra_a_mostrar = self.rayas_para_palabra(self.palabra_a_adivinar[0])
        else:
            self.palabra_a_adivinar[0] = palabra
            self.palabra_a_mostrar = self.rayas_para_palabra(palabra)
        self.pista = ""
        self.dificultad = nivel_dificultad
        self.vidas_restantes = 5
