'''
Desafio - 2

Crie um script python que leia dois numeros
e tente mostrar a soma entre ele.

Metodo 5 Q's:

1 - Quais são os dados de entrada necessarios?
-> input = numero_1;
-> input = numero_2.

2 - O que devo fazer com esses dados?
-> Exibir na tela a soma desses dois numeros.

3 - Quais são as restrições desse problema?
-> São dois numerais, que devem realizar a operação soma;


4 - Qual é o resultado esperado?
-> A exibição da soma desses dois numeros.

5 - Qual é a sequencia de passos a serem feitas?

Pseudocódigo:
# 1 - input numero_1
# 2 - input numero_2
# 3 - print numero_1 + numero_2 
Código final abaixo:
'''
print('===== Desafio 3 =====')
n_1 = int(input('\nDigite o primeiro valor:  ')) # É necessario converter os valores recebido para numerais, para realizar uma operação matemática, pois sem a conversão, o valor armazenado é de string(caracteres).
n_2 = int(input('Digite o segundo valor:  ')) # Outra alternativa é converter os valores no codigo que ira realizar a operação matematica Ex.: print (int (n_1)+int(n_2))
print(n_1 + n_2) # print (int (n_1)+int(n_2))
print('A soma do valor',n_1, 'com o valor',n_2,'resulta no valor', n_1 + n_2)
print('=====================')

'''
Alternativa - 2
n_1 = input('Digite o primeiro valor:  ')   
n_2 = input('Digite o segundo valor:  ')
print( int(n_1) + int(n_2)) 
'''