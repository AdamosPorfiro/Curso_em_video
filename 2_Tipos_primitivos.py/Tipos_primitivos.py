''' 
===== Tipos primeitivos =====

O que é tipos primitivos?
-> São um conjunto de tipos de dados básicos, existem 4 tipos primitivos mais básicos:

1 - int = 4, 0, -7, 2000 -> numeros inteiros;
2 - float = 4.7, 5.6, 0.0  -> numero real;
3 - bool = verdadeiro ou falso (True e False) -> Valores booleanos;
4 - str = olá, palavras, '5.6', ' ' - strings são palavras, caracteres ou simbolos;

'''


print('===== Tipos primitivos =====')

'''
n1 = input('Digite um número: ')
n2 = input('Digite mais número: ')
s = n1+n2 #O código não fara a soma, pois o sinal da operação soma, está funcionando como concatenação, unindo esses valores, pois eles são reconhecidos como strings(caracteres) e não numeros inteiros(numerais) para que seja feito a soma;
print('Resultado da soma é:{}'.format(s))
'''

# Para funcionar de forma que a operação matematica soma seja feita, é necessario converter os valores recebidos para tipos inteiros, utilizando a função int();
n1 = int(input('Digite um número: ')) #<- O dado recebido já é convertido para tipo inteiro e jogado em n1 como um numero inteiro;
n2 = int(input('Digite mais número: ')) #<- Perceba que a função deve fechar todo o input;
s = n1+n2 #<- Assim o dado convertido será reconhecido como um numero inteiro e a operação será feita corretamente;
print('A soma entre {}+{} vale: {}'.format(n1, n2, s)) 

#Type: Dentro da função print vai printar o tipo primitivo dos dados que serão exibidos na tela
n_1 = input('Digite um numero: ') 
print (type(n_1)) # Type, valida pra gente o tipo primitivo dos dados que foram armazenado e serão exibidos na tela; nesse caso é str


np1 = input('Digite algo ')
print (np1.isnumeric()) # Vai perguntar se np1 é numérico Ex.: np1 = 5 = True ou np1 = 3a = False (3 é numerico, "a" não é);

np1 = input('Digite algo ')
print (np1.isalpha()) # Vai perguntar se np1 é letra;
