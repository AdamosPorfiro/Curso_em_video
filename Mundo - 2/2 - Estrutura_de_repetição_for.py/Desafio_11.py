'''
Desenvolva um programa que leia, nome, idade e sexo de quatro pessoas. No final do programa mostre:

- A média de idade do grupo;
- Qual é o nome do homem mais velho;
- E quantas mulheres tem menos de 20 anos;
'''
# Ler todos os dados de entrada e armazenar nas respectivas listas;
nome = []
idade= []
sexo = []
for c in range(2):
    n = str(input('Qual o seu nome?\nNome: '))
    i = int(input('Qual a sua idade?\nIdade: '))
    s = int(input('Qual o seu sexo? 1 - Masculino  2 - Feminino\nEscolha: '))
    nome.append(n)
    idade.append(i)
    if s == 1:
        s = 'Masculino'
        sexo.append(s)
    elif s == 2:
        s = 'Feminino'
        sexo.append(s)
#Vamos calcular a média de idade;
soma = 0
for item in idade:
    soma = (soma + item)
print('\nA média de idade é: {:.0f}'.format(soma/2))
# Qual o nome do homem mais velho?
m_idade = idade[0]
for f in range(len(idade)):
    if  f>m_idade:
        m_idade = f # Identificado o indice da maior idade
        print(m_idade)


