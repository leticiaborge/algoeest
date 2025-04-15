notas = []

for i in range(5):
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))
    notas.append(nota)

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)
print(f"A média das notas é: {media:.2f}")
