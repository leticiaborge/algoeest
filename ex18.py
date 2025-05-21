
salario_base = float(input("Digite o salário base: R$ "))
horas_extras = int(input("Digite o número de horas extras trabalhadas: "))
valor_hora_extra = 23.10
total_horas_extras = horas_extras * valor_hora_extra
salario_total = salario_base + total_horas_extras
print(f"Salário base: R$ {salario_base}")
print(f"Total de horas extras: {horas_extras} horas")
print(f"Valor total das horas extras: R$ {total_horas_extras}")
print(f"Salário total (com horas extras): R$ {salario_total}")
