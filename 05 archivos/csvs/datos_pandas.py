import pandas as pd
from matplotlib import pyplot as plt

# generar data frame desde la carga del archivo
df = pd.read_csv('chat_performance_clean.csv')

# imprimir la cabecera del data frame
print(df.head())

# imprimimos la forma del data frame
print(df.shape)

#generamos un nuevo data frame a partir de un agrupamiento del original
df_chats_usuarios = df.groupby('user_id')['chat_id'].count().reset_index()
#bautizamos las columnas
df_chats_usuarios.columns = ['user_id', 'number_chats']
# ordenamos los valores
df_chats_usuarios = df_chats_usuarios.sort_values(
    'number_chats',
    ascending = False
    )
# imprimir la cabecera del data frame
print(df_chats_usuarios.head())
# imprimimos la forma del data frame
print(df_chats_usuarios.shape)

# construcción de la figura
# parametros
plt.rcParams['figure.figsize'] = [20, 20]

df_chats_usuarios[:10].plot(
    x = 'user_id',
    y = 'number_chats',
    kind = 'bar',
    legend = False,
    color = 'blue',
    width = 0.8
    )

plt.ylabel("Numbre of chats")
plt.xlabel("User")
plt.title("Chats per user")

# genero el archivo de la gráfica
plt.savefig("chats_per_user.png")
