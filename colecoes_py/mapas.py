"""mapas -> dicionarios
represetnados por chaves (chave/ receita"""

receita = {'jan': 100, 'fev': 50, 'mar': 150}

# iterar sobre dicionarios (chave/valor)

'''for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

print(receita.keys()) #traz dicionario de chaves

for chave in receita.keys():
    print(receita[chave])

#acessando os valores

print(receita.values()) # vizualização de valor

for valor in receita.values():
    print(valor)'''
print(receita.items())

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

#soma*, Valor Max*, Valor Min*, tamanho
# * -> Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values())) # para saber o tamanho da lista