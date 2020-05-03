#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:44:50 2019

@author: Cristian
"""

from mrjob.job import MRJob
import time
import math
import datetime


                                
## creamos una clase para contar con MrJobs
class MRminutosporPais (MRJob):
    """ 
    La calse MRminutosporPais contara los minutos totales en el fichero llamadas2020.txt
    de una forma mas eficiente. Por tanto, utilizando la metodologia MAPREDUCE
    podemos contar cuantas veces un pais llama a otro y sumar estos minutos.redondeados
    superiormente estos minutos se redondean con la funcion time.strptime
    
    Esta funcion se debe ejecutar en linea de comandos.
    
    Parameters
    ----------------------------
    la funcion necesita indicarsele que fichero va gestionar. En este caso:
    llamadas2020.txt. 
    Por tanto, se ejecuta como MRminutosporPais() llamadas2020.txt
    
    Return
    ---------------------------------
    Una lista de los valores de los minutos totales entre las parejas de paises
    pais que la emite y pais que la recibe. 
    
    
    
    Example
    ----------------
    >>> Python MRminutosporPais() llamadas2020.txt
    
    
    """
    def mapper(self, _,line):
        linea=line.split('#')
        letraemisor=linea[3][1]
        letrareceptor=linea[4][1]
        x=linea[2]
        x=x.strip()
        min_seg=(time.strptime(x,'%M:%S'))
        min_seg
        minutos_redondeados=math.ceil((datetime.timedelta(minutes=min_seg.tm_min,seconds=min_seg.tm_sec).
                                       total_seconds())/60)
        minutos_redondeados
        yield ("minutos totales:"+letraemisor+letrareceptor) ,minutos_redondeados
    
    
    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRminutosporPais.run()



