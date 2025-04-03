NOTA1= int(input (" adicione a primeira nota"))
NOTA2= int(input (" adicione a segunda nota"))
NOTA3= int(input (" adicione a terceira nota"))
md=(NOTA1+NOTA2+NOTA3) /3
if md >=7:
    print ("aprovado")
elif md<7 and md >5:
    print ("recuperaçaõ")
else:
    print("reprovado querido(A)")