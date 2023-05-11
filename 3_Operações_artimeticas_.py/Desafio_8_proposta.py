'''
===== Desafio 8 prosta =====

Faça um programa permita o usuario digitar o valor do produto e o seu
respectivo desconto e exiba para o usuario o valor final do produto com desconto.

Analise criticamente:
Supondo que um produto tenha o valor de R$ 50.0 reais e o seu desconto é de 10% o programa vai ler esses dois valores e calcular o valor final

Lembrando que para descobrir quanto é 10% de R$ 50.0 o calculo é valor = 50 * 10 / 100 = 5
Para validar que R$ 5.00 é 10% de R$ 50.0 a formula porcentagem = o desconto em reais / valor do produto * 100 sendo então:
porcentagem = 5/50*100=10 logo, R$ 5.00 é 10% de R$ 50.0

Metodo dos 5Q's

1 - Quais são os dados de entrada?
-> input valor_produto
-> input valor_desconto
Talvez uma variavel resultado = valor_final_produto

2 - O que deve ser feito com esses dados?
-> Deve calcular o valor do produto com o respectivo desconto e exibir na tela para o usuario.

3 - Quais são as restrições desse problema?
-> Como iremos trabalhar com dinheiro, teremos casas decimais, valores reais (float)

4 -Qual o resultado esperado?
-> Que seja feito o calculo do produto com seu respectivo desconto e o valor final do produto com desconto seja exibido na tela.

5 - Quais são os passos a serem tomados para se alcançar o resultado?
#1 input valor_produto;
#2 input valor_desconto;
#3 resultado = valor_real_desconto;
#3 print valor_produto * valor_desconto / 100 = valor_real_desconto;
#4 print valor_produto - valor_real_desconto = valor_final.

'''

print('\n','=' * 18, 'Calculadora de desconto', '=' * 18, '\n\nUse apenas numeros e ponto para separar os decimais Ex.: 54.90')
v_p = float(input('\nDigite o valor do produto\nR$ '))
v_d = float(input('\nDigite o desconto do produto\n'))
v_f = (v_p * v_d / 100)
print('O valor com desconto: R$ {:.2f}\nO valor sem desconto: R$ {}\nO valor do desconto: {}%'.format(v_p - v_f, v_p, v_d))
print('=' * 62 )
