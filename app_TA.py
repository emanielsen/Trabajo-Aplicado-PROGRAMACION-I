#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:07:22 2026

@author: emanielsen
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# esto lo hice para probar y ver si me funciona el dashboard ya que tuve malas experiencias con esto
diccio_cont = {
    "R": 15,
    "A": 22,
    "I": 18,
    "S": 12,
    "E": 30,
    "C": 20}

diccio_max_raisec = {"E": 30}

dataset_ganador = pd.DataFrame({
    "carrera": ["Administración", "Marketing", "Economía"],
    "porcentaje_cantidad": [50, 30, 20],
    "promedio_satisfaccion": [85, 80, 75]})




st.title("Dashboard RIASEC")


letra_ganadora = list(diccio_max_raisec.keys())[0]

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





