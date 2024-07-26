Feature: Ingresar Nombre de Usuario y Seleccionar Dificultad
  Scenario: Usuario arriesga una palabra con dificultad "fácil"
    Given que estoy en la página de ingreso de nombre
    When ingreso el nombre "Alexis"
    And hago clic en el botón "Siguiente"
    Then debo ser redirigido a la página de elección de dificultad
    When selecciono la dificultad "fácil" y el juego se genera con la palabra "dubi" y pista "Arquero de la seleccion Argentina 2024 dicho con dislexia"
    Then debo ser redirigido a la página de juego
    When arriesgo la palabra "dubi"
    Then la palabra "dubi" debería ser registrada como adivinada
  
  Scenario: Usuario arriesga una palabra con dificultad "difícil"
    Given que estoy en la página de ingreso de nombre
    When ingreso el nombre "Alexis"
    And hago clic en el botón "Siguiente"
    Then debo ser redirigido a la página de elección de dificultad
    When selecciono la dificultad "difícil" y el juego se genera con la palabra "hipopotomonstrosesquipedaliofobia" y pista "El temor irracional a las palabras largas o complejas"
    Then debo ser redirigido a la página de juego
    When arriesgo la palabra "palabraLargaFobia"
    Then la palabra "palabraLargaFobia" debería ser registrada como no adivinada "hipopotomonstrosesquipedaliofobia"

  Scenario: Usuario arriesga letras en un juego de dificultad "media"
    Given que estoy en la página de ingreso de nombre
    When ingreso el nombre "Alexis"
    And hago clic en el botón "Siguiente"
    Then debo ser redirigido a la página de elección de dificultad
    When selecciono la dificultad "media" y el juego se genera con la palabra "naufragio" y pista "Hundimiento o destrucción de una embarcación en el mar."
    Then debo ser redirigido a la página de juego
    When arriesgo la letra "n"
    Then la letra "n" debería ser registrada como usada
    When arriesgo la letra "a"
    Then la letra "a" debería ser registrada como usada
    When arriesgo la letra "u"
    Then la letra "u" debería ser registrada como usada
    When arriesgo la letra "f"
    Then la letra "f" debería ser registrada como usada
    When arriesgo la letra "r"
    Then la letra "r" debería ser registrada como usada
    When arriesgo la letra "g"
    Then la letra "g" debería ser registrada como usada
    When arriesgo la letra "i"
    Then la letra "i" debería ser registrada como usada
    When arriesgo la letra "o"
    Then la letra "o" debería ser registrada como usada    
    Then la palabra "naufragio" debería ser registrada como adivinada

  Scenario: Usuario arriesga letras en un juego de dificultad "fácil"
    Given que estoy en la página de ingreso de nombre
    When ingreso el nombre "Alexis"
    And hago clic en el botón "Siguiente"
    Then debo ser redirigido a la página de elección de dificultad
    When selecciono la dificultad "fácil" y el juego se genera con la palabra "gato" y pista "Animal doméstico de cuatro patas, conocido por su agilidad y sus bigotes."
    Then debo ser redirigido a la página de juego
    When arriesgo la letra "n"
    Then la letra "n" debería ser registrada como usada
    When arriesgo la letra "a"
    Then la letra "a" debería ser registrada como usada
    When arriesgo la letra "u"
    Then la letra "u" debería ser registrada como usada
    When arriesgo la letra "g"
    Then la letra "g" debería ser registrada como usada
    When arriesgo la letra "t"
    Then la letra "t" debería ser registrada como usada
    When arriesgo la letra "q"
    Then la letra "q" debería ser registrada como usada
    When arriesgo la letra "z"
    Then la letra "z" debería ser registrada como usada
    When arriesgo la letra "l"
    Then la letra "l" debería ser registrada como usada    
    Then la palabra "naugtqzl" debería ser registrada como no adivinada "gato"