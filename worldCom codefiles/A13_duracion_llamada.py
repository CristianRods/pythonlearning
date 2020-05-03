#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:08:52 2019

@author: Cristian
"""

import random
# importamos la libreria de random
import numpy as np
#importamos numpy
import datetime
from datetime import timedelta

# Si lo queremos generar uniformemente entre un minuto y una hora:

def duracion_call_unif(x,y):

    """ 
    Funcion que genera la duracion para cada llamada, siendo el numero de llamadas el rango que va x a y
    en nuestro caso sera de 0 a 5000 llamadas que se generar entre las 1 minutos - 1 hora y 0-59 segundos.
    
    Parameters
    ----------
    x= comienzo del intervalo
    y= final del intervalo
    
    Return
    ----------
    string
    una lista de y valores aleatorios que son duraciones de llamada en minutos y segundos. 
    
    Example - Para el ejercicio generaremos 1.
    -----
    duracioncallunif"(0,1)""
    
    '0:02:07 # # # '
    """

    duracall=[] #hora del establecimiento de la llamada
    for i in range(x,y):
        # si generasemos la duracion de la llamada uniformemente, se podria hacer de la siguiente manera
        duracion=timedelta(hours=(random.randint(0,1)),minutes=(random.randint(1,59)),seconds=(random.randint(0,59)))
        duracall.append(str(duracion)+" # ")
    return(str(duracall))



# Si lo generamos No uniforme y distribuida alrededor de 5 min.

def duracion_call_no_unif():
    """ 
    Funcion que genera la duracion para cada llamada, siendo el numero de llamadas '(y)',
    en nuestro caso sera de 5000 llamadas que se generaran con un valor central de 5 min y 0-59 segundos de manera 
    no uniforme.
    Ademas de graficar la distribucion de la frecuencia de los minutos de la llamada
    
    Parameters
    ----------
   	
    
    Return
    ----------
    string
    una lista de y valores aleatorios que son duraciones de llamada en minutos y segundos. 
    
    Example - Para el ejercicio generaremos 10:
    -----
    dura_call_no_unif"(0,10)""
    
     ['# 05:57 # ',
     ' # 05:15 # ',
     ' # 07:33 # ',
     ' # 06:19 # ',
     ' # 04:09 # ',
     ' # 07:11 # ',
     ' # 05:36 # ',
     ' # 06:54 # ',
     ' # 03:10 # ',
     ' # 03:00 # ',
     ' # 04:26 # ',
     ' # 05:39 # ',
     ' # 04:46 # ',
     ' # 04:59 # ',
     ' # 04:35 # ']
    """
    duracion=[]
    for i in range(1):
        dh=str(datetime.time(0,(np.random.poisson(lam=5)),(random.randint(0,59))))
        duracion.append(str(dh[3:]))
        
# Generamos graficos de todos los numeros generados aleatoriamente    
    #plt.hist(minu, bins=10, alpha=1, density=True, edgecolor = 'black',  linewidth=1)
    #plt.ylabel('frecuencia')
    #plt.xlabel('minutos')
    #plt.show()
    #plt.savefig('histograma.duracionllamada.jpg',bbox_inches='tight',dpi=300)
    print(type(duracion))
    return(duracion)

