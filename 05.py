import os
os.system('cls')

def soma_imposto(taxa_imposto, custo):
    taxa_imposto = taxa_imposto / 100
    custo += custo * taxa_imposto
    return custo

taxa = float(input('Informe a taxa: '))
custo = float(input('informe o custo do produto: '))

print(f'Novo valor de custo é {soma_imposto(taxa,custo):.2f}')
