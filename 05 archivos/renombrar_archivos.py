from os import path, listdir, rename

lista = listdir('fuentes/renombrables')

for a in lista:
    if path.exists('fuentes/renombrables/' + str(a)):
        rename('fuentes/renombrables/' + str(a),
               'fuentes/renombrables/renombrado_' + str(a))
    else:
        print("el archivo %s no existe" % str(a))
