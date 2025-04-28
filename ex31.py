numero= int(input("digite um numero"))
def tabuada (numero):
    print (f"tabuada do {numero}:")
    for i in range (1,11):
        print(f"{numero} x" ,i, "=" ,numero* i)
              
tabuada(numero)
