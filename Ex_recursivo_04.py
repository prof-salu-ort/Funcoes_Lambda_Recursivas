'''
Soma de Lista: 
Crie uma função recursiva que calcule a soma de todos os números em uma lista. 
Dica: O caso base é quando a lista está vazia (soma = 0). 
O passo recursivo soma o primeiro elemento ao resultado da função chamada 
com o restante da lista.
'''

numeros = [1,2,3,4,5,6, 7]
#interativa
def soma_lista_interativa(lista):
    soma = 0
    for x in lista:
        soma += x
    return soma

print(soma_lista_interativa(numeros)) #15

def soma_lista_recursivo(lista, tamanho):
    #1. caso base
    if tamanho < 1:
        return 0
    #Passo recursivo
    return lista[tamanho-1] + soma_lista_recursivo(lista, tamanho-1)

print(soma_lista_recursivo(numeros, len(numeros))) #15