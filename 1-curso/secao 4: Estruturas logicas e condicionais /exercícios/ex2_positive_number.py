"""
2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule 
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""
import math

NUMBER = int(input('Digite um número inteiro:'))

if NUMBER > 0:
    RAIZ_QUADRADA = math.sqrt(NUMBER)
    print('O número é:', NUMBER)
    print("Sua raíz quadrada é:", RAIZ_QUADRADA)

else:
    print("Número Negativo!")
    
