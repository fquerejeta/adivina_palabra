import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../../')
from src.main.utils.Juego import Juego


def test_juego_init():
    juego_test = Juego(45)
    assert juego_test.numIntentos == 45

