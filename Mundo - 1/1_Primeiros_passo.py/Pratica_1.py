'''
É chamado de função os codigos que  possuem () paranteses. Ex.: print()
Geralmente dentro dos parenteses teremos especificadores como '' aspas simples inidicando uma string ou
mesmo uma operação com sinais ou condicionais;

'''
print('Olá,mundo!') # Ele vai exibir na tela o que esta dentro do parentese com as aspas.

'''
Sintaxe vai dar erro, toda mensagem deve estar com aspas simples ou duplas
print(Olá, mundo)

'''
print(7+4) #Aqui o resultado será 11.

print ('7 '+'4') # Vai exibir os 2 numeros juntado-os, sendo assim será 74.

print('olá,mundo', 5) # Aqui ele vai exibir a olá, mundo e n° 5, porém o uso do sinal "+" nesse caso não é viavel e a sintaxe dará erro.

'''
Variaveis - utilizamos ela para armazenar informações, python reconhece essas informações como um objeto. Ex.:Idade, nome, peso.
Isso vai permitir que possamos usa-lá para algum fim, funcionalidade, cadastro, para exibir algo para usuario e etc.

idade = 11
= É igual a receber, então idade vai receber o valor 11.
'''

nome_1= 'Adamos' # Variavel nome, recebe, string (os caracteres) > A d a m o s;
idade_1= 29 # Variavel idade, recebe, numeros 29;
peso_1 = 100 # Variavel peso, recebe, numeros 100;
print(nome_1,idade_1,peso_1) # Podemos usar função print, para exibir para o usuario os valores armazenados dentro das variaveis.

'''
Para criarmos uma interação com o usuario utilizamos "input" que significa "leia" Ex.: 

nome=input('Qual é o seu nome?') <- Variavel nome, recebe o resultado do input que é o que o usuario irá digitar.

'''

nome=input('Qual é o seu nome?\n')  #Nome1 vai receber o input que o usuario irá interar(digitar);
idade=input('Qual é a sua idade\n')  #Idade1 vai receber o input que o usuario irá interar(digitar);
peso=float(input('Qual é o seu peso?\n'))   #Peso1vai receber o input que o usuario irá interar(digitar);
print("\nNome: {}\nIdade: {}\nPeso: {}Kg".format(nome,idade,peso)) # Vai exibir os valores, informações, objetos armazenados.
