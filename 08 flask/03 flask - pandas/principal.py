from flask import Flask, request, render_template

import pandas as pd
import matplotlib.pyplot as plt
import base64
import io

app = Flask(__name__)

@app.route('/cargador', methods=['POST', 'GET'])
def cargador():
    if request.method == 'GET':
        return render_template('carga.html')
    else:
        archivo = request.files['file']
        archivo_cargado = archivo.filename

        archivo.save(archivo_cargado)

        df = pd.read_csv(archivo_cargado)
        shape_original = df.shape

        df = df.groupby(['generos'])['mascotas','hijos','edades'].median().reset_index()

        df.plot(figsize = (10, 10),
                title = 'Mediana de valores',
                kind = 'bar',
                x = 'generos'
            )

        img = io.BytesIO()

        plt.legend()
        plt.savefig(img, format='png')
        img.seek(0)

        plot_url = base64.b64encode(img.getvalue()).decode()

        return render_template('resultados.html',
                               imagen = plot_url, 
                               tabla = df.to_html(classes='data', header=True, index=False))


if __name__ == '__main__':
    app.run()
