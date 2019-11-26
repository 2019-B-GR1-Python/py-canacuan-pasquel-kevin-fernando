# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:36 2019

@author: kfc0_
"""

import pandas as pd
import os

# 1. JSON CSV HTML XML ....
# 2. Binary files -> (!#mf-.1234'120)
# 3. Bases de datos relacionales

path = "C://Users//kfc0_//Python//Pandas//data//artwork_data.csv"
path2 = "D://EPN//9no Semestre//py-canacuan-pasquel-kevin-fernando//03-pandas//data//artwork_data.csv"

df = pd.read_csv(
        path2,
        nrows = 10)

columnas = ['id', 'artist', 'title',
            'medium', 'year',
            'acquisitionYear', 'height',
            'width', 'units']

df2 = pd.read_csv(
        path2,
        nrows = 10,
        usecols = columnas)

df3 = pd.read_csv(
        path2,
        nrows = 10,
        usecols = columnas,
        index_col = 'id')


path_guardado = "D://EPN//9no Semestre//py-canacuan-pasquel-kevin-fernando//03-pandas//data//artwork_data.pickle"
df3.to_pickle(path_guardado)
df4 = pd.read_csv(
        path2)


path_guardado_bin = "D://EPN//9no Semestre//py-canacuan-pasquel-kevin-fernando//03-pandas//data//artwork_data_completo.pickle"
df4.to_pickle(path_guardado_bin)

df5 = pd.read_pickle(path_guardado)


