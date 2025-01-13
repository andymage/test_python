# Test - Leobardo Daniel Sánchez García 

# Generando lista con los primeros dos números de la secuencia de Finobacci 
secuencia_finobacci = [0, 1]
nuevo_numero = 0
# Genernado bucle para añadir los números faltantes de la secuencia
while True:
    
    nuevo_numero = secuencia_finobacci[-2] + secuencia_finobacci[-1]

    if nuevo_numero > 1000000:
        break
    else:
        secuencia_finobacci.append(nuevo_numero)

print("La secuencia de Finobacci hasta 1,000,000 es: \n{}".format(secuencia_finobacci))