'''
Nome:Livia Mikaele Martins Vasconselos
Data:21/08
Enunciado:Questão 2

'''
lista = list()
while True:
    numero = int(input('Digite um numero'))
    if numero in lista:
        print('Esse numero ja esta na lista.Digite outro numero')
        continue

    lista.append(numero)
    resp = input('Deseja continuar? s/n')
    if resp == 'n':
        break
print('Sua lista é' ,lista)
print(sorted(lista))
maior = max(lista)
menor = min(lista)
pos_max = lista.index(maior)
pos_min = lista.index(menor)
print('O maior numero digitado foi {} que esta na posiçao {}'  .format(maior,pos_max))
print('O menor numero digitado foi {} que esta na posiçao {}'  .format(menor,pos_min))
