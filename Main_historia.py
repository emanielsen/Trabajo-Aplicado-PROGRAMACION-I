import pandas as pd
from src.Clasif_rtas import clasif_rtas


archivo = 'data/base_datos_holland_carreras_5000.xlsx'
df = pd.read_excel(archivo)
#llamar a filtar_dataset (cuendo sepa que me devuelve)
amigo1 = input("ingrese el nombre de un amigo: ")
amigo2 = input("ingrese el nombre de otro amigo: ")
amigo3 = input("ingrese el nombre de un tercer amigo: ")

lista_historia = [
    # 0
    f'{amigo1}, {amigo2}, {amigo3} y vos son un grupo de amigos. ¡El cumpleaños de {amigo3} es en 10 días! Estás pensando organizarle un cumpleaños a {amigo3}:\nPreferirías:\na) Organizarlo vos solo\nb) Pedirle ayuda a {amigo1} y {amigo2}',
    
    # 1
    'Tus amigos se enteraron y te quieren ayudar (Tus amigos justo tuvieron la misma idea, y también quieren hacer una fiesta sorpresa)\n¿Te gustaría empezar a organizarlo ahora (aunque falte bastante para la fecha)?\na) Sí\nb) No',
    
    # 2
    f'{amigo1} le contó a los papás de {amigo3} y ellos sugirieron arrancar hoy mismo!\nEntonces:\n¿Qué tanto preferís ser el responsable de la planificación de actividades?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 3
    '¿Qué tanto te gustaría hacer una lluvia de ideas para planear la fiesta?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 4
    'Tus amigos quieren sugerir ideas para el evento:\n¿Qué tan abierto estás a seguir las ideas de tus amigos?\nResponde del 1-7 (1 siendo mucho y 7 siendo que prefieres seguir tus ideas propias)',
    
    # 5
    'En el caso que prefieras seguir tus propias ideas (responder 1 si no fue el caso)\n¿Qué tan bueno sos convenciendo a los demás sobre tu punto de vista?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 6
    'En caso de que tengas que seguir las ideas de los demás (responder 1 si no fue el caso),\n¿Qué tanto te gustaría que las ideas sean detalladas y específicas?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 7
    f'A {amigo2} se le ocurrió algo para hacer:\n¿Qué tanto te gustaría que te especifiquen qué hacer de antemano?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 8
    'Si, en cambio, son tus ideas las que se siguen (responder 1 si no fue el caso),\n¿Qué tanto te gusta dirigir a los demás?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 9
    'Si te encontras a cargo del evento (responder 1 si no fue el caso)\n¿Te gustaría poder chequear lo que hacen tus amigos para llegar a tiempo?\na) Sí\nb) No',
    
    # 10
    f'{amigo1} está encargado de comprar la torta, pero sabés que es medio despistado,\n¿Preferís pensar en posibles problemas (como que se olvide de comprarla) y pensar en sus soluciones?\na) Sí\nb) No',
    
    # 11
    'A la hora de pensar en un regalo,\n¿Qué tan probable es que le des un regalo hecho por vos (alguna manualidad)?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 12
    'Si deciden regalar algo hecho por ustedes (responder 1 si no fue el caso),\n¿Es probable que le prestes mucha atención a los detalles?\na) Sí\nb) No',
    
    # 13
    f'¿Te gustaría dibujarle algo a {amigo3} como regalo?\na) Sí\nb) No',
    
    # 14
    f'¿Te gustaría inventarle/armarle algo a {amigo3} (como una manualidad) como regalo?\na) Sí\nb) No',
    
    # 15
    f'Como regalarle a {amigo3} algo hecho por ustedes es mucho trabajo, se reparten tareas.\n{amigo1} y {amigo2} no tienen muy en claro cómo hacer su parte.\n¿Te molestaría explicarles cómo hacerlas?\na) No\nb) Sí',
    
    # 16
    'Deciden que trabajar juntos es más divertido y tienen que organizar en dónde se encontrarán:\n¿Qué tanto te gustaría que se juntaran en una plaza o en algún lugar al aire libre para trabajar?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 17
    'Es el día del cumpleaños. Tus amigos y vos decidieron hacer la fiesta sorpresa en el patio de tu casa, por mayoría de votación.\n¿Te gusta estar a diario al aire libre?\na) Sí\nb) No',
    
    # 18
    'Notás que la organización de los preparativos podría ser más eficiente si alguno toma el rol de guiar o supervisar al resto, ya que hay poco tiempo y mucho para hacer.\nPreferís:\na) Supervisar al resto\nb) Tener instrucciones claras que seguir',
    
    # 19
    'Tu tarea consiste en poner la mesa, inflar globos y ordenar un poco tu patio. Son bastantes cosas que hacer en poco tiempo.\n¿Qué tanto te gustaría hacer cada tarea con cuidado, paso a paso, incluso con el tiempo limitado?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 20
    'Tenés que ir a buscar los globos para inflar de tres colores distintos. Te das cuenta que no hay cantidades iguales de cada color. Querés ponerlos a cierta distancia, llenando las paredes o postes donde podés colocarlos, usando la menor cantidad de globos.\n¿Te gusta este tipo de trabajo con números y eficiencia?\na) Sí\nb) No',
    
    # 21
    'Empiezan a organizar los preparativos, y uno de tus amigos está colgando unas guirnaldas. Ves que no está alcanzando a colgarlas, porque es más bajo. Podrías ayudarlo ahora, pero aún tenés mucho que hacer por tu parte.\n¿Qué tanto considerás ayudar a tu amigo o, en cambio, asumís que se las puede arreglar solo?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 22
    'Con tus amigos deciden escribirle una cartita o dedicatoria pegada al envoltorio del regalo. Alguien debe encargarse de eso.\n¿Se te da bien escribir este tipo de cosas?\na) Sí\nb) No',
    
    # 23
    'Terminan de preparar todo para la fiesta y ya se hace la hora del cumpleaños. Llegan el cumpleañero y más amigos.\n¿Usualmente qué tan seguido inicias las conversaciones con la gente?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 24
    'Te das cuenta que el cumpleañero se está acercando al lugar donde escondieron su regalo para dárselo después. Rápidamente debés improvisar para dirigirlo hacia otro lado, así no se da cuenta de la sorpresa.\n¿Se te da bien crear historias ficticias para, en este caso, improvisar y hacer que el regalo no sea descubierto?\na) Sí\nb) No',
    
    # 25
    'Afortunadamente, lograste disuadir al cumpleañero. Pero al volver, se tropieza con el cable del parlante, entonces se caen el parlante y el cumpleañero al piso. Rápidamente van con dos amigos a ver si está bien.\n¿Qué tan bien se te da ocuparte de los demás?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 26
    'Por suerte, tu amigo apenas se raspó y está bien. El que no está bien es el parlante, que ahora no funciona. Entonces proponen que alguien lo arregle para que la fiesta no se quede sin música.\n¿Qué tanto te gusta estar en un ambiente donde puedas resolver problemas mecánicos o reparar aparatos de este tipo?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 27
    'Aunque intentan arreglarlo, no lo logran. Te acordás que en el ático de tu casa hay una guitarra vieja y un piano. Podría alguien (o vos mismo) animarse a tocar un instrumento.\n¿Qué tanto disfrutás de tocar un instrumento musical?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 28
    'Vas al ático a ver si estaban los instrumentos. Afortunadamente, siguen ahí. Como estás muy ocupado atendiendo gente, otra persona se ofreció a tocar música.\n¿Qué tanto te gusta ocuparte de los demás en el cumpleaños?\nResponde del 1-7 (1 siendo poco y 7 siendo mucho)',
    
    # 29
    'Se está haciendo tarde y es el momento de soplar las velas. El cumpleañero les agradece a todos por preparar la fiesta sorpresa, porque la disfrutó mucho y la pasó muy bien.\nFIN',]

lista_rtas =[]

for elemento in lista_historia:
    print(elemento)
    rta = input("ingrese su respuesta: ")
    while rta not in ["a","b","1","2","3","4","5","6","7"]:
        print("respuesta invalida, responder con lo pedido")
        print(elemento)
        rta = input("ingrese su respuesta: ")
    lista_rtas.append(rta)
    
# llamar a finales para imprimir el final

diccio_cont = clasif_rtas(lista_rtas, diccio_indice) #hacer diccio indice

max_raisec = 0
for claves in diccio_cont:
    if diccio_cont[clave] > max_raisec:
        max_raisec = diccio_cont[clave]
        diccio_max_raisec = {clave: max_raisec}

        






