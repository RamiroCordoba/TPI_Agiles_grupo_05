import pytest
from core.ahorcado import *


def test_iniciar_juego():
    juego = Ahorcado()
    assert juego.vidas == 5
    assert juego.vidas_restantes == 5
    assert juego.letras_adivinadas == []


def test_intento_letra_valida():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "escoba"
    assert juego.intento("e") == True
    assert juego.letras_adivinadas == ["e"]
    assert juego.vidas_restantes == 5


def test_intento_letra_fallida():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "escoba"
    assert juego.intento("z") == False
    assert juego.letras_adivinadas == []
    assert juego.vidas_restantes == 4
