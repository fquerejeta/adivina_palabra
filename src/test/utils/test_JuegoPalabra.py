import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../../')
from src.main.utils.JuegoPalabra import JuegoPalabra

def test_juegoNumero_init():
    palabraAdivinar = 'casa'
    juegoPalabra_test = JuegoPalabra(4, len(palabraAdivinar), palabraAdivinar)
    assert (juegoPalabra_test.numIntentos == 4) & (juegoPalabra_test.numeroAdivinar == len(palabraAdivinar)) & (juegoPalabra_test.palabraAdivinar == palabraAdivinar)

def test_juegoPalabra_comprobar_palabra_correcto():
    palabraAdivinar = 'casa'
    juegoPalabra_test = JuegoPalabra(4, len(palabraAdivinar), palabraAdivinar)
    resultado = juegoPalabra_test.comprobarPalabra(palabraAdivinar)
    assert (resultado == True)

def test_juegoPalabra_comprobar_palabra_incorrecto():
    palabraAdivinar = 'casa'
    juegoPalabra_test = JuegoPalabra(4, len(palabraAdivinar), palabraAdivinar)
    resultado = juegoPalabra_test.comprobarPalabra('cada')
    assert (resultado == False)