"""
1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0.
"""

contador = 0
indice = 1

while contador < 5:
    if indice % 3 == 0:
        print(f'O numero {indice} é múltiplo de 3.')
        contador = contador + 1
    indice = indice + 1