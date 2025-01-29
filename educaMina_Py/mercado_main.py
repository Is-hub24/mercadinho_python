from lista_de_mercado import ListaMercado

def imprimir_menu():
    # Função para exibir o menu e capturar a opção do usuário
    item_menu = input('\n1. Adicionar Itens \n'
          '2. Remover item da lista\n'
          '3. Exibir a lista de compras\n'
          '4. Encerrar\n'
          'Digite sua opção:')

    return item_menu # Retorna a opção escolhida pelo usuário

if __name__ == '__main__':
    # Cria uma instância da classe ListaMercado
    lista1 = ListaMercado()

    # Inicia um loop infinito para o menu
    while True:
        # Exibe o menu e captura a escolha do usuário
        item_menu = imprimir_menu()

        if item_menu == '1':
            # Se a opção for '1', adiciona um item à lista
            lista1.adicionar_item(input("Insira um item: "))
            print(lista1) # Exibe a lista atualizada

        elif item_menu == '2':
            # Se a opção for '2', remove um item da lista
            lista1.remover_item(input('Insira o intem que deseja remover: '))
            print('A sua lista de mercado é: ',lista1) # Exibe a lista atualizada

        elif item_menu == '3':
            # Se a opção for '3', exibe a lista de compras atual
            print('Exibindo sua lista', lista1) # Exibe a lista atualizada

        elif item_menu == '4':
            # Se a opção for '4', encerra o programa
            print('Lista encerrada, obrigado! ')
            break

        else:
            # Se o usuário digitar uma opção inválida, exibe uma mensagem de erro
            print('Item não encontrado :(')
