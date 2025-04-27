"""
    Recebe temperatura em feirenheit e converte pra celcius.
"""

valor = float(input('Digite o valor a ser convertido: '))
conversor = (valor - 32) / 1.8

print(f'A temperatura em Celsius é: {conversor} Cº')
