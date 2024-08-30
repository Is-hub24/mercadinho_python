class ListaMercado:
    def __init__(self):
        self.lista_mercado = []

    def adicionar_item(self, item):
        self.lista_mercado.append(item)

    def remover_item(self, item):
        try:
            self.lista_mercado.pop(self.lista_mercado.index(item))
        except:
            print('Item nao encontrado :( ')

    def __repr__(self):
        return str(self.lista_mercado)

pass