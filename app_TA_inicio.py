
import streamlit as st

# --- 1. CONFIGURACIÓN INICIAL Y ESTADO DE SESIÓN ---
st.set_page_config(page_title="Historia Interactiva - Test Holland", layout="centered")

# Inicializamos las variables de estado si es la primera vez que se carga la página
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 0
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {} # Diccionario para guardar {id_pregunta: respuesta}

# --- 2. DEFINICIÓN DE LAS PREGUNTAS ---
# Mantenemos el orden estricto de los archivos. 
# Nota: Completa las preguntas intermedias (del 1 al 17) siguiendo este mismo formato.
preguntas = [
    {
        "id": 0, 
        "tipo": "opcion",
        "texto": "¡El cumpleaños de tu amigo es en 10 días! Estás pensando organizarle un cumpleaños. Preferirías:", 
        "opciones": ["a) Organizarlo vos solo", "b) Pedirle ayuda a tus otros amigos"]
    },
    {
        "id": 1, 
        "tipo": "opcion",
        "texto": "Tus amigos se enteraron y te quieren ayudar. ¿Confías en vos mismo para empezar a organizarlo ahora y llegar con todo?", 
        "opciones": ["a) Sí", "b) No"]
    },
    {
        "id": 2, 
        "tipo": "escala",
        "texto": "¿Qué tanto preferís ser el responsable de la planificación de actividades?", 
        "min": 1, "max": 7
    },
    # ... [AGREGA AQUÍ LAS PREGUNTAS DE LA 3 A LA 17] ...
    {
        "id": 18, 
        "tipo": "opcion",
        "texto": "Durante el evento, a la hora de manejar los imprevistos y coordinar, descubres que prefieres:", 
        "opciones": ["a) Liderar la situación", "b) Tener instrucciones claras que seguir"]
    }
]

# --- 3. LÓGICA DE LOS FINALES ---
def mostrar_final():
    st.title("🎂 El desenlace de la fiesta...")
    
    # Obtenemos las respuestas clave
    rta_0 = st.session_state.respuestas.get(0)
    rta_18 = st.session_state.respuestas.get(18)
    
    # Traducimos las respuestas a las variables de la historia
    trabajo_independiente = "solo" in rta_0
    trabajo_equipo = "ayuda" in rta_0
    
    liderar = "Liderar" in rta_18
    seguir_instrucciones = "instrucciones" in rta_18

    st.markdown("---")
    
    # 1) Final Malo: Liderar + Independiente
    if liderar and trabajo_independiente:
        st.subheader("Final 'Malo' (Te gusta liderar y trabajar de manera independiente)")
        st.write("Te enfocaste mucho en mandar y dar indicaciones sobre cómo tenían que ser las cosas, pero como preferías trabajar por tu cuenta, no dejaste que los demás aportaran ideas. Al final, lograste hacer todo, pero hubo mucha tensión con tus amigos. El cumpleañero se divirtió, pero el grupo quedó un poco peleado.")
    
    # 2) Final Malo: Instrucciones + Independiente
    elif seguir_instrucciones and trabajo_independiente:
        st.subheader("Final 'Malo' (Te gusta tener instrucciones claras y trabajar de manera independiente)")
        st.write("Trabajaste mucho y no pudiste disfrutar tanto de la fiesta como tus amigos. Terminaste siguiendo todas las instrucciones que te proponían, sin discutir las cosas en grupo, ya que preferiste trabajar de manera independiente. Al final, el cumpleañero disfrutó de la fiesta pero quedaste frustrado y cansado.")
        
    # 3) Final Bueno: Liderar + Equipo
    elif liderar and trabajo_equipo:
        st.subheader("Final 'Bueno' (Te gusta liderar y trabajar en equipo)")
        st.write("¡Tu organización del cumpleaños quedó espectacular! Lograste coordinar con tus amigos para que todos aportaran ideas y rápidamente asumiste el rol de guía. Gracias a tu capacidad de liderazgo, tus amigos colaboraron de manera equitativa. ¡El cumpleañero disfrutó mucho su fiesta sorpresa!")
        
    # 4) Final Bueno: Instrucciones + Equipo
    elif seguir_instrucciones and trabajo_equipo:
        st.subheader("Final 'Bueno' (Te gusta tener instrucciones claras y trabajar en equipo)")
        st.write("¡Tu capacidad de cooperación con tus amigos hizo que la fiesta saliera muy bien! Al preferir seguir las instrucciones que proponía uno de tus amigos, te enfocaste en que tu parte saliera perfecta. Lograste cooperar con el resto para que, a pesar de las dificultades, ¡el cumpleañero disfrutara de su fiesta sorpresa!")
    
    st.markdown("---")
    if st.button("Volver a jugar"):
        st.session_state.pregunta_actual = 0
        st.session_state.respuestas = {}
        st.rerun()

# --- 4. INTERFAZ PRINCIPAL ---
st.title("🕵️‍♂️ Misión: Cumpleaños Sorpresa")

# Verificamos si ya terminamos todas las preguntas
if st.session_state.pregunta_actual >= len(preguntas):
    mostrar_final()
else:
    # Mostramos la pregunta actual
    pregunta = preguntas[st.session_state.pregunta_actual]
    
    st.progress((st.session_state.pregunta_actual) / len(preguntas), text=f"Pregunta {pregunta['id']} de {preguntas[-1]['id']}")
    
    st.write(f"### {pregunta['texto']}")
    
    # Formulario para evitar recargas hasta que el usuario haga clic en "Siguiente"
    with st.form(key=f"form_{pregunta['id']}"):
        
        # Renderizamos el input correcto según el tipo de pregunta
        if pregunta['tipo'] == "opcion":
            respuesta_usuario = st.radio("Selecciona tu respuesta:", pregunta['opciones'])
        elif pregunta['tipo'] == "escala":
            respuesta_usuario = st.slider("Del 1 al 7:", min_value=pregunta['min'], max_value=pregunta['max'], value=4)
            
        submit_button = st.form_submit_button(label='Siguiente ➡️')
        
        if submit_button:
            # Guardamos la respuesta en el historial
            st.session_state.respuestas[pregunta['id']] = respuesta_usuario
            # Avanzamos a la siguiente pregunta
            st.session_state.pregunta_actual += 1
            # Recargamos la app para mostrar la siguiente pantalla
            st.rerun()