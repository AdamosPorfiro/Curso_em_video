'''
===== Exercício 20 =====

O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

1 - Quais são os dados de entrada?
-> import biblioteca random a função shuflle
-> input grupo_1;
-> input grupo_2;
-> input grupo_3;
-> input grupo_4;

2 - O que devo fazer com esses dados?
-> Vai sortear a ordem de apresentação de quatro grupos de alunos e mostrar a ordem sorteada

3 - Quais são as restrições desse problema?
-> Iremos sortear uma ordem de elementos usando biblioteca shuffle

4 - Qual o resultado esperado?
-> Exibir na tela a ordem sorteada

5 - Quais são os passos para se alcançar o resultado?
-> Importar a biblioteca random função shuffle
-> input grupo_1;
-> input grupo_2;
-> input grupo_3;
-> input grupo_4;
-> Declaro variavel que vai ser minha lista de grupos e dentro dela coloco os inputs grupos[grupo1, grupo 2...];
-> Uso a função shuffle na lista;
-> Print a lista grupos;

'''
print('\n'+ '=' * 21, 'Embaralhador de elementos', '=' * 21)
from random import shuffle
grupo1 = str(input('Digite nome do 1° grupo: '))
grupo2 = str(input('Digite nome do 2° grupo: '))
grupo3 = str(input('Digite nome do 3° grupo: '))
grupo4 = str(input('Digite nome do 4° grupo: '))
grupos = [grupo1, grupo2, grupo3, grupo4]
shuffle(grupos)
print('\nApresentação será na ordem: ', grupos,'\n' + '=' * 70)
