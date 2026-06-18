def rtas_A_B(list_rtas, i, cont, diccio_indice):
    """
    Se busca el índice de donde pertenece la pregunta y se acumula un valor específico al puntaje de la personalidad en específico.

    Parameters
    ----------
    list_rtas : lista
        Contiene todas las respuestas del usuario en estilo de string.
    i : int
        Valor índice del que se utiliza para buscar de qué personalidad pertenece la respuesta.
    cont : diccionario
        Es el contador de puntajes para cada personalidad del R.A.I.S.E.C. del usuario.
    diccio_indice : diccionario
        Diccionario con las claves de R.A.I.S.E.C. con una lista dentro de cada clave que contiene los números para saber a qué personalidad pertenece cada respuesta.

    Returns
    -------
    cont
        Diccionario contador.
    """
    
    for clave in diccio_indice:
        for e in diccio_indice[clave]:
            if e == i:
                if list_rtas[i] == "a":
                    cont[clave] += 3
                    return cont

def sumar_autoestimacion(list_rtas, i, cont, diccio_indice):
    '''
    Se busca el índice de donde pertenece la pregunta y se acumula un valor específico al puntaje de la personalidad en específico.

    Parameters
    ----------
    list_rtas : lista
        Contiene todas las respuestas del usuario en estilo de string.
    i : int
        Valor índice del que se utiliza para buscar de qué personalidad pertenece la respuesta.
    cont : diccionario
        Es el contador de puntajes para cada personalidad del R.A.I.S.E.C. del usuario.
    diccio_indice : diccionario
        Diccionario con las claves de R.A.I.S.E.C. con una lista dentro de cada clave que contiene los números para saber a qué personalidad pertenece cada respuesta.

    Returns
    -------
    cont
        Diccionario contador.
    '''
    for lista in diccio_indice:
        for e in diccio_indice[lista]:
            if e == i:
                if list_rtas[i] == "1":
                    cont[lista] += 1
                    break
                elif list_rtas[i] == "2":
                    cont[lista] += 2
                    break
                elif list_rtas[i] == "3":
                    cont[lista] += 3
                    break
                elif list_rtas[i] == "4":
                    cont[lista] += 4
                    break
                elif list_rtas[i] == "5":
                    cont[lista] += 5
                    break
                elif list_rtas[i] == "6":
                    cont[lista] += 6
                    break
                else:
                    cont[lista] += 7
                    break
    return cont

def clasif_rtas(list_rtas, diccio_indice):
    '''
    Dentro de esta función, se va a crear el diccionario "cont" que contiene las iniciales de las personalidades R.A.I.S.E.C.
    Se redirige a la función "rtas_A_B" o "sumar_autoestimacion" dependiendo de qué clase de pregunta es ya sabiendo las posiciones de los tipos de respuesta.
    Finalmente, se sobreescribe lo que acumula el diccionario "cont" para así poder reutilizarlo en la siguiente iteración del bucle.

    Parameters
    ----------
    list_rtas : lista
        Contiene todas las respuestas del usuario en estilo de string.
    diccio_indice : diccionario
        Diccionario con las claves de R.A.I.S.E.C. con una lista dentro de cada clave que contiene los números para saber a qué personalidad pertenece cada respuesta.

    Returns
    -------
    cont
        Diccionario contador ya filtrado con todos los puntos de las respuestas.
    '''
    cont = {"R": 0, "A": 0, "I": 0, "S": 0, "E": 0, "C": 0}
    for i in range(len(list_rtas)):
        if (i == 0) or (i == 1) or (i == 9) or (i == 10) or (i == 12) or (i == 13) or (i == 15) or (i == 18) or (i == 19) or (i == 21) or (i == 23) or (i == 25):
            cont = rtas_A_B(list_rtas, i, cont, diccio_indice)
        else:
            cont = sumar_autoestimacion(list_rtas, i, cont, diccio_indice)
    return cont