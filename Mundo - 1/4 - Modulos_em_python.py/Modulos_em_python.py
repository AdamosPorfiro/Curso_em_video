'''
O que são modulos em python?
R: São arquivos  que contem definições e comandos em python que são usados para trazer certas funcionalidades, 
tornando mais eficiente o código, gasto menor de memoria e código mais limpo.

Comando usar para adicionar modulos no python usamos o comando: 
import - > importa todo um conjunto de comandos de um módulo;
from (modulo) import (Nome do comando) -> Vai importar o modulo com apenas o comando especifico, que deseja usar;

biblioteca muito usada que vem com o phyton:

math = importa um modulo com funcionalidades matemáticas extras;
Ceil -> Faz arredondamentos pra cima;
floor -> Faz arredondamentos para baixo;
trunc -> Vai truncar um numero, eliminando da virgula adiante, sem fazer arredondamento
pow -> Potência;
sqrt -> Pra calcular raiz quadrada;
factorial -> Calcula o fatorial de um numero.

Aqui possui todas as funções e o seu objetivo:
https://docs.python.org/pt-br/3/library/math.html?highlight=matematicos

exemplo para importar apenas uma das funcionalidade: "from math import factorial" ou "from math import factorial, sqrt".

'''
'''
print('\n'+'=' * 6,'Importando todo o modulo', '=' * 6,'\n')
import math
num = int(input('Digite um numero\n'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {} arredondado pra cima\nA raiz de {} é igual a {} arredondado pra baixo\nA raiz quadrada de {} é igual a {} Sem arredondamento e virgula'.format(num, math.ceil(raiz), num, math.floor(raiz), num, math.trunc(raiz)))
#Repare que o trunc e o floor obtem o mesmo resultado, porém cuidado ao usa-los, use conforme o necessario;


print('\n'+'=' * 6,'Importando apenas funcionalidade', '=' * 6,'\n')
from math import sqrt,ceil
num = int(input('Digite um numero\n'))
raiz = sqrt(num)
print('A raiz quadra de {} é igual a {}'.format(num, ceil(raiz)))


print('\n'+'=' * 6,'Gerando numeros aleatórios', '=' * 6,'\n')
import random
num = random.randint(1, 10)#Gera numeros aleatórios de 1 a 10. radon gera numeros aleatórios com decimais entre 0 e 1
print(num)


import emoji# Para instalar essa funcionalidade, foi necessario instalar a biblioteca usando pip install emoji. Disponivel na comunidade python PyPi;
print(emoji.emojize('Olá, mundo 🌍')) # Para vermos quais são os pacotes de modulo instalados basta abrir o terminal e digitar "pip list";
# Para desinstalar basta usar o comando no terminal: pip uninstall "nome do modulo";

'''