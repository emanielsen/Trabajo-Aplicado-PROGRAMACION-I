def rtas_A_B(list_rtas, i, cont, diccio_indice):
    for e in diccio_indice.values:
        if e == i:
            
    pass

def sumar_autoestimacion(list_rtas, i, cont, diccio_indice):
    pass

def clasif_rtas(list_rtas, diccio_indice):
    cont = {"R": 0, "A": 0, "I": 0, "S": 0, "E": 0, "C": 0}
    for i in range(len(list_rtas)):
        if i == 0:#posición
            cont = rtas_A_B(list_rtas, i, cont, diccio_indice)
        else:
            cont = sumar_autoestimacion(list_rtas, i, cont, diccio_indice)
    return cont