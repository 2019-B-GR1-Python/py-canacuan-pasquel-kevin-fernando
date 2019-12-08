# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:57:49 2019

@author: kfc0_
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado_bin = "D://EPN//9no Semestre//py-canacuan-pasquel-kevin-fernando//03-pandas//data//artwork_data_completo.pickle"
df5 = pd.read_pickle(path_guardado_bin)
df = df5.iloc[49980:50519,:].copy()

### EXCEL ###
path_guardado = 'D://EPN//9no Semestre//py-canacuan-pasquel-kevin-fernando//03-pandas//data//mi_df_completo.xlsx' 
# df.to_excel(path_guardado)
df.to_excel(path_guardado, index = False) #elimina los indices

columnas = ['artist', 'title', 'year'] #toma ciertas columnas
df.to_excel(path_guardado, columns = columnas, index = False)

### Multiples hojas de trabajo ###
path_multiple = 'D://EPN//9no Semestre//py-canacuan-pasquel-kevin-fernando//03-pandas//data//mi_df_multiple.xlsx' 
writer = pd.ExcelWriter(path_multiple,
                        engine = 'xlsxwriter') #motor q ayuda a realizar cosas en Excel

df.to_excel(writer, sheet_name = 'Primera')
df.to_excel(writer, sheet_name = 'Segunda', index = False)
df.to_excel(writer, sheet_name = 'Tercera', columns = columnas)

writer.save()  #guardar el archivo

### Mas operaciones en Excel ###
num_artistas = df['artist'].value_counts()
path_colores = 'D://EPN//9no Semestre//py-canacuan-pasquel-kevin-fernando//03-pandas//data//mi_df_colores.xlsx' 
writer = pd.ExcelWriter(path_colores,
                        engine = 'xlsxwriter')

num_artistas.to_excel(writer, 
                      sheet_name='Artistas')

hoja_artistas = writer.sheets['Artistas']


rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)

formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas,
                                 formato_artistas)
# writer.save()

workbook = writer
worksheet = workbook.add_worksheet()
data = [10, 40, 50, 20, 10, 50]
worksheet.write_column('B2:B', data)

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})
# Add a series to the chart.
chart.add_series({'values': '=$A$1:$A$6'})
# Insert the chart into the worksheet.
worksheet.insert_chart('D1', chart)

workbook.close()




