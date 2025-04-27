"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores lidos.
"""


"""
                    MINHA TENTATIVA
                    
VALORES = []

while VALOR in VALORES < 6:
    VALORES = int(input("digite um número inteiro:"))

print ("Os valores são: ", VALORES)

"""

lista: list[int] = []

while len(lista) < 6:
    valor: int = int(input(f'Informe o valor {len(lista) + 1}/6: '))
    lista.append(valor)


for valor in lista:
    print(valor)