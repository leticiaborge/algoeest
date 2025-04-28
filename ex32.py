def tabuada_personalizada (base,inicio,fim):
    print (f"tabuada do {base} de {inicio} a {fim};")
    for j in range (inicio, fim +1):
        print (f"{base} x {j} = {base * j}")
        
        
base= int(input("digite o numero para começar"))
inicio= int(input("digite o numero para inicio"))
fim= int(input("digite o numero para fim"))

        
#uso
tabuada_personalizada (base, inicio, fim)
