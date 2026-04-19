"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)
#   - Número elevado a 1 (resultado: el mismo número)
#   - Base negativa con exponente par (resultado positivo)
#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)
#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.

@pytest.mark.parametrize("a, b, expected", [
    (5, 0, 1),            # Cualquier número elevado a 0 es 1
    (-10, 0, 1),          # Negativo elevado a 0 es 1
    (7, 1, 7),            # Elevado a 1 da el mismo número
    (-5, 1, -5),          # Negativo elevado a 1 da el mismo número
    (-3, 2, 9),           # Base negativa con exponente par 
    (-2, 3, -8),          # Base negativa con exponente impar
    (9, 0.5, 3.0),        # Exponente decimal
    (2, -1, 0.5),         # Exponente negativo
])

def test_pow_parametrizado(a, b, expected):
    """Pruebas variadas para la potenciación."""
    assert pow_(a, b) == pytest.approx(expected)