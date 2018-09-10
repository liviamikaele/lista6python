'''
Nome:Lívia Mikaele Martins Vasconselos
Data:10/09
Enunciado:Questão 7

'''

Qp = 0
nome = []
peso = []

while True:
    Qp = 1+Qp
    n = input('Digite seu nome:')
    p = int(input('Digite seu peso:'))
    nome.append(n)
    peso.append(p)


    resposta = input('Deseja sair?(s/n)')
    if resposta == 'S':
        break

maxx = max(peso)
posicao = peso.index(maxx)

print('quantidade de pessoas',Qp)
print('peso maximo:',maxx)
print('nome',nome[posicao])

minx = min(peso)
posicao = peso.index(minx)

print('peso minimo:',minx)
print('nome:',nome[posicao])

mediana = maxx - minx / 2

pessoas_mais_leves = []
pessoas_mais_pesadas = []
cont = 0
for n in peso:
    if n < mediana:
        pessoas_mais_leves.append([nome[cont],n])
    else:
        pessoas_mais_pesadas.append([nome[cont],n])

    cont += 1

print(pessoas_mais_leves)
print(pessoas_mais_pesadas)
