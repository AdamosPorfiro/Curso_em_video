"""

Desafio 10

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

Considere
U$$1,00 = R$3,27

"""
print("{:=^45}".format(" Desafio 10 "))
print("{:^45}".format("Cotação: U$$ 3,27"))
n = float(input("  Quanto possui de dinheiro em REAIS R$: "))
qtd_dolar = n/3.27
print("\nCom R$ {}\nVocê pode adiquir U$$ {:.1f}".format(n, qtd_dolar))
print("{:=^45}".format(""))