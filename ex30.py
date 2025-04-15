palavras = []

for i in range(5):
    palavra = input(f"Digite a {i+1}ª palavra: ")
    palavras.append(palavra)

palindromos = []

for palavra in palavras:
    if palavra == palavra[::-1]:
        palindromos.append(palavra)

print("Palavras palíndromas:", palindromos)