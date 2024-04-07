# Reto-8-
# ¡PYTHON FC!

<details>
  <summary>¡ESCUDO!</summary>
  
  [![PYTHON-F-C-B.jpg](https://i.postimg.cc/1Xpw71f0/PYTHON-F-C-B.jpg)](https://postimg.cc/jnSDC96C)

</details>

# 1
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```ruby
  def elevar_cuadrado (i : int) -> int: 
    return i ** 2

if __name__ : "__main__"  
i  : int
for i in range (101):
    cuadrado = elevar_cuadrado(i)
    print (f"el cuadrado de {i} es {cuadrado}")

```

# 2
Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```ruby
i : int 
    
print (f"los numeros impares desde 1 hasta 999 son:")
for i in range (1, 1000, 2):
    print (i)

print (f"los numeros pares desde 2 hasta 1000 son:")
for i in range (2, 1001, 2):
    print (i)
```
# 3
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```ruby
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
```
# 4
Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```ruby
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
```
# 5
Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```ruby
def dos_cuadrado (n : float) -> float:
    return 2 ** n

if __name__ == "__main__":
    n = float(input("ingrese la potencia de 2: "))
    potencia = dos_cuadrado(n)
    for i in (n, n+1):
        print (f"2 elevado a la {n} es igual a: {potencia} ")
# esta forma es un poco trampa pero al menos no hay problema en ingresar potencia fraccionaria o negativa
```
# 6
Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
```ruby
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
```
# 7
Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```ruby
 
numeros1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros1:
    print(f"la tabla del {numero} es:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")

```
# 8
Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

$$e^x \approx exp(x,n) \approx \sum_{i=0}^{n}\frac{x^i}{i!}$$

```ruby
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
    x : float = float(input("Ingrese el exponente de e: ")) 
    n : int = int(input("Ingrese el numero de terminos de la serie: ")) 

    # cabe aclarar que entre mayor sea x para que el resultado sea preciso n debe aumentar tambien

    valor_real = math.exp(x)
    valor_aprox = aprox_exp(x, n)
    diferencia = abs(valor_real - valor_aprox) / valor_real * 100

    print(f"Valor real: {valor_real}")
    print(f"Aproximación: {valor_aprox}")
    print(f"Diferencia: {diferencia} %")

# despues de 15 terminos de la serie el resultado tiene un error de menos del 0.1%
```
# 9
Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$

```ruby
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

# despues de 10 terminos de la serie el resultado tiene un error de menos del 0.1%
```
# 10
Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$

```ruby
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

# despues de 7 terminos de la serie el resultado tiene un error de menos del 0.1%
```
