"""Tests para la función div(a, b) -> float."""

import pytest

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - División que da resultado decimal (float)
#   - División con números negativos
#   - División por cero → debe lanzar ZeroDivisionError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_div_por_cero():
#     with pytest.raises(ZeroDivisionError):
#         div(10, 0)

@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 2.5),          # Resultado decimal (float)
    (1, 2, 0.5),           # Resultado menor a 1
    (-10, 2, -5.0),        # Numerador negativo
    (10, -2, -5.0),        # Denominador negativo
    (-10, -2, 5.0),        # Ambos negativos
    (0, 5, 0.0),           # Cero dividido algo
])

def test_div_parametrizado(a, b, expected):
    """Pruebas para divisiones que deben funcionar correctamente."""
    assert div(a, b) == pytest.approx(expected)


def test_div_por_cero():
    """Verifica que dividir por cero lance la excepción ZeroDivisionError."""
    # El bloque 'with' atrapa la excepción. Si la función NO lanza el error, el test falla.
    with pytest.raises(ZeroDivisionError) as excinfo:
        div(10, 0)
    
    # Verificar que el mensaje de error sea el correcto
    assert str(excinfo.value) == "division by zero"