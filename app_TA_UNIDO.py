#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 23:11:51 2026

@author: emanielsen
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ==============================================================================
# --- 1. FUNCIONES ORIGINALES (Intactas) ---
# ==============================================================================

def filtrar_codigo(dataset):
    serie_letras = []
    for codigo in dataset["holland_code"]:
        primera_letra = codigo[0]
        serie_letras.append(primera_letra)
    return pd.Series(serie_letras)

def filtrar_dataset(dataset):
    nuevo_dataset = pd.DataFrame()
    for columna in dataset.columns:
        if columna == "id_persona":
            nuevo_dataset["id_persona"] = dataset["id_persona"]
        elif columna == "holland_code":
            nuevo_dataset["holland_code"] = filtrar_codigo(dataset)
        elif columna == "carrera_elegida":
            nuevo_dataset["carrera_elegida"] = dataset["carrera_elegida"]
        elif columna == "nivel_satisfaccion":
            nuevo_dataset["nivel_satisfaccion"] = dataset["nivel_satisfaccion"]
    return nuevo_dataset

@st.cache_data 
def procesar_excel():
    # Asegúrate de que la ruta al archivo excel sea correcta según tu repositorio
    dataset = pd.read_excel("data/base_datos_holland_carreras_5000.xlsx")
    nuevo_dataset = filtrar_dataset(dataset)
    return metricas(nuevo_dataset)

def metricas(nuevo_dataset):
    carreras_R, carreras_A, carreras_I, carreras_S, carreras_E, carreras_C = {}, {}, {}, {}, {}, {}
    satisfaccion_R, satisfaccion_A, satisfaccion_I, satisfaccion_S, satisfaccion_E, satisfaccion_C = {}, {}, {}, {}, {}, {}

    for i in range(len(nuevo_dataset)):
        fila = nuevo_dataset.iloc[i]
        personalidad = fila["holland_code"]
        carrera = fila["carrera_elegida"]
        nivel_sat = fila["nivel_satisfaccion"]

        for letra, dict_carreras, dict_satis in [
            ("R", carreras_R, satisfaccion_R), ("A", carreras_A, satisfaccion_A),
            ("I", carreras_I, satisfaccion_I), ("S", carreras_S, satisfaccion_S),
            ("E", carreras_E, satisfaccion_E), ("C", carreras_C, satisfaccion_C)
        ]:
            if letra in personalidad:
                if carrera in dict_carreras:
                    dict_carreras[carrera] += 1
                else:
                    dict_carreras[carrera] = 1
                
                if carrera in dict_satis:
                    dict_satis[carrera].append(nivel_sat)
                else:
                    dict_satis[carrera] = [nivel_sat]

    def armar_df(dict_carreras, dict_satis):
        total = sum(dict_carreras.values())
        filas = []
        if total == 0: return pd.DataFrame({"carrera":[], "porcentaje_cantidad":[], "promedio_satisfaccion":[]})
        for carrera, cantidad in dict_carreras.items():
            porcentaje = (cantidad / total) * 100
            promedio_satis = sum(dict_satis[carrera]) / len(dict_satis[carrera])
            filas.append({"carrera": carrera, "porcentaje_cantidad": porcentaje, "promedio_satisfaccion": promedio_satis})
        return pd.DataFrame(filas)

    dataset_R = armar_df(carreras_R, satisfaccion_R)
    dataset_A = armar_df(carreras_A, satisfaccion_A)
    dataset_I = armar_df(carreras_I, satisfaccion_I)
    dataset_S = armar_df(carreras_S, satisfaccion_S)
    dataset_E = armar_df(carreras_E, satisfaccion_E)
    dataset_C = armar_df(carreras_C, satisfaccion_C)

    return dataset_R, dataset_A, dataset_I, dataset_S, dataset_E, dataset_C

def rtas_A_B(list_rtas, i, cont, diccio_indice):
    for clave in diccio_indice:
        for valor in diccio_indice[clave]:
            if valor == i:
                if list_rtas[i] == "a":
                    cont[clave] += 3
    return cont

def sumar_autoestimacion(list_rtas, i, cont, diccio_indice):
    for clave in diccio_indice:
        for valor in diccio_indice[clave]:
            if valor == i:
                if list_rtas[i] == "1": cont[clave] += 1
                elif list_rtas[i] == "2": cont[clave] += 2
                elif list_rtas[i] == "3": cont[clave] += 3
                elif list_rtas[i] == "4": cont[clave] += 4
                elif list_rtas[i] == "5": cont[clave] += 5
                elif list_rtas[i] == "6": cont[clave] += 6
                elif list_rtas[i] == "7": cont[clave] += 7
    return cont

