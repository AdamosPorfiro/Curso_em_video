'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre
o seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40: Obesidade mórbida;

'''
print("-="*20)
print("\33[1;34m{:>29}\33[m".format(" Calculadora de IMC "))
print("-="*20)
peso = float(input("Informe o seu peso em kg: "))
altura = float(input("Informa a sua altura: "))
imc = (peso/altura)/altura

if imc < 18.5:
    print(f"O seu IMC é de {imc:.2f} e você está abaixo do peso")
elif imc >= 18.5 and imc <= 25:
    print(f"O seu IMC é de {imc:.2f} e você está no peso ideal")
elif imc >= 25 and imc <= 30:
    print(f"O seu IMC é de {imc:.2f} e você está com sobrepeso")
elif imc >= 30 and imc <= 40:
    print(f"O seu IMC é de {imc:.2f} e você está com obsidade")
else:
    print("Você está com obesidade mórbida")
print("-="*20)