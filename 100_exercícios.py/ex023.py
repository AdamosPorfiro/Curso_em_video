'''
Faça um programa que leia  um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

Analise critica: Deve ler um numero de 0 a 9999, sendo que temos uma leitura de numero com milhar, centenas, dezenas e unidades.
Caso o usuario digite valor apenas com centena Ex: 100 Logo o programa deve mostrar apenas a unidade, dezena e centena;
Outro exemplo: 10 unidade, dezena. 

Ex.: Digite um numero: 1834;
-> Unidade: 4;
-> Dezena: 3;
-> Centena: 8;
-> Milhar: 1.

1 - Quais são os dados de entrada?
-> Input numero 0 a 9999

2 - Oque deve ser feito com esses dados?
-> Deve ler e mostrar na tela cada um dos digitos separados

3 - Quais são as restrições do programa?
-> Apenas numeros de 0 a 9999;
-> Deve ser convertido para string, já que numeros inteiros são do tipo primitivo e não suportam indexação.

4 - Qual o resultado esperado?
-> Mostre na tela cada um dos digitos separados, unidade, dezena, centena, milhar.

5 - Quais são os passos necessarios para se alcançar o resultado esperado?
1 - input do numero 0 a 9999;
2 - Converte numero para string, pois, um numero inteiro não possui indexação;
3 - Usar lens para verificar quantos digitos possui;
4 - Usar if, elif, else para comparar as quantidades de digitos;
5 - print os indices nas casas corretas, unidade, dezena, centena, milhar.

'''

'''
# Funciona até milhar:

n = str(input('Digite um numero entre 0 a 9999\nNumero: '))
print('\nNumero digitado: {}\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(n, n[3], n[2], n[1], n[0]))

# Funciona bem, porém usa operadores aritméticos
n = int(input('Digite um numero de 0 a 9999: '))
unidade = n % 10
dezena = (n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 1000) % 10
print('\nUnidade: {:.0f}\nDezena: {:.0f}\nCentena: {:.0f}\nMilhar: {:.0f}'.format(unidade,dezena,centena,milhar))
'''

# Utilizando apenas manipulação de texto

n = str(input('Digite um numero entre 0 e 9999:\nNúmero: '))
tamanho = len(n)
if(tamanho == 4):
    print('\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar {}'.format(n[3], n[2], n[1], n[0]))
elif(tamanho == 3):
    print('\nUnidade: {}\nDezena: {}\nCentena: {}'.format(n[2], n[1], n[0]))
elif(tamanho == 2):
    print('\nUnidade: {}\nDezena: {}'.format(n[1], n[0]))
else:
    print('\nUnidade: {}'.format(n[0]))