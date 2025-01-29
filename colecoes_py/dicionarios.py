'''os dicionarios também chamado de mapas
from tuplas import tupla

Os dicionarios são coleçoes do tipo chave/valor

   [0, 1, 2] chave
   [1, 2, 3] valor 
   os dicionarios sao representados por chaves {}
   
   print(type({}))
   Sobre dicionarios:
            chave valor sao separados por :
            tanto chave quando valor pode ser de qualquer tipo de dado;
            podemos misturar os tipos de dados
            '''


#criação de dicionarios

#Forma 1 - mais comum

paises = {'br': 'Brasil', 'eua': 'estados unidos', 'py': 'Paraguai'} #chave/valor = 1 elemento

print(paises)
print(type(paises))

#forma 2 - menos comum

'''paises = dict(br='Brasil', eua='estados unidos', py='Paraguai')'''

#acessando elementos

#forma 1 - acessando via chave, da mesma forma quee lista/tuplas
print(paises['br'])
print(paises['py'])

'''caso tentamos fazer um acesso ultilizando uma chave que nao existe, teremos o erro keyerror'''

#forma 2 - acessando via get (recomendado)
print(paises.get('br'))
print(paises.get('ro')) #caso o get nao encontre o obj com a chave informada será retornada None

pais = paises.get('py', 'não encotrado') #podemos definir um valor padra para caso ano encontrarmos o obj com a chave informada

print('encontrei o pais', pais)

print('br' in pais)
print('ru' in pais)
print('estados unidos' in pais)

if 'ru' in paises:
    russia = paises('ru')

'''podemos usar qualquer tipo de dados (int, bool, float, str) inlusive a lista, tupla dicionarios como chaves'''
# tuplas pode, ser usadas como chave de dicioanrios pois as mesmas sao imutavbeis
localidade = {
    (35.4169, 54.666): 'Escritorio em tokio',
    (35.428, 54.464): 'escrotório em NY',
    (35.454, 54.343): 'escritorio em sp',
}

print(localidade)
print(type(localidade))

''' Adicionar elementos em um dicionario'''

receita =  {'jan':100, 'fev':120, 'mar': 100}

print(receita)
print(type(receita))

#forma 1 - mais comum

receita['abr'] = 350

print(receita)

#forma 2

novo_dado = {'maio': 500}

receita.update((novo_dado))

print(receita)

'''Adiconando dados em um dicionario'''

# forma 1

receita['mai'] = 550
print(receita)

# forma 2

receita.update({'mai': 600})

print(receita)

# conclusão 1: A forma de adicionar novo elementos ou atualizar dados em um dicioanrio é a mesma
# conclusão 2: nao podemos ter chaves repetidas

'''Como remover dados'''
#mais comum
ret = receita.pop('mar') # .pop é ultilizado para remover o ultimo elemento da lista e é retornado para visualização
print(ret)

print(receita)
#obs: necessario sempre informar a chave, e caso nao encontre o elemento, um keyerror sera retornado

#forma 2

del receita['fev']

print(receita) # caso nao exista, retorna keyerror

'''metodos para dicionarios'''

#forma 1 - deep copy

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

#copiando um dict para outro

novo = d.copy()

print(novo)

novo['d'] = 4

print(d)
print(novo)

# forma 2 - shellow copy

novo = d

print(novo)

novo['e']  = 10

print(d)
print(novo)

#FORMA NAO USUAl de criação de dict

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile', 'desconhecido'])
print(usuario)
print(type(usuario))

# o metodo .fomkeys recebe dois parametros: um iteravel e um valor
# ele vai gerar para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11),'novo')
print(veja)