"""
Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.

"""
print("-="*20)
print("{:>25}".format(" Desafio 52 "))
print("-="*20)
n = int(input("Informe um numero inteiro: "))

divisor = 0
for c in range(1, n+1):
    if n % c != 0:
        print(f"\33[0;32m{c}\33[m",end=' ')
    if n % c == 0: # Se o numero informado for divisivel por 3 numeros ele não é primo
        print(f"\33[0;31m{c}\33[m",end=' ')
        divisor += 1
if divisor >= 3:
    print("\n"+"="*65)
    print(f"O número {n} foi divisível {divisor} vezes e por isso ele não é primo")
    print("="*65)
else:
    print("\n"+"="*65)
    print(f"Sim, o número {n} foi divisível {divisor} vezes e por isso ele é primo")
    print("="*65)
print("\n\33[0;31mvermelho\33[m é a indicação do numero que é divisivel pelo número que você informou")
print("\33[0;32mVerde\33[m é a indicação do numero que é não é divisivel pelo número que você informou")
print("-="*40)
    