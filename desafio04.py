n = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(n))
print('è somente espaço?: ', n.isspace())
print('É um numero?: ', n.isnumeric())
print('É alfabetico>: ', n.isalpha())
print('É alphanumerico?: ', n.isalnum())
print('Esta em maiuscula?:', n.isupper())
print('Esta em minusculas?:', n.islower())
print('Está capitalizada?: ', n.istitle())
