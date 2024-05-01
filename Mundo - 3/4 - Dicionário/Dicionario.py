"""
Dicionarios são estruturas de dados semelhantes as tuplas e listas porém, podemos usar  indices literais, usando letras, palavras

Dicionarios são identificados por {Chaves}
podemos declarar com chaves ou usando Função dict()
ex:

dados = {'Pedro', 25}
           nome  idade <<<< Indices
dados = {"nome: Pedro", "idade: 25"}
print(dados['nome'])  <<<<<< nome
print(dados['idade']) <<<<<< idade
dados["sexo"] = "M"   <<<<<< cria indice com nome sexo e adiciona M dentro  
deldados['idade']


filme = {
    'titulo': 'Star wars',
    'ano': 1977,
    'diretor': 'Geroge Lucas'
}

print(filme.values()) #Mostra os valores
print(filme.keys()) #mostra os indices(chaves)
print(filme.items()) #Mostra os dois valores e indices(chaves)
for k, v in filme.items():
    print(f"O {k} é {v}")

pessoas = {
    'nome': 'Gustavo', 
    'sexo': 'M', 
    'idade': 22
    }

print(f"O {pessoas["nome"]} tem {pessoas["idade"]} anos")
#del pessoas['sexo']
pessoas['nome'] = 'Adamos'
pessoas['idade'] = 30
pessoas['peso'] = 110,5
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k,v in pessoas.items():
    print(f"{k} = {v}")

brasil = []
estado_1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado_2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado_1)
brasil.append(estado_2)

print(estado_1)
print(estado_2)
print(brasil[0]['uf'])
"""

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input("Unidade Federativa: "))
    estado['sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f"O campo {k} tem valor {v}") 