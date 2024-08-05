from behave import given, when, then
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que estoy en la página de ingreso de nombre')
def step_given_en_pagina_ingreso_nombre(context):
    context.browser.get('http://localhost:5000/')
    time.sleep(1)

@when('ingreso el nombre "{nombre}"')
def step_when_ingreso_nombre(context, nombre):
    input_nombre = context.browser.find_element(By.NAME, 'nombre')
    input_nombre.send_keys(nombre)
    time.sleep(1)

@when('hago clic en el botón "Siguiente"')
def step_when_hago_clic_en_guardar(context):
    boton_siguiente = context.browser.find_element(By.CSS_SELECTOR, 'form button[type="submit"]')
    boton_siguiente.click()
    time.sleep(1)

@then('debo ser redirigido a la página de elección de dificultad')
def step_then_redirigido_a_elegir_dificultad(context):
    time.sleep(1)
    assert "elegir_dificultad" in context.browser.current_url

@when('selecciono la dificultad "{dificultad}" y el juego se genera con la palabra "{palabra}" y pista "{pista}"')
def step_when_selecciono_dificultad_y_juego_se_genera(context, dificultad, palabra, pista):
    # Seleccionar la dificultad
    time.sleep(1)
    if dificultad == "fácil":
        boton_dificultad = context.browser.find_element(By.CSS_SELECTOR, 'form[action*="facil"] button[type="submit"]')
    elif dificultad == "media":
        boton_dificultad = context.browser.find_element(By.CSS_SELECTOR, 'form[action*="media"] button[type="submit"]')
    elif dificultad == "difícil":
        boton_dificultad = context.browser.find_element(By.CSS_SELECTOR, 'form[action*="dificil"] button[type="submit"]')
    else:
        raise ValueError("Dificultad no reconocida")

    context.browser.execute_script("arguments[0].setAttribute('type', 'button')", boton_dificultad)
    
    boton_dificultad.click()
    time.sleep(1)
   
    context.browser.get(f"http://localhost:5000/inicio/?{dificultad}&palabra={palabra}&pista={pista}")
    time.sleep(1)
    assert "inicio" in context.browser.current_url


@then('debo ser redirigido a la página de juego')
def step_then_redirigido_a_pagina_de_juego(context):
    time.sleep(1)
    assert "inicio" in context.browser.current_url

@when('arriesgo la letra "{letra}"')
def step_when_arriesgo_letra(context, letra):
    input_letra = context.browser.find_element(By.ID, 'letra')
    input_letra.send_keys(letra)
    wait = WebDriverWait(context.browser, 10)
    boton_enviar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Arriesgar letra']")))
    boton_enviar.click()
    time.sleep(1)

@then('la letra "{letra}" debería ser registrada como usada')
def step_then_letra_registrada(context, letra):
    wait = WebDriverWait(context.browser, 10)
    # Seleccionar el elemento <p> que contiene el texto "Letras usadas:"
    letras_usadas_elemento = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[strong[contains(text(), 'Letras usadas:')]]")))
    letras_usadas_texto = letras_usadas_elemento.text
    print(f'Contenido actual de letras usadas: {letras_usadas_texto}')
    # Asegurarse de que la letra esté en el texto después de "Letras usadas: "
    letras_usadas_texto = letras_usadas_texto.replace("Letras usadas: ", "")
    assert letra in letras_usadas_texto, f'La letra {letra} no está registrada como usada.'




@when('arriesgo la palabra "{palabra}"')
def step_when_arriesgo_palabra(context, palabra):
    wait = WebDriverWait(context.browser, 10)
    input_palabra = wait.until(EC.presence_of_element_located((By.ID, 'palabraA')))
    input_palabra.send_keys(palabra)
    boton_enviar = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Arriesgar Palabra']")))
    boton_enviar.click()
    time.sleep(1)


@then('la palabra "{palabra}" debería ser registrada como adivinada')
def step_then_palabra_adivinada(context, palabra):
    wait = WebDriverWait(context.browser, 10)
    palabra_a_mostrar_texto = wait.until(EC.visibility_of_element_located((By.ID, 'palabra_a_mostrar'))).text
    assert palabra.lower() == palabra_a_mostrar_texto.lower().replace(" ", "").lower(), f'La palabra {palabra} está registrada como adivinada.'

@then('la palabra "{palabra}" debería ser registrada como no adivinada "{palabraAdi}"')
def step_then_palabra_no_adivinada(context, palabra, palabraAdi):
    wait = WebDriverWait(context.browser, 10)
    palabra_a_mostrar_texto = wait.until(EC.visibility_of_element_located((By.ID, 'palabra_a_mostrar'))).text
    palabra_a_mostrar = palabra_a_mostrar_texto.replace(" ", "").lower()
    palabra_esperada = palabraAdi.replace(" ", "").lower()
    
    assert palabra_a_mostrar != palabra_esperada, f'La palabra "{palabra}" debería ser registrada como no adivinada.'
