"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Raíz de 0 (resultado: 0.0)
#   - Raíz de un número que no es cuadrado perfecto (resultado decimal)
#   - Raíz de un número negativo → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_sqrt_negativo():
#     with pytest.raises(ValueError):
#         sqrt(-4)

@pytest.mark.parametrize("x, expected", [
    (0, 0.0),             # Raíz de 0
    (1, 1.0),             # Raíz de 1
    (2, 1.41421356),      # No es cuadrado perfecto (resultado irracional)
    (10, 3.16227766),     # Otro número con muchos decimales
    (0.25, 0.5),          # Raíz de un número decimal
])
def test_sqrt_parametrizado(x, expected):
    """Pruebas para raíces válidas usando aproximación para decimales."""
    # Usar approx es vital para raíces como la de 2 o 10
    assert sqrt(x) == pytest.approx(expected)


def test_sqrt_negativo():
    """Verifica que la raíz de un número negativo lance ValueError."""
    with pytest.raises(ValueError) as excinfo:
        sqrt(-4)
    
    # Verificamos el mensaje de la excepción
    assert "no admite números negativos" in str(excinfo.value)