
#Manejo de archivos.
#Libreria para argumentos en linea de comandos

import argparse
#Lectura del archivo de texto
#definicion de los argumento por linea de comando
parser = argparse.ArgumentParser(description="Manejador de archivos")
parser.add_argument("input_file", help="Ruta del archivo de texto(.txt)")
parser.add_argument("input_word", help="Palabra a buscar en texto")
args = parser.parse_args()

ftext = args.input_file
fword = str(args.input_word).lower().strip()
#procesamiento de archivo de texto
with open(ftext, "r") as datos:
    contenido = datos.read()
    count = 0
    contenido = contenido.lower()
    spr_char = ",¡!¿?#_-*$+=;:.<>{[]}()"
    for chr in spr_char: # elimino caracteres especiales
        contenido = contenido.replace(chr,"")
    list_cont = contenido.split()
    if fword in list_cont: # se verifica si existe la palabra en la lista
        for word in list_cont:
            if word == fword:
                count += 1
        print(f"Se encontraron {count} coinsidencias con la palabra \'{args.input_word}\'")
    else:
        print("No se encuentra la palabra en el texto")
