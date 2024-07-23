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


def test_mostrar_letra_correcta_una_letra_acertada():
    juego = Ahorcado()
    juego.palabra_a_adivinar = [
        "gato",
        "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes.",
    ]
    juego.letras_arriesgada = ["a"]
    juego.mostrar_letra_correcta("a")
    assert juego.palabra_a_mostrar == ["_", "a", "_", "_"]


def test_mostrar_letra_correcta_variass_letras_acertadas():
    juego = Ahorcado()
    juego.palabra_a_adivinar = [
        "gato",
        "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes.",
    ]
    juego.letras_arriesgada = ["a", "t"]
    juego.mostrar_letra_correcta("a")
    juego.mostrar_letra_correcta("t")
    assert juego.palabra_a_mostrar == ["_", "a", "t", "_"]


def test_mostrar_letra_correcta_letra_no_acertada():
    juego = Ahorcado()
    juego.palabra_a_adivinar = [
        "gato",
        "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes.",
    ]
    juego.letras_arriesgada = []
    juego.mostrar_letra_correcta("z")
    assert juego.palabra_a_mostrar == ["_", "_", "_", "_"]


def test_mostrar_letra_correcta_todas_letras_acertadas():
    juego = Ahorcado()
    juego.palabra_a_adivinar = [
        "gato",
        "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes.",
    ]
    juego.letras_arriesgada = ["g", "a", "t", "o"]
    juego.mostrar_letra_correcta("o")
    assert juego.palabra_a_mostrar == ["g", "a", "t", "o"]


def test_mostrar_letra_correcta_con_letra_repetida():
    juego = Ahorcado()
    juego.palabra_a_adivinar = ["mama", "Palabra que significa madre."]
    juego.letras_arriesgada = ["m"]
    juego.mostrar_letra_correcta("m")
    assert juego.palabra_a_mostrar == ["m", "_", "m", "_"]
