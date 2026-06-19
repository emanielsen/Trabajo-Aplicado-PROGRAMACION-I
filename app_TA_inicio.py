
import streamlit as st

# --- 1. CONFIGURACIÓN INICIAL Y ESTADO DE SESIÓN ---
st.set_page_config(page_title="Misión: Cumpleaños Sorpresa", layout="centered")

# Inicializamos las variables de estado si es la primera vez que se carga la app
if 'configurado' not in st.session_state:
    st.session_state.configurado = False
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 0
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}
if 'nombres_amigos' not in st.session_state:
    st.session_state.nombres_amigos = {"amigo1": "", "amigo2": "", "amigo3": ""}

# --- 2. PANTALLA INICIAL: REGISTRO DE NOMBRES EN EL DASHBOARD ---
if not st.session_state.configurado:
    st.title("🎬 Configuración de la Historia")
    st.write("Antes de empezar, introduce los nombres de tus amigos para personalizar la experiencia:")
    
    # Formulario en el dashboard para capturar los nombres de una sola vez
    with st.form(key="form_nombres"):
        nom1 = st.text_input("Nombre del primer amigo (Amigo 1):", value="Tomás")
        nom2 = st.text_input("Nombre del segundo amigo (Amigo 2):", value="Lucas")
        nom3 = st.text_input("Nombre del cumpleañero (Amigo 3):", value="Mateo")
        
        boton_guardar = st.form_submit_button("Comenzar Historia 🚀")
        
        if boton_guardar:
            if nom1.strip() == "" or nom2.strip() == "" or nom3.strip() == "":
                st.error("Por favor, completa todos los nombres para poder continuar.")
            else:
                st.session_state.nombres_amigos["amigo1"] = nom1
                st.session_state.nombres_amigos["amigo2"] = nom2
                st.session_state.nombres_amigos["amigo3"] = nom3
                st.session_state.configurado = True
                st.rerun()

