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
expr = str(input('Digite uma expressão: '))
pilha = []
for símb in expr:
    if símb == '(':
        pilha.append('(')
    elif símb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está invalida!')