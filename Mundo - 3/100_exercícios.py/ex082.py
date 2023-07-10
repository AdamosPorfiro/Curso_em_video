'''
Crie um programa onde o usuario digite uma expressão qualquer que usa parentêses, seu
aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
fechado na ordem correta.
'''
from sympy import sympify, symbols
expr = input('Digite uma expressão matematica: ')
Simbolos = symbols('x y ()')
try:
    expr = sympify(expr)
    print('Expressão é válida!')

except(SyntaxError,TypeError):
    print('Expressão não é válida!')