def clasif_rtas(list_rtas, diccio_indice):
    cont = {"R": 0, "A": 0, "I": 0, "S": 0, "E": 0, "C": 0}
    for i in range(len(list_rtas)):
        if list_rtas[i] is None:
            continue
        if i in [0,1,9,10,12,13,15,18,19,21,23,25]:
            cont = rtas_A_B(list_rtas, i, cont, diccio_indice)
        else:
            cont = sumar_autoestimacion(list_rtas, i, cont, diccio_indice)
    return cont

def diseño(diccio_cont, dataset_ganador, letra_ganadora): 
    nombres = {"R":"Realista", "I":"Investigador", "A":"Artístico", "S":"Social", "E":"Emprendedor", "C":"Convencional"}
    st.header(f"Tu personalidad predominante es: {nombres.get(letra_ganadora, letra_ganadora)}")
    
    st.subheader("Carreras elegidas")
    fig1, ax1 = plt.subplots()
    ax1.pie(dataset_ganador["porcentaje_cantidad"], labels=dataset_ganador["carrera"], autopct="%1.1f%%")
    st.pyplot(fig1)
    
    st.subheader("Elección vs Satisfacción")
    fig2, ax2 = plt.subplots()
    ax2.plot(dataset_ganador["carrera"], dataset_ganador["porcentaje_cantidad"], label="Porcentaje de elección")
    ax2.plot(dataset_ganador["carrera"], dataset_ganador["promedio_satisfaccion"], label="Satisfacción")
    ax2.legend()
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig2)
    
    st.subheader("Perfil RIASEC")
    categorias = list(diccio_cont.keys())
    valores = list(diccio_cont.values())
    angulos = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False)
    valores.append(valores[0])
    angulos = np.append(angulos, angulos[0])
    
    fig3, ax3 = plt.subplots(subplot_kw={"polar": True})
    ax3.plot(angulos, valores)
    ax3.fill(angulos, valores, alpha=0.25)
    ax3.set_xticks(angulos[:-1])
    ax3.set_xticklabels(categorias)
    st.pyplot(fig3)

# ==============================================================================
# --- 2. CONFIGURACIÓN INICIAL Y ESTADO DE SESIÓN ---
# ==============================================================================

st.set_page_config(page_title="Misión: Cumpleaños Sorpresa", layout="centered")

if 'configurado' not in st.session_state:
    st.session_state.configurado = False
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 0
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}
if 'nombres_amigos' not in st.session_state:
    st.session_state.nombres_amigos = {"amigo1": "", "amigo2": "", "amigo3": ""}

# ==============================================================================
# --- 3. PANTALLA INICIAL: REGISTRO DE NOMBRES ---
# ==============================================================================

if not st.session_state.configurado:
    st.title("🎬 Configuración de la Historia")
    st.write("Antes de empezar, introduce los nombres de tus amigos para personalizar la experiencia:")
    
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

