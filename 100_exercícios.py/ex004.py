# Faça um programa que  leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as  informações possiveis sobre ele.
"""
print('===== Exercício 4 =====')

n1 = input('Digite algo: ')
print (type(n1))
print ('Os dados digitados são alfabeticos?', n1.isalpha())
print ('Os dados digitados são numericos?', n1.isalnum())
print ('Os dados digitados são numeros decimais ?', n1.isdecimal())
print ('Os dados digitados são alfabeticos e numericos ?', n1.isalnum())
print ('Os dados digitados são espaços em branco ?', n1.isspace()) # Deve ter um espaço vazio (space) do teclado;
print ('Os dados digitados são do padrão ASCII?', n1.isascii()) # Hello ou 12345;
print ('Os dados digitados são todos digitos?', n1.isdigit())
print ('Os dados digitados é um identificador valido?', n1.isidentifier()) # _valido = 123 ou valido = 123;
print ('Os dados digitados usam letras minusculas?', n1.islower())
print ('Os dados digitados usam letras maiusculas?', n1.isupper())
print ('Os dados digitados foram escritos um titulo (Capitalizado)?', n1.istitle()) # O Pequeno Príncipe_observe as letras maiusculas; (Capitalizado)
print ('Os dados digitados são caracteres imprimiveis?', n1.isprintable())
"""

# Utilizando função forma
print('\n'+'\033[1;43m' + ' ' * 5,'Exercício 4',' ' * 5,'\033[m')

n1 = input('\nDigite algo: ').strip()
print ('{}{}{} é alfabeticos?'.format('\033[36m',n1, '\033[m'), n1.isalpha())
print('{}{}{} é numerico?'.format('\033[36m',n1, '\033[m'), n1.isalnum())
print('{}{}{} é um alfanumerico?'.format('\033[36m', n1, '\033[m'), n1.isalnum())