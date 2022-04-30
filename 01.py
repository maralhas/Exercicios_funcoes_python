def imprimir_triangulo_de_numeros(n: int):
    for linha in range(1, n +1):
        for coluna in range(1, linha +1):
            print(coluna, end = '   ')
        print('')

print('triangulo com 1')
imprimir_triangulo_de_numeros(1)
print('triangulo com 2')
imprimir_triangulo_de_numeros(2)
print('triangulo com 3')
imprimir_triangulo_de_numeros(3)