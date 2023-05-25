'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu
preço normal e condição de pagamento:

- A vista dinheiro / cheque: 10% de desconto;
- A vista no cartão: 5% de desconto;
- Em até 2x no cartão: preço normal;
- Em 3x ou mais no cartão: 20% de juros;

Analise:

Vamos supor um produto no valor de R$ 85,00
A vista e cheque ele tem desconto de 10%
FORMULA: Valor_c_desconto = (Valor_produto * porcentagem_desconto)/100
x = (85 *10)/100
x = 850 / 100
x = 8.5
Desconto é de R$ 8,50 
10% de R$ 85,00 é: R$ 8,50

A vista no cartão: 5% desconto
x = (85*5)/100
x = 425 / 100
x = 4,25
Desconto é de R$ 4,25
5$ de R$ 85,00 é: R$ 4,25

Em até 2x no cartão: R$ 85,00
x = 85 / 2
x = 42,50
Cada mensalidade ficará R$ 42,50

EM até 3x ou mais no cartão o juros a pagar é de 20%.
Parcela = 85 / 3
Parcela = 28,33

Juros = (85*20)/100
Juros = 1700 / 100
Juros = 17

(Juros + Parcela) * 3 = R$ 135,99
Juros = R$ 17,00
1º parcela: R$ 45,33
2º parcela: R$ 45,33
3º parcela: R$ 45,33
Total: R$ 135,99

1 - Quais são os dados de entrada?
input preço;
input pagamento;

2 - O que devo fazer com esses dados
Calcular o preço do produto considerando o seu preço normal e as condições de pagamento

3 - Quais são as restrições desse problema?
- A vista dinheiro / cheque: 10% de desconto;
- A vista no cartão: 5% de desconto;
- Em até 2x no cartão: preço normal;
- Em 3x ou mais no cartão: 20% de juros;

4 - Qual é o resultado esperado?
Calcular o preço do produto considerando o seu preço normal e as condições de pagamento e
exibir para o usuario o preço final do produto;

5 - Quais são os passos necessarios para se alcançar o resultado esperado?
1 - input preço;
2 - input 1 - PG_VISTA 2 - PG_CARTÃO_VISTA 3 - PG_CARTÃO_PARCELADO
3 - V = (preço*10)/100
4 - C_V = (preço*5)/100
5 - J = (preço*20)/100
6 - if input == 1
        print Pagamento a vista tem 10% de desconto
        \nO preço do produto é R$ {preço}
        \nVocê vai pagar R$ {V} 
7 - if input == 2
        print Pagamento no cartão a vista tem 5% de desconto
        \nO preço do produto é R$ {preço}
        \nVocê vai pagar R$ {C_V}
8 - if input == 3
        input Quantas parcelas você quer?
        if == 2
            print Pagamento em 2x no cartão não tem juros
            \nO preço do produto é R$ {preço}
            \n1° Parcela R$ {preço/2}
            \n2° Parcela R$ {preço/2}
        else
            print Pagamento em {input} no cartão tem 20% de juros
            \nO preço do produto é R$ {preço}
            \nCada parcela ficará R$ {(J + preço)/input}

'''
P = float(input('Informe o preço do produto\nR$ '))
PG = int(input('\n1 - Pagamento dinheiro\n2 - Pagamento débito\n3 - Pagamento crédito\nPagamento: '))
#Á vista
V = ((P*10)/100)
#Cartão á vista
C_V = ((P*5)/100)
#Juros
J = ((P*20)/100) 
#Condições
if PG == 1:
    print('\nPagamentos á vista tem 10%','de desconto\nPreço do produto é R$ {}\nVocê vai pagar R$ {}'.format(P, P-V))
elif PG == 2:
    print('\nPagamento no cartão débito tem 5%','de desconto\nPreço do produto é R$ {}\nVocê vai pagar R$ {}'.format(P, P-C_V))
elif PG == 3:
    N_P = str(input('\nQuantas parcelas você quer?\n'))
    if N_P == 1:
        print('\nPagamento parcelado em até 1x não tem juro!\nPreço do produto é R$ {}\nParcela R$ {}'.format(P, P))
    elif N_P == 2:
        print('\nPagamento parcelado em até 2x não tem juro!\nPreço do produto é R$ {}\n1° Parcela R$ {}\n2° Parcela R$ {}'.format(P, P/2, P/2))
    else:
        Co = int(N_P)
        print('\nPagamento parcelados acima de 2x tem 20%','de juros!\nPreço do produto é R$ {}\nCada Parcela Aplicado o juros fica R$ {:.2f}\nNumero de parcelas: {}\nTotal com juros R$ {}'.format(P, (P/Co)+J, N_P, ((P/Co)+J)*Co))



