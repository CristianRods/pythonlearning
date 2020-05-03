#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 20:23:59 2019

@author: Cristian
"""
from mrjob.job import MRJob

import time
import math
import datetime
import numpy as np

tarifas_llamadas=(np.loadtxt('tarifasllamadas2020.txt',delimiter="  ",usecols=(),dtype=float))
def buscar_indice(y):
    """
    La funcion buscar_indice nos ayudara a ubicar en una lista una letra y 
    devolver un valor que usaremos como indice. Esta funcion la usaremos como 
    puntero. 
    Parameters
    ----------------
    y='una letra'
    Return
    ----------------
    int
    nos sirve de indice para ubicar dentro de una lista de varios elementos 
    cual es el correspondiente a esa letra dada en el parametro
    
    """
    if y==("A"):
        return(0)
    if y==("B"):
        return(1)
    if y==("C"):
        return(2)
    if y==("D"):
        return(3)
    if y==("E"):
        return(4)
## creamos una clase para contar con MrJobs
class MRingresos_totales_porPais (MRJob):
    """ 
    La clase MRingresos_totales_porPais contara los minutos totales pero ademas 
    los multiplicara por el coste por minuto. Los minutos totales se recogen del
    fichero llamadas2020.txt y se redondean superiormente.
    Por tanto, utilizando la metodologia MAPREDUCE, vamos a sumar los minutos
    y multiplicarlos por las tarifas correspondientes a cada pais cuando llama.
    
    Estos minutos se redondean con la funcion time.strptime y los costes los 
    sacamos con la funcion buscar_indice(y).
    
    Esta funcion se debe ejecutar en linea de comandos.
    
    Parameters
    ----------------------------
    la funcion necesita indicarsele que fichero va gestionar. En este caso:
    llamadas2020.txt. 
    Por tanto, se ejecuta como MRingresos_totales_porPais() llamadas2020.txt
    
    Return
    ---------------------------------
    Una lista de los valores de los minutos totales entre las parejas de paises
    pais que la emite y pais que la recibe. 
    
    
    
    Example
    ----------------
    >>> Python MRingresos_totales_porPais() llamadas2020.txt
    """
            
            
    def mapper(self, _,line):
        linea=line.split('#')
        letraemisor=linea[3][1]
        letrareceptor=linea[4][1]
        minutos_line=linea[2]
        minutos=minutos_line.strip()
        min_seg=(time.strptime(minutos,'%M:%S'))
        min_seg
        minutos_redondeados=math.ceil((datetime.timedelta(minutes=min_seg.tm_min,
                                                          seconds=min_seg.tm_sec).total_seconds())/60)
        minutos_redondeados
        indice_emisor=buscar_indice(letraemisor)
        indice_receptor=buscar_indice(letrareceptor)
        tarifas=tarifas_llamadas[indice_emisor][indice_receptor]
        yield (letraemisor+letrareceptor) ,minutos_redondeados*tarifas
    
    
    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRingresos_totales_porPais.run()