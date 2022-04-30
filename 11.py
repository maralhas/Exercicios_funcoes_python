import os
os.system('color')
os.system('cls')

def mes_por_extenso (mes):
    lista_mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    mes = lista_mes[mes -1]
    return print(f'{dia} de {mes} de {ano}')

data = input('Informe a data no formato DD/MM/AAAA: ')

dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])

dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or  (ano % 400 == 0):
        dias_por_mes[1] +=1
    if dia <= dias_por_mes[1]:
        mes_por_extenso(mes)
        os.system('color a')
        print('A data é válida.')
    else:
        mes_por_extenso(mes)
        os.system('color 4')
        print('A data é inválida.')

elif dias_por_mes[mes - 1] >= dia:
    mes_por_extenso(mes)
    os.system('color a')
    print('A data é válida.')
else:
    mes_por_extenso(mes)
    os.system('color 4')
    print('A data é inválida.')