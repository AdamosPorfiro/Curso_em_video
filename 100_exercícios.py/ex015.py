'''
===== Exercício 15 =====

Escreva um programa que  pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele
foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60.00 por dia R$ 0.15 centavos por km rodado.

Analise criticamente: Vamos supor que eu aluguei um carro por 7 dias e rodei 680km. Formula:
dias alugados = qtd de dias * valor alguel por dia;
Custo por km = qtd km rodado * custo por km rodado;

7 * 60 = R$ 420
6800 * 0.15 = R$ 102
O total a pagar sobre o alguel do carro é de: R$ 522.00.

Metodo dos 5 Q's

1 - Quais são os dados de entrada?
-> input qtd_dias;
-> input qtd_km.

2 - O que eu devo fazer com esses dados?
-> Deve calcular o preço a pagar, sabendo que o carro custa R$ 60.00 por dia R$ 0.15 centavos por km rodado, exibir o resultado na tela.

3 - Quais são as restrições do problema?
-> Nenhuma

4 - Qual deve ser o resultado alcançado?
-> Deve exibir para o usuario o preço final do aluguel do carro, calculando os dias e os km rodados;

5 - Quais são os passos para se alcançar o resultado?

1 - input qtd_dias
2 - input qtd_km
3 - print da qtd_dias * 60 + qtd_km * 0.15

'''

print ('\n'+'=' * 21, 'Alguel de carros R$ 60.0 o dia e R$ 0.15 por km rodado', '=' * 21, '\nNão é necessario usar virgula ou ponto para separar os decimais de km Ex.: Quantidade de km: 15250')
dias = int(input('\nPor quantos dias ficou com o carro?\nQuantidade de dias:  '))
km = float(input('\nQuantos km você rodou com o carro?\nQuantidade Km rodado:  '))
print('\nO carro foi alugado por {} dias que equivale R${}.\nFoi rodado {} km e equivale a R$ {:.2f}.\nO preço final do alguel é de: R$ {:.2f}'.format(dias, dias * 60, km, km * 0.15, dias * 60 + km * 0.15),'\n' + '=' * 98)