# --- 3. FLUJO PRINCIPAL DE LA HISTORIA ---
else:
    # Recuperamos los nombres guardados en la sesión para usarlos en los f-strings
    amigo1 = st.session_state.nombres_amigos["amigo1"]
    amigo2 = st.session_state.nombres_amigos["amigo2"]
    amigo3 = st.session_state.nombres_amigos["amigo3"]

    # Definición de las 30 preguntas utilizando las variables locales ya cargadas
    preguntas = [
        {
            "id": 0,
            "tipo": "opcion",
            "texto": f"{amigo1}, {amigo2}, {amigo3} y vos son un groupo de amigos. ¡El cumpleaños de {amigo3} es en 10 días! Estás pensando organizarle un cumpleaños a {amigo3}:\nPreferirías:",
            "opciones": [f"a) Organizarlo vos solo", f"b) Pedirle ayuda a {amigo1} y {amigo2}"]
        },
        {
            "id": 1,
            "tipo": "opcion",
            "texto": "Tus amigos se enteraron y te quieren ayudar (Tus amigos justo tuvieron la misma idea, y también quieren hacer una fiesta sorpresa)\n¿Confias en vos mismo para empezar a organizarlo ahora y llegar con todo? (aunque no falte tanto para la fecha)?",
            "opciones": ["a) Sí", "b) No"]
        },
        {
            "id": 2,
            "tipo": "escala",
            "texto": f"{amigo1} le contó a los papás de {amigo3} y ellos sugirieron arrancar hoy mismo!\nEntonces:\n¿Qué tanto preferís ser el responsable de la planificación de actividades?",
        },
        {
            "id": 3,
            "tipo": "escala",
            "texto": "¿Qué tanto te gustaría hacer una lluvia de ideas para planear la fiesta?",
        },
        {
            "id": 4,
            "tipo": "escala",
            "texto": "Tus amigos quieren sugerir ideas para el evento:\n¿Qué tan abierto estás a seguir las ideas de tus amigos?\n(Nota: 1 siendo mucho y 7 siendo que prefieres seguir tus ideas propias)",
        },
        {
            "id": 5,
            "tipo": "escala",
            "texto": "En el caso que prefieras seguir tus propias ideas (responder 1 si no fue el caso)\n¿Qué tan bueno sos convenciendo a los demás sobre tu punto de vista?",
        },
        {
            "id": 6,
            "tipo": "escala",
            "texto": "Qué tan predispuesto/a estarías a cargar algo pesado que requiera fuerza para llevar al cumpleaños?",
        },
        {
            "id": 7,
            "tipo": "escala",
            "texto": f"A {amigo2} se le ocurrió algo para hacer:\n¿Qué tanto te gustaría que te especifiquen qué hacer de antemano?",
        },
        {
            "id": 8,
            "tipo": "escala",
            "texto": "Si, en cambio, son tus ideas las que se siguen (responder 1 si no fue el caso),\n¿Qué tanto te gusta dirigir a los demás?",
        },
        {
            "id": 9,
            "tipo": "opcion",
            "texto": "Si te encontras a cargo del evento (responder 1 si no fue el caso)\n¿Te gustaría poder chequear lo que hacen tus amigos para llegar a tiempo?",
            "opciones": ["a) Sí", "b) No"]
        },
        {
            "id": 10,
            "tipo": "opcion",
            "texto": f"{amigo1} está encargado de comprar la torta, pero sabés que es medio despistado,\n¿Preferís pensar en posibles problemas (como que se olvide de comprarla) y pensar en sus soluciones?",
            "opciones": ["a) Sí", "b) No"]
        },
        {
            "id": 11,
            "tipo": "escala",
            "texto": "A la hora de pensar en un regalo,\n¿Qué tan probable es que le des un regalo hecho por vos (alguna manualidad)?",
        },
        {
            "id": 12,
            "tipo": "opcion",
            "texto": "Si deciden regalar algo hecho por ustedes (responder 1 si no fue el caso),\n¿Es probable que le prestes mucha atención a los detalles?",
            "opciones": ["a) Sí", "b) No"]
        },
        {
            "id": 13,
            "tipo": "opcion",
            "texto": f"¿Te gustaría dibujarle algo a {amigo3} como regalo?",
            "opciones": ["a) Sí", "b) No"]
        },
        {
            "id": 14,
            "tipo": "escala",
            "texto": "Suponiendo que les quede tiempo libre extra antes de que lleguen los invitados,\n¿Qué tanto te pondrías a leer un libro en ese tiempo muerto?",
        },
        {
            "id": 15,
            "tipo": "opcion",
            "texto": f"Como regalarle a {amigo3} algo hecho por ustedes es mucho trabajo, se reparten tareas.\n{amigo1} y {amigo2} no tienen muy en claro cómo hacer su parte.\n¿Te molestaría explicarles cómo hacerlas?",
            "opciones": ["a) No", "b) Sí"]
        },
        {
            "id": 16,
            "tipo": "escala",
            "texto": "En caso que se rompa o dañe algún aparato u objeto en el cumpleaños,\n¿qué tan dispuesto/preparado estás para arreglarlo?",
        },
        {
            "id": 17,
            "tipo": "escala",
            "texto": "Qué tanto te propondrías reunir la información de las personas que asistirán al cumpleaños, para organizar a los invitados en una lista?",
        },
        {
            "id": 18,
            "tipo": "opcion",
            "texto": "Es el día del cumpleaños. Tus amigos y vos decidieron hacer la fiesta sorpresa en el patio de tu casa, por mayoría de votación.\n¿Te gusta estar a diario al aire libre?",
            "opciones": ["a) Sí", "b) No"]
        },
        {
            "id": 19,
            "tipo": "opcion",
            "texto": "Notás que la organización de los preparativos podría ser más eficiente si alguno toma el rol de guiar o supervisar al resto, ya que hay poco tiempo y mucho para hacer.\nPreferís:",
            "opciones": ["a) Supervisar al resto", "b) Tener instrucciones claras que seguir"]
        },
        {
            "id": 20,
            "tipo": "escala",
            "texto": "Tu tarea consiste en poner la mesa, inflar globos y ordenar un poco tu patio. Son bastantes cosas que hacer en poco tiempo.\n¿Qué tanto te gustaría hacer cada tarea con cuidado, paso a paso, incluso con el tiempo limitado?",
        },
        {
            "id": 21,
            "tipo": "opcion",
            "texto": "Tenés que ir a buscar los globos para inflar de tres colores distintos. Te das cuenta que no hay cantidades iguales de cada color. Querés ponerlos a cierta distancia, llenando las paredes o postes donde podés colocarlos, usando la menor cantidad de globos.\n¿Te gusta este tipo de trabajo con números y eficiencia?",
            "opciones": ["a) Sí", "b) No"]
        },
        {
            "id": 22,
            "tipo": "escala",
            "texto": "Empiezan a organizar los preparativos, y uno de tus amigos está colgando unas guirnaldas. Ves que no está alcanzando a colgarlas, porque es más bajo. Podrías ayudarlo ahora, pero aún tenés mucho que hacer por tu parte.\n¿Qué tanto considerás ayudar a tu amigo o, en cambio, asumís que se las puede arreglar solo?",
        },
        {
            "id": 23,
            "tipo": "opcion",
            "texto": "Con tus amigos deciden escribirle una cartita o dedicatoria pegada al envoltorio del regalo. Alguien debe encargarse de eso.\n¿Se te da bien escribir este tipo de cosas?",
            "opciones": ["a) Sí", "b) No"]
        },
        {
            "id": 24,
            "tipo": "escala",
            "texto": "Terminan de preparar todo para la fiesta y ya se hace la hora del cumpleaños. Llegan el cumpleañero y más amigos.¿Usualmente qué tan seguido inicias las conversaciones con la gente?",
        },
        {
            "id": 25,
            "tipo": "opcion",
            "texto": "Te das cuenta que el cumpleañero se está acercando al lugar donde escondieron su regalo para dárselo después. Rápidamente debés improvisar para dirigirlo hacia otro lado, así no se da cuenta de la sorpresa.\n¿Se te da bien crear historias ficticias para, en este caso, improvisar y hacer que el regalo no sea descubierto?",
            "opciones": ["a) Sí", "b) No"]
        },
        {
            "id": 26,
            "tipo": "escala",
            "texto": "Afortunadamente, lograste disuadir al cumpleañero. Pero al volver, se tropieza con el cable del parlante, entonces se caen el parlante y el cumpleañero al piso. Rápidamente van con dos amigos a ver si está bien.\n¿Qué tan bien se te da ocuparte de los demás?",
        },
        {
            "id": 27,
            "tipo": "escala",
            "texto": "Por suerte, tu amigo apenas se raspó y está bien. El que no está bien es el parlante, que ahora no funciona. Entonces proponen que alguien lo arregle para que la fiesta no se quede sin música.\n¿Qué tanto te gusta estar en un ambiente donde puedas resolver problemas mecánicos o reparar aparatos de este tipo?",
        },
        {
            "id": 28,
            "tipo": "escala",
            "texto": "Aunque intentan arreglarlo, no lo logran. Te acordás que en el ático de tu casa hay una guitarra vieja y un piano. Podría alguien (o vos mismo) animarse a tocar un instrumento.\n¿Qué tanto disfrutás de tocar un instrumento musical?",
        },
        {
            "id": 29,
            "tipo": "escala",
            "texto": "Vas al ático a ver si estaban los instrumentos. Afortunadamente, siguen ahí. Otra persona se ofreció a tocar música, ya que te avisaron que varias guirnaldas se descolgaron y salieron volando por el viento.\n¿Qué tanto te propondrías a armar nuevas guirnaldas y a hacer manualidades?",
        }
    ]

    # --- 4. LÓGICA DE DETECCIÓN DE FINALES (Basado en Pregunta 0 y 19) ---
    def mostrar_final():
        st.title("🎂 El desenlace de la fiesta...")
        
        rta_0 = st.session_state.respuestas.get(0)
        rta_19 = st.session_state.respuestas.get(19)
        
        trabajo_independiente = "solo" in rta_0
        trabajo_equipo = "ayuda" in rta_0
        
        liderar = "Supervisar" in rta_19
        seguir_instrucciones = "instrucciones" in rta_19

        st.markdown("---")
        
        if liderar and trabajo_independiente:
            st.subheader("Final 'Malo' (Te gusta liderar y trabajar de manera independiente)")
            st.write("Te enfocaste mucho en mandar y dar indicaciones sobre cómo tenían que ser las cosas, pero como preferías trabajar por tu cuenta, no dejaste que los demás aportaran ideas. Al final, lograste hacer todo, pero hubo mucha tensión con tus amigos. El cumpleañero se divirtió, pero el grupo quedó un poco peleado.")
        
        elif seguir_instrucciones and trabajo_independiente:
            st.subheader("Final 'Malo' (Te gusta tener instrucciones claras y trabajar de manera independiente)")
            st.write("Trabajaste mucho y no pudiste disfrutar tanto de la fiesta como tus amigos. Terminaste siguiendo todas las instrucciones que te proponían, sin discutir las cosas en grupo, ya que preferiste trabajar de manera independiente. Al final, el cumpleañero disfrutó de la fiesta pero quedaste frustrado y cansado.")
            
        elif liderar and trabajo_equipo:
            st.subheader("Final 'Bueno' (Te gusta liderar y trabajar en equipo)")
            st.write("¡Tu organización del cumpleaños quedó espectacular! Lograste coordinar con tus amigos para que todos aportaran ideas y rápidamente asumiste el rol de guía. Gracias a tu capacidad de liderazgo, tus amigos colaboraron de manera equitativa. ¡El cumpleañero disfrutó mucho su fiesta sorpresa!")
            
        elif seguir_instrucciones and trabajo_equipo:
            st.subheader("Final 'Bueno' (Te gusta tener instrucciones claras y trabajar en equipo)")
            st.write("¡Tu capacidad de cooperación con tus amigos hizo que la fiesta saliera muy bien! Al preferir seguir las instrucciones que proponía uno de tus amigos, te enfocaste en que tu parte saliera perfecta. Lograste cooperar con el resto para que, a pesar de las dificultades, ¡el cumpleañero disfrutara de su fiesta sorpresa!")
        
        st.markdown("---")
        if st.button("Volver a jugar 🔄"):
            st.session_state.pregunta_actual = 0
            st.session_state.respuestas = {}
            st.session_state.configurado = False  # Para permitir cambiar nombres al reiniciar
            st.rerun()

    # --- 5. INTERFAZ PRINCIPAL DE LAS PREGUNTAS ---
    st.title("🕵️‍♂️ Misión: Cumpleaños Sorpresa")

    if st.session_state.pregunta_actual >= len(preguntas):
        mostrar_final()
    else:
        pregunta = preguntas[st.session_state.pregunta_actual]
        
        progreso = st.session_state.pregunta_actual / len(preguntas)
        st.progress(progreso, text=f"Progreso de la historia: Pregunta {pregunta['id']} de 29")
        
        st.markdown("---")
        st.write(f"### {pregunta['texto']}")
        
        with st.form(key=f"form_preg_{pregunta['id']}"):
            if pregunta['tipo'] == "opcion":
                respuesta_usuario = st.radio("Selecciona una opción:", pregunta['opciones'])
            elif pregunta['tipo'] == "escala":
                respuesta_usuario = st.slider("Responde del 1 al 7 (1: poco, 7: mucho):", min_value=1, max_value=7, value=4)
                
            submit_button = st.form_submit_button(label='Siguiente pregunta ➡️')
            
            if submit_button:
                st.session_state.respuestas[pregunta['id']] = respuesta_usuario
                st.session_state.pregunta_actual += 1
                st.rerun()