"""
Melhore o DESAFIO 51, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
print("-="*20)
print("{:>25}".format(" Desafio 62 "))
print("-="*20)

termo = int(input("Informe o termo: "))
razão = int(input("Informe a razão: "))
sair = 0
pa = termo

while sair < 10:
    pa += razão
    sair += 1
    print(f"{pa}", end= ' ⮕ ')
mais_termos = int(input("\nDeseja ver mais termos? Quantos, se deseja sair digite 0:  "))




    
