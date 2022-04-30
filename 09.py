import os
os.system('cls')

# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(numero):
    resultado = str(numero)[::-1]
    return resultado

while True:
    try:
        numero = int(input('Informe um numero inteiro: '))
    except:
        print('Informe apenas números inteiros. ')
    else: 
        print(f'O reverso de {numero} é {reverso(numero)}')
        break