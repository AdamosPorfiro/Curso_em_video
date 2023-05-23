'''
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço
da passagem, cobrando R$0,50 por km para viagem de até 200km e R$ 0,45 para viagens
mais longas.

Analise: 
Vamos ler uma distância e se a distância for de até 200km vamos calcular cada km sendo R$ 0,50
Se não viagens mais longas serão R$ 0,45 cada km;

1 Quais são os dados de entrada?
- input distância;
- variavel 1 = distância * 0.50;
- Variavel 2 = distância * 0.45.

2 - Oque devo fazer com esses dados?
- Deve Calcular o preço da passagem, cobrando R$0,50 por km para viagem de até 200km 
e R$ 0,45 para viagens mais longas.

3 - Quais são as restrições desse problema?
- Numero decimais;
- Viagens até 200km é R$ 0.50
- Viagens acima de 200km é R$ 0.45

4 - Qual é o resultado esperado?
- Exibir para o usuario o valor da viagem com base nos kilometros da viagem.

5 - Quais são os passos para se alcançar o resultado?
*1 input Distância
*2 if Distância <= 200 
        r = Distância * 0.50 
        print O valor da viagem é de R$ r
    else 
        r = Distância * 0.45
        print O valor da viagem é de R$ r
'''
print('\n' + '=' * 8,'Calculadora - Preço de viagens', '=' * 8)
d = float(input('\nQual a distância da sua viagem?\nDistância (km): '))
if d <= 200:
    r = d * 0.50
    print('O valor da sua passagem é de R$ {:.2f}'.format(r))
else:
    r = d * 0.45
    print('O valor da sua passagem é de R$ {:.2f}'.format(r))
print('=' * 48)