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
#2 - Chamar a função upper com um print;
#3 - Chamar a função lower com um print;
#4 - CHamar a função replace para tirar os espaços e len para contar os caracteres;
#5 - Chamar a função find para achar o primeiro indice e contar o indice daquela palavra

'''
print('=' * 40)
nome = str(input('Nome completo: '))
nome1 = "".join(nome.split())
print ('\nTudo maiúsculo:', nome.upper(),'\nTudo minúsculo:', nome.lower(),'\nQuantidade de caracteres:',len(nome1),'\n' + nome1, '\n' + '=' * 40 )