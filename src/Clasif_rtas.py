def rtas_A_B(list_rtas, i, cont, diccio_indice):
    for lista in diccio_indice:
        for e in diccio_indice[lista]:
            if e == i:
                if list_rtas[i] == "a":
                    cont[lista] += 1
    return cont

def sumar_autoestimacion(list_rtas, i, cont, diccio_indice):
    for lista in diccio_indice:
        for e in diccio_indice[lista]:
            if e == i:
                if list_rtas[i] == "1":
                    cont[lista] += 1
                elif list_rtas[i] == "2":
                    cont[lista] += 2
                elif list_rtas[i] == "3":
                    cont[lista] += 3
                elif list_rtas[i] == "4":
                    cont[lista] += 4
                elif list_rtas[i] == "5":
                    cont[lista] += 5
                elif list_rtas[i] == "6":
                    cont[lista] += 6
                else:
                    cont[lista] += 7
    return cont

def clasif_rtas(list_rtas, diccio_indice):
    cont = {"R": 0, "A": 0, "I": 0, "S": 0, "E": 0, "C": 0}
    for i in range(len(list_rtas)):
        if i == 0:#posición
            cont = rtas_A_B(list_rtas, i, cont, diccio_indice)
        else:
            cont = sumar_autoestimacion(list_rtas, i, cont, diccio_indice)
    return cont