'''
Crie um programa onde o usuario passa a digitar varios valores númericos e cadastre-os em
uma lista. Caso o número já exista lá dentro, ele não será adicionado.

No final, serão exibidos todos os valores únicos digitados, em ordem crescente
'''
numeros = []

while True:
    print("-="*15)
    num = int(input("Digite um número: "))
    #Verifica se existe algum numero repetido na lista
    if num in numeros[0:]:
        print("Número informado já existe na lista")
        print("-="*15)
    #Se não tiver nenhum número repetido ele prossegue adicionando o numero informado a lista
    else:
        numeros.append(num)
        print("Número cadastrado com sucesso!!!")
        print("-="*15)
    while True:
        continuar = str(input("Deseja continuar [S|N]: ")).strip().upper()
        #Continue executando a variavel continuar caso nao informe o valor solicitado corretamente
        if continuar not in 'SN':
            print("Ops, ERRO! digite corretamente")
            continue
        #Caso digite S o programa sai da variavel continuar e repete a variavel num
        if continuar in 'S':
            break
        #Caso digite N o programa encerra e mostra o resultado
        if continuar in 'N':
            break
    #Verificação de repetição do loop
    if continuar in 'S':
        continue
    #Verificação de saída do loop
    elif continuar in 'N':
        break 
print(sorted(numeros))