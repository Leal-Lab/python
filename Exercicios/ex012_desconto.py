"""
    Recebe um valor e retorna o total com 5% de desconto.
"""

valor = float(input('Digite o valor do produto: R$ '))
total_desc = valor - (valor * 5 / 100)
print ('O valor com desconto é: R$', total_desc)
