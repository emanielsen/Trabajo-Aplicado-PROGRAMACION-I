

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def diseño (diccio_cont,dataset_ganador, letra_ganadora):
    st.title("Dashboard RIASEC")
    
    
    
    
    nombres = {
        "R":"Realista",
        "I":"Investigador",
        "A":"Artístico",
        "S":"Social",
        "E":"Emprendedor",
        "C":"Convencional"}
    
    st.header(f"Tu personalidad profesional predominante es: {nombres[letra_ganadora]}")
    
    
    
    st.subheader("Carreras elegidas")
    
    fig1, ax1 = plt.subplots()
    
    ax1.pie(
        dataset_ganador["porcentaje_cantidad"],
        labels=dataset_ganador["carrera"],
        autopct="%1.1f%%")
    
    st.pyplot(fig1)
    
    
    
    st.subheader("Elección vs Satisfacción")
    
    fig2, ax2 = plt.subplots()
    
    ax2.plot(
        dataset_ganador["carrera"],
        dataset_ganador["porcentaje_cantidad"])
    
    ax2.plot(
        dataset_ganador["carrera"],
        dataset_ganador["promedio_satisfaccion"])
    
    ax2.legend([
        "Porcentaje de elección",
        "Satisfacción"])
    
    st.pyplot(fig2)
    
    
    st.subheader("Perfil RIASEC")
    
    categorias = list(diccio_cont.keys())
    valores = list(diccio_cont.values())
    
    angulos = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False)
    
    
    valores.append(valores[0])
    angulos = np.append(angulos, angulos[0])
    
    fig3, ax3 = plt.subplots(
        subplot_kw={"polar": True})
    
    ax3.plot(angulos, valores)
    
    ax3.fill(
        angulos,
        valores,
        alpha=0.25)
    
    ax3.set_xticks(angulos[:-1])
    ax3.set_xticklabels(categorias)
    
    st.pyplot(fig3)





