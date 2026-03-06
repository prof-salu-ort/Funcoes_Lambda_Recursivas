'''
Crie uma função que calcule o valor fatorial de um numero de forma recursiva.
'''

def fatorial_interativo (n):
    fat = 1
    for x in range(1, n+1):
        fat *= x
    return fat

#!5 ==> 1 * 2 * 3 * 4 * 5
#print(fatorial_interativo(5))

def fatorial_recursivo(n):
    #caso base
    if n == 1:
        return 1
    return n * fatorial_recursivo(n-1)

print(fatorial_recursivo(5))

