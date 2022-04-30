import os
os.system('cls')

def contador_de_digitos(numero):
    resultado = len(str(numero))
    return resultado

while True:
    try:
        numero = int(input('Informe um numero inteiro: '))
    except:
        print('Informe apenas números inteiros. ')
    else: 
        print(f'O numero {numero} tem {contador_de_digitos(numero)} digito(s)')
        break