
"""
Desafio 34

Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.

- Para salarios acima de R$ 1250,00 calcule um aumento de 10%

- Para os inferiores ou iguais o aumento é de 15%

"""

print("{:=^55}".format(" Desafio 34 "))
salario = float(input("Informe o seu salario R$ "))

if salario > 1250:
    print(f"Quem ganhava R${salario} passa a ganhar R${salario*10/100+salario}")
else:
    print(f"Quem ganhava R${salario} passa a ganhar R${salario*15/100+salario}")
    
"""
if salario > 1250:
    print("\nVocê terá um aumento de 10%' e agora receberá R$ {}".format(salario*10/100+salario))
else:
    print("\nVocê terá um aumento de 15%' e agora receberá R$ {}".format(salario*15/100+salario))

print("{:=^55}".format(""))
"""