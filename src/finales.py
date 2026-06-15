def finales (lista_rtas):
    '''
    esta funcion identifica la pocicion de las rtas para encontar las que corresponde a la determinacion del final

    Parameters
    ----------
    lista_rtas : lista 
        lista con strings "a" y "b", aparte de numeros del "1-7".
    raises: 
        indexerror: si la lista esta vacia
    Returns
    -------
    print con el final correspndiente.

    '''
    lista_finales = []
    if lista_rtas == []:
        raise IndexError("no hay respuestas que determinen el final")
    for i in range(len(lista_rtas)):
        if i == 0 or i == 18:
            lista_finales.append(lista_rtas[i])
    if lista_rtas == ["a", "a"]:
        print("Al final, tu forma de ver las cosas hizo que la fiesta de cumpleaños saliera perfecta, pero en tu cabeza. Al querer liderar la preparación pero simultáneamente al no querer cooperar con tus amigos, al final tus amigos se quedaron frustrados porque sus ideas nunca fueron escuchadas. Esto provocó que las dificultades ocurridas sean manejadas únicamente por vos. Al menos el cumpleañero disfrutó la fiesta… no?")
    elif lista_rtas == ["a", "b"]:
        print("¡Tu organización del cumpleaños quedó espectacular! Lograste coordinar con tus amigos para que todos aportaran ideas y rápidamente asumiste el rol de guía de la preparación. Calculaste que todo saliera a la perfección, y así fue. Aunque ocurrieron imprevistos, los manejaron apropiadamente. Gracias a tu capacidad de liderazgo, tus amigos colaboraron de manera equitativa ¡La suma de estos factores hizo que al cumpleañero disfrutara mucho su fiesta sorpresa!")
    elif lista_rtas == ["b", "a"]:
        print("Trabajaste mucho y no pudiste disfrutar tanto de la fiesta como tus amigos. Terminaste siguiendo todas las instrucciones que te proponían, sin discutir las cosas en grupo, ya que preferiste trabajar de manera independiente. Lograron sobrepasar las dificultades, pero no lograron cooperar para resolverlas de forma más eficiente. Al final, el cumpleañero disfrutó de la fiesta pero quedaste frustrado y cansado.")
    else:
        print ("¡Tu capacidad de cooperación con tus amigos hizo que la fiesta saliera muy bien! Al preferir seguir las instrucciones que proponía uno de tus amigos, te enfocaste en que tu parte saliera bien. También lograste cooperar con el resto para que, a pesar de las dificultades, ¡el cumpleañero disfrutara de su fiesta sorpresa!")
            
        
            
        

