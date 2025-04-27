"""
    O programa recebe determinado valor e o converte em kilômetros e centímetros.
"""

valor = float(input('Digite o valor (em metros) a ser convertido: '))
km = valor / 1000
cm = valor * 100

print(f'O valor {valor} totaliza {km} kilômetros, {cm} centímetros.')
