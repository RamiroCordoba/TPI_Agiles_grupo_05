import pytest
from core.ahorcado import *


def test_ocultar_palabra():
    un_juego = Ahorcado()
    assert un_juego.rayas_para_palabra("Perro") == "_ _ _ _ _"
