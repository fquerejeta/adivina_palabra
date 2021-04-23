import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../../')
from src.main.utils.JuegoNumero import JuegoNumero

numeroIntentos = 4
numero = 45

def test_juegoNumero_init():
    juegoNumero_test = JuegoNumero(numeroIntentos, numero)
    assert (juegoNumero_test.numIntentos == 4) & (juegoNumero_test.numeroAdivinar == 45)

def test_juegoNumero_comprobar_numero():
    juegoNumero_test = JuegoNumero(numeroIntentos, numero)
    assert (juegoNumero_test.comprobarNumero(45) == True)

def test_juegoNumero_comprobar_numero_incorrecto():
    juegoNumero_test = JuegoNumero(numeroIntentos, numero)
    assert (juegoNumero_test.comprobarNumero(8) == False)