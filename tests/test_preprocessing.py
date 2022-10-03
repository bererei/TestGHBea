from modeltools.preprocessing import get_numerical_features
import pandas as pd
import pytest  # https://docs.pytest.org/en/7.1.x/

# Para hacer tests más complejos:
## https://docs.pytest.org/en/6.2.x/parametrize.html
## https://docs.pytest.org/en/6.2.x/fixture.html

# Para ejecutar pytest en terminal: pytest

def test_get_numerical_features_simple():
    """En este test vamos a probar que logra distinguir entre cadenas de textos y números enteros"""

    df = pd.DataFrame({
    "numerica": [5],
    "categorica": ["rojo"]
    })

    # Assert es "como un if" pero que falla si la condición es falsa. Esto es ideal para los tests.

    assert get_numerical_features(df) == ["numerica"]
