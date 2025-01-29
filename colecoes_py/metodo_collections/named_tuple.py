'''
Named Tuple

relembrando tupla

tupla = (1, 2, 30)

print(tupla[1])

->sao tuplas diferenciadas, onde especificamos um nome para a mesma e também parametros
'''

from collections import namedtuple

#definindo o nome do parametro

# forma 1 -

cachorro = namedtuple('cachorro', 'idade raca nome')

# forma 2

cachorro1 = namedtuple('cachorro', 'idade, raca, idade' )

# forma 3

cachorro2 = namedtuple('cachorro', ['idade', 'raca', 'nome' ])

# usando

ray = cachorro(idade=2, raca='chow-chow', nome='ray')
print(ray)
