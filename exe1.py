'''
Nome:Livia Mikaele Martins Vasconselos
Data:21/08
Enunciado:Questão 1

'''

lista = list()
for n in range(5):
    numero = int(input('Digite o {} numero:' .format(n+1)))
    lista.append(numero)
maior = max(lista)
menor = min(lista)
pos_max = lista.index(maior)
pos_min = lista.index(menor)

print('O maior numero digitado foi {} que esta na posiçao {}' .format(maior,pos_max))
print('O menor numero digitado foi {} que esta na posiçao {}' .format(menor,pos_min))

    
    
