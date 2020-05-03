#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:50:10 2019

@author: Cristian
"""
import pandas as pd
#importamos la libreria panda
import numpy as np
#importamos numpy
import random
#importamos random
    
def genera_clave_cliente_aleatoria():
    
    """ 
    la función genera_clave_cliente_aleatoria dara como resultado un par de codigos de cliente. 
    Es decir, genera una clave para quien emite la llamada y quien la recibe, generando un codigo 
    de cliente para cada tipo de llamada,respectivamente.
    En este caso, se selecciona el pais del emisor y receptor en funcion de la poblacion, dando mas probabilidad
    a el pais con mas poblacion y con una probabilidad proporcional a la poblacion de cada uno sobre el 
    total de individuos en la muestra. Ademas, el numero del cliente es unico y elegimos al azar el cliente
    del registro de la empresa.
    Este codigo tiene en cuenta los planes de expansion de la compania y si se incorpora un cliente solamente
    necesitara anadir una linea mas de codigo en las partes de la funcion de generacion de numeros de cliente y
    eleccion aleatoria siguiendo la secuencia en los indices de la lista.
    
    
    Parameters
    ----------------------------
    no tiene parameters
    
    Return
    ---------------------------------
    string
    Devuelve "clavellamada" codigos de llamada de cada tipo (emisor y receptor).
    
    Example
    ----------------
    >>> genera_clave_cliente_aleatoria()
    'D-018 # E-370 # '
    
    """  
    tablapaises=pd.read_csv('Paises_Clientes.csv')
    tablapaises['Total']= tablapaises.sum(axis=1)
    frec=list(tablapaises.values)
    poblacion=list(frec[0])
    #----------------------#
    i=0
    j=(len(poblacion)-1)
    frecuenciapoblacion=[]
    for x in poblacion:
        if i < j:
            frecuenciapoblacion.append((poblacion[i]/poblacion[j]))
        i=i+1
    #print("suma de probabilidades de cada letra de pais:"sum(frecuenciapoblacion)) #control de probabilidad
    
    # generamos el pool de clientes. Para ello, utilizamos la poblacion registrada y creamos los codigos de 
    #cliente segun dicha poblacion registrada en cada pais. Dando un numero secuencial a cada cliente.
    # Tambien utilizamos la inforamacion misma del fichero para generar su numero de forma que si se incorpora
    #un pais en sus planes de expasion se pueda incorporar facilmente una linea mas para generar sus codigos
    
    codigo_num_clientepaisA=[ "A"+"-"+str(numero).zfill(3) for numero in range(1,poblacion[0]+1)]
    codigo_num_clientepaisB=[ "B"+"-"+str(numero).zfill(3) for numero in range(1,poblacion[1]+1)]
    codigo_num_clientepaisC=[ "C"+"-"+str(numero).zfill(3) for numero in range(1,poblacion[2]+1)]
    codigo_num_clientepaisD=[ "D"+"-"+str(numero).zfill(3) for numero in range(1,poblacion[3]+1)]
    codigo_num_clientepaisE=["E"+"-"+str(numero).zfill(3) for numero in range(1,poblacion[4]+1)]
    
    #guardamos todos los codigos en un pool de clientes total
    lista_codigos=[codigo_num_clientepaisA,
                   codigo_num_clientepaisB,
                   codigo_num_clientepaisC,
                   codigo_num_clientepaisD,
                   codigo_num_clientepaisE]

    #iteraremos de forma que eligamos del pool de clientes un par de clientes como emisor y receptor de forma
    #aleatoria 
    
    for i in range(1):
        lista_codigoEmisor=np.random.choice((lista_codigos),p=(frecuenciapoblacion))
        if lista_codigoEmisor[1][0] == "A":
            codEmisor=lista_codigoEmisor[(random.randint(0,(poblacion[0]-1)))]
        if lista_codigoEmisor[1][0] == "B":
            codEmisor=lista_codigoEmisor[(random.randint(0,(poblacion[1]-1)))]
        if lista_codigoEmisor[1][0] == "C":
            codEmisor=lista_codigoEmisor[(random.randint(0,(poblacion[2]-1)))]
        if lista_codigoEmisor[1][0] == "D":
            codEmisor=lista_codigoEmisor[(random.randint(0,(poblacion[3]-1)))]
        if lista_codigoEmisor[1][0] == "E":
            codEmisor=lista_codigoEmisor[(random.randint(0,(poblacion[4]-1)))]
            
    for i in range(1):
        lista_codigoReceptor=np.random.choice((lista_codigos),p=(frecuenciapoblacion))
        if lista_codigoReceptor[1][0] == "A":
            codReceptor=lista_codigoReceptor[(random.randint(0,(poblacion[0]-1)))]
        if lista_codigoReceptor[1][0] == "B":
            codReceptor=lista_codigoReceptor[(random.randint(0,(poblacion[1]-1)))]
        if lista_codigoReceptor[1][0] == "C":
            codReceptor=lista_codigoReceptor[(random.randint(0,(poblacion[2]-1)))]
        if lista_codigoReceptor[1][0] == "D":
            codReceptor=lista_codigoReceptor[(random.randint(0,(poblacion[3]-1)))]
        if lista_codigoReceptor[1][0] == "E":
            codReceptor=lista_codigoReceptor[(random.randint(0,(poblacion[4]-1)))]


    if codEmisor!=codReceptor:
        clavellamadas=(" # "+str(codEmisor)+" # "+str(codReceptor)+" # ")
    while codEmisor==codReceptor:
    #print(codReceptor)
        for i in range(1):
            lista_codigoEmisor=np.random.choice((lista_codigos),p=(frecuenciapoblacion))
            if lista_codigoEmisor[1][0] == "A":
                codEmisor=lista_codigoEmisor[(random.randint(0,(poblacion[0]-1)))]
            if lista_codigoEmisor[1][0] == "B":
                codEmisor=lista_codigoEmisor[(random.randint(0,(poblacion[1]-1)))]
            if lista_codigoEmisor[1][0] == "C":
                codEmisor=lista_codigoEmisor[(random.randint(0,(poblacion[2]-1)))]
            if lista_codigoEmisor[1][0] == "D":
                codEmisor=lista_codigoEmisor[(random.randint(0,(poblacion[3]-1)))]
            if lista_codigoEmisor[1][0] == "E":
                codEmisor=lista_codigoEmisor[(random.randint(0,(poblacion[4]-1)))]
        for i in range(1):
            lista_codigoReceptor=np.random.choice((lista_codigos),p=(frecuenciapoblacion))
            if lista_codigoReceptor[1][0] == "A":
                codReceptor=lista_codigoReceptor[(random.randint(0,(poblacion[0]-1)))]
            if lista_codigoReceptor[1][0] == "B":
                codReceptor=lista_codigoReceptor[(random.randint(0,(poblacion[1]-1)))]
            if lista_codigoReceptor[1][0] == "C":
                codReceptor=lista_codigoReceptor[(random.randint(0,(poblacion[2]-1)))]
            if lista_codigoReceptor[1][0] == "D":
                codReceptor=lista_codigoReceptor[(random.randint(0,(poblacion[3]-1)))]
            if lista_codigoReceptor[1][0] == "E":
                codReceptor=lista_codigoReceptor[(random.randint(0,(poblacion[4]-1)))]
                
        clavellamadas=(" # "+str(codEmisor)+" # "+str(codReceptor)+" # ")
    print(clavellamadas)
    return(clavellamadas)
if __name__=="__main__":
    genera_clave_cliente_aleatoria()