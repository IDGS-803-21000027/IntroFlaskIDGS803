from io import open

archivo_texto = open('IntroFlaskIDGS803/anombres.txt', 'r')

#archivo_texto.write('\n datos en el archivo')

#archivo_texto.close()

for lineas in archivo_texto.readlines():
    print(lineas.rstrip())

#archivo_texto.seek(0)

#print(archivo_texto.read())


archivo_texto.close()