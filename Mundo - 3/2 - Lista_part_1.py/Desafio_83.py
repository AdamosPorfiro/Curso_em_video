'''
Crie um programa onde o usuario digite uma expressão qualquer que usa parentêses, seu
aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
fechado na ordem correta.

from sympy import sympify, symbols # Modulo sympy que faz verificação de expressões matematicas
expr = input('Digite uma expressão: ') # Input expressão
Simbolos = symbols('x y ()') #
try:
    expr = sympify(expr)
    print('A expressão é valida')

except(SyntaxError, TypeError):
    print('Expressão Invalida!')
'''

conchetes_abre = []
conchetes_fecha = []
expressão = str(input("Digite uma espressão matemática: "))

#Criamos um FOR para passar por cada conchete que abre e fecha para armazena-los
for c in expressão:
    if c in '(':
        conchetes_abre.append(c)
    if c in ')':
        conchetes_fecha.append(c)

#A cada vez que ele passa o laço ele remove o último conhecete que abre
    if len(conchetes_abre) >= 1 and len(conchetes_fecha) >= 1:
        conchetes_abre.pop()
        conchetes_fecha.pop()

#Verifica as listas para confirmar se os conchetes estão corretos
if len(conchetes_abre) == 0 and len(conchetes_fecha) == 0:
        print("Expressão válida!")
        print(conchetes_fecha)
else:
    print("Expressão inválida!")
    print(conchetes_fecha)