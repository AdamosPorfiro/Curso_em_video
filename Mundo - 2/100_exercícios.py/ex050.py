'''
Desenvolva um programa que leia 6 numeros inteiros, e mostre a soma apenas daqueles que forem pares, se o valor digitado for
impar desconsidere-o


'''
print('{:=^30}\n{:^6}{}'.format('','','Soma de pares'))
soma = 0 # Inicio uma variavel 0 para armazenar a soma
for c in range(6): # Repetição dos comandos 6 vezes
    n1 = int(input('Informe um numero inteiro: ')) # Receber dados do usuario
    if n1%2 == 0: # Verificar se o numero é par
        soma += n1 # Somar e armazenar na variavel soma o resultado
print('A soma dos numero pares é: {}\n{:=^30}'.format(soma,''))