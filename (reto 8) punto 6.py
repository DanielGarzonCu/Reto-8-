def x_elevado_n(x: float, n: int) -> float:
    resultado = 1
    for k in range(n):
        resultado *= x
    return resultado

# como la coleccion empieza desde 0 y con incremeno 1 (positivo) no sera posible utilizar potencias negativas o fracciones.

if __name__ == "__main__":
    x = float(input("Ingrese la base de la potencia: "))
    n = int(input("Ingrese la potencia: "))
    resultado_final = x_elevado_n(x, n)
    print(f"{x} elevado a la {n} es igual a {resultado_final}")
