

idade=int(input("insira a sua idade"))
acompanhado=str(input("voce está acompanhado sim ou nao"))
menbro=str(input("voce esta como membro sim ou nao"))
if idade>18:
    print("voce tem acesso ao clube")
elif menbro == "nao":
 print("voce não é membro, deve pagar um ingresso")
elif acompanhado == "sim":
    print("pague meia entrada")
