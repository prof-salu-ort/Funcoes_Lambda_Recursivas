'''
Ordenação Personalizada: 
Você tem uma lista de produtos representada por tuplas: 
produtos = [("Teclado", 150), ("Mouse", 80), ("Monitor", 900)]. 
Use a função sorted com uma função lambda para ordenar essa lista pelo preço 
(o segundo elemento da tupla) em ordem crescente.

'''
produtos = [("Teclado", 150), ("Mouse", 80), ("Monitor", 900)]

lista_produtos_ordenados = list(sorted(produtos, key=lambda x: x[1]))
lista_produtos_ordenados = list(sorted(produtos, key=lambda x: x[1], reverse=True))

print(lista_produtos_ordenados)