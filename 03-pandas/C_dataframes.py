# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:23 2019

@author: kfc0_
"""

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)
# Elementos del dataframe separados en series
s1 = df1[0]
s2 = df1[1]
s3 = df1[2]

# ELementos de la serie separados por c/u
s1[0]
s1[1]

#Añadir una columna
#serie_nueva = pd.Series([11,12])
#df1[4] = serie_nueva
df1[3] = s1
df1[4] = s1 * s2

datos_fisicos_uno = pd.DataFrame(
        arr_pand,
        columns = [
                'Estatura (cm)',
                'Peso (kg)',
                'edad(anios)'])

datos_fisicos_dos = pd.DataFrame(
        arr_pand,
        columns = [
                'Estatura (cm)',
                'Peso (kg)',
                'edad(anios)'],
        index = ['Kevin', 'Fernando'])

df1.index = ['Kevin', 'Fernando']
df1.index = ['Pepe', 'Fernando']
df1.columns = ['A', 'B', 'C', 'D', 'F']

