import re
# 2
# Abrimos el archivo de texto y lo leemos línea por línea
sorted_lines = ""
todos_los_datos = ""
with open("participantes.txt", "r") as archivo:
    for linea in archivo:
        # Utilizamos una expresión regular para buscar las líneas que no comienzan con una letra
        if re.match(r'^[^a-zA-Z]', linea):
            # Utilizamos la función split() para separar la línea en elementos
            elementos = linea.split()
            numero = elementos[0]
            nombre = elementos[-3] + " " + elementos[-2] + " " + elementos[-1]
            #print(f"{i}. {numero} {nombre}")
            sorted_lines += f"{numero} {nombre}\n"
            if re.match(r'^9,0000*', linea):
                todos_los_datos += linea
            with open("archivo_sin_ordenar.txt", "w") as f:
                f.writelines(sorted_lines)
            with open("archivo_todos_los_datos.txt", "w") as f:
                f.writelines(todos_los_datos)