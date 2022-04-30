import os
import random
os.system('cls')

def embaralhar(palavra):
    palavra = list(palavra)
    random.shuffle(palavra)
    print(palavra)
    palavra = ''.join(palavra)
    return print( palavra.upper() )

embaralhar(input('Digite uma palavra: '))