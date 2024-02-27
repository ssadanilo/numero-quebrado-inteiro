import math

numero_quebrado = float(input('Digite um número bem quebrado: '))
numero_inteiro = (numero_quebrado.__trunc__())
print(f'O número digitado é {numero_quebrado} e sua versão inteira é {numero_inteiro}')