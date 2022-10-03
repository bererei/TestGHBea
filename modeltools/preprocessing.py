"""
Este módulo contiene helpers (funciones auxiliares) para el preprocesamiento de datos.
"""

import numpy as np  # Ahora quedará declarada en .toml

def get_numerical_features(df):
    """ Función que devuelve todas las variables cuantitativas de un dataframe"""
    return list(df.select_dtypes(include=[np.number]).columns)  # Lo casteo a lista para que aunque esté vacío me de una lista.


