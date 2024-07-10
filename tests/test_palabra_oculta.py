import pytest
from core.ahorcado import *


def test_ocultar_palabra_de_5_letras():
    un_juego = Ahorcado()
    assert un_juego.rayas_para_palabra("Perro") == "_ _ _ _ _"


def test_ocultar_palabra_de_6_letras():
    un_juego = Ahorcado()
    assert un_juego.rayas_para_palabra("campos") == "_ _ _ _ _ _"


def test_ocultar_palabra_de_8_letras():
    un_juego = Ahorcado()
    assert un_juego.rayas_para_palabra("caramelo") == "_ _ _ _ _ _ _ _"
