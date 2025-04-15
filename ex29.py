valores = []

for i in range(4):
    numero = int(input(f"Digite o {i+1}º número: "))
    valores.append(numero)

multiplicador = int(input("Digite um número para multiplicar os valores: "))

novos_valores = []
for valor in valores:
    novos_valores.append(valor * multiplicador)

print("Valores após a multiplicação:", novos_valores)
