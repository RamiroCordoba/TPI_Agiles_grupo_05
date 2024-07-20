import pytest
from core.ahorcado import *
from unittest.mock import patch

# Usamos mock_choice porque al ejecutar los tests no nos permite ingresar datos manualmente. De esta forma, podemos validarlos.


@patch("random.choice")
def test_generar_palabra_facil(mock_choice):
    mock_choice.return_value = "gato"

    juego = Ahorcado()
    palabra = juego.generar_palabra("facil")
    mock_choice.assert_called_once_with(dificultad_baja)
    # Verifica que la palabra generada es 'gato'
    assert palabra == "gato"


@patch("random.choice")
def test_generar_palabra_media(mock_choice):
    mock_choice.return_value = "cirugia"

    juego = Ahorcado()
    palabra = juego.generar_palabra("media")

    # Verifica que random.choice fue llamado con dificultad_media
    mock_choice.assert_called_once_with(dificultad_media)
    # Verifica que la palabra generada es 'cirugia'
    assert palabra == "cirugia"


@patch("random.choice")
def test_generar_palabra_alta(mock_choice):
    # Configura el valor que devolverá random.choice
    mock_choice.return_value = "hipopotomonstrosesquipedaliofobia"

    juego = Ahorcado()
    palabra = juego.generar_palabra("alta")

    # Verifica que random.choice fue llamado con dificultad_alta
    mock_choice.assert_called_once_with(dificultad_alta)
    # Verifica que la palabra generada es 'hipopotomonstrosesquipedaliofobia'
    assert palabra == "hipopotomonstrosesquipedaliofobia"
