'''
Crie um programa que faça o computador jogar jokenpô com você;

Analisando: Jekenpô é uma brincadeira infantil que utiliza apenas as mãos e gestos simples
para determinar quem é vencedor;

Gestos: Pedra, Papel e tesoura
Pedra = Mão fechada;
Papel = Mão aberta;
Tesoura = Feche o dedo minimo e anela e segure-os os o polegar;

Regras:

1 - Pedra ganha da tesoura;
2 - Papel ganha da pedra;
3 - Tesoura ganha do papel;

1 - Quais são os dados de entrada?
- input computador;
- input usuario;

2 - O que devo fazer com esses dados?
- Com base no resultado dos dados de entrada do computador e do usuario e as regras da brincadeira, iremos determinar
quem foi o ganhador;

3 - Quais são as restrições desse problema?
#1 - Pedra ganha da tesoura;
#2 - Papel ganha da pedra;
#3 - Tesoura ganha do papel;

4 - Qual é o resultado esperado?
- Exibir quem ganhou e perder com base nos dados de entrada e as regras da brincadeira

5 - Quais foram os passos necessarios para se alcançar o resultado esperado?
1 - input computador []
2 - input usuario;
3 - variavel1 = fazer maquina sortear um elemento da lista input computador;/
4 - if variavel1 == PEDRA and usuario == PAPEL
        print Voce ganhou
    if variavel1 == PAPEL and usuario == TESOURA
        print Voce ganhou
    if variavel1 == TESOURA and usuario == PEDRA
        print Voce ganhou
    else 
        print A maquina venceu
'''
print('\n'+'-=-'* 9,'JOKEMPÔ', '-=-' * 9)
from random import choice
c = [ 'PEDRA', 'PAPEL', 'TESOURA']
m = choice(c)
u = str(input('\nEscolha: Pedra | Papel | Tesoura\n')).upper()
if m == 'PEDRA' and u == 'PAPEL':
    print('\nParabéns, você ganhou!\nVocê usou {} e a máquina usou {}'.format(u, m))
elif m == 'PAPEL' and u == 'TESOURA':
    print('\nParabéns, você ganhou!\nVocê usou {} e a máquina usou {}'.format(u,m))
elif m == 'TESOURA' and u == 'PEDRA':
    print('\nParabens, você ganhou!\nVocê usou {} e a máquina usou {}'.format(u,m))
elif m == u:
    print('\nEmpate! Você usou {} e a maquina {}'.format(u,m))
else:
    print('\nO Computador ganhou usando {} e você usou {}'.format(m, u))
print('\n'+'-=-' * 21)