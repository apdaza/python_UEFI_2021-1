import sqlite3 as sql

conn = sql.connect('datos.db')

conn.execute('create table ciudades(nombre TEXT, hijos TEXT, mascotas TEXT)')

conn.close()
