quantidade = 0
lista_produtos = []
for i in range(150):
    produto = input('Digite o nome do produto: ')
    if produto == '':
      print('Lista de produtos ', lista_produtos, quantidade)
      break
    else:
      quantidade = quantidade + 1
      lista_produtos.append(produto)