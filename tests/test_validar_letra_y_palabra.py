import pytest
from core.ahorcado import *


def test_letra_pertenece():
    un_juego = Ahorcado()
    un_juego.palabra_a_adivinar = "caramelo"
    assert un_juego.letra_pertenece_palabra("c") == True


def test_letra_Nopertenece():
    un_juego = Ahorcado()
    un_juego.palabra_a_adivinar = "caramelo"
    assert un_juego.letra_pertenece_palabra("x") == False


def test_palabra_pertenece():
    un_juego = Ahorcado()
    un_juego.palabra_a_adivinar = "caramelo"
    assert un_juego.adivina_palabra("caramelo") == True


def test_palabra_Nopertenece():
    un_juego = Ahorcado()
    un_juego.palabra_a_adivinar = "caramelo"
    assert un_juego.adivina_palabra("Programar") == False
