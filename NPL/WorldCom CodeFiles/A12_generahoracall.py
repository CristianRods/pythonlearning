#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 16:28:07 2019

@author: Cristian
"""

from datetime import timedelta
#importamos datetime y timedelta
import random
# importamos la libreria de random

def generahoracall(x,y):

    """ 
    Funcion que genera la hora de establecimiento para cada llamada desde x a y
    en nuestro caso sera de 0 a 5000 llamadas que se generar entre las 8 y 23 horas.
    
    Parameters
    ----------
    x= comienzo del intervalo
    y= final del intervalo
    
    Return
    ----------
    string
    un rango de 5000 valores aleatorios con la hora el establecimiento de llamada entre los valores de 8 y 23 horas 
    y 0-50 minutos
    
    Example - Para el ejercicio generaremos 5000 ya que son las llamadas de la muestra
    -----
    
    #generahoracall(0,1)
    10:50 # '
    """
    
    horacall=[] #hora del establecimiento de la llamada
    for i in range(x,y):
        # generamos la hora de establecimiento de llamada
        horasllam=timedelta(hours=(random.randint(8,23)),minutes=(random.randint(0,59))) 
        horas=(str(horasllam))
        hora_llamada=horas[0:5] #limpiamos los segundos, siguiendo el formato de la descripcion del ejercicio
        horacall.append(hora_llamada+" # ")
    return(horacall)
