#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 01:24:40 2019

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
import matplotlib.pyplot as plt
#importamos matplotlib.pyplot para poder realizar los graficos

def Totales_marginales():
    """
    la funcion generara los totales marginales de las llamadas. 
    Generando un Dataframe para los minutos de las llamadas desde cada pais y tambien para los minutos 
    de las llamadas que han recibido cada uno, respectivamente desde el pais A hasta E.
    Posteriormente, se analiza los minutos totales por pais y minutos totales generados en todas las llamadas
    por los que la compania ha prestado sus servicios.
    
    Posteriormente, asociamos los costes generados en la matriz de tarifas de llamadas a los minutos generados
    por cada pais cuando ha realizado una llamada, dandonos el coste total soportado por cada pais.
    
    Por ultimo, graficos sobre estos totales marginales de minutos de las llamadas, el reparto de minutos 
    totales generados por cada pais y el coste de cada uno. 
    
    Parameters
    ----------------------------
    none
    
    Return
    ---------------------------------
    Dataframes con minutos totales pais Emisor/ Receptor, total minutos por pais, total minutos de duracion
    de todas las llamadas.
    Arrays
    Coste por minuto por pais desde A a E
    Costes totales por pais desde A hasta E.
    Graficos
    
    Example
    ----------------
    >>> Totales_marginales()

    totales marginales de minutos por pais, llamadas emitidas y recibidas:
    pais_idEmisor
    A     6848
    B     2459
    C    11250
    D     5630
    E     3804
    Name: duracion_minutos, dtype: int64
    ---------------------------
    pais_idReceptor
    A     7220
    B     2152
    C    11317
    D     5792
    E     3510
    Name: duracion_minutos, dtype: int64
    total de minutos por pais:
      Pais  duracion_minutos
    0    A             14068
    1    B              4611
    2    C             22567
    3    D             11422
    4    E              7314
    ---------------------------
    Minutos totales en fichero:
         duracion_minutos
    sum             29991
    --------------------
    costes minuto por pais:
     [[13.3 14.4 11.2  9.6 17.2]]
    ----------------
    costes totales por pais
    [[ 91078.4  35409.6 126000.   54048.   65428.8]]
    """
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

    #-------------------------#
    print('Cuidado: Se han incorporado elementos nuevos al dataframe llamadas2020')

    #total marginal de minutos desde un pais a los otros
    total_llamadas_recibidas_Pais=llamadas2020.groupby(['pais_idReceptor'])['duracion_minutos'].sum()
    total_llamadas_emitidas_Pais=llamadas2020.groupby(['pais_idEmisor'])['duracion_minutos'].sum()
    print("totales marginales de minutos por pais, llamadas emitidas y recibidas:")

    print(total_llamadas_emitidas_Pais)
    print("---------------------------")
    print(total_llamadas_recibidas_Pais)
    #-----------------#
    
    #minutos totales por pais
    paises=np.array(['A', 'B', 'C', 'D', 'E'])
    total_flujo_llam_pais=(llamadas2020.groupby('pais_idEmisor')
                           ['duracion_minutos'].sum().
                           reset_index())+(llamadas2020.groupby('pais_idReceptor')
                                           ['duracion_minutos'].sum().reset_index())
    total_flujo_llam_pais=total_flujo_llam_pais.drop(['pais_idEmisor','pais_idReceptor'],axis=1)
    total_flujo_llam_pais.insert(0,"Pais", paises)
    total_flujo_llam_pais
    print("total de minutos por pais:")
    print(total_flujo_llam_pais)
    print("---------------------------")
    
    
    #--------------#
    total_minutos_porpais=llamadas2020.agg({"duracion_minutos" : ["sum"]}, axis='rows')
    #llamadas2020.agg({"duracion_minutos" : ["sum"]})
    #total_minutos_totales_array=np.array(total_minutos_totales)
    print("Minutos totales en fichero:")
    print(total_minutos_porpais)
    print('----------------')
    #-----------------#
    
    
    #creamos el array de costes totales
        # leer fichero con numpy   
    tarifas_llamadas=(np.loadtxt('tarifasllamadas2020.txt',delimiter="  ",usecols=(),dtype=float))
    preciosEmisor=[]
    for pais in range(5):
        costeemitir=(tarifas_llamadas[pais].sum())
        preciosEmisor.append(costeemitir)
    preciosEmisor = np.asarray(preciosEmisor)
    costes=np.reshape(preciosEmisor,(1,5))
    print("costes minuto por pais:""\n",costes)
    print('----------------')
    print("costes totales por pais")
    total_llamadas_emitidas_Pais_array=np.array(total_llamadas_emitidas_Pais)
    costes_pais=total_llamadas_emitidas_Pais_array*costes
    print(costes_pais)
    #--------------------#
    
    #--------------------#
    #Graficamos ambos marginales.
    
    #paises
    paises=np.array(['A', 'B', 'C', 'D', 'E'])
    #lista de emitidas totales
    llamadas_emitidas=total_llamadas_emitidas_Pais.to_list()
    #lista de recibidas totales
    llamadas_recibidas=total_llamadas_recibidas_Pais.to_list()
    
    #Grafico de barras para las emtidas totales por cada pais
    #Grafico de barras para las emtidas totales por cada pais
    plt.subplot(1,3,1)
    plt.bar(paises,llamadas_emitidas, color='green')
    plt.subplot(1,3,2)
    plt.bar(paises,llamadas_recibidas, color='orange')
    plt.suptitle('Minutos Totales Emitidos / recibidos por País')
    plt.ylabel('minutos')
    plt.xlabel('paises')
    #grafico de tarta  minutos totales por pais
    plt.subplot(1,3,3)
    total_flujo_llam_pais['duracion_minutos'].plot(kind='pie', labels=paises, title='Total minutos por pais')
    plt.title= "Total minutos por pais" 
    return(plt.show())
    
if __name__== '__main__':
    Totales_marginales()
