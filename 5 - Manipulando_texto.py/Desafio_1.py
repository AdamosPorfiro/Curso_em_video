'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

-> O nome com todas as letras maiusculas;
-> O nome com todas as letras minusculas;
-> Quantas letras ao todo sem considerar os espaços;
-> Quantas letras tem o primeiro nome;

Metodo dos 5 Q's

1 - Quais são os dados de entrada?
R:  input Nome_completo

2 - O que devo fazer com esses dados?
R: Deve mostrar o nome com todas as letras minusculas e depois minusculas;
   Quantas letras tem ao todo sem considerar os espaços entre cada plavra(nome);
   Quantas letras tem o primeiro nome.

3 - Quais são as restrições desse problema?
R: Apenas string e funções do python vamos usar.

4 - Qual o resultado esperado?
R: input Nome_completo
-> O nome com todas as letras maiusculas;
-> O nome com todas as letras minusculas;
-> Quantas letras ao todo sem considerar os espaços;
-> Quantas letras tem o primeiro nome;

5 - Quais são os passos necessarios para se alcançar o resultado esperado?
R: 

#1 - input nome_completo;
#2 - Variavel_1 = "".join(nome_completo.split());
#3 - Variavel_2 = nome_completo.split();
#4 - Print nome_completo.upper / nome_completo.lower / nome_junto / len(Variavel_2[0]).
'''
print('=' * 40)
nome = str(input('Nome completo: '))
nome_junto = "".join(nome.split())
p_n = nome.split()
print('\nAnalisando o seu nome...\nTudo maiúsculo:', nome.upper(),'\nTudo minúsculo:', nome.lower(),'\nQuantidade de caracteres ao todo:', len(nome_junto),'\nQuantidade de caracteres 1° nome:',len(p_n[0]),'\n' + "=" * 40)