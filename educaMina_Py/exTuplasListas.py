from lista_de_mercado import ListaMercado



def imprimir_menu():
    item_menu = input('\n1. Adicionar Itens \n'
          '2. Remover item da lista\n'
          '3. Exibir a lista de compras\n'
          '4. Encerrar\n'
          'Digite sua opção:')

    return item_menu

if __name__ == '__main__':
    lista1 = ListaMercado()
    while True:
        item_menu = imprimir_menu()
        if item_menu == '1':
            lista1.adicionar_item(input("Insira um item: "))
            print(lista1)
        elif item_menu == '2':
            lista1.remover_item(input('Insira o intem que deseja remover: '))
            print('A sua lista de mercado é: ',lista1)
        elif item_menu == '3':
            print('Exibindo sua lista', lista1)
        elif item_menu == '4':
            print('Lista encerrada, obrigado! ')
            break
        else:
            print('Item não encontrado :(')



    pass
