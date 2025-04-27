"""
    Criar um programa que dê uma descrição completa a partir de um dado recebido.
"""

slot = input('Digite algo: ')

print(f'{slot} tem {len(slot)} caracteres')
print(f'O tipo do dado é  : {type(slot)}')
print('É alfabético?', slot.isalpha())
print('É numérico?', slot.isnumeric())
print('Tem espaços?', slot.isspace())
print('É alfanumérico?', slot.isalnum())
