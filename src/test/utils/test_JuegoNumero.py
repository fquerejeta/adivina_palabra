import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../../')
from src.main.utils.JuegoNumero import JuegoNumero


def test_juegoNumero_init():
    juegoNumero_test = JuegoNumero(4, 45)
    assert (juegoNumero_test.numIntentos == 4) & (juegoNumero_test.numeroAdivinar == 45)