"""
    Programa recebe dois valores e mostra qual deles é o maior valor.
"""

valor_A = input('Digite o primeiro valor: ')
valor_B = input('Digite o segundo valor: ')

   
if valor_A < valor_B:
    print(f'{valor_B} é maior que {valor_A}.')
    
elif valor_A == valor_B:
    print(f"Os valores ({valor_A}) são iguais!")
    
else: 
    print(f'{valor_A} é maior que {valor_B}.')