# ==============================================================================
# --- 4. FLUJO PRINCIPAL DE LA HISTORIA Y RESULTADOS ---
# ==============================================================================
else:
    amigo1 = st.session_state.nombres_amigos["amigo1"]
    amigo2 = st.session_state.nombres_amigos["amigo2"]
    amigo3 = st.session_state.nombres_amigos["amigo3"]

    preguntas = [
        {"id": 0, "tipo": "opcion", "texto": f"{amigo1}, {amigo2}, {amigo3} y vos son un grupo de amigos. ¡El cumpleaños de {amigo3} es en 10 días! Estás pensando organizarle un cumpleaños a {amigo3}:\nPreferirías:", "opciones": [f"a) Organizarlo vos solo", f"b) Pedirle ayuda a {amigo1} y {amigo2}"]},
        {"id": 1, "tipo": "opcion", "texto": "Tus amigos se enteraron y te quieren ayudar\n¿Confias en vos mismo para empezar a organizarlo ahora y llegar con todo?", "opciones": ["a) Sí", "b) No"]},
        {"id": 2, "tipo": "escala", "texto": f"{amigo1} le contó a los papás de {amigo3} y ellos sugirieron arrancar hoy mismo!\nEntonces:\n¿Qué tanto preferís ser el responsable de la planificación de actividades?"},
        {"id": 3, "tipo": "escala", "texto": "¿Qué tanto te gustaría hacer una lluvia de ideas para planear la fiesta?"},
        {"id": 4, "tipo": "escala", "texto": "Tus amigos quieren sugerir ideas para el evento:\n¿Qué tan abierto estás a seguir las ideas de tus amigos?"},
        {"id": 5, "tipo": "escala", "texto": "En el caso que prefieras seguir tus propias ideas\n¿Qué tan bueno sos convenciendo a los demás sobre tu punto de vista?"},
        {"id": 6, "tipo": "escala", "texto": "Qué tan predispuesto/a estarías a cargar algo pesado que requiera fuerza para llevar al cumpleaños?"},
        {"id": 7, "tipo": "escala", "texto": f"A {amigo2} se le ocurrió algo para hacer:\n¿Qué tanto te gustaría que te especifiquen qué hacer de antemano?"},
        {"id": 8, "tipo": "escala", "texto": "Si, en cambio, son tus ideas las que se siguen\n¿Qué tanto te gusta dirigir a los demás?"},
        {"id": 9, "tipo": "opcion", "texto": "Si te encontras a cargo del evento\n¿Te gustaría poder chequear lo que hacen tus amigos para llegar a tiempo?", "opciones": ["a) Sí", "b) No"]},
        {"id": 10, "tipo": "opcion", "texto": f"{amigo1} está encargado de comprar la torta, pero sabés que es medio despistado,\n¿Preferís pensar en posibles problemas y pensar en sus soluciones?", "opciones": ["a) Sí", "b) No"]},
        {"id": 11, "tipo": "escala", "texto": "A la hora de pensar en un regalo,\n¿Qué tan probable es que le des un regalo hecho por vos?"},
        {"id": 12, "tipo": "opcion", "texto": "Si deciden regalar algo hecho por ustedes,\n¿Es probable que le prestes mucha atención a los detalles?", "opciones": ["a) Sí", "b) No"]},
        {"id": 13, "tipo": "opcion", "texto": f"¿Te gustaría dibujarle algo a {amigo3} como regalo?", "opciones": ["a) Sí", "b) No"]},
        {"id": 14, "tipo": "escala", "texto": "Suponiendo que les quede tiempo libre extra antes de que lleguen los invitados,\n¿Qué tanto te pondrías a leer un libro en ese tiempo muerto?"},
        {"id": 15, "tipo": "opcion", "texto": f"Se reparten tareas. {amigo1} y {amigo2} no tienen muy en claro cómo hacer su parte.\n¿Te molestaría explicarles cómo hacerlas?", "opciones": ["a) No", "b) Sí"]},
        {"id": 16, "tipo": "escala", "texto": "En caso que se rompa o dañe algún aparato u objeto en el cumpleaños,\n¿qué tan dispuesto/preparado estás para arreglarlo?"},
        {"id": 17, "tipo": "escala", "texto": "Qué tanto te propondrías reunir la información de las personas que asistirán al cumpleaños, para organizar a los invitados en una lista?"},
        {"id": 18, "tipo": "opcion", "texto": "Es el día del cumpleaños. Tus amigos y vos decidieron hacer la fiesta sorpresa en el patio de tu casa.\n¿Te gusta estar a diario al aire libre?", "opciones": ["a) Sí", "b) No"]},
        {"id": 19, "tipo": "opcion", "texto": "Notás que la organización de los preparativos podría ser más eficiente si alguno toma el rol de guiar o supervisar al resto.\nPreferís:", "opciones": ["a) Supervisar al resto", "b) Tener instrucciones claras que seguir"]},
        {"id": 20, "tipo": "escala", "texto": "Tu tarea consiste en poner la mesa, inflar globos y ordenar un poco tu patio.\n¿Qué tanto te gustaría hacer cada tarea con cuidado, paso a paso, incluso con el tiempo limitado?"},
        {"id": 21, "tipo": "opcion", "texto": "Tenés que ir a buscar los globos para inflar de tres colores distintos. Querés ponerlos usando la menor cantidad de globos.\n¿Te gusta este tipo de trabajo con números y eficiencia?", "opciones": ["a) Sí", "b) No"]},
        {"id": 22, "tipo": "escala", "texto": "Uno de tus amigos está colgando unas guirnaldas y no alcanza.\n¿Qué tanto considerás ayudar a tu amigo o asumís que se las puede arreglar solo?"},
        {"id": 23, "tipo": "opcion", "texto": "Deciden escribirle una cartita pegada al envoltorio del regalo.\n¿Se te da bien escribir este tipo de cosas?", "opciones": ["a) Sí", "b) No"]},
        {"id": 24, "tipo": "escala", "texto": "Llegan el cumpleañero y más amigos.\n¿Usualmente qué tan seguido inicias las conversaciones con la gente?"},
        {"id": 25, "tipo": "opcion", "texto": "El cumpleañero se está acercando al lugar donde escondieron su regalo.\n¿Se te da bien crear historias ficticias para improvisar y hacer que el regalo no sea descubierto?", "opciones": ["a) Sí", "b) No"]},
        {"id": 26, "tipo": "escala", "texto": "Se tropieza con el cable del parlante y se caen el parlante y el cumpleañero al piso.\n¿Qué tan bien se te da ocuparte de los demás?"},
        {"id": 27, "tipo": "escala", "texto": "Tu amigo está bien, pero el parlante no funciona. Proponen que alguien lo arregle.\n¿Qué tanto te gusta estar en un ambiente donde puedas resolver problemas mecánicos o reparar aparatos de este tipo?"},
        {"id": 28, "tipo": "escala", "texto": "Te acordás que en el ático de tu casa hay una guitarra vieja y un piano.\n¿Qué tanto disfrutás de tocar un instrumento musical?"},
        {"id": 29, "tipo": "escala", "texto": "Te avisan que varias guirnaldas se descolgaron y salieron volando por el viento.\n¿Qué tanto te propondrías a armar nuevas guirnaldas y a hacer manualidades?"}
    ]

    # --- LÓGICA DE DETECCIÓN DE FINALES Y DASHBOARD ---
    if st.session_state.pregunta_actual >= len(preguntas):
        st.title("🎉 ¡Misión Completada!")
        
        # Transformamos las respuestas al formato necesario para 'clasif_rtas()'
        list_rtas = []
        for i in range(30):
            rta = st.session_state.respuestas.get(i)
            if isinstance(rta, str):
                list_rtas.append(rta[0].lower()) 
            else:
                list_rtas.append(str(rta))       
        
        diccio_indice = {
            "R":[6,16,18,27,29],
            "A":[11,13,23,25,28],
            "I":[3,4,10,14,17],
            "S":[0,15,22,24,26],
            "E":[1,2,5,8,9],
            "C":[7,12,19,20,21]
        }
        
        # Procesamiento de Datos 
        diccio_cont = clasif_rtas(list_rtas, diccio_indice)
        letra_ganadora = max(diccio_cont, key=diccio_cont.get)
        
        datasets = procesar_excel()
        mapeo = {"R":0, "A":1, "I":2, "S":3, "E":4, "C":5}
        dataset_ganador = datasets[mapeo[letra_ganadora]]

        # Sistema de pestañas (Tabs)
        tab_historia, tab_dashboard = st.tabs(["📖 Desenlace de la Historia", "📊 Tu Dashboard RIASEC"])

        with tab_historia:
            rta_0 = st.session_state.respuestas.get(0, "")
            rta_19 = st.session_state.respuestas.get(19, "")
            trabajo_independiente = "solo" in rta_0
            trabajo_equipo = "ayuda" in rta_0
            liderar = "Supervisar" in rta_19
            seguir_instrucciones = "instrucciones" in rta_19

            if liderar and trabajo_independiente:
                st.subheader("Final 'Malo'")
                st.write("Te enfocaste mucho en mandar y dar indicaciones sobre cómo tenían que ser las cosas, pero preferiste trabajar solo. Hubo tensión con tus amigos.")
            elif seguir_instrucciones and trabajo_independiente:
                st.subheader("Final 'Malo'")
                st.write("Trabajaste mucho y no pudiste disfrutar tanto. Terminaste siguiendo instrucciones sin discutir en grupo. Quedaste frustrado y cansado.")
            elif liderar and trabajo_equipo:
                st.subheader("Final 'Bueno'")
                st.write("¡Tu organización quedó espectacular! Lograste coordinar con tus amigos, aportaron ideas y asumiste el rol de guía.")
            else:
                st.subheader("Final 'Bueno'")
                st.write("¡Tu capacidad de cooperación hizo que la fiesta saliera muy bien! Siguiendo las instrucciones de uno de tus amigos, te enfocaste en que tu parte saliera perfecta.")

            if st.button("Volver a jugar 🔄"):
                st.session_state.pregunta_actual = 0
                st.session_state.respuestas = {}
                st.session_state.configurado = False  
                st.rerun()

        with tab_dashboard:
            diseño(diccio_cont, dataset_ganador, letra_ganadora)

    # --- INTERFAZ DE PREGUNTAS ---
    else:
        st.title("🕵️‍ Misión: Cumpleaños Sorpresa")
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
                
            if st.form_submit_button('Siguiente pregunta ➡️'):
                st.session_state.respuestas[pregunta['id']] = respuesta_usuario
                st.session_state.pregunta_actual += 1
                st.rerun()