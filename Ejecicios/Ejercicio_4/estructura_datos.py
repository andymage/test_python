

def numRepetidos(list_num):# funcion para valores repetidos
    set_list = set(list_num) #valores unicos
    num_rep = {}
    for uniq in set_list:
        indices = [i for i, x in enumerate(list_num) if x == uniq] #lista de frecuencia
        num_rep[uniq] = len(indices)
    frecc = list(num_rep.values())
    if frecc.count(max(frecc)) == 1:
        return max(num_rep, key=num_rep.get)
    else:
        return min(num_rep, key=num_rep.get)



list_num = [3,3,4,4,5,5,5,1]

respuesta = numRepetidos(list_num)
print(respuesta)