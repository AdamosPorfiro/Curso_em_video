"""
Desafio 29

Escreva um programa que leia a velocidade de um carro:

- Se ele ultrapassar a velocidade de 80km/h mostre uma mensagem que ele foi multado

A multa ira custa R$ 7,00 por cada km acima do limite

"""
print("{:=^45}".format(" Desafio 29 "))
velocidade = float(input("Informe a velocidade do carro: "))
if velocidade > 80:
    print("\nVocê levou uma multa no valor de R$ {:.2f}\nDirija com cuidado!".format((velocidade-80)*7))
else:
    print("\nAtenção, Dirija com cuidado!")
print("{:=^45}".format(""))