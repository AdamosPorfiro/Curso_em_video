# Faça um programa que  leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as  informações possiveis sobre ele.
'''
print('===== Desafio 2 =====')
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
'''
# Utilizando função format
print('===== Desafio 2 =====')

n1 = input('Digite algo: ')
print ('{} é alfabeticos?'.format(n1), n1.isalpha())
print('{} é numerico?'.format(n1), n1.isalnum())
print('{} é um alfanumerico?'.format(n1), n1.isalnum())

