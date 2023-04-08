import locale
# 3
# Configurar local adecuado para el archivo (por ejemplo, España)
locale.setlocale(locale.LC_ALL, 'es_ES.utf-8')

# Abrir el archivo original
with open("archivo_sin_ordenar.txt", "r") as f:
    lines = f.readlines()

# Ordenar las líneas por el número en orden descendente
sorted_lines = sorted(lines, key=lambda x: locale.atof(x.split()[0]), reverse=True)

# Añadimos la posición a cada línea para facilitar la lectura
i = 1
listado_ordenado = ""
for linea in sorted_lines:
    listado_ordenado += f'{i}. {linea}'
    i+=1
# Crear un nuevo archivo y guardar las líneas ordenadas
with open("archivo_ordenado.txt", "w") as f:
    f.writelines(listado_ordenado)

