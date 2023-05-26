'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos
ele vai pagar.

Calcule o valor de prestação mensal, sabendo que ele não pode exceder 30% do salário ou
então o empréstimo será negado.

Analise: 
    - Vamos perguntar o valor da casa;
    - Salario do comprador;
    - Em quantos anos ele quer pagar a casa.

    Em seguida vamos calcular a prestação mensal da casa, lembrando que o salário não pode exceder
    30% ou o empréstimo será negado;

    EX: 
    Valor da casa: R$ 200.000;
    Salario: R$ 3.000;
    Pagar em: 15 anos;

        Calcular quanto é 30% de R$ 3000:
        x = salario*(percentual/100)
        x = 3000=(30/100)
        x = 900.0
        Não pode passar de R$ 900 mensais;

        Calcular quantos meses tem 15 anos:
        meses = anos * 12;
        meses = 15 * 12;
        meses = 180
        15 anos, possuem 180 meses;

        Calcular a mensalidade:
        m = vl_casa / meses
        m = 200000 / 180
        m = 1.111,11

        Logo o empréstimo será negado, já excede os 30% do salário;

Metodo dos 5 Q's

1 - Quais são os dados de entrada?
-> input vl_casa;
-> input salario;
-> input qtd_anos_pg;

2 - O que devo fazer com esses dados?
-> Deve calcular quanto é 30% do salario, quantos meses tem os informados, qual é a mensalidade
da casa a pagar;
-> Caso o valor da mensalidade não exceda o valor de 30% do salario o emprestimo será aceito,
caso contrario, será negado;

3 - Quais são as restrições desse problema?
-> Calcule o valor de prestação mensal, sabendo que ele não pode exceder 30% do salário;

4 - Qual é o resultado esperado?
-> Que seja exibido para o usuario se o emprestimo será aprovado ou não!

5 - Quais foram os passos realizados para se alcançar o resultado esperado?
#1 input vl_casa;
#2 input salario;
#3 input qtd_anos;
#4 v1 = salario*(30/100)
#5 v2 = qtd_ano_pg * 12
#6 v3 = vl_casa / v2
7# if v3 > v1
8#        print Empréstimo negado!
9# else:
10#       print Empréstimo aceito!

'''

print ('\n'+'-=-' * 8,'Adambank','-=-' * 8,'\nInstruções:\n-> Não use pontos ou virgulas para separar os decimais.')

c = float(input('\nQual o valor da casa?\nR$ '))
s = float(input('\nQual o valor do seu salário?\nR$ '))
m = float(input('\nCom quantos anos deseja quitar o empréstimo?\nAnos: '))

#=================================================================================
#Calculando quanto é 30% do salário informado;
s1 = s*(30/100)
#Calculando quantos meses tem os anos informado;
m1 = m * 12
#Calculando a mensalidade;
c1 = c / m1
#=================================================================================
if s1 >= c1:
    print('\nA mensalidade fica em: R$ {:.2f}\nParabéns, o seu emprestimo está {}aprovado!{}'.format(c1,'\033[1;32m','\033[m'))
else:
    print('\nA mensalidade é de: {:.2f}\nExcede a percentual máximo do seu salario que é de R$ {:.2f} mês.''\033[31m''\nEmpréstimo Negado!' '\033[m'.format(c1, s1))
print('\n' + '-=-' * 20)


