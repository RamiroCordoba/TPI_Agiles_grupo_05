class Ahorcado:
    def __init__(self):
        self.palabra_vacia = ""
        self.palabra_NoVacia = ""

    def rayas_para_palabra(self, la_palabra):
        rayas = len(la_palabra)
        self.palabra_vacia = "_ " * rayas
        return self.palabra_vacia.strip()
    
    def letra_pertenece_palabra(self,letra):
        return letra in self.palabra_NoVacia
    
    def adivina_palabra(self,palabra):
        return self.palabra_NoVacia == palabra