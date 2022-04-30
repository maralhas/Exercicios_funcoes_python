import os
import random
import re
from wsgiref import validate
os.system('cls')
 
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

def jogar_dados():
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    print(f'Primeiro dado: {dado_1}')
    print(f'Segundo dado: {dado_2}')
    return dado_1 + dado_2

rodada = 1
ponto = 0
validador = False
while True:
    iniciar = input('Desejar lançar um par de dados? [S]Sim [N]não: ')
    iniciar = iniciar.upper()
    if iniciar == 'S':
        soma = jogar_dados()
        if rodada == 1:
            if soma == 7 or soma == 11:
                print('Você é um "natural" e ganhou')
                break
            elif soma == 2 or soma == 3 or soma == 12:
                print('Craps - Você Perdeu')
                break
            elif soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
                print(f'{soma} este é seu ponto')
                ponto = soma
                print('Seu objetivo agora é continuar jogando os dados até tirar este número novamente.')
            rodada += 1
        else:
            if ponto == soma:
                validador = True
                print('Tirou o seu ponto')
                print('Agora já pode tirar 7 pra ganhar')
                rodada += 1
            elif (validador == False) and soma == 7:
                print('Você perdeu')
                rodada += 1
                break
            elif (validador == True) and soma == 7:
                print('Você ganhou')
            else:
                 print('Seu objetivo agora é continuar jogando')

    else:
        break

