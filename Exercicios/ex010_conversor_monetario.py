"""
    Programa recebe valor e o converte em dólar, euro e bitcoin
"""

valor = float(input('Digite o valor em reais pra conversão: R$ '))

dolar = valor / 5.7
euro = valor / 6.4
bitcoin = valor / 83000

print(f'R$ {valor} convertido dá aproximadamente:')
print(f'Em dólar: {dolar}')
print(f'Euro: {euro}')
print(f'Bitcoin: {bitcoin}')
