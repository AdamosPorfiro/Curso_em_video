'''
Desenvolva um programa que leia, nome, idade e sexo de quatro pessoas. No final do programa mostre:

- A média de idade do grupo;
- Qual é o nome do homem mais velho;
- E quantas mulheres tem menos de 20 anos;
'''

def processar_dados():
    nome = []
    idade = []
    sexo = []
    media = 0
    maior_idade = 0
    homem_mais_velho = ''
    qtd_mulher_menor_20 = 0
    for c in range(1,5):
        print('----------------- {}°Pessoa -----------------'.format(c))
        n = str(input('Nome completo: ')).strip()
        i = int(input('Idade: '))
        s = int(input('1 - Masculino 2 - Feminino: '))
        print('{:=^50}'.format(''))
        nome.append(n)
        idade.append(i)
        if i == i:
            media = (media+i)
        if s == 1:
            s = 'Masculino'
            sexo.append(s)
            if i>maior_idade:
                homem_mais_velho = n
                maior_idade = i
                if s == 1 and i > maior_idade:
                    maior_idade = i
        elif s == 2:
            s = 'Feminino'
            sexo.append(s)
            if i<20:
                qtd_mulher_menor_20 = qtd_mulher_menor_20+1
        elif s != 1 and s != 2:
            print('Algo deu errado, tente novamente!')
            return
    print('''\nA média de idade do grupo é de:{:.0f}
        \nO homem mais velho tem {} anos e se chama: {}
        \nQuantidade de mulheres menores de 20 anos é: {}'''
        .format(media/4,maior_idade,homem_mais_velho,qtd_mulher_menor_20
        ))
processar_dados()












