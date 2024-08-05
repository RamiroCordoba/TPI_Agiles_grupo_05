import pytest
from core.ahorcado import *


def test_estado_del_juego():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "gato"
    juego.letra_pertenece_palabra("g")
    juego.letra_pertenece_palabra("a")
    assert juego.se_termino_el_juego() == False


def test_juego_terminado_con_ganador():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "gato"
    juego.intento("g")
    juego.intento("a")
    juego.intento("t")
    juego.intento("o")
    assert juego.se_termino_el_juego() == True


def test_juego_terminado_con_perdedor():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "gato"
    juego.intento("q")
    juego.intento("w")
    juego.intento("y")
    juego.intento("m")
    juego.intento("z")
    assert juego.se_termino_el_juego() == True
