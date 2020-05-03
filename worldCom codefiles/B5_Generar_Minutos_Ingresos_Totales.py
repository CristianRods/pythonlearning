#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 00:23:24 2019

@author: Cristian
"""
import datetime
#importamos datetime 
import time
#importamos la funcion time
import math
#importamos la funcion math
import numpy as np
#importamos numpy
import pandas as pd
#importamos la libreria panda


def ingresos_totales():
    
    """ Esta funcion generara las matrices de duracion total de minutos
    y los ingresos de la empresa por pais en un matriz aplicando las tarifas
    de llamadas designadas en el fichero "tarifasllamdas2020.txt".
    Para ello multiplicara las tarifas de llamadas por las duraciones totales
    de las llamadas desde un pais a otro. 
    
    Parameters
    -----------------
    esta funcion no tiene parametros
    
    Return
    ------------------
    Dos ficheros que almacena las matrices de tiempo total en minutos y el 
    total de ingresos generados por las llamadas entre paises. 
    
    
    Example
    --------------------
   
    print(ingresos_totales)
   
    [[ 4538.7   247.   3691.8  5566.5   248.7]
     [  504.    487.2   650.4  1995.    418. ]
     [10714.2   559.8  9746.1  2648.4  5389.8]
     [ 5432.5  1195.6  7193.6  4184.   2178. ]
     [ 1927.2  1715.   4911.8  3074.5   612. ]]
    
    
    """
    # leer fichero con numpy   
    tarifas_llamadas=(np.loadtxt('tarifasllamadas2020.txt',delimiter="  ",usecols=(),dtype=float))
    
   
    #cargar fichero llamadas2020.txt en dataframe
    fichero_llamadas2020='llamadas2020.txt'
    cabeceras=['fecha_llamada','hora_llamada','duracion',"idEmisor","idReceptor","mensaje"]
    llamadas2020=pd.read_csv(fichero_llamadas2020,sep=" # ",names=cabeceras,header=None,engine='python')
    
    #llamadas2020.tail() si se quiere ver el fichero los ultimos elementos.
    """separamos en un nuevo dataframe los tres elementos que utilizaremos para construir nuestra matriz de llamadas
    totales.
    """ 
    #En primer lugar, separamos los elementos que necesitamos en un nuevo dataframe
    df_llamadas=(llamadas2020[['duracion','idEmisor','idReceptor']])
    
    #Almacenamos en una lista el tiempo redondeado
    
    tiempo_llamada=[]
    for registro_tiempo in df_llamadas.duracion:
        tiempo_llamada.append(registro_tiempo)
    df_tiempo=[]
    for tiempo in range(len(df_llamadas)):
        min_seg=(time.strptime(tiempo_llamada[tiempo],'%M:%S'))
        minutos_redondeados=math.ceil((datetime.timedelta(minutes=min_seg.tm_min,seconds=min_seg.tm_sec).total_seconds())
                                      /60)
        df_tiempo.append(minutos_redondeados)
    
    llamadas2020['duracion_minutos']= (df_tiempo)
    
    #--------------#
    
    #Almacenamos en otra lista la letra del codigo de la llamada
    
    df_emisor=[]
    lista_indices_df_llamadas=list(df_llamadas.index)
    for indice in lista_indices_df_llamadas:
        letra=df_llamadas.idEmisor[indice][0][0]
        df_emisor.append(letra)
    llamadas2020['pais_idEmisor']=(df_emisor)
    
    #"------------------"
    
    df_receptor=[]
    for indice in lista_indices_df_llamadas:
        letra=df_llamadas.idReceptor[indice][0][0]
        df_receptor.append(letra)
    llamadas2020['pais_idReceptor']=(df_receptor)
    
    #"------------------"
    
    print('Cuidado: Se han incorporado elementos nuevos al dataframe llamadas2020')
    llamadas2020.head()
    minutos_totales=llamadas2020.groupby(['pais_idEmisor','pais_idReceptor'],as_index = False).sum().pivot(
        'pais_idEmisor','pais_idReceptor')
   
    # generamos la matriz de minutos totales 
    minutos_totales=np.array(minutos_totales)
    
    #generamos la matriz de ingresos totales
    ingresos_totales=np.array(minutos_totales*tarifas_llamadas)
   
    #"-----------------------"
    # generar fichero en el disco 
    np.savetxt('ingresos_totales.txt',(ingresos_totales),delimiter="  ",fmt="%0.1f")
    
    
    #-------------------------#
    
    print("minutos totales:")
    print(minutos_totales)
    print("---------------")
    print("ingresos totales:")
    print(ingresos_totales)
if __name__ == '__main__':
    ingresos_totales()
