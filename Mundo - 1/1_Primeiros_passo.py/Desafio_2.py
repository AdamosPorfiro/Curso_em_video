'''
Desafio - 2

Crie um script python que leia o dia, o mês e o ano de nascimento
de uma pessoa e mostre uma mensagem com a data formatada.

Metodo 5 Q's:

1 - Quais são os dados de entrada necessarios?
-> input = dia_nascimento;
-> input = mês_nascimento;
-> input = anos_nascimento;
-> input = Respota_final.

2 - O que devo fazer com esses dados?
-> Mostre uma mensagem com a data(dados) formatada, Ex.: Você nasceu no dia ## do mês ## e ano ####. Correto?

3 - Quais são as restrições desse problema?
-> 

4 - Qual é o resultado esperado?
-> Mostrar uma mensagem com os dados formatados para o usuario.

5 - Qual é a sequencia de passos a serem feitas?

Pseudocódigo:
# 1 - input = dia_nascimento;
# 2 - input = mês_nascimento;
# 3 - input = anos_nascimento;
# 4 - print = Você nasceu no dia ## do mês ## e ano ####, correto?

Código final abaixo:
'''
from datetime import datetime
from emoji import emojize
print(emojize('===== Desafio 2 - \33[0;32mUpado\33[m :dorso_da_mão_com_dedo_indicador_apontando_para_cima: =====',language='pt'))
dia = int(input('\nQual foi o dia do seu nascimento?\n')) # 10
mes = int(input('Qual foi o mês do seu nascimento?\n')) # novembro
ano = int(input('Qual foi o ano do seu nascimento?\n')) # 1993

if mes == datetime.today().month and dia <= datetime.today().day:
    idade = datetime.today().year - ano
else:
    idade = datetime.today().year - ano - 1
#print('Você nasceu no dia,',dia,mes, 'de',ano,' ') # Você nasceu no dia, 10 de novembro', de 1993. Correto?
print(emojize(f"Você nasceu no dia {dia} do mes {mes} no ano de {ano} e tem atualmente {idade} anos :bebê:",language='pt'))