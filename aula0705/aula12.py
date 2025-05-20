meu_dicionario = {}

quantidade = int(input('Quantos pares chave-valor voce que adicionar? '))

for i in range(quantidade):
    chave = input('Digite a chave: ')
    valor = input('Digite o valor: ')
    meu_dicionario[chave] = valor
    
print('Dicionario resultante: ', meu_dicionario)
