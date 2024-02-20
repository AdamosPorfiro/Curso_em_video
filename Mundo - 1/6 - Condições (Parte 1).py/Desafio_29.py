"""
Desafio 29

Escreva um programa que leia a velocidade de um carro:

- Se ele ultrapassar a velocidade de 80km/h mostre uma mensagem que ele foi multado

A multa ira custa R$ 7,00 por cada km acima do limite

"""
print("{:=^35}".format(" Desafio 29 "))
velocidade = float(input("Informe a velocidade do carro: "))
if velocidade > 80:
    print("\nVocê utrapassou a velocidade de 80km/h")
    print("por isso levou uma multa no valor de R$ {:.2f}\nATENÇÂO, Dirija com cuidado!".format((velocidade-80)*7))
else:
    print("\nObrigado, Dirija com segurança!")
print("{:=^35}".format(""))