import os
from traceback import print_tb
os.system('cls')

def valor_pagamento(valor_prestacao, dias_atraso):
    valor_prestacao += valor_prestacao * 0.03 
    dias_atraso = dias_atraso * 0.001
    valor_prestacao += valor_prestacao * dias_atraso
    return valor_prestacao

quant = 0
valor_total = 0
print('Para sair do programa informe prestação igual a 0 (zero)')

while True:
    while True:
        try:
            valor_da_prestacao = float(input('Digite o valor da prestação: '))
        except ValueError:
            print('Informe apenas números.')
        else:
            break
    while True:
        try:
            dias_em_atraso = int(input('Informe os dias em atraso: '))
        except ValueError:
            print('Informe apenas numero inteiros ou 0 para sair')
        else:
            break
    if dias_em_atraso == 0:
        break
    print(f'O valor a ser pago é: {valor_pagamento(valor_da_prestacao, dias_em_atraso):.2f}')
    quant += 1
    valor_total += valor_pagamento(valor_da_prestacao, dias_em_atraso)
print('Relatorio do dia: ')
print(f'Quantidade de prestações: {quant}')
print(f'Valor total {valor_total:.2f}')
