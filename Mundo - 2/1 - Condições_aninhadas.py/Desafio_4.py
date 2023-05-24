'''
Faça um programa que leia o nome de um nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamente;

Seu programa tambem deverá mostrar o tempo que falta ou que passou do prazo.

Analise: 
    Vamos pedir para o usuario input do seu nome completo e data de nascimento
        Ex: Nome completo: Adamos Porfiro da Silva
            Nascimento: 10/11/1993
    
    Vamos calcular a idade atual:
        Data atual: 23/05/2023
        Nascimento: 10/11/1990

        idade = 2023 - 1993 = 30
        mês = data atual < mes nascimento então idade = idade - 1
        idade = 30 - 1 = 29 anos

    Se idade for menor que 18 anos, então você ainda vai se alistar ao serviço militar
    e faltam apenas {};
        Se não se a idade for igual a 18 e até 22 anos, então deve se alistar no exército;
            Se não você já passou o tempo de alistamento; 

1 - Quais são os dados de entrada?
         input nome_completo
         input nascimento

2 - O que devo fazer com esses dados?
        Calcular sua idade atual e de acordo com a idade exibir para o usuario:
                - Se ele ainda vai se alistar ao serviço militar;
                - Se é a hora de se alistar;
                - Se já passou do tempo do alistamente;

3 - Quais são as restrições do problema?
        Usar condições para determinar o caminho, essas condições tem como base idades maximas;
        Numeros inteiros

4 - Qual é o resultado esperado?
            - Exibir na tela para o usuario:
                    - Se ele ainda vai se alistar ao serviço militar;
                    - Se é a hora de se alistar;
                    - Se já passou do tempo do alistamente;

5 - Quais são os passos necessarios para se alcançar o resultado esperado?

    1 input nome
    2 input nascimento
    3 i = ano_atual - nascimento
    4 if i <= 18:
        print Você ainda vai se alistar no serviço militar, primeiro complete 18 anos
        faltam apenas {}
    5 if i >= 18 and i <= 22 
        print Você deve se alistar no exército
    6 else:
        print Você já passou do tempo de alistamento;
                
'''
#Dados de entrada;
from datetime import date
print('\nPreencha com essa formatação, nascimento:', '\033[31m''11 1993''\033[m')
n = str(input('\nNome completo: ')).strip()
i = str(input('Mês e ano de nascimento:  ')).strip().split()

#Calculando idade;
idade = date.today().year - int(i[1])
mes = int(i[1])

#Verificando o mês caso mês atual seja menor que o informado;
if date.today().month < mes:
    idade = date.today().year - int(i[1]) - 1 
    if idade < 18:
            print('\n{} você possui apenas {} anos, volte quando completar 18 anos.'.format(n, idade))
    elif idade >= 18 and idade <= 22:
             print('''\n{} você possui {} anos e está na hora de você se alistar. Acesse no periodo de 1 de janeiro até 30 de junho: https://alistamento.eb.mil.br/ faça o cadastro e
                    compareça a junta militar mais proxima da sua localidade'''.format(n,idade))
    else:
            print('{} você possui {} anos e já passou da idade, mas compareça ao junta militar mais proxima da sua localidade para se alistar e pegar sua dispensa militar.'.format(n,idade))

#Verificando o mês caso mês atual seja maior que o informado;
if date.today().month > mes:
    idade = idade
    if idade < 18:
            print('\n{} você possui apenas {} anos, volte quando completar 18 anos.'.format(n, idade))
    elif idade >= 18 and idade <= 22:
             print('''\n{} você possui {} anos e está na hora de você se alistar. Acesse no periodo de 1 de janeiro até 30 de junho: https://alistamento.eb.mil.br/ faça o cadastro e
                    compareça a junta militar mais proxima da sua localidade'''.format(n,idade))
    else:
            print('{} você possui {} anos e já passou da idade, mas compareça ao junta militar mais proxima da sua localidade para se alistar e pegar sua dispensa militar.'.format(n,idade))