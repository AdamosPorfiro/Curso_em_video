"""
Desafio 31

Desenvolva um programa que pergunte a distancia da sua viagem em KM.

Calcule o preço da passagem cobrando R$ 0,50 por km para viagens de até 200km
e R$0,45 para viagens mais longas

"""
print("{:=^50}".format(" Desafio 31 "))
v_km = float(input("Informe a distância em km da sua viagem: "))
if v_km <= 200:
    print("\nO valor da passagem fica R$ {:.2f}".format(v_km*0.50))
else:
    print("\nO valor da passagem fica R$ {:.2f}".format(v_km*0.45))
print("{:=^50}".format(""))