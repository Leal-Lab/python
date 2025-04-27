"""
3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
seu valor na tela, até que seu valor seja 100000 (cem mil).

CONTADOR = 0

while CONTADOR <= 100000:
    print(CONTADOR)
    CONTADOR = CONTADOR + 1000

"""


"""
Depois de fazer o exercício é que me liguei que a proposta era de usar range. Vamos a ele:
"""

for num in range (0, 100001, 1000):
    print (num)
