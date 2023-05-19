'''
Faça um programa que leia uma frase pelo teclado e mostre:

-> Quantas vezes apareçe a letra "A";
-> Em que posição ela aparece a primeira vez;
-> Em que posição ela aparece a ultima vez.

Analise critica: Vamos usar a função "count()" que vai contar quantas vezes a letra "A" apareçe na frase e usaro função "find()" que vai
indicar em que posição ele apareçe a primeira e ultima vez fin() = vai encontrar onde a letra apareçe a primeira vez e rfind() onde a letra 
apareçe a ultima vez

1 - Quais são os dados necessarios?
input frase;

2 - O que devo fazer com esses dados
Exibir: 
-> Quantas vezes apareçe a letra "A";
-> Em que posição ela aparece a primeira vez;
-> Em que posição ela aparece a ultima vez.

3 - Quais são as restrições desse problema?
A = Maiusculo

4 - Qual é o resultado esperado?
-> Quantas vezes apareçe a letra "A";
-> Em que posição ela aparece a primeira vez;
-> Em que posição ela aparece a ultima vez.

5 - Quais os passos para se alcançar o resultado esperado?
1 - input frase;
2 - converter tudo para maiusculo;
3 - print frase.count("A")
4 - print frase.find("A")
5 - print frase.rfind("A")

'''

frase = str(input('Digite uma frase\n'))
m = frase.upper()
print('\nApareçe {} vezes\nApareçe primeiro no indice {}\nApareçe a ultima vez no indice {}'.format(m.count("A"), m.find("A"), m.rfind("A")))