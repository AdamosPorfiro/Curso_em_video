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
    situação = "\33[1;31mREPROVADO\33[m"
elif media >= 5 and media < 7:
    situação = "\33[1;33mRECUPERAÇÂO\33[m"
else:
    situação = "\33[1;32mAPROVADO\33[m"
print(f"A sua média é de {media}.\nA sua situação é {situação}")
print("-=" * 20)
