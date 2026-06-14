# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 15:28:49 2026

@author: Tomas Lopez Durand
"""

def rtas_A_B():
    pass

def sumar_autoestimacion():
    pass

def clasif_rtas(list_rtas, diccio_indice):
    cont = {"R": 0, "A": 0, "I": 0, "S": 0, "E": 0, "C": 0}
    for i in range(len(list_rtas)):
        if i == 0:#posición
            cont = rtas_A_B(cont, diccio_indice)
        else:
            cont = sumar_autoestimacion(cont, diccio_indice)
    return cont