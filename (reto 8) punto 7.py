
numeros1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros1:
    print(f"la tabla del {numero} es:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")