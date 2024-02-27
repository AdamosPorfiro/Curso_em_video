'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:

- A vista dinheiro / cheque: 10% de desconto;
- A vista no cartão: 5% de desconto;
- Em até 2x no cartão: preço normal;
- Em 3x ou mais no cartão: 20% de juros;

'''
print("-="*30)
print("{:>36}".format(" Bazar do dodô "))
print("-="*30)
vl_produto = float(input("Qual o valor do produto R$ "))
print("""Como deseja pagar:
    [ 1 ] A vista no dinheiro/cheque
    [ 2 ] A vista no cartão
    [ 3 ] Em até 2x no cartão
    [ 4 ] Em 3x ou mais no cartão""")
pagamento = int(input("Escolha: "))

if pagamento == 1:
    print(f"\nVocê terá um desconto de 10%\nEquivalente a R${vl_produto*10/100:.2f} de descontoe\nO total a pagar é R$ {vl_produto-(vl_produto*10/100):.2f}")
elif pagamento == 2:
    print(f"\nVocê terá um desconto de 5%\nEquivalente a R${vl_produto*5/100:.2f} de desconto\nO total a pagar é R$ {vl_produto-(vl_produto*5/100):.2f}")
elif pagamento == 3:
    print(f"\nVocê irá pagar R$ {vl_produto} parcelado 2x de R$ {vl_produto/2:.2f}, SEM JUROS")
elif pagamento == 4:
    parcelado = int(input("Informe quantas vezes deseja parcelar: "))
    juros = vl_produto+(vl_produto*20/100)
    print(f"\nVocê irá pagar com 20% de juros\nEquivalente a R${juros:.2f}\nQue será parcelado em {parcelado}x de R$ {juros/parcelado:.2f} ")
print("-="*30)

