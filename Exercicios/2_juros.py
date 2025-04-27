"""
Crie um programa que calcula os juros de um depósito bancário.
"""

valor = float(input('Digite o valor do depósito:'))
anos = int(input('Digite o tempo (em anos) do depósito:'))
taxa = float(input('Digite o valor da taxa referente ao depósito:'))

juros = valor * anos * taxa / 100

print(f'O total é: ', juros)
