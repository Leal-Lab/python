"""
    Programa recebe altura e largura, retorna em metros quadrados e a quantidade de tinta em litros.
"""

altura = float(input('Digite o valor da altura: '))
largura = float(input('Digite o valor da largura: '))

m2 = altura * largura
tinta = m2 / 2

print(f'A superfície tem {m2} metros quadrados. Use {tinta} litros para pintar uma demão.')
