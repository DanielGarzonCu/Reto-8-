def dos_cuadrado (n : float) -> float:
    return 2 ** n

if __name__ == "__main__":
    n = float(input("ingrese la potencia de 2: "))
    potencia = dos_cuadrado(n)
    for i in (n, n+1):
        print (f"2 elevado a la {n} es igual a: {potencia} ")
# esta forma es un poco trampa pero al menos no hay problema en ingresar potencia fraccionaria o negativa