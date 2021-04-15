from src.main.utils.Juego import Juego
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


class JuegoNumero(Juego):
    def __init__(self, numIntentos, numero):
        Juego.__init__(self, numIntentos)
        self.numeroAdivinar = numero
        self.numerosIntentosFallidos = []

    def adivinarNumero(self):
        numero = 0
        while (self.numIntentos > 0):
            repetir = True
            while (repetir):
                try:
                    numero = int(input("Adivine el número:"))
                    self.numIntentos -= 1
                except Exception:
                    logger.error('Debe introducir un número')
                else:
                    repetir = False

            if self.numeroAdivinar > numero:
                print(f"Intento erróneo. El número a adivinar es mayor.{self.numIntentos} intentos disponibles.")
            elif self.numeroAdivinar == numero:
                textoIntentos = ','.join(self.numerosIntentosFallidos)
                print(f"Ha acertado el número! Los intentos fueron los siguientes:{textoIntentos}.")
                return True
            else:
                print(f"Intento erróneo. El número a adivinar es menor.{str(self.numIntentos)} intentos disponibles.")

            self.numerosIntentosFallidos.append(str(numero))
        return False
