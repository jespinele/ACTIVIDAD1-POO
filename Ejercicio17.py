import math
class calcular:
    @staticmethod
    def area (radio):
        return math.pi * math.pow(radio,2)
    @staticmethod
    def longitudcir (radio):
        return 2 * math.pi * radio
radio = float(input("Ingrese el radio del circulo que desea medir en cm: "))
area = calcular.area(radio)
longitudcir = calcular.longitudcir(radio)
print(f"El area del circulo es de {area:.2f}cm y la longitud de su circunferencia es {longitudcir:.2f}cm")