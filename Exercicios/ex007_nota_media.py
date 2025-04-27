"""
    Recebe 4 notas e retorna a média do aluno.
"""

nota_A = float(input('Digite a primeira nota: '))
nota_B = float(input('Digite a segunda nota: '))
nota_C = float(input('Digite a terceira nota: '))
nota_D = float(input('Digite a quarta nota: '))

media = nota_A + nota_B + nota_C + nota_D / 4
print(f'A média do candidato é: {media}')
