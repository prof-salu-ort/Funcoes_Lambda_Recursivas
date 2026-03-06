'''
Dobro dos Números: 
Dada a lista numeros = [5, 12, 7, 15, 10], utilize a função
map e uma função lambda para criar uma nova lista onde cada elemento é o
quadrado do valor original.

'''
numeros = [5, 12, 7, 15, 10]

lista_quadrado = list(map(lambda x: x ** 2, numeros))

print(lista_quadrado)