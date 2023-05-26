'''
A confedereção nacional de natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: Mirim;
- Até 14 anos: Infantil;
- Até 19 anos: Junior;
- Até 20 anos: Sênior;
- Acima: Master.

1 - Quais são os dados de entrada?
 - input Ano de nascimento

2 - O que devo fazer com esses dados?
 - Calcular a idade do usuario com base no ano de nascimento informado e dizer a categoria sendo:
        - Até 9 anos: Mirim;
        - Até 14 anos: Infantil;
        - Até 19 anos: Junior;
        - Até 20 anos: Sênior;
        - Acima: Master.

3 - Quais são as restrições desse problema?
        - Até 9 anos: Mirim;
        - Até 14 anos: Infantil;
        - Até 19 anos: Junior;
        - Até 25 anos: Sênior;
        - Acima: Master.

4 - Qual é o resultado esperado?
Com base na idade do usuario seja exibido a sua categoria correspondente

5 - Quais são os passos para se alcançar o resultado esperado?

#1 input ano_nascimento;
#2 idade = ano_atual - ano_nascimento;
#3 if idade > 0 and <= 9
        print Você tem {} anos e sua categoria é: MIRIM
#4 if idade > 9 and idade <= 14
        print Você tem {} anos e sua categoria é: INFANTIL
#5 if idade > 14 and idade <= 19
        print Você tem {} anos e sua categoria é: JUNIOR
#6 if idade > 19 and idade <= 20
        print Você tem {} anos e sua categoria é: SÊNIOR
#7 else
        print Você tem {} anos e sua categoria é: MASTER
'''

#Dados entrada e calculando idade
from datetime import date
i = int(input('Ano de nascimento: '))
idade = date.today().year - i
#Condição categorias
if idade < 3:
    print('Você possui {} e não pode participar. Volte quando possuir no minímo 3 anos'.format(idade))
elif idade <= 9:
    print('Você tem {} anos e sua categoria é: {}MIRIM{}'.format(idade, '\033[1;44m', '\033[m'))
elif idade <= 14:
    print('Você tem {} anos e sua categoriaé: {}INFANTIL{}'.format(idade, '\033[1;46m', '\033[m'))
elif idade <= 19:
    print('Você tem {} anos e sua categoria é: {}JUNIOR{}'.format(idade, '\033[1;45m', '\033[m'))
elif idade <= 25:
    print('Você tem {} anos e sua categoria é: {}SÊNIOR{}'.format(idade, '\033[1;43m', '\033[m'))
else:
    print('Você tem {} anos e sua categoria é: {}MASTER{}'.format(idade,'\033[1;42m', '\033[m'))