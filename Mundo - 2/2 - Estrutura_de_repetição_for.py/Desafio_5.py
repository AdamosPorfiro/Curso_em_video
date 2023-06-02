'''
Desenvolva um programa que leia 6 numeros inteiros, e mostre a soma apenas daqueles que forem pares, se o valor digitado for
impar desconsidere-o


'''

print('Soma dos valores pares')
# Receber os dados
soma = 0 # Iniciar uma variavel 0, que vai armazenar a soma dos elementos pares;
cont = 0
for c in range(1, 7): # Faço um contador for que vai repetir 6 vezes;
     n1 = int(input('Informe o {} º valor: '.format(c))) # Pergunto para o usuario o numero desejado;
     if n1%2==0: # Monto uma estrutura de condição que vai verificar se o numero informado é par;
        soma += n1 # Chamo a variavel soma que vai somar o valor par digitado com o que estiver armazenado. Ex: 0+2=2 na segunda vez vai ser 2+4=6 e assim por diante;
        cont += 1
print('Você informou {} pares.\nSoma de todos eles fica {}.'.format(cont,soma)) # Exibo para o usuario o resultado da soma de todos os valores;
        
        
        
