"""
Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.

- Para salário superiores a R$1.250.00, calcule um aumento de 10%.

- Para os inferiores ou iguais, o aumento é de 15%

Analise: Vamos perguntar o salário de um funcionário e em seguida calcular o aumento desse salario:

Sendo, se o salário for superior a R$ 1.250.00 o aumento será de 10%;

senão o aumento será de 15%;

1 - Quais são os dados de entrada?
- input salario;

2 - O que devo fazer com esses dados?
- Calcular o valor do aumento desse input com base no valor, caso seja um valor menor que R$ 1250.00 o aumento é de 15%;
Senão o caso seja valores maiores que isso o aumento é de 10%;

3 - Quais são as restrições desse problema?
- Para valores maiores de R$1.250,00 o aumento é de 10%;
- Para valores menores ou igual a R$ 1.250,00 o aumento é de 15%;

4 - Qual o resultado esperado?
- Que o valor do aumento do salário do usuario seja calculado corretamente]
- Sendo 10% para salarios acim de R$1250,00;
- e 15% para salários abaixo ou igual a R$ 1250,00;

5 - Quais são os passos necessarios para se alcançar o resultado esperado?
-> input salário;
-> if salário >= 1251;
        print O aumento é de 10%, portanto o aumento fica R$ salário * (10/100) e total é R$ salário * (10/100) + salário;;
-> else:
        print O aumento é de 15%, portanto o aumento fica R$ salário * (15/100) e o total é de R$ salário * (15/100) + salário;

"""
print("\n" + "=" * 52, "\nUse ponto para separar os decimais. Ex: R$ 1300.75")
s = float(input("\nDigite o seu salário\nR$ "))
if s >= 1251:
    print(
        "\nO valor do aumento é de 10%, sendo R$ {:.2f}\nTotal R$ {:.2f}".format(
            s * (10 / 100), s * (10 / 100) + s
        )
    )
else:
    print(
        "\nO valor do aumento é de 15%, sendo R$ {:.2f}\n Total R$ {:.2f}".format(
            s * (15 / 100), s * (15 / 100) + s
        )
    )
print("=" * 52)
