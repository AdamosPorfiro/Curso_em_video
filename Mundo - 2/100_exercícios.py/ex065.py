'''
Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução:
 - mostre a média entre todos os valores 
 - qual foi o maior e o menor valor lidos.
O programa deve perguntar ao usúario se ele que ou não continuar a digitar valores.

1 Quais são os dados de entrada?
input numero
input sair

2 O que eu devo fazer com esses dados?
Ao final da execução vamos exibir:
- Média entre todos os valores;
- Qual foi o maior e o menor valor lido;
- Se o usuario deseja sair ou não;

3 Quais são as restrições desse problema?
Numero inteiros;
Média dos valores informados;
Qual foi o maior valor lido;
Deseja sair sim ou não?

4 Qual o resultado esperado?
Ao final da execução vamos exibir:
- Média entre todos os valores;
- Qual foi o maior e o menor valor lido;
- Se o usuario deseja sair ou não;

5 Quais são os passos necessarios para se alcançar o resultado esperado?
media = 0
contador = 0
maior = 0
menor = 0
while sair in 'Nn'
    input numero: 
    input sair [S/N]?
    contador += 1
    media += numero
    if numero > maior
        maior = numero
    if numero < menor
        menor = numero
    if sair in 'Ss':
        print Média de todos os valores {media/contador}
        print Maior numero informado foi {maior}
        print Menor numero informado foi {menor}
print Obrigado!
'''
media = 0
contador = 0
verificado = 0
maior = 0
menor = None
sair = 'N'
while sair in 'Nn':
    n1 = int(input('Informe um número: '))
    sair = str(input('Ao sair uma analise será feita quer sair ? [S/N]: '))
    contador+=1
    media+=n1
    if n1 > maior:
        maior = n1
    if menor is None or n1 < menor:
        menor = n1
    if sair in 'Ss':
        print('\nA média dos valores é: {:.1f}\nO maior valor informado foi: {}\nO menor valor informado foi: {}'.format(media/contador,maior, menor))


