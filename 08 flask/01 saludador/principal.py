from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hola/<usuario>')
def hola(usuario):
    lenguajes = {'python': 70, 'java': 20, 'php': 10}
    return render_template('hola.html', nombre = usuario,
                           uso_lenguajes = lenguajes)

if __name__ == '__main__':
    app.run()
