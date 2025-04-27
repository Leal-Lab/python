"""
    Recebe um valor numérico e acrescenta outro valor recebido em percentual.
"""

salario = float(input('Digite o salário atual: R$ '))
percentual = float(input('Digite o percentual de reajuste: '))

novo_salario = salario + (salario * percentual / 100)
print('Seu novo salário é de: R$', novo_salario)
