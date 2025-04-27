"""
    Recebe um número e mostra sua tabuada.
"""


i = 1


valor = int(input('Digite um valor para exibir sua tabuada: '))
print('=' * 12)

while i <= 10:
    print (f'{valor} X {i} = ', valor * i)
    i += 1

print('=' * 12)
