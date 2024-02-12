'''
Desafio 12

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço.
Com 5% de desconto

'''

print("{:=^50}".format(" Desafio 12 "))
p = float(input("Informe o valor do produto R$ "))
novo_p = p-((p*5)/100)
print("O produto tem 5% de desconto. O novo preço é R$ {:.2f}".format(novo_p))
print("{:=^50}".format(""))