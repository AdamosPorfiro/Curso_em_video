'''
Desenvolva um programa que leia, nome, idade e sexo de quatro pessoas. No final do programa mostre:

- A média de idade do grupo;
- Qual é o nome do homem mais velho;
- E quantas mulheres tem menos de 20 anos;
'''
nome = []
idade = []
sexo = []
media = 0
maior_idade = 0
homem_mais_velho = ''
qtd_mulher_menor_20 = 0
for c in range(4):
    n = str(input('Qual o seu nome?\nNome: '))
    i = int(input('Qual a sua idade?\nIdade: '))
    s = int(input('Qual o seu sexo? 1 - Masculino 2 - Feminino:\nEscolha: '))
    nome.append(n)
    idade.append(i)
    if s == 1:
        s = 'Masculino'
        sexo.append(s)
        if i>maior_idade:
            homem_mais_velho = n
            maior_idade = i
    
    elif s == 2:
        s = 'Feminino'
        sexo.append(s)
        if i<20:
            qtd_mulher_menor_20 = qtd_mulher_menor_20+1
    else:
        print('Ops, informação errada tente novamente!')
        break
    #Calcular média 
for item in idade:
    media = (media + item)
print('''\nA média de idade é de:{:.0f}
      \nO homem mais velho é: {}
      \nQuantidade de mulheres menores que 20 anos é: {}'''
      .format(media/4,homem_mais_velho,qtd_mulher_menor_20
    ))













