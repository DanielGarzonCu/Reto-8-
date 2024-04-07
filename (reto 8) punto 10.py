import math

def arcotg_aprox(x: float, n: int) -> float:
    aprox = 0
    for i in range(n+1): 
        aprox += (-1) ** i * ((x ** ( 2 * i + 1)) / ( 2 * i + 1))
    return aprox

if __name__  == "__main__":

    x = float(input("Ingrese el valor de x: "))
    while x < -1 or x > 1 or x == 0:
            x = float(input("El x ingresado no corresponde al rango establecido"))
    n = int(input("Ingrese el número de términos de la serie: "))
    valor_real = math.atan(x)
    valor_aprox = arcotg_aprox(x, n)
    diferencia = abs(valor_real - valor_aprox)

    print(f"El valor real de arcotg({x}) es {valor_real}")
    print(f"La aproximación de arcotg({x}) con {n} términos es {valor_aprox}")
    print(f"La diferencia entre el valor real y la aproximación es del {((diferencia / valor_real) * 100):.2f}%")
