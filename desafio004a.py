n = input('Digite algo: ')
print('O tipo primitivo desse valor é {}.'.format(type(n)))
print('Só tem espaços?', n.isspace())
print('É alfanumérico?', n.isalnum())
print('É um número?', n.isnumeric())
print('É alfabético?',n.isalpha())
print('Está em maiúscula?', n.isupper())
print('Está em minúscula?', n.islower())
print('Está capitalizada?', n.istitle())
