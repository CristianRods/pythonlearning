#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 01:50:08 2019

@author: Cristian
"""
import numpy as np
#importamos numpy para manejar arrays
import pandas as pd
#importamos pandas para manejar dataframes 

def generaclavecliente_misma_probabilidad(y):
    """ 
    Esta funcion que genera la clave de dos clientes que posteriormente estaran en la llamada registrada,
    siendo el numero de llamadas '(y)' que vamos a generar. 
    la clave del cliente se compone de la letra del pais en el que reside el cliente y 3 digitos que van
    del 0 a 9 que componen el numero de la clave. 
    Tanto la letra como los digitos tiene la misma probabilidad de 0 a 9. Que juntandolos pueden ir del 000 a 999.
    
    Parameters
    ----------
    y= Numero de par de codigos de clientes. 
    las claves de los paises estan en el fichero de proyecto Paises-Clientes. Para generar la clave 
    solo utilizaremos las letras del pais del Data Frame.
    
    Return
    ----------
    string
    una lista de 'y' valores aleatorios que componen la clave de llamada.
    Por un lado utiliza una lista de los nombres de los paises "Paises" y por otro los numeros que componen
    la clave de llamada "clavellamada"
    
    Example 
    -----------------------
    generaclavecliente"(1)""
     # D-677 # A-421 #
    """
    #cargamos nuestro fichero
    ficheroPaises= 'Paises_Clientes.csv' 
    tablapaises=pd.read_csv(ficheroPaises)
    Paises=list(tablapaises.head(5))
    #clavellamada=[]
    for i in range(0,y):
        codLetra=np.random.choice((Paises))
        codNum1=np.random.randint(0,9)
        codNum2=np.random.randint(0,9)
        codNum3=np.random.randint(0,9)
        codLetra2=np.random.choice((Paises))
        codNum4=np.random.randint(0,9)
        codNum5=np.random.randint(0,9)
        codNum6=np.random.randint(0,9)
        codEmisor=(codLetra+"-"+str(codNum1)+str(codNum2)+str(codNum3))
        codReceptor=(codLetra2+"-"+str(codNum4)+str(codNum5)+str(codNum6))
        if codLetra!=codLetra2:
            clavellamada=(" # "+codEmisor+" # "+codReceptor+" # ")
        print(clavellamada)
if __name__== '__main__':
    generaclavecliente_misma_probabilidad(1) 