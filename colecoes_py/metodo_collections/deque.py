'''
modo collections - deque

uma lista de aula perfomance
'''

from collections import deque

deq = deque('geek')

print(deq)

deq.append('y')

print(deq)

# remover elementos

print(deq.pop()) #remove e retorna o ultimo elemento

print(deq.popleft()) #remove o primeiro elemento

print(deq)