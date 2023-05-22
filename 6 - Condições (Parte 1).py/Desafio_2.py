'''
Escreva um programa que leia a velocidade de um carro.

- Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.

- A multa vai custar R$7,00 por cada km acima do limite.

Analise critica:
Vamos ler a velocidade do carro, pedindo para o usuario um input da velocidade que ele estava;
Se o carro estiver acima de 80km/h vamos print uma mensagem dizendo que ele foi multado e
em seguida outro print exibindo o valor da soma de R$ 7,00 por a cada km acima do permitido. Ex.:
Se a pessoa estiver a 95km/h vamos exibir você foi multado e recebera uma multa no valor de R$ 105,0
multiplicando o excedente de 15km com o valor de cada km R$ 7,00.

1 - Quais são os dados de entrada?
- input velocidade_carro.

2 - O que devo fazer com esses dados?
- Deve ler a velocidade;
- Deve dizer se vai tomar multa ou não;
- Deve mostrar o valor da multa com base de R$ 7.00 por km ultrapassado.

3 - Quais são as restrições desse problema?
- nenhuma.

4 - Qual é o resultado esperado?
- Ler a velocidade e exibir se usuario tomou multa ou não e o valor da multa a pagar.

5 - Quais são os passos para se alcançar o resultado esperado?
#1 input usuario;
#2 if input usuario >= 80 print Você foi multado e o valor da multa é:  input usuario - 80 * 7;
#3 if input usuario <= 79 print você não foi multado
'''

v = float(input('Qual velocidade que o carro estava?\nVelocidade: '))
if(v > 80):
    print('\nATENÇÂO, Você foi multado.\nO valor da multa é de R$ {:.2f}.'.format((v - 79) * 7))
else:
    print('\nPARABÉNS,Você não foi multado!')
print('Tenha um bom dia, dirija com segurança!\n')
    