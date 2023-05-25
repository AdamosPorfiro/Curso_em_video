'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre
o seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40: Obesidade mórbida;

Analise: 
Vamos precisar do peso de uma pessoa em (kg) e altura em (m):
Peso: 108.56kg Altura: 1.95m

Usamos a formula: IMC = PESO / (ALTURA²), logo:
IMC = 108.56 / (1.95²)
IMC = 29.44

Entre 25 até 30 SOBREPESO;

1 - Quais são os dados de entrada?
- input peso
- input altura

2 - O que devo fazer com esses dados?
- Calcular o IMC do usuario e exibi-lo na tela indicando algumas informações como:
- Abaixo de 18.5: Abaixo do peso;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40: Obesidade mórbida;

3 - Quais são as restrições desse problema?
- Peso e altura são numero reais;
- Calcular IMC

4 - Qual é o resultado esperado?
- Calcular o IMC do usuario e exibi-lo para o usuario com algumas informações;
- Abaixo de 18.5: Abaixo do peso;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40: Obesidade mórbida;

5 - Quais são os passos necessarios para se alcançar o resultado?
1 - input peso e altura
2 - IMC = peso / (altura²)
3 - if IMC < 18.5
        print Abaixo do peso
    if IMC >= 18.5 and IMC < 25
        print Peso ideal
    if IMC >= 25 and IMC < 30
        print Sobrepeso
    if IMC >= 30 and IMC < 40
        print Obesidade
    else
        print Obesidade Móbida
'''

#Receber os dados de entrada e calcular o IMC;
print('\n' + '-=-' * 5, 'Calculadora IMC', '-=-' * 5)
p = float(input('\nInforme o seu peso '))
a = float(input('\nInforme o seu altura '))
IMC = p / (a**2)
#Criar as condições e exibi-las para o usuario;
if IMC < 18.5:
    print ('O seu IMC: {:.2f} e você está ABAIXO DO PESO'.format(IMC))
elif IMC >= 18.5 and IMC < 25:
    print('O seu IMC: {:.2f} e você está no PESO IDEAL'.format(IMC))
elif IMC >= 25 and IMC < 30:
    print('O seu IMC: {:.2f} e você está com SOBREPESO'.format(IMC))
elif IMC >= 30 and IMC < 40:
    print('O seu IMC: {:.2f} e você está com OBESIDADE'.format(IMC))
else:
    print('O seu IMC: {:.2f} e você está com OBESIDADE MÒRBIDA'.format(IMC))
print('\n' + '-=-' * 15)
