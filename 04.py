import os
os.system('cls')

def verificar(valor):
    if valor >= 0:
        return 'P'
    elif valor < 0:
        return 'N'

print(verificar(int(input('Digite um numero: '))))
