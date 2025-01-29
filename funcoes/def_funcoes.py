'''
denindo funçes

- Pequenos partes de codigo que realizam taferas especificas
- pode ou nao recber entradas de dados e retornar uma saida de dados
- uteis para executar procedimentos similares por repetidas vezes
- uma função que realiza muitas tarefas dentro dela, é bom fazer uma refificação para que seja simplificada
'''

#exemplo de ultilização

cores = ['verde', 'azul', 'amarelo', 'branco']

'''
forma geral de definir uma função é:

def nome_da_funcao(parametro_de_entrada):
    bloco_da_funcao 
    
onde:
- nome_da_funcao -> sempre com letras minusculas, se for nome composto, separar por underline 
- parametros de entrada -> opcionais, mais de um cada um separado por virgula, podendo ser opcional ou nao;
- bloca_da_funcao -> também chaamdo de corpo da função ou implementação onde processamento acontece (pode ter ou nao retorno da função
- def -> definição de funçoes e termina com dois pontos, a prox linhaa sera respeitando a indentação de 4 espaços

'''

#def a primeira função

def diz_oi():
    print('oi!') #obs: podemos realizar outras funções dentro, executa apenas uma tarefa (apenas diz oi)

# ultilizando funções

#chamada de execução
diz_oi() #sempre colocar o parenses junto com o nome da dunção

#ex 2
def cantar_parabens(): # -> desta maneira nada acontece, deve-se executar
    print('parabens pra voce')
    print('nesta data querida')
    print('muitas felicidades')

cantar_parabens() #->  desta forma que voce executa a função

'''for n in range(0):
    cantar_parabens()'''

# podemos criar variaveis do tipo de uma função atraves de uma variavel

canta = cantar_parabens()

canta()
