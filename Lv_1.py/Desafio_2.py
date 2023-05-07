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
print('===== Desafio 2 =====')
dia = input('Qual foi o dia do seu nascimento? ') # 10
mes = input('Qual foi o mês do seu nascimento? ') # novembro
ano = input('Qual foi o ano do seu nascimento? ') # 1993
print('Você nasceu no dia,'+dia+' de '+mes+', de '+ano+'. Correto?') # Você nasceu no dia, 10 de novembro', de 1993. Correto?
