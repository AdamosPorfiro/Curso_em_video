'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre
o seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40: Obesidade mórbida;

'''
print("-="*25)
print("\33[1;34m{:>34}\33[m".format(" Calculadora de IMC "))
print("-="*25)
peso = float(input("Informe o seu peso em kg: "))
altura = float(input("Informa a sua altura: "))
imc = peso/(altura**2)
print(f"O IMC está em {imc:.2f} com status ", end="")

if imc < 18.5:
    print("\33[1;31mABAIXO DE PESO\33[m")
elif imc <= 25:
    print("\33[1;32mPESO IDEAL\33[m")
elif imc <= 30:
    print("\33[1;34mSOBREPESO\33[m")
elif imc <= 40:
    print("\33[1;33mOBESIDADE\33[m")
else:
    print("\33[1;31mOBESIDADE MORBIDA\33[m")
print("-="*25)