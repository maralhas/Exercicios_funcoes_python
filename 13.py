import os
os.system('cls')

# Desenha moldura. 
# Construa uma função que desenhe um retângulo usando os caracteres 
# ‘+’ , ‘−’ e ‘| ‘. 
# Esta função deve receber dois parâmetros, linhas e colunas, 
# sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. 
# Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.

def retangulo(largura, altura):
    if largura > 20:
        largura = 20
    if altura > 20:
        altura = 20
    print('-+-' * largura)

    coluna = 0
    while coluna < altura:
        z = '|'
        print(f'{z}{z:>{(largura *3 - 1)}}')
        coluna +=1
        print('-+-' * largura)

largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
retangulo(largura, altura)
