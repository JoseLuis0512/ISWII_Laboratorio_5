# test_app.py

from src.app import sumar, restar

def test_sumar():
    assert sumar(2, 3) == 5

def test_restar():
    assert restar(5, 3) == 1