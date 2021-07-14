from flask import *

app = Flask(__name__)

@app.route('/saludo')
def principal():
    return "Hola mundo en flask"

@app.route('/saludo/<nombre>')
def saludador(nombre):
    return "Hola " + nombre

@app.route('/despedida')
def despedida():
    return "Que tengas buen día"

@app.route('/dia/<int:dia>')
def dia_semana(dia):
    dias = ['domingo', 'lunes', 'martes', 'miercoles']
    if dia in range(len(dias)):
        return dias[dia]
    else:
        return "no se que dia es"

@app.route('/suma/<int:n1>/<int:n2>')
def suma(n1, n2):
    return str(n1 + n2)

app.run()
