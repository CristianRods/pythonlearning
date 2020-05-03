#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 21:20:09 2019

@author: Cristian
"""
from bs4 import BeautifulSoup as bs
#importamos la funcion BeautifulSoup
import requests as req
#importamos la funcion request 

#En primer lugar, abrimos el fichero 
def webscrapping():
    
    '''Esta funcion generar un fichero con una lista de pares:"Palabra-Frecuencia". 
    para ello hacemos webscrapping de los elementos almacenados en una tabla 
    en la pagina web wikitionary.org definiendo su url dentro de la funcion. Para ello, se extraen los elementos
    se procesan como xlm y luego se limpia el fichero construyendo una lista a partir de la tabla almacenada en
    la pagina web.
    
    Parameters
    -----------------
    esta funcion no tiene parametros
    
    Return
    ------------------
    esta funcion devuelve un fichero csv con una lista de 1000 palabras y su frecuencia ordenada de mayor a menor.
    
    Example
    --------------------
    print(listapalabras[0])
    
    ('de', 40880)
    
    '''
    f_listapalabras=open("flistapalabras","w")
    
    # indicar la ruta
    url="https://es.wiktionary.org/wiki/Wikcionario:Frecuentes-(1-1000)-Subt%C3%ADtulos_de_pel%C3%ADculas"

    #extraer elementos
    webcontent=req.get(url).text

    #Procesar la informacion de la extracion como xlm
    content=bs(webcontent,"lxml")

    #Tenemos que pensar como llegar a los elementos de la tabla
    #como sacarlos y darles el formato adecuado
    #primero accedemos a la tabla y posteriormente a sus elementos
    
    #definimos esta tabla como tablaorg "\tabla origen"
    tablaorg=content.find('table',attrs={'class':'wikitable'})
    
    #iteramos hasta sacar todos los elementos de la tabla
    #al estar en varias tablas necesitaremos hacer lo mismo pero dos veces cambiando la tablaorg por la de la otra pagina
    palabra=""
    frecuencia=0
    nroFila=0
    listapalabras=[]
    for fila in tablaorg.find_all("tr"):
        if nroFila>=1:
            nroCelda=0
            for celda in fila.find_all('td'):
                if nroCelda==1:
                    palabra=celda.text.replace("\n","")
                if nroCelda==2:
                    frecuencia=int(celda.text)
                    listapalabras.append((palabra,frecuencia))
                nroCelda=nroCelda+1
        nroFila=nroFila+1
#-----------------------------------------------------------#
    #almacenamos el fichero y lo cerramos
    for letra,numero in listapalabras:
        f_listapalabras.write('\n'.join(["%s;%s" % (letra, numero)])+"\n")
    f_listapalabras.close()
    print(listapalabras[0])
if __name__== '__main__':
	webscrapping()