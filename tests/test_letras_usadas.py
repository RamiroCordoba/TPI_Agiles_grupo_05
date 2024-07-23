import pytest
from core.ahorcado import *


def test_letras_usadas():
    juego = Ahorcado()
    juego.letras_adivinadas.append("P")
    assert juego.letras_usadas("P") == True


def test_letras_usadas_letra_ya_usada():
    juego = Ahorcado()
    juego.letras_adivinadas = ["a", "e", "i"]
    assert juego.letras_usadas("a") == True
    assert juego.letras_usadas("e") == True
    assert juego.letras_usadas("i") == True


def test_letras_usadas_letra_no_usada():
    juego = Ahorcado()
    juego.letras_adivinadas = ["a", "e", "i"]
    assert juego.letras_usadas("o") == False
    assert juego.letras_usadas("u") == False


def test_letras_usadas_letras_usadas_vacio():
    juego = Ahorcado()
    juego.letras_adivinadas = []
    assert juego.letras_usadas("a") == False
    assert juego.letras_usadas("e") == False
