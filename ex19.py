idade=int(input("insira a sua idade"))
genero=str(input("insira o seu genero masculino ou feminino"))
atleta=str(input("voce é atleta sim ou não"))
if idade<=15:
    print("oferecer artigos infantis")
elif idade>15 and idade<21 and genero == "feminino":
    print("oferecer maquiagem e moda")
elif idade>15 and idade<32 and atleta == "sim" and genero == "masculino":
    print("oferecer artigos esportivos")
elif idade>15 and idade<21 and atleta == "não" and genero == "mascuino":
    print("oferecer video  games")
elif idade>21 and idade<32 and genero == "masculino" and atleta == "não":
    print("oferecer livros, jardinagem e eletrodomésticos")
elif idade>22 and idade<35 and genero == "feminino":
    print("oferecer artigos esportivos e itens de casa")
