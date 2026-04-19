"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Sumar dos números negativos
#   - Sumar un número positivo y uno negativo
#   - Sumar con cero
#   - Sumar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
#
# Ejemplo de test parametrizado:
#
# @pytest.mark.parametrize("a,b,expected", [
#     (..., ..., ...),
#     (..., ..., ...),
# ])
# def test_add_parametrizado(a, b, expected):
#     assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (-1, -1, -2),          # Sumar dos números negativos
    (5, -3, 2),            # Sumar un positivo y un negativo
    (10, 0, 10),           # Sumar con cero
    (2.5, 3.5, 6.0),       # Sumar dos números decimales (float)
])

def test_add_parametrizado(a, b, expected):
    """Pruebas para la suma usando parametrización."""
    assert add(a, b) == expected