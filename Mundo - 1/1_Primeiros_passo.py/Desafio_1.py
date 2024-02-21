'''
Desafio - 1

Crie um script python que leia o nome de uma pessoa e mostra 
uma mensagem de boas-vindas de acordo com o valor digitado.

Metodo 5 Q's:

1 - Quais são os dados de entrada necessarios?
-> input = Nome_da_pessoa

2 - O que devo fazer com esses dados?
-> Ele mostra uma mensagem de boas-vindas de acordo com o valor digitado.

3 - Quais são as restrições desse problema?
-> 

4 - Qual é o resultado esperado?
-> Receber os dados e mostra uma mensagem de boas-vindas de acordo com os dados digitados

5 - Qual é a sequencia de passos a serem feitas?

Pseudocódigo:
# 1 - input = nome_usuario
# 2 - print (nome_usuario, mensagem de boas vindas)

Código final abaixo:
'''
from emoji import emojize
from datetime import datetime
print('{:=^50}'.format(emojize(" Desafio 1 -> \33[0;32mUPADO\33[m :dorso_da_mão_com_dedo_indicador_apontando_para_cima: ",language='pt')))

nome = input('Qual é o seu nome?\n')
if datetime.today().hour < 12:
    hour = "Bom dia"
elif datetime.today().hour >= 12 and datetime.today().hour <= 18:
    hour = "Boa tarde"
else:
    hour = "Boa noite"
print (f'\n{hour}, \33[1;33m{nome}\33[m!!\nÉ um imenso prazer conhece-lo(a),seja bem vindo(a) ao \33[1;34mpython.\33[m')