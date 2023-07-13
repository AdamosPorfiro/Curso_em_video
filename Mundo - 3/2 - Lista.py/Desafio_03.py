"""
Crie um programa onde o usuario pode digitar cinco valores númericos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort())

No final, mostre a lista ordenada na tela.
"""
'''
l_n = [] # Lista vazia
for c in range(5): # Vai repetir 5x o input
    n = int(input("Digite um número: ")) # input
    if len(l_n) == 0: # Verificar se a listá está vazia 0
        l_n.append(n) # Se estiver vazia ele vai armazenar um valor digitado
    else: # se não
        index = 0 # Variavel que vai ser a chave de cada elemento criar dentro da lista
        while index < len(l_n) and n > l_n[index]: # Em quanto chave for < quantidade de elementos e n > que o ultimo elemento dentro da chave determinada por ultimo
            index += 1 # Ele vai adicionar +1 ao index e então index passa a ser 1...2...3... e assim por diante
        l_n.insert(index, n) # E vai inserir o index que é a chave e armazenar n input do usuario dentro
print(f"Você digitou os valores {l_n}") # Vamos printar a lista


l_n = [] # Lista vazia
for c in range(5): # Repetir 5 vezes o input
    n = int(input('Digite um número: ')) # input
    if len(l_n) == 0: # Vai verificar se está vazia, se sim ele armazena n na lista
        l_n.append(n)
    else: 
        chave = 0 # Vai ser o indice que vai nos guiar dentro da lista
        while chave < len(l_n) and n > l_n[chave]: # Em quanto chave = indice for menor que o comprimento da lista e n > que o elemento dentro da lista
            chave+=1 # Se for verdadeiro ele adiciona +1 ao indice, para verificar, se der falso, ele sai do loop
        l_n.insert(chave,n) # E inseri a chave e o numero informado pelo usuario
print(f'Você digitou os números: {l_n}') # e imprimi na tela para o usuario
'''
l_n = [] # Lista vazia
for c in range(5): # Laço repetição 5x
    n = int(input('Digite um valor: ')) # input
    if c == 0 or n > l_n[-1]: # se c for igual a 0 ou n for maior que o último elemento da lista, então ele vai inserir um elemento no final da lista
        l_n.append(n)
        print('Adicionado no final da lista')
    else: # Senão
        pos = 0 # posição = 0
        while pos < len(l_n): # laço que vai passar pelas posições, Em quanto pos for menor que posição da lista
            if n <= l_n[pos]: # Se n for menor ou igual a algum elemento da lista da posição especifica
                l_n.insert(pos, n) # Insere um elemento ali
                print(f'Foi adicionado a posição {pos}')
                break # pausa o laço
            pos += 1 # Adiciona +1 ao pos
print(f'Os valores digitados em ordem foram {l_n}')