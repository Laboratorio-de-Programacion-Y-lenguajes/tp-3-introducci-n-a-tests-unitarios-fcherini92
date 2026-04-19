"""Tests para la función sub(a, b) -> float."""

import pytest

from src.calculator import sub


# --- EJEMPLO (no borrar) ---
def test_sub_resta_positivos():
    """Ejemplo: 5 - 2 debe dar 3."""
    assert sub(5, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Restar un número mayor al primero (resultado negativo)
#   - Restar cero
#   - Restar dos números negativos
#   - Restar dos números decimales (float)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

@pytest.mark.parametrize("a, b, expected", [
    (2, 5, -3),           # Restar un número mayor al primero (resultado negativo)
    (10, 0, 10),          # Restar cero
    (-5, -2, -3),         # Restar dos números negativos
    (5.5, 2.1, 3.4),      # Restar dos números decimales (float)
])
def test_sub_parametrizado(a, b, expected):
    """Pruebas parametrizadas para la resta."""
    # Tip: Usamos pytest.approx para comparar floats y evitar errores de precisión
    assert sub(a, b) == pytest.approx(expected)
