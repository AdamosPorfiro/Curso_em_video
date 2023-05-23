'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

Analise:
Regra: 
1 - Ano para ser bissexto ele deve ser divisivel por 4
2 - Caso ele seja divisivel por 100, ele não é bissexto, porém caso seja divisivel por 400
então ele é bissexto.


1 - Quais os dados de entrada?
- input ano

2 - O que devo fazer com esses dados?
- Exibir se é ano BISSEXTO

3 - Quais são as restrições desse problema?
- Apenas numero inteiros: anos;
- Deve ser divisivel por 4;
- Se o ano for divisivel por 100, ele não é bissexto exceto se ele for divisivel por 400.

4 - Qual é o resultado esperado?
- Exibir se o ano é bissexto ou não.

5 - Quais são os passos para se alcançar o resultado esperado?
#1 - input ano;
#2 - if ano % 4 == 0 and ano % 400 % 4 print Sim, é BISSEXTO;
#3 - else print Não é BISSEXTO.
'''
print(
    '=' * 65 +
    '\nCalculadora de ano bissexto'
    )
from datetime import date

a = int(input('Informe o ano que deseja analisar? Digite 0 para ano atual:\nAno: '))

if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('Sim, o ano {} é BISSEXTO'.format(a))
else:
    print('Não, o ano {} não é BISSEXTO'.format(a))
print('=' * 65)
  
