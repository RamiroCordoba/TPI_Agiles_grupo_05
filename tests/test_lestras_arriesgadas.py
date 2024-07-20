import pytest
from core.ahorcado import *


@pytest.fixture
def ahorcado():
    return Ahorcado()


def test_letra_en_lista(ahorcado):
    ahorcado.letras_arriesgada = ["a", "e", "i"]
    assert ahorcado.letras_arriesgadas_en_el_juego("a") == True


def test_letra_no_en_lista(ahorcado):
    ahorcado.letras_arriesgada = ["a", "e", "i"]
    assert ahorcado.letras_arriesgadas_en_el_juego("o") == False
