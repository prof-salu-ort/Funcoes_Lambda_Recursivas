'''
Filtragem de Strings Curtas: 
Dada a lista de nomes nomes = ["Ana", "Beatriz", "Caio", "Daniela", "Edu"], 
utilize a função filter e uma função lambda para retornar apenas os nomes 
que possuem 3 letras ou menos.
'''
nomes = ["Ana", "Beatriz", "Caio", "Daniela", "Edu"]

lista_nomes = list(filter(lambda nome : len(nome) <= 3, nomes))

print(lista_nomes)