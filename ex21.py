# Cria a lista com 10 números inteiros fornecidos pelo usuário
numeros = []
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

soma = 0
for numero in numeros:
    soma = soma+numero

print(f"Soma de todos os números: {soma}")
