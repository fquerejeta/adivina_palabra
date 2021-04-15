# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import logging
from src.main.utils.JuegoPalabra import JuegoPalabra


logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    repetir = True
    palabraAdivinar = input("introduzca palabra")
    while (repetir):
        if str(palabraAdivinar) and len(palabraAdivinar) > 1:
            repetir = False
        else:
            print("Debe introducir una palabra")

    repetir = True
    while (repetir):
        try:
            intentos = int(input("introduzca intentos permitidos:"))
        except Exception:
            logger.error('Debe introducir un número')
        else:
            repetir = False

    juego = JuegoPalabra(intentos, len(palabraAdivinar), palabraAdivinar)
    numeroAcertado = juego.adivinarNumero()
    if numeroAcertado:
        juego.adivinarPalabra()

    print("Juego Finalizado")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
