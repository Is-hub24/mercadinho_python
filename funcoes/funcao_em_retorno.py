'''
funcoes com retorno

'''

'''numeros = [1, 2, 3]

ret = numeros.pop()

print(f'retorno de pop {ret}')

ret_pr = print(numeros)

print('retorno de print', ret_pr)'''

'''def quadrado_7():
    print(7 * 7)

#quadrado_7() -> nao esta retornando, mas sim imprimindo

ret = quadrado_7()

print(f'retorno {ret}')

- Nao é necesssario a criação de uma variavel parareceber o retorno da função'''

# refatorar para que ela retorne o valor

def quadrado_7():
    return 7 * 7 # usado para tirar o resultado da função

ret = quadrado_7()

print('retorno', ret)