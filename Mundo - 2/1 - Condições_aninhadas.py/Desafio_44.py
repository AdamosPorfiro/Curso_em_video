'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:

- A vista dinheiro / cheque: 10% de desconto;
- A vista no cartão: 5% de desconto;
- Em até 2x no cartão: preço normal;
- Em 3x ou mais no cartão: 20% de juros;

'''
vl_produto = float(input("Qual o valor do produto R$ "))
pagamento = int(input("""Como deseja pagar:
    1 - A vista no dinheiro
    2 - A vista no cartão
    3 - Em até 2x no cartão
    4 - Em 3x ou mais no cartão
    Opção: """))

if pagamento == 1:
    print(f"\nVocê terá um desconto de 10% e irá pagar apenas R$ {vl_produto-(vl_produto*10/100):.2f}")
elif pagamento == 2:
    print(f"\nVocê terá um desconto de 5% e irá pagar apenas R$ {vl_produto-(vl_produto*5/100):.2f}")
elif pagamento == 3:
    print(f"\nVocê irá pagar R$ {vl_produto} parcelado 2x de R$ {vl_produto/2}")
elif pagamento == 4:
    parcelado = int(input("Informe quantas vezes deseja parcelar: "))
    juros = vl_produto+(vl_produto*20/100)
    print(f"\nVocê irá pagar R$ {juros} parcelado em {parcelado}x de R$ {juros/parcelado:.2f} ")
    

