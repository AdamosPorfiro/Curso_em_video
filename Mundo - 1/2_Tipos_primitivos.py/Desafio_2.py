# Faça um programa que  leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as  informações possiveis sobre ele.
'''
print('===== Desafio 2 =====')
n1 = input('Digite algo: ')
print (type(n1))
print ('Os dados digitados são alfabeticos?', n1.isalpha()) -> Verifica se é uma strign com letras "Alfabético";
print ('Os dados digitados são numeros decimais ?', n1.isdecimal());
print ('Os dados digitados são alfabeticos e numericos ?', n1.isalnum())-> Verificar se é "Alphanumerico" com letras e números;
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

'''
print('===== Desafio 2 =====')


n1 = input('Digite uma frase: ')
print ('{} é alfabeticos?'.format(n1), n1.isalpha())
print('{} é Alfanumerico?'.format(n1), n1.isalnum())
print('{} é um número decimal?'.format(n1), n1.isdecimal())
print('{} é um espaço em branco?'.format(n1), n1.isspace())
print('{} está no padrão ASCII?'.format(n1), n1.isascii())
print('{} são todo digitos?'.format(n1), n1.isdigit())
print('{} é um identificador valido?'.format(n1), n1.isidentifier())
print('{} Possuem letras minusculas?'.format(n1), n1.islower())
print('{} Possuem letras maiusculas?'.format(n1), n1.isupper())
print('{} Foi escrito em formato de titulo?'.format(n1), n1.istitle())
print('{} São imprimiveis?'.format(n1), n1.isprintable())
'''

# Verifique cada caracter da frase utilizando os verificadores



