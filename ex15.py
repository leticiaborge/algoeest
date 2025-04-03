nome= input (" nome do produto")
quantidade= int (input (" adicione quantidade de produtos comprados"))
preco= float(input(" adicione o preço unitário de cada produto"))  
total= quantidade*preco
desconto5 = total* 0.05
if total >= 100:
     print(total-desconto5)
else: 
     print("sem desconto")