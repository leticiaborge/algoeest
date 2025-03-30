valor = int(input("Insira o valor da compra"))
descont10 = valor - valor * 0.1
descont20 = valor - valor * 0.2
descont25 = valor - valor * 0.25 
if valor < 100:
     print(valor)
elif valor >= 100 and valor < 500: 
     print(descont10)
elif valor >= 500 and valor < 1000:
     print(descont20)
else: 
     print(descont25) 