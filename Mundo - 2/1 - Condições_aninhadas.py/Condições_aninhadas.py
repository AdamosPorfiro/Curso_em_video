'''
O que é condição aninhada?
R: Quando surgem situações que exigem mais de 2 opções, sendo, 3, 4, 5 opções, usamos a condição
aninhada para fazer com que as outras situações aconteça, ou seja, condição aninhada é quando
temos mais de uma condição dentro de um bloco de if, elif, else;

Com a condição aninhada podemos criar condições que o programa pode seguir por varios caminhos
diferentes, são condições dentro de condições por isso se chama aninhado;

if = SE, pode ser usado algumas vezes com certa condição; -> É uma condição obrigatória;
elif = SE NÂO, SE, pode ser usado varias vezes; -> É uma condição opcional;
else = SENÃO, pode ser usado nenhuma ou uma vez; -> É uma condição opcional;

'''

nome = str(input('Qual é o seu nome: '))
if nome == 'Adamos':
    print('\033[31m''Que nome bonito!''\033[m')
elif nome == 'Maria' or nome == 'João' or nome == 'Pedro':
    print('\033[1;33m''O seu nome é popular no brasil!''\033[m')
elif nome in 'Adamos Vilma Alesson Antonio':
    print('\033[35m''O seu nome é um belo nome feminino!''\033[m')
else:
    print('O seu nome é bem normal!')
print('Tenha um bom dia, {}{}{}!'.format('\033[32m',nome,'\033[m'))