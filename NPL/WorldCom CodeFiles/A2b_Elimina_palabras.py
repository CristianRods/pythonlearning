#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 10:13:33 2019

@author: Cristian
"""

import csv
# import cvs
try:
    import nltk
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    
except:
#importamos la lista de stopwords desde la libreria nltk
    from stop_words import get_stop_words
#importamos la lista stop-words en caso de que no sirva la libreria nltk

def eliminapalabras():
    """
    Esta funcion requiere de definir una lista de palabras que se quiere modificar eliminando algunas palabras
    para ello se necesita definir primero el conjunto de palabras que se van a modificar como 'conjuntodepalabras'
    y luego el listado de palabras que se quieren eliminar del conjunto como 'palabrasprohibidas'
    
    Parameters
    --------------------------------------
    
    
    Return
    ---------------------
    list
    la función generara una lista nueva de palabras 'conjuntopalabras' que será el resultado
    de eliminar los elementos de la intersección entre el conjunto de palabras 
    y las palabras prohibidas. Se almacenara un fichero en el disco con las palabras
    de la lista 'conjuntopalabras' y devolvera el primer elemento de esa lista'
    
    Ejemplo
    ------------------
    eliminapalabras(0)
    ['si', '6927']
    """
    corpus=open('Corpus_palabras.txt',"w")
    with open('flistapalabras') as fichero:
        csv_reader = csv.reader(fichero, delimiter=';')
        listapalabras=[]
        for i in csv_reader:
            listapalabras.append(i)
        fichero.close()
    #print(listapalabras)

    #transformamos la lista de palabras del fichero para crear una lista de pares palabra-frecuencia de nuevo
    nuevo_conjunto_palabras=[] 
    for linea in listapalabras:
        palabra=linea[0]
        #print(palabra)
        numero=linea[1]
        par=[palabra,numero]
        nuevo_conjunto_palabras.append(par)
    
    #---------#
    #generamos la lista de palabras que vamos a eliminar del nuevo conjunto de palabras
    try:
        palabrasprohibidas = stopwords.words('spanish')
    except:
        palabrasprohibidas=get_stop_words('spanish')
    #print(palabrasprohibidas[1])
    #---------#
    #vamos a generar un nuevo conjuntopalabras con su frecuencia
    #con los elementos de la lista del conjunto de palabras que no son prohibidas 
    conjuntopalabras=[]                  
    for palabra in nuevo_conjunto_palabras:
        if palabra[0] not in palabrasprohibidas:
            conjuntopalabras.append(palabra)
    #print(len(conjuntopalabras))
        #escribimos el fichero en un archivo de disco
    for letra,numero in conjuntopalabras:
            corpus.write('\n'.join(["%s;%s" % (letra, numero)])+"\n")
 
    corpus.close()
    # para ejemplificar que escribe la funcion en el fichero
    print(conjuntopalabras[0])
    return(conjuntopalabras[0])

if __name__=="__main__":
    eliminapalabras()
    

