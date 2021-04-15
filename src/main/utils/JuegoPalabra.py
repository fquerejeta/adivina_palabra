from src.main.utils.JuegoNumero import JuegoNumero
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


class JuegoPalabra(JuegoNumero):
    def __init__(self, numIntentos, numero, palabra):
        JuegoNumero.__init__(self, numIntentos, numero)
        self.palabraAdivinar = palabra

    def adivinarPalabra(self):
        palabraAdivinarTupla = tuple(self.palabraAdivinar)
        letrasAcertadas = []
        for i in range(len(palabraAdivinarTupla)):
            letrasAcertadas.append("*")

        letrasIntentos = []
        while (self.numIntentos > 0):
            repetir = True
            while (repetir):
                try:
                    print("adivine letra introduzca 1")
                    print("adivine palabra introduzca 0:")
                    respuesta = int(input(""))
                    self.numIntentos -= 1
                except Exception:
                    logger.error('Debe introducir un número')
                else:
                    repetir = False

            if respuesta == 0:
                palabra = input("adivine palabra:")
                if palabra == self.palabraAdivinar:
                    print("Ha acertado la palabra!")

                    textoIntentos = ','.join(self.numerosIntentosFallidos)
                    print(f"Los intentos numero de letras fueron los siguientes: {textoIntentos}.")

                    textoIntentos = ','.join(letrasIntentos)
                    print(f"Los intentos de letras fueron los siguientes: {textoIntentos}.")

                    break
                else:
                    print(f"Intento erróneo. No es la palabra.{palabra}.{str(self.numIntentos)} intentos disponibles.")
            elif respuesta == 1:
                letra = input("adivine letra:")
                indice = 0
                for x in palabraAdivinarTupla:
                    if x == letra:
                        letrasAcertadas[indice] = letra
                    indice = indice + 1
                textoLetras = ''.join(letrasAcertadas)
                if letra in palabraAdivinarTupla:
                    print(
                        f"Intento correcto. Existe la letra.{textoLetras}.{str(self.numIntentos)} intentos disponibles.")
                else:
                    print(
                        f"Intento erróneo. No existe la letra.{textoLetras}.{str(self.numIntentos)} intentos disponibles.")
                letrasIntentos.append(letra)
