'''
Listas compostas
São lsitas dentro de listas


Variavel1 = []
variavel2 = [['nome', idade] ['nome', idade]]
                0        1       0       1   
                indice 0         indice 1   

teste = []
teste.append('Gustavo')
teste.append(40)
galera_1 = []
galera_1.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera_1.append(teste)
print(galera_1)
galera_2 = [['Adamos', 29], ['Pedro', 15], ['João', 25], ['Alesson', 19]]
print(galera_2[0])
print(galera_2[0][1])
print('=' * 30)
for p in galera_2:
    print(f'{p[0]} tem {p[1]} anos de idade')
    
galera = []
dado = []
totalmai = totalmeno = 0
for c in range (0,3):
    dado.append(str(input('Digite nome: ')))
    dado.append(int(input('Digite idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera,'\n')

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totalmai +=1
    else:
        print(f'{p[0]} é menor de idade')
        totalmeno += 1
print(f'Temos {totalmai} maiores e {totalmeno} menores de idade')


galera = [['João', 19],['Ana', 33],['Joaquim',13],['Maria', 45]]
for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idade")
    '''
galera = []
dado = []
total_maior = total_menor = 0

#Vai armazenar e criar uma copia dos arquivos e depois limpar uma das listas
for c in range(0,3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

#Analise de maiores e menores de idade e o total de cada um
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade")
        total_maior += 1
    else:
        print(f"{p[0]} é menor de idade")
        total_menor += 1
print(f"Temos {total_maior} maiores e {total_menor} menores")