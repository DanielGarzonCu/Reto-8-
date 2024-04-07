def factorial(n: int) -> int:
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

if __name__ == "__main__":
    n = int(input("Ingrese un numero natural: "))
    for n in range(1, n + 1):
        resultado_factorial = factorial(n)
        print(f"El factorial de {n} es {resultado_factorial}")