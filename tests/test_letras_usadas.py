import pytest
from core.ahorcado import *

def test_letras_usadas():
    juego = Ahorcado()
    juego.letras_adivinadas.append("P")
    assert juego.letras_usadas("P") == True