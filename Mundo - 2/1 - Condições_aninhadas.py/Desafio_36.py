"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

Calcule o valor de prestação mensal, sabendo que ele não pode exceder 30% do salário ou
então o empréstimo será negado.

Perguntar: 
- o valor da casa
- o salario do comprador
- em quantos anos ele irá pagar

calcular a prestação mensal
se a prestação for 30% maior que o salario o empréstimo será negado

"""
print("-="*20)
print("{:>27}".format("Banco do Adamos"))
print("-="*20)
valor_casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o seu salário? R$"))
anos_pagar = int(input("Em quantos anos pretende pagar a casa? "))

vl_prestação = valor_casa/anos_pagar # Valor da prestação

if salario*30/100+salario < vl_prestação:
    print(f"A prestação no valor de R${vl_prestação} é 30% maior que o seu salario\nPor isso o empréstimo foi: \33[1;31mNEGADO\33[m")
else:
    print(f"A prestação no valor de R${vl_prestação} foi: \33[1;32mAPROVADO\33[m")
