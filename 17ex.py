nota1=int(input("insira uma nota"))
nota2=int(input("insira segunda nota"))
nota3=int(input("insira terceira nota"))
soma=nota1+nota2+nota3
media=soma/3
if media>=7:
    print("aluno está aprovado")
elif media<7 and media>5:
    print("aluno está em recuperação")
else:
    print("aluno reprovado")
