"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)
#   - Lista con números negativos
#   - Lista con números decimales (float)
#   - Lista vacía → debe lanzar ValueError
#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_mean_lista_vacia():
#     with pytest.raises(ValueError):
#         mean([])

@pytest.mark.parametrize("values, expected", [
    ([10], 10.0),                # Lista con un solo elemento
    ([-1, -2, -3], -2.0),        # Lista con números negativos
    ([1.5, 2.5, 5.0], 3.0),      # Lista con números decimales (float)
    ([1, 2], 1.5),               # Resultado decimal de enteros
])

def test_mean_parametrizado(values, expected):
    """Pruebas para promedios con diferentes tipos de listas."""
    assert mean(values) == pytest.approx(expected)


def test_mean_lista_vacia():
    """Verifica que pasar una lista vacía lance ValueError."""
    with pytest.raises(ValueError) as excinfo:
        mean([])
    
    # Verifica el mensaje 
    assert "requiere una lista no vacía" in str(excinfo.value)
