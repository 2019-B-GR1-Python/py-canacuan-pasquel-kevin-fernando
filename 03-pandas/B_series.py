# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:24:44 2019

@author: kfc0_
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

seria_a = pd.Series(lista_numeros)

serie_b = pd.Series(tupla_numeros)

serie_c = pd.Series(np_numeros)

serie_d = pd.Series([True,
                     False,
                     12,
                     12.12,
                     "Kevin",
                     None,
                     (),
                     [],
                     {"nombre":"Kev"}])

serie_d[3]

lista_ciudades = ["Ambato", "Cuenca", "Loja", "Quito"]

serie_ciudad = pd.Series(lista_ciudades, index = ["A", "C", "L", "Q",])

serie_ciudad["Q"]
serie_ciudad[3]

valores_ciudad = {"Ibarra":9500, "Guayaquil":10000, "Cuenca": 7000, "Quito":8000, "Loja":3000}

serie_valor_ciudad = pd.Series(valores_ciudad)
serie_valor_ciudad[0]
serie_valor_ciudad["Ibarra"]

ciudades_menores_5000 = serie_valor_ciudad < 5000  # devuelve una serie de booleanos
s5000 = serie_valor_ciudad[ciudades_menores_5000]

serie_valor_ciudad = serie_valor_ciudad * 1.1   # aumentar el 10%

serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50 

print("Lima" in serie_valor_ciudad)
print("Loja" in serie_valor_ciudad)

rsquare = np.square(serie_valor_ciudad)



ciudades_uno = pd.Series({
			"Montanita":300,
			"Guayaquil":10000,
			"Quito":2000 })

ciudades_dos = pd.Series({
			"Loja":300,
			"Guayaquil":10000 })

ciudades_uno["Loja"] = 0
ciudades_dos["Montanita"] = 0
ciudades_dos["Quito"] = 0

print(ciudades_uno + ciudades_dos)


ciudad_add = ciudades_uno.add(ciudades_dos)

ciudades_concatenadas = pd.concat([ciudades_uno, ciudades_dos])

ciudades_concatenadas_v = pd.concat(([ciudades_uno, ciudades_dos]),verify_integrity = True)

# concat y append son lo mismo

ciudades_append = ciudades_uno.append(ciudades_dos)


ciudades_uno.max()
pd.Series.max(ciudades_uno)
np.max(ciudades_uno)

ciudades_uno.min()
pd.Series.min(ciudades_uno)
np.min(ciudades_uno)

# Estadistica
ciudades_uno.mean() #media
ciudades_uno.median() #mediana
np.average(ciudades_uno) #promedio


ciudades_uno.head(2) 	# tomar los primeros valores
ciudades_uno.tail(2)	# tomar los ulimos valores

ciudades_uno.sort_values(ascending = False).head(2)	#ordenar valores o indice
ciudades_uno.sort_values().tail(2)

# Ejercicio
# 0 - 1000 5%
# 1001 - 5000 10%
# 5001 - 20000 15%

def calculo(valor):
    if(valor <= 1000):
        return valor * 1.05
    if(valor > 1000 and valor <= 5000):
        return valor * 1.10
    if(valor > 5000):
        return valor * 1.15

ciudad_calculada = ciudades_uno.map(calculo)

# Cuando NO CUMPLE la condicion
# Aplica la formula
ciudades_uno.where(ciudades_uno > 1000,
                   ciudades_uno * 1.05)




