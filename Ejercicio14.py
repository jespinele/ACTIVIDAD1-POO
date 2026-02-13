import math
class calcular:
    @staticmethod
    def cuadrado (numero):
        return math.pow(numero,2)
    def cubo (numero):
        return math.pow(numero,3)
numero = float(input("Ingrese un número para hallar su cuadrado y su cubo "))
cuadrado = calcular.cuadrado(numero)
cubo = calcular.cubo(numero)
print(f"{numero} elevado al cuadrado es igual a {cuadrado}")
print(f"{numero} elevado al cubo es igual a {cubo}")
