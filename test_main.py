import pytest
from main import sumar

def test_sumar_positivo():
    """Prueba la suma de números positivos."""
    assert sumar(2, 3) == 5

def test_sumar_cero():
    """Prueba la suma que resulta en cero."""
    assert sumar(-1, 1) == 0

def test_sumar_negativos():
    """Prueba la suma de números negativos."""
    assert sumar(-2, -3) == -5