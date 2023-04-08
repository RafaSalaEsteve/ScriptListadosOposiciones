import PyPDF2
# 1
# Abre el archivo PDF y extrae el contenido de todas las páginas
with open('Provisional_Maestros-824-969.pdf', 'rb') as archivo:
    lector = PyPDF2.PdfReader(archivo)
    texto_completo = ''
    for pagina in range(len(lector.pages)):
        texto_completo += lector.pages[pagina].extract_text()

# Busca las líneas que contienen los nombres y las puntuaciones de los participantes
lineas = texto_completo.split('\n')
participantes = []
for indice, linea in enumerate(lineas):
    # Busca el nombre
    if ',' in linea and linea.count(',') == 1:
        partes = linea.split(',')
        print(partes)
        apellidos, nombre = partes[0].strip(), partes[1].strip()

        print(nombre)
        # Busca la puntuación total en la línea siguiente
        if 'Puntuación total' in lineas[indice+1]:
            puntuacion_total = int(lineas[indice+1].split()[-1])
            participantes.append((nombre + ' ' + apellidos, puntuacion_total))

# Ordena los participantes por puntuación de mayor a menor
participantes_ordenados = sorted(participantes, key=lambda x: x[1], reverse=True)

# Escribe los participantes ordenados en un archivo de texto
with open('participantes.txt', 'w') as archivo:
    archivo.write(texto_completo)
    #for participante in participantes_ordenados:
    #    archivo.write(participante[0] + ' ' + str(participante[1]) + '\n')


# Imprime los participantes ordenados
for participante in participantes_ordenados:
    print(participante[0], participante[1])

