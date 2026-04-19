"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero
#   - Multiplicar dos números negativos (resultado positivo)
#   - Multiplicar un positivo y un negativo (resultado negativo)
#   - Multiplicar por 1 (elemento neutro)
#   - Multiplicar dos decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

@pytest.mark.parametrize("a, b, expected", [
    (5, 0, 0),             # Multiplicar por cero
    (0, -10, 0),           # Cero por un negativo
    (-3, -4, 12),          # Dos números negativos (resultado positivo)
    (5, -2, -10),          # Un positivo y un negativo (resultado negativo)
    (7, 1, 7),             # Multiplicar por 1 (elemento neutro)
    (-5, 1, -5),           # Negativo por 1
    (2.5, 2.0, 5.0),       # Dos decimales (float)
    (1.5, 0.5, 0.75),      # Floats más complejos
])
def test_mul_parametrizado(a, b, expected):
    """Pruebas variadas para la multiplicación."""
    # Usamos pytest.approx para evitar errores de redondeo en floats
    assert mul(a, b) == pytest.approx(expected)