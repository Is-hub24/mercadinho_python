'''
modulo collections - default dict

dicionario = {'curso': 'programação em python'}

print(dicionario)

print(dicionario['curso'])

default dict -> informamos um valor default, podendo usar lambda
                será ultilizado sempre que nao houver um valor definido

                -> nao existe Keyerror:
                Caso tentamos acessar uma chave que não existe, essa chave será criada e o valor default será atribuindo
'''

from collections import defaultdict
from email.policy import default

dicionario = defaultdict(lambda: 0) #Lambdas -> São funções sem nome, que poodem ou não receber parametros de entrada e retornar valores

dicionario['curso'] = 'programacao_python'

print(dicionario)

print(dicionario['outro'])

print(dicionario)