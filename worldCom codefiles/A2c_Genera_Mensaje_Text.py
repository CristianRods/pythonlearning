#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:32:07 2019

@author: Cristian
"""

import random
# importamos la libreria de random
import numpy as np
#importamos numpy
import csv
#importamos la funcion csv
def generatext():
    """
    Esta funcion permitira generar una lista de palabras significativas de una supuesta 
    conversacion de longitud entre 5 y 25 palabras por llamada. Este 'mensaje' se produce de elegir del 
    corpus generado y almacenado en el fichero txt en el disco llamado "Corpus_palabras.txt"
    
    Parameters
    --------------------------------------
    
    Return
    ---------------------
    list
    la función generara una lista nueva de palabras 'nuevoconjuntopalabras' que será el resultado de eliminar los elementos de la intersección entre
    el conjunto de palabras y las palabras prohibidas.
    
    """
    #generamos el listado de conjuntopalabras que contiene el listado de 
    # palabras finales para crear los mensajes. 

    conjuntopalabras=[]
    with open('Corpus_palabras.txt') as corpus:
        corpus_reader = csv.reader(corpus, delimiter=';')
        conjuntopalabras=[]
        for i in corpus_reader:
            conjuntopalabras.append((i))
        corpus.close()
    print(conjuntopalabras[1])

    #generamos una lista de pares con una longitud de 500 valores y seleccionamos cada tupla de forma aleatoria
    #al mismo tiempo.

    lista_palabra_frecuencia=[]
    while (len(lista_palabra_frecuencia))<=499:
        i=random.randint(0,819)
        palabra=conjuntopalabras[i][0]
        frecuencia=int(conjuntopalabras[i][1])
        if (palabra,frecuencia) not in lista_palabra_frecuencia:
                lista_palabra_frecuencia.append((palabra,frecuencia))
    #print(len(lista_palabra_frecuencia))
    

    #reordenamos la lista
    lista_palabra_frecuencia.sort(key=lambda frecuencia: frecuencia[1],reverse=True)

    
    print('generando mensaje')

    # la generacion de la frecuencia absoluta de las palabras 
    #dentro del conjunto de palabras elegidas aleatoriamente

    frecuencias=[]
    for i in range(len(lista_palabra_frecuencia)):
        numero=(lista_palabra_frecuencia[i][1])
        frecuencias.append(numero)
    frecuenciaabs = 0
    for i in frecuencias:
        frecuenciaabs = frecuenciaabs+i
    frecuenciaabs

    i=0
    #j=(len(frecuencias))
    frecuenciarelativas=[]
    for frec in frecuencias:
        frecuenciarelativas.append((frec)/frecuenciaabs)
        i=i+1

    palabras=[]
    for i in range(len(lista_palabra_frecuencia)):
        palabra=(lista_palabra_frecuencia[i][0])
        palabras.append(palabra)
    
    listamensajes=[]
    for i in range(random.randint(5,25)):
        mensaje=np.random.choice((palabras),p=(frecuenciarelativas))
        #print(len(listamensajes))
        if mensaje not in listamensajes:
            listamensajes.append(mensaje)
    mensajetext=" ".join(listamensajes)
    print(mensajetext)
    return(mensajetext)
if __name__== '__main__':
	generatext()