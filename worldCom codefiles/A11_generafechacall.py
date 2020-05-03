#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:23:12 2019

@author: Cristian
"""

import random
# importamos la libreria de random


def generafechacall(y,z):
    
    """ 
    Funcion que genera fecha de establecimiento para cada llamada en un rango
    de y elementos en el primer trimestre del ano determinado 'z'. 
    
    Parameters
    ----------
    y= numero de elementos que se van generar
    z= ano sobre el que se quiere generar la muestra
    
    Return
    ----------
    string
    
    una lista de hasta "y" fechas aleatorios comprendidas entre el mes 1 y 3.
    para el ano que se determine como 'z'.
    
    Precondition
    ------------
    y > 0
    
    
    Example - Para el ejercicio generaremos 5000 ya que son las llamadas de la muestra
    -----
    
    #generafechacall(1,2020)
    '2020-03-25' # '
    
    
    """
    assert y > 0, "el numero de elementos a generar debe ser superior a 0"
    fechas=[]
    for i in range (y):
        
        codigo_mes=random.randint(1,3)
        if codigo_mes==2:
            codigo_dia=random.randint(1,29)
        else:
            codigo_dia=random.randint(1,30)
        if codigo_mes<=9:
            codigo_mes="0"+str(codigo_mes)
        else:
            codigo_mes
        if codigo_dia<=9:
            codigo_dia="0"+str(codigo_dia)
        else:
            codigo_dia
        fechas.append(str(z)+"-"+str(codigo_mes)+"-"+str(codigo_dia)+" # ")
    print(fechas)
    return(fechas)