from flask import Flask, render_template, request, redirect, url_for, session
from core.ahorcado import Ahorcado


app = Flask(__name__)
app.secret_key = 'your_secret_key' 

# Crear una instancia del juego
ahorcado = Ahorcado()

@app.route('/')
def ingresar_nombre():
    return render_template('nombre.html')

@app.route('/guardar_nombre', methods=['POST'])
def guardar_nombre():
    nombre_usuario = request.form['nombre']
    session['nombre'] = nombre_usuario  
    return redirect(url_for('elegir_dificultad'))

@app.route('/elegir_dificultad')
def elegir_dificultad():
    if 'nombre' not in session:
        return redirect(url_for('ingresar_nombre'))  
    return render_template('inicio.html')

@app.route('/inicio/<nivel>')
def iniciar_juego(nivel):
    if 'nombre' not in session:
        return redirect(url_for('ingresar_nombre'))  
    ahorcado.iniciar_juego(nivel_dificultad=nivel)
    return redirect(url_for('inicio'))

@app.route('/inicio')
def inicio():
    if 'nombre' not in session:
        return redirect(url_for('ingresar_nombre'))  
    print(ahorcado.palabra_vacia)
    return render_template(
        'juego.html',
        palabra_a_mostrar=" ".join(ahorcado.palabra_a_mostrar),
        pista=ahorcado.dame_una_pista(),
        intentos_restantes=ahorcado.vidas_restantes,
        letras_usadas=ahorcado.letras_arriesgada,
        juego_finalizado=ahorcado.partida_concluida,
        palabra_adivinada=ahorcado.palabra_a_adivinar[0],
        img = ahorcado.img,
        long = ahorcado.long,
        pal_arriesgada= ahorcado.palabra_vacia,
        nombre_usuario=session.get('nombre')  
    )

@app.route('/intentar', methods=['POST'])
def intentar():
    letra = request.form['letra'].lower()
    if not ahorcado.partida_concluida:
        ahorcado.intento(letra)
        ahorcado.se_termino_el_juego()
    else:
        ahorcado.fin_juego()
    return redirect(url_for('inicio'))

@app.route('/intentarP', methods=['POST'])
def intentarP():
    palabraA = request.form['palabraA'].lower()
    ahorcado.intentoP(palabraA)
    ahorcado.se_termino_el_juego()
    if ahorcado.palabra_a_adivinar[0].replace(" ","") == palabraA.replace(" ",""):
        ahorcado.palabra_a_mostrar = ahorcado.palabra_a_adivinar[0]
    else:
        ahorcado.palabra_a_mostrar = palabraA
    return redirect(url_for('inicio'))

@app.route('/reiniciar')
def reiniciar():
    ahorcado.reiniciar_juego()
    return redirect(url_for('elegir_dificultad'))  


if __name__ == '__main__':
    app.run(debug=True)