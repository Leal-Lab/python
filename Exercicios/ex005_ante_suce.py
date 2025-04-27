"""
    Recebido um valor, mostra o antecessor e o sucessor dele.
"""

valor = int(input('Digite um número: '))
antecessor = valor - 1
sucessor = valor + 1

print(f'O valor {valor} é precedido de {antecessor}, e sucedido por {sucessor}')
