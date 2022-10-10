from modeltools.preprocessing import get_numerical_features
import pandas as pd
import pytest  # https://docs.pytest.org/en/7.1.x/

# Para hacer tests más complejos:
## https://docs.pytest.org/en/6.2.x/parametrize.html
## https://docs.pytest.org/en/6.2.x/fixture.html

# Para ejecutar pytest en terminal: pytest


def test_get_numerical_features_simple():

    """En este test vamos a probar que logra distinguir entre cadenas de textos y números enteros"""

    df = pd.DataFrame({"numerica": [7], "categorica": ["rojo"]})

    # Assert es "como un if" pero que falla si la condición es falsa. Esto es ideal para los tests.

    assert get_numerical_features(df) == ["numerica"]


def test_get_numerical_features_empty():

    """Este test comprueba que se devuelve una lista vacía si no hay ninguna variable num."""

    df = pd.DataFrame({"categorica": ["rojo"]})

    assert get_numerical_features(df) == []


def test_get_numerical_features_zero_columns():

    """Este test comprueba que se devuelve una lista vacía si el dataframe no tiene ninguna columna."""

    df = pd.DataFrame()

    assert get_numerical_features(df) == []


def test_get_numerical_features_zero_rows():

    """Este test comprueba que se devuelve la variable correspondiente si el DF
    tiene una variable numérica pero NINGUNA FILA."""

    df = pd.DataFrame({"numerica": pd.Series(dtype=int)})

    assert get_numerical_features(df) == ["numerica"]


def test_get_numerical_features_complex():

    """Este test comprueba que funciona correctamente con número complejos."""

    df = pd.DataFrame({"compleja": [complex(3, 5)]})

    assert get_numerical_features(df) == ["compleja"]


def test_get_numerical_features_int_and_float():

    """Este test comprueba que funciona correctamente
    cuando hay una columna integer y una flotante"""

    df = pd.DataFrame({"integer": [5], "flotante": [5.50]})

    assert get_numerical_features(df) == ["integer", "flotante"]


def test_get_numerical_features_columns_withoutname():

    """Este test comprueba que funciona correctamente
    cuando hay columnas numéricas sin nombre (columnas
    con numeros/posiciones)"""

    df = pd.DataFrame(
        [[1, "a"]]  # Las columnas tienen nombre 0 y 1, para 1 y "a", respectivamente.
    )

    assert get_numerical_features(df) == [0]


def test_wrong():

    assert 1 == 1
