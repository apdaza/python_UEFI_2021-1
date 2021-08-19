from flask import Flask, request, render_template

import pandas as pd
import matplotlib.pyplot as plt
import base64
import io

import sqlite3 as sql

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


@app.route('/guardar', methods=['POST', 'GET'])
def guardar():
    if request.method == 'GET':
        return render_template('carga2.html')
    else:
        archivo = request.files['file']
        archivo_cargado = archivo.filename
        df = pd.read_csv(archivo_cargado)
        df = df.groupby(['ciudades'])['mascotas','hijos'].median().reset_index()
        print(df.head())
        try:
            for index, row in df.iterrows():
                with sql.connect('datos.db') as conn:
                    cur = conn.cursor()
                    cur.execute('Insert into ciudades(nombre, hijos, mascotas) values(?,?,?)',
                                (row['ciudades'], row['mascotas'], row['hijos']))
                    conn.commit()
        except:
            conn.rollback()
        finally:
            conn.row_factory = sql.Row
            cur = conn.cursor()
            cur.execute('select * from ciudades')
            rows = cur.fetchall()
            conn.close()
            
        
        return render_template('listado.html', data = rows)

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
