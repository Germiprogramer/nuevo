#ADIVINA EL NUMERO

from random import *

numero = randint(1,100)

def comparar(num, op):
    if op == num:
        print("Felicidades, el numero es {}".format(num))
    elif op > num:
        print("el numero es menor que {}".format(op))
    elif num > op:
        print("el numero es mayor que {}". format(op))


def adivinar(num):
    opcion = None
    while opcion != numero:
        opcion = int(input("Elige un número del 1 al 100"))
        comparar(numero, opcion)