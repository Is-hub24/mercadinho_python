'''
Modulos Collections - counter (contador)

collections - high-performace container datetypes

couter -> recebe um iteravel como parametro e cria um objeto do tipo collections counter que é parecido com dicionarios
          contendo como chave o elementos da lista passada como parametro e como valor a quantidade de ocorrencias
          desse elemento.

'''

from collections import Counter
from gettext import textdomain

#exemplo 1

'''lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 3, 45, 45, 66, 66, 66, 23, 34 ]

res = Counter(lista)

print(type(res))

print(res) # retornou -> valor: ocorrencia
'''
#exemplo 2
'''fala = input('escreva como esta sendo seu dia em no maximo duas palavras: ')

palavra = fala.split() # -> usado para separar e contar as palavras

res = Counter(palavra)

print(res)

# exemplo 3

fala = input('escreva como esta sendo seu dia em no maximo duas palavras: ')

print(Counter(fala)) # -> usado para contar a ocorrencia da repetição das letras na frase escrita'''

#ex 4

# encrontrando as 5 palavras com mais ocorrencias no texto - .most_common

texto = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore 
magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occ
aecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'''

palavras = texto.split()

res = Counter(palavras)

print(res)

print(res.most_common((5)))