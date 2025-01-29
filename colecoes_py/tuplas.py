'''Desempacotamento de Tuplas
Caso voce peça para desempactorar numeros diferentes do elementos da tupla dará erro ValueError'''

tupla = ('Isis', 'Silva')

escola, curso = tupla

print(escola)
print(curso)

'''Soma, valor Maximo, Valor minimo e tamanho
se os valores forem todos inteiros ou reais'''

tupla = (1, 2, 3, 4, 5, 6,)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

'Concatenação de tuplas'

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) #tuplas sao imutaveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)

#Tuplas sao imutáveis, mas podemos sobreescever seus valores
tupla1 = tupla1 + tupla2
print(tupla1)

'verificar se determinado elemento está contido na tupla'

tupla = (1, 2, 3)

print(3 in tupla) #retorna true ou false

'iterando sobre uma tupla'

for n in tupla: #n é o
    print(n)

for indice, valor in enumerate(tupla): #enumerate = enumerar/enumerado indice = posição do elemeto da lista 0, 1, 2, 3, ...
    print(indice, valor)

'contando elemento dentro de uma tupla'

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b' )

print(tupla.count('a')) #.count é ultilizado para contar a repetição do elemento indicado

' dicas na ultilização de tulas, devemos usar tuplas swmpre que modificar dados contidos em uma coleção'

'exemplo 1'

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro','dezembro')

print(meses)

'acesso de elementos é semelhante a lista'
print(meses[5])

#iterar no while
i = 0

'''while i < len(meses): """ Return the number of items in a container. """
    print(meses[i])
    i = i + 1'''

'verificamos qual o indice um elemento esta na tupla '

print(meses.index('janeiro',6, 2))

'slicing - tupla (inicio:fim:passo)'

'por quê ultilizar tuplas?'
'sao mais rapidas do que lista, deixa seu codigo mais seguro (imutavel)'

'copiando uma tupla para outra'

tupla = (1, 2, 3)
print(tupla)

nova = tupla # na tupla nao temos o problema de shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)

print(nova)
print(tupla)