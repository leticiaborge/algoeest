# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Cria uma lista vazia para armazenar a tabuada
tabuada = []

# Preenche a lista com os resultados da tabuada de 1 a 10
for i in range(1, 11):
    resultado = numero * i
    tabuada.append(resultado)

# Exibe os valores armazenados na lista
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {tabuada[i-1]}")
