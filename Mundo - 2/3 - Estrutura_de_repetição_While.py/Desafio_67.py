'''
Faça um programa que faça a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
O programa será interronpido quando o valor digitado for negativo.
'''
print("-="*18)
print("{:>23}".format(" Desafio 67 "))
print("-="*18)
while True:
    print("="*50)
    n = int(input("Quer ver a tabuada de qual valor: "))
    for c in range(1,11):
        if n < 0:
            break
        else:
            print(f"{n} x {c:2} = {c*n:2}")
    if n < 0:
        print("="*50)
        break
print(f"Programa de tabuada \33[1;31mENCERRADO\33[m Volte sempre!!!")
