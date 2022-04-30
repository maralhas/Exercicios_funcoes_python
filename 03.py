import os
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
os.system('cls')

def soma(primeiro, segundo, terceiro):
    resultado =  primeiro + segundo + terceiro
    return resultado

print(f'O resultado da some é: {soma(2,3,5)}')