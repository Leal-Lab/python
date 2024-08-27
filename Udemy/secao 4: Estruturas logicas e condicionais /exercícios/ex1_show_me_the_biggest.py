'''
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
'''

VALOR_A = int(input('Digite o primeiro valor:'))
VALOR_B = int(input('Digite o segundo valor:'))

if VALOR_A < VALOR_B:
    print('Valor B é Maior')

elif VALOR_A == VALOR_B:
    print('Valores são iguais')

else:
    print('Valor A é Maior')
