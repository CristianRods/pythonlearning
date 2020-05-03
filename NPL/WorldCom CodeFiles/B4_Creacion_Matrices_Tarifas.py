#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 23:48:09 2019

@author: Cristian
"""
import random
# importamos la libreria de random
import numpy as np
#importamos numpy


def generar_matrices_tarifas():
    
    """
    la función generara dos ficheros en disco. El primero corresponde
    a la renta per capita de cada pais, 'RentaperCapita_Paises' y el segundo
    a una matriz 5x5 con las tarifas de llamadas de cada pais a los otros que 
    hemos recogido en el fichero.
    Posteriormente, el programa carga los ichero como dos arrays para ser utilizados
    mas adelante.
    
    Parameters
    ----------------------------
    none
    
    Return
    ---------------------------------
    fichero
    
    se almacenan los ficheros descritos con un array 2x5 y otro 5x5.
    
    Example
    ----------------
    >>> generar_matrices_tarifas()
    
    [['A' 'B' 'C' 'D' 'E']
     ['2300' '1000' '2000' '1500' '2300']]
    [[1.9 3.6 0.3 3.3 2.6]
     [4.3 2.3 0.6 4.1 2.6]
     [0.3 2.3 2.9 3.1 4. ]
     [4.9 0.8 5.  4.2 2.3]
     [3.6 3.4 4.3 3.1 2.6]] 
    
    
    """

    #crear matriz y guardar en fichero con dos arrays una para los nombres de paises y otra para la 	renta per capita
    paises=np.array(['A', 'B', 'C', 'D', 'E'])
    renta_per_capita=np.array([2300,1000,2000,1500,1750], dtype=object)
    
    #Generar una matriz 5x5 con las tarifas de llamada
    tarifas=np.array([],dtype=float)
    paises=np.array(['A', 'B', 'C', 'D', 'E'])
    while len(tarifas)<=24:
        tarifa=(round(random.uniform(0.1,5),2))
        tarifas=np.append(tarifas,[[tarifa]])
    tarifas=tarifas.reshape(5,5)
    
    #Guardamos matrices en ficheros
    rentapercapita_datos = (paises, renta_per_capita)
    np.savetxt('RentaperCapita_Paises.csv',(rentapercapita_datos),delimiter=' ',fmt='%s')
    np.savetxt('tarifasllamadas2020.txt',(tarifas),delimiter="  ",fmt="%f")
   
    return(print(tarifas))
    
if __name__== '__main__':
    generar_matrices_tarifas()