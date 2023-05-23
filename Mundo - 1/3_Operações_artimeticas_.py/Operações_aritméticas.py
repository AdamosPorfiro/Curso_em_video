'''
Operações aritméticas

O que são operações aritméticas?
-> Executam operações matematicas, ou seja, calculos. Em programação usamos simbolos para representar esses operadores e realizar calculos:

+ = Adição;
- = subtração;
/ = Divisão;
* = Multiplicação;
** = Potência(Raiz quadrada);
// = Divisão inteira;
% = Portcentagem (Não calcula porcentagem, mas modulo que é o resto da divisão).

5 + 2 == 7  -> operando + operando igual a 7
5 - 2 == 3 
5 / 2 == 2.5
5 * 2 == 10
5 ** 2 == 25
5 // 2 == 2
5 % 2 == 1

Ordem de precedência:

->1° A ser executado e resolvido () dentro de parenteses;
->2° A ser executado e resolvido ** potência;
->3° A ser executado e resolvido * / // % multiplicação, divisão, divisão inteira, modulo(resto da divisão);
->4° A ser executado + - soma, subtração.

'''

'''
print (5+3*2) # 1° executado multiplicação 3 * 2 = 6 + 5 = 11 e por ultimo a soma;
print (5*3+4**2) # 1° executado potência 4**2 = 16 e 2° executado multiplucação 5 * 3 = 15 e 3° executado é a soma, somando os 2 resultados 16 + 15 = 31;
print (3*(5+4)**2) # Nesse caso devido ao parentese, ele tem maior prioridade sendo 3 + 4 = 7 ** 2 = 49 * 3 = 243 em seguida 2° potência e 3° multiplicação;
print(4**3) 
print(pow(4,3)) # Podemos usar os operadores e tambem a função interna de potência(Lembrando que utilizando a função a ordem de precedencia é perdida);
print(81**(1/2)) # Calcular a  raiz quadrada de um numero é a mesma coisa que criar a potência dele por meio;
print(127**(1/3)) # Raiz cubica;
print ('oi' + 'olá') # Ele vai juntar oi com olá;
print('oi' * 5) # Repete "oi" 5x;
print('oi' * 20) # Repete "oi" 20x;
print('='*50)


nome = str(input ('Qual o seu nome? '))
print ('É prazer te conhecer {:<20}!'.format(nome)) # Faz alinhamento a esquerda com 20 espaços, utlizando ">" ele fara a direita, usando "^" ele fica centralizado e "=^" exibi o nome dessa forma: =====nome===== utilizando 20 espaços;


n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
print ('A soma vale {}'.format(n1+n2)) # Nesse caso nao precisamos de outro variavel, seria necessario caso fossemos usar em outro momento;

print('=' * 50)


n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
a  = n1 + n2
b = n1 * n2
c = n1 / n2
d = n1 // n2
e = n1 ** n2
print('A soma é: {} o produto é: {} e a divisão é: {:.2f}'.format(a, b, c)) # Fazendo o calculo com 4 e 3 na divisão o numero é real com varias casas decimais, podemos limitar isso utlizando :.2 casas decimais e f de flutuantes;
print ('A divisão inteira é: {} e a potência é: {}'.format(d, e))

'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
a  = n1 + n2
b = n1 * n2
c = n1 / n2
d = n1 // n2
e = n1 ** n2
print('\nA soma é: {}\nO produto é: {}\nDivisão é: {:.2f}'.format(a, b, c), end='.  ')  # Podemos usar "end" para dizer que mesmo com 2 prints não haverá quebra de linha, então ele vai exibir os 2 prints na mesma linha 
print ('A divisão inteira é: {}Potência é: {}'.format(d, e)) # Podemos utilizar tambem "\n" nova quebra de linha, para quebrar linhas e organizar os prints um abaixo do outro, como desejar.

