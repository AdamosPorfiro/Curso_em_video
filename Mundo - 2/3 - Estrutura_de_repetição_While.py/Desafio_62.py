"""
Melhore o DESAFIO 51, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
print("-="*20)
print("{:>25}".format(" Desafio 62 "))
print("-="*20)

termo = int(input("Informe o termo: "))
razão = int(input("Informe a razão: "))
pa = int(input("Informe quantos termos deseja ver: "))
calculo = termo
qtd_termo = 0
mais_termos = 1
while mais_termos != 0:
    while pa != 0:
        calculo += razão
        pa -= 1
        print(f"{calculo-razão}", end= ' ⮕ ')
    print("Acabou")
    mais_termos = int(input("\nDeseja ver mais termos? Quantos, se deseja sair digite 0:  "))
    pa = mais_termos
    qtd_termo += pa
print(f"A progressão foi finalizada com {qtd_termo} termos mostrados")
print("-="*35)



    
