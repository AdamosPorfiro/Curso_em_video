'''
Crie um programa que leia duas notas do aluno e calcule a sua média, mostrando uma mensagem
no final de acordo com a média atingida:

- Média abaixo de 5.0: Reprovado;
- Média entre 5.0 e 7.0: Recuperação;
- Média 7.0 ou superior: Aprovado;

'''
print("-=" * 20)
print("{:>25}".format(" Desafio 40 "))
print("-=" * 20)
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = nota1*nota2/2

if media < 5:
    situação = "REPROVADO"
elif media >= 5 and media < 7:
    situação = "em RECUPERAÇÂO"
else:
    situação = "APROVADO"
print(f"Você está {situação}")
