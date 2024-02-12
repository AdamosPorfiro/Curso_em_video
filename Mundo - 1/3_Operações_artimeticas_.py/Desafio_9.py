"""

Desafio 9

Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

5 Q's

1 - Quais são os dados de entrada?
- Um numero inteiro

2 - O que devo fazer com esses dados?
- Mostrar na tela para o usuario a tabuada no numero que ele informou

3 - Quais são as restrições do problema?
- Apenas numeros inteiros

4 - Qual o resultado esperado?
- Tabuada do numero informado

5 - Quais os passos necessarios para se alcançar o resultado?
- input n
- print 1xn=n*1 2xn=n*2 3xn=n*3 4xn=n*4 5xn=n*5 6xn=n*6 7xn=n*7 8xn=n*8 9xn=n*9 10xn=n*10

"""
print("{:=^50}".format(" Desafio 9 "))
n = int(input("Informe um numero para saber sua tabuada: "))
print("\nTabuada do {}".format(n))
print("{} x {:2} = {:2}".format(n,1,n*1))
print("{} x {:2} = {:2}".format(n,2,n*2))
print("{} x {:2} = {:2}".format(n,3,n*3))
print("{} x {:2} = {:2}".format(n,4,n*4))
print("{} x {:2} = {:2}".format(n,5,n*5))
print("{} x {:2} = {:2}".format(n,6,n*6))
print("{} x {:2} = {:2}".format(n,7,n*7))
print("{} x {:2} = {:2}".format(n,8,n*8))
print("{} x {:2} = {:2}".format(n,9,n*9))
print("{} x {} = {}".format(n,10,n*10))
print("{:=^50}".format(""))