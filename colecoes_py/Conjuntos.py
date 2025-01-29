'''
conjuntos

referencia a teoria dos conjuntos em matematica

sao chamados de Sets (conjuntos)

nao possuem duplicados nem ordenados

comjuntos nao sao indexados ( nao tem acesso ao indice)

usado para armazenar elementos sem importar a ordenação, com chaves e valores duplicados

usa-se {} chaves

diferença entre conjuntos(set) e Mapas (dict)
  mapas -> chave/valor
  conjuntos -> apenas valor
'''

# definindo um conjunto

# forma 1

'''s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # -> valores repetidos

print(s)
print(type(s))'''

#valores repetidos serão ignorados e nao farao parte do conjunto sem apresentar error

#forma 2 ( mais comum)

'''s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

if 3 in s:
    print(" tem o 3")
else:
    print('nao tem')'''

#importante lembrar:
 #nao tenho valores duplicados
 #nao temos elementos ordenados


'''lista = [99, 2, 2, 34, 34, 23, 12, 1, 44, 5] -> ordem digitada
print(f'listas: {lista} com {len(lista)} elementos')

tupla = 99, 2, 2, 34, 34, 23, 12, 1, 44, 5 -> ordem digitada
print(f'tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([99, 2, 2, 34, 34, 23, 12, 1, 44, 5], 'dict') # .fromkeys -> Create a new dictionary with keys from iterable and values set to value.
print(f'dicionario: {dicionario} com {len(dicionario)} elementos') -> ordem digitada

conjunto = {99, 2, 2, 34, 34, 23, 12, 1, 44, 5} -> nao respeita a ordem de digitação
print(f'conjunto: {conjunto} com {len(conjunto)} elementos')'''

'''# aceita todo tipo de dados misturados em sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

#podemos iterar em um set normalmente
for valor in s:
    print(valor)'''

# uso interessantes com set

# formulario de cadstro para uma feira ou museu, e os visitantes informar manualmente a ciadade de onde vieram
# nos adicionamos cada cidade em uma lista py, ja que uma lista podemos adicionar novos elementos e ter repetição

'''cidades = ['bh', 'Sp', 'campo grande', 'cuiaba', 'campo grande', 'Sp', 'cuiaba']

print(cidades)
print(len(cidades))

#quantas cidades distintas, ou seja, unica temos:

print(len(set(cidades))) #ira remover as cidades repetidas, retornar as cidades e o total'''

'''#adiconando elementos em um conjunto .add

s = {1, 2, 3}

s.add(4)
print(s)
'''
'''# remover elementos .remove/.discard
s = {1, 2, 3}
print(s)

#forma 1

s.remove(3) #-> nao é indice, mas sim o valor 3 da lista
print(s) #-> conjuntos nao sao indexados

# forma 2 .discard

s.discard(2)
print(s)

#caso nao encontre o elementos, nenhum valor é retornado'''

# copiando conjuntos dentro de outro conjuto

s = {1, 2, 3}
print(s)

# forma 1 - deep copy  novo.add(4)

'''novo = s.copy() -> cria um novo espaço 
print(novo)

novo.add(4)

print(novo)
print(s)

# forma 2 - shallow novo = s

novo = s

novo.add(4) -> substitui

print(novo)
print(s)'''

'''# podemos remover todos os itens de um conjunto .clear

s.clear()
print(s)'''

# metodos matematicos de conjuntos
# dois conjuntos {estudantes_python} e {estudantes_java}

estudantes_python = {'marcos', 'patricia', 'ellen', 'pedro', 'julia', 'guilherme'}
estudantes_java = {'fernando', 'gustavo', 'julia', 'ana'}

'''# alguns alunos que estudam py que tambem estudam java
# precisamos gerar um conjunto com os nomes unicos

# forma 1 - ultilizando .union ( mais recomendado)

unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)

# forma 2 - |

unicos2 = estudantes_python | estudantes_java

print(unicos2)'''

'''#gerar um conjunto de estudantes que estao em ambos os cursos

# forma 1 - .intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)


#forma 2 - &

ambos2 = estudantes_python & estudantes_java
print(ambos2)'''

'''# estudantes que estão apenas em um curso .difference

so_py = estudantes_python.difference(estudantes_java)
print(so_py)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)'''

# Soma*, Valor Max*, Valor Min*, Tamanho
# * sae os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))