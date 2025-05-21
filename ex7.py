num1 =int(input("Insira o primeiro número"))
num2 =int(input("Insira o segundo número"))
opcao = input("Insira a operação desejada (soma, subtração, multiplicação, divisão)")
soma=num1+num2
sub=num1-num2
mult=num1*num2
div=num1/num2
if opcao == "soma":
    print(soma)
elif opcao == "subtração":
    print(sub)
elif opcao == "multiplicação":
    print(mult)
elif opcao == "divisão":
    print(div)
else:
    print("Operação inválida")
