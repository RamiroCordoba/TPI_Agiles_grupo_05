import pytest
from unittest.mock import patch
from core.ahorcado import Ahorcado


# Test para iniciar_juego
@patch(
    "core.ahorcado.random.choice",
    return_value=[
        "gato",
        "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes.",
    ],
)
def test_iniciar_juego(mock_random_choice):
    juego = Ahorcado()
    juego.iniciar_juego(nivel_dificultad="facil")
    assert juego.palabra_a_adivinar == [
        "gato",
        "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes.",
    ]
    assert juego.palabra_a_mostrar == ["_", "_", "_", "_"]
    assert juego.vidas_restantes == 5
    assert (
        juego.pista
        == "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes."
    )


# Test para dame_una_pista
def test_dame_una_pista():
    juego = Ahorcado()
    juego.pista = (
        "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes."
    )
    assert (
        juego.dame_una_pista()
        == "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes."
    )


# Test para intentoP
def test_intentoP_correcto():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="gato", pista="Animal doméstico de cuatro patas")
    juego.intentoP("gato")
    assert juego.palabra_a_mostrar == ["g", "a", "t", "o"]
    assert juego.vidas_restantes == 5
    assert juego.partida_concluida is True


def test_intentoP_incorrecto():
    juego = Ahorcado()
    juego.iniciar_juego(palabra="gato", pista="Animal doméstico de cuatro patas")
    juego.intentoP("perro")
    assert juego.palabra_a_mostrar == ["p", "e", "r", "r", "o"]
    assert juego.vidas_restantes == 0
    assert juego.partida_concluida is True


# Test para reiniciar_juego
@patch(
    "core.ahorcado.random.choice",
    return_value=[
        "gato",
        "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes.",
    ],
)
def test_reiniciar_juego(mock_random_choice):
    juego = Ahorcado()
    juego.iniciar_juego(nivel_dificultad="facil")
    juego.intento("a")
    assert juego.letras_arriesgada == ["a"]
    juego.reiniciar_juego()
    assert juego.letras_arriesgada == []
    assert juego.palabra_a_mostrar == ["_", "_", "_", "_"]
    assert juego.vidas_restantes == 5
    assert (
        juego.pista
        == "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes."
    )
