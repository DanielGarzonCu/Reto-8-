def elevar_cuadrado (i : int) -> int: 
    return i ** 2

if __name__ : "__main__"  
i  : int
for i in range (101):
    cuadrado = elevar_cuadrado(i)
    print (f"el cuadrado de {i} es {cuadrado}")
