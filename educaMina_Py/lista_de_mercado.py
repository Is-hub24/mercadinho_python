class ListaMercado:
    def __init__(self):
        # Inicializa a lista de mercado como uma lista vazia
        self.lista_mercado = []

    def adicionar_item(self, item):
        # Adiciona um item à lista de mercado
        self.lista_mercado.append(item)

    def remover_item(self, item):
        # Remove um item da lista de mercado pelo nome
        try:
            # Encontra o índice do item na lista e o remove usando pop()
            self.lista_mercado.pop(self.lista_mercado.index(item))
        except:
            # Se o item não for encontrado, exibe uma mensagem de erro
            print('Item nao encontrado :( ')

    def __repr__(self):
        # Representa a lista de mercado como uma string
        # Isso permite que a lista seja exibida diretamente ao imprimir um objeto da classe
        return str(self.lista_mercado)

pass