#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:41:51 2019

@author: Cristian
"""

import A11_generafechacall as A11
import A12_generahoracall as A12
import A13_duracion_llamada as A13
import A1bc_Generar_Clave_Cliente_aleatoria as A1bc
import A2c_Genera_Mensaje_Text as A2c
import sys


y = int(sys.argv[1])
def generarllamadas2020(y):
    
    """
    la función genera un fichero de 'y' lineas que se compondra cada linea
    de una fecha de llamada, un hora de llamada, duracion de la llamada,una clave
    de identificacion de quien realiza y recibe la llamada y las palabras clave
    de la llamada que quiere obtener la empresa.
    
    Parameters
    ----------------------------
    y= el numero lineas que quiere recoger en el archivo de llamadas 
    
    Return
    ---------------------------------
    fichero
    
    se almacena un fichero con las llamadas realizads y los registros compuestos
    por la informacion descrita.
    
    Example
    ----------------
    >>>Python generarllamadas2020.py 1
    2020-03-08 # 9:46:00 # 6:31 # C-775 # C-464 # siempre necesito sabes toma teléfono real dime bueno loco tan hacemos ver aqui 
    """
    assert y > 0, "el numero de llamadas a recoger en el fichero debe ser superior a 0"
    llamadas2020=open("llamadas.txt","w")
    for i in range(y):
        a=A11.generafechacall(1,2020)
        b=A12.generahoracall(0,1)
        c=A13.duracion_call_no_unif()
        d=A1bc.genera_clave_cliente_aleatoria()
        e=A2c.generatext()
        llamadas2020.write(str(a[0]) +str(b[0])+str(c[0]) +str(d) + e+"\n")
    llamadas2020.close()
    print(llamadas2020)

if __name__== '__main__':
	generarllamadas2020(y)