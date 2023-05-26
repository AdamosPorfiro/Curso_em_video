'''
Crie um programa que leia duas notas do aluno e calcule a sua média, mostrando uma mensagem
no final de acordo com a média atingida:

- Média abaixo de 5.0: Reprovado;
- Média entre 5.0 e 6.9: Recuperação;
- Média 7.0 ou superior: Aprovado;

Analisar: Para calcularmos a média usamos a soma de um conjunto de elemento e dividimos pela
quantidade de elementos: 

Formula fica: 
    Ex: nota 1 = 8 | nota 2 = 10
    soma = nota 1 + nota 2
    soma = 8 + 10 = 18
Média:
    Quantidade de elementos no conjunto é de: nota 1 = 8 | nota 2 = 10 são 2 elementos;
    média = soma / qtd. elementos
    média = 18 / 2
    média = 9

    A média desse aluno é de 9.

1 - Quais são os dados de entrada?
input nota_1
input nota_2

2 - O que devo fazer com esses dados?
Calcular a média e exibir na tela para o usuario conforme a sua média:
- Média abaixo de 5.0: Reprovado;
- Média entre 5.0 e 6.9: Recuperação;
- Média 7.0 ou superior: Aprovado;

3 - Quais são as restrições do problema?
- Média abaixo de 5.0: Reprovado;
- Média entre 5.0 e 6.9: Recuperação;
- Média 7.0 ou superior: Aprovado;

4 - Qual é o resultado esperado?
Calcular a média e exibir na tela para o usuario informações conforme a sua média:
- Média abaixo de 5.0: Reprovado;
- Média entre 5.0 e 6.9: Recuperação;
- Média 7.0 ou superior: Aprovado;

5 - Quais são os passos necessarios para se alcançar o resultado esperado?
input nota_1
input nota_2
r = nota_1 + nota_2 / 2
if r < 5.0
    print Média abaixo de 5.0 você está: Reprovado
elif r >= 5.0 and r <= 6.9
    print Média entre 5.0 e 6.9 você está: Recuperação
else
    print Média {} você está: Aprovado
'''
#Recebendo o input e calculando media;
n1 = float(input('Informe nota 1: '))
n2 = float(input('Informe nota 2: '))
media = (n1 + n2) / 2
#condições com base na nota;
if media < 5:
    print('A sua média é: {:.1f} e está {}REPROVADO!{}'.format(media,'\033[1;31m', '\033[m'))
elif media >= 5 and media <= 6.9:
    print('A sua média é: {:.1f} e está em {}RECUPERAÇÃO{}'.format(media, '\033[1;33m', '\033[m'))
else:
    print('A sua média é: {:.1f} e está {}APROVADO{}'.format(media, '\033[1;32m', '\033[m'))