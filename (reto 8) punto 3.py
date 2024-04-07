n = int(input("ingrese un numero natural mayo o igual a 2:"))
# recordar que los numeros racionales no son ni pares ni impares 
if n < 2: print ("el numero es menor que 2 ingrese otro valor")
else:
    if n % 2 == 0:
        for n in range (n, 1, -2):
            print (n)
    else:
        n -= 1
        for n in range (n, 1, -2):
            print (n)