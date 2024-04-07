import math

def aprox_exp(x, n):
    aprox = 0
    for i in range(n):
        termino = x**i / factorial(i)
        aprox += termino
    return aprox

# En ningun momento se nos dice que podemos importar la función de factorial desde math entonces usamos la que habiamos establecido previamente
def factorial(i: int) -> int:
    resultado = 1
    for k in range(1, i + 1):
        resultado *= k
    return resultado


if __name__ == "__main__":

    i : int
    resultado_factorial = factorial(i)
    x : float = float(input("Ingrese el exponente de e: ")) 
    n : int = int(input("Ingrese el numero de terminos de la serie: ")) 

    # por lo general cuand0 n >= 15 el resultado es muy preciso

    valor_real = math.exp(x)
    valor_aprox = aprox_exp(x, n)
    diferencia = abs(valor_real - valor_aprox) / valor_real * 100

    print(f"Valor real: {valor_real}")
    print(f"Aproximación: {valor_aprox}")
    print(f"Diferencia: {diferencia} %")


    