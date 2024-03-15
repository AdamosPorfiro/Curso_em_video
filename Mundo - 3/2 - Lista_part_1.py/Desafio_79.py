'''
Crie um programa onde o usuario passa a digitar varios valores númericos e cadastre-os em
uma lista. Caso o número já exista lá dentro, ele não será adicionado.

No final, serão exibidos todos os valores únicos digitados, em ordem crescente
'''
numeros = []
while True:
    num = int(input("Digite um número: "))
    numeros.append(num)
    print("Número cadastrado com sucesso!!!")
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