numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Pares:", pares)
print("Ímpares:", impares)
