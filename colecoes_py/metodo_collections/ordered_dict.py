'''
dicionario = {'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5} # -> ordem nao é garantida

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')'''
from typing import OrderedDict

'''from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c':3, 'd':4, 'e':5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')'''

# entendendo a diferença de dict e Orderned Dict

dict1 = {'a':1, 'b':2}
dict2 = {'b':2, 'a':1}

print(dict1 == dict2) # True -> A ordem dos elementos nao imnporta para o dicionario

# orderned dict

odict1 = OrderedDict({'a':1, 'b':2})
odict2 = OrderedDict({'b':2, 'a':1})

print(odict1 == odict2) #false -> a ordem importa para o ordered dict