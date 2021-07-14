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
        opcion = request.form['opcion']
        print(opcion)
        archivo.save(archivo_cargado)

        df = pd.read_csv(archivo_cargado)
        shape_original = df.shape

        df, titulo = agrupar(opcion, df)
        
        df.plot(figsize = (10, 10),
                title = titulo,
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

def agrupar(opc, df):
    if opc == 'mediana':
        df = df.groupby(['generos'])['mascotas','hijos','edades'].median().reset_index()
        title = 'Mediana de valores'
    elif opc == 'minimo':
        df = df.groupby(['generos'])['mascotas','hijos','edades'].min().reset_index()
        title = 'Valores mínimos'
    else:
        df = df.groupby(['generos'])['mascotas','hijos','edades'].max().reset_index()
        title = 'Valores máximos'
    return df, title


if __name__ == '__main__':
    app.run()
