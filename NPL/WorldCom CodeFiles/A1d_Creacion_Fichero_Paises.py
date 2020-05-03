#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 17:57:14 2019

@author: Cristian
"""

import pandas as pd
#importamos pandas para manejar dataframes

def GenerarTablaPaises():
    """ 
    Funcion que genera un fichero con la poblacion y los nombres de paises
    que se guarda en disco como 'Paises_Clientes'.
    
    Parameters
    ----------
    no necesita parameters
    
    Return
    ----------
    fichero en disco guardado en la carpeta llamado de Paises_Clientes.csv
    y un dataframe llamado tablapaises
    
    """
    
    paises=['A', 'B', 'C', 'D', 'E']
    poblacion=[(300,100,500,250,150)]
    paises_df = pd.DataFrame(poblacion,columns=paises)
    paises_df
    paises_df.to_csv('Paises_Clientes.csv',header=True, index=False)
    
    "--------------"
    #cargamos el fichero y creamos un dataframe llamado tablapaises
    fichero='Paises_Clientes.csv'
    tablapaises=pd.read_csv(fichero)
    print(tablapaises)
    return(tablapaises)
if __name__== '__main__':
	GenerarTablaPaises()