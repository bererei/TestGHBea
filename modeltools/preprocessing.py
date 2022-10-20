"""
Este módulo contiene helpers (funciones auxiliares o herramientas) para el preprocesamiento de datos.
"""

import numpy as np  # Ahora quedará declarada en .toml


def get_numerical_features(df) -> list[int]:
    """
    Función que devuelve todas las variables cuantitativas de un dataframe.

    Parámetros
    ------------

    df: dataframe

    Ejemplos
    ------------

    >>> from modeltools.preprocessing import get_numerical_features
    >>> import pandas as pd
    >>> df = pd.DataFrame({'a':[1]})
    >>> get_numerical_features(df)
    ['a']
    """

    return list(
        df.select_dtypes(include=[np.number]).columns
    )  # Lo casteo a lista para que aunque esté vacío me de una lista.


def get_numerical_features2(df):
    """
    Función que devuelve todas las variables cuantitativas de un dataframe.

    :param df: dataframe
    :type df: pandas.DataFrame
    :return: lista de nombres de columnas

    >>> from modeltools.preprocessing import get_numerical_features
    >>> import pandas as pd
    >>> df = pd.DataFrame({'a':[1]})
    >>> get_numerical_features(df)
    ['a']
    """
    return list(
        df.select_dtypes(include=[np.number]).columns
    )  # Lo casteo a lista para que aunque esté vacío me de una lista.


def count_numerical_features(df):
    get_numerical_features(df)


def half(x):
    """
    >>> from modeltools.preprocessing import half
    >>> half(4)
    2
    """

    return int(x / 2)
