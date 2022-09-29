"""
Este módulo contiene helpers (funciones auxiliares) para el preprocesamiento de datos.
"""

import numpy as np  # Ahora quedará declarada en .toml

def get_numerical_features(df):
    """ Función que devuelve todas las variables cuantitativas de un dataframe"""
    return df.select_dytypes(include=[np.number]).columns