import math

def aproximar_seno(x, n):
    suma = 0
    for i in range(n):
        termino = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        suma += termino
    return suma

def factorial(n: int) -> int:
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


if __name__  == "__main__":
    x = float(input("Ingrese el valor de x para calcular sen(x): "))
    n = int(input("Ingrese el numero de terminos de la serie: "))
    aproximacion = aproximar_seno(x, n)
    valor_real = math.sin(x)
    print(f"Aproximacion de sen({x}) usando {n} terminos: {aproximacion}")
    print(f"Valor real de sen({x}): {valor_real}")
    print(f"Porcentaje de error: {((abs(valor_real - aproximacion) / valor_real) * 100):.2f} %") #Truquito : aproximamos a dos decimales