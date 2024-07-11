class Ahorcado:
    def __init__(self):
        self.palabra_vacia = ""
        self.palabra_a_adivinar = ""
        self.vidas = 5
        self.vidas_restantes = 5
        self.letras_adivinadas = []

    def rayas_para_palabra(self, la_palabra):
        rayas = len(la_palabra)
        self.palabra_vacia = "_ " * rayas
        return self.palabra_vacia.strip()

    def letra_pertenece_palabra(self, letra):
        if letra in self.palabra_a_adivinar:
            self.letras_adivinadas += letra
            return True
        else:
            self.vidas_restantes -= 1
            return False

    def adivina_palabra(self, palabra):
        return self.palabra_a_adivinar == palabra

    def intento(self, letra):
        print(letra)
        if self.letra_pertenece_palabra(letra):
            return True
        else:
            return False
