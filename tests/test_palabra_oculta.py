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


def test_letra_pertenece():
    un_juego = Ahorcado()
    un_juego.palabra_NoVacia = 'caramelo'
    assert un_juego.letra_pertenece_palabra("c") == True


def test_letra_Nopertenece():
    un_juego = Ahorcado()
    un_juego.palabra_NoVacia = 'caramelo'
    assert un_juego.letra_pertenece_palabra("x") == False


def test_palabra_pertenece():
    un_juego = Ahorcado()
    un_juego.palabra_NoVacia = 'caramelo'
    assert un_juego.adivina_palabra("caramelo") == True

def test_palabra_Nopertenece():
    un_juego = Ahorcado()
    un_juego.palabra_NoVacia = 'caramelo'
    assert un_juego.adivina_palabra("Programar") == False