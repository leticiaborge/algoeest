import random
numero_secreto = random.randint(1, 20)
palpites = []

acertou = False

while not acertou:
    palpite = int(input("Digite seu palpite (entre 1 e 20): "))
    palpites.append(palpite)
    
    if palpite == numero_secreto:
        acertou = True
        print("Parabéns! Você acertou!")
    else:
        print("Errado! Tente novamente.")

print("Seus palpites foram:", palpites)