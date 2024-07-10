class Ahorcado:
    def __init__(self):
        self.palabra_vacia = ""

    def rayas_para_palabra(self, la_palabra):
        rayas = len(la_palabra)
        self.palabra_vacia = "_ " * rayas
        return self.palabra_vacia.strip()
