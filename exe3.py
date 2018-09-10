'''
Nome:Livia Mikaele Martins Vasconselos
Data:21/08
Enunciado:Quetão 3
'''

lista = list()

for n in range(5):
    numero = int(input('numero:'))
    if len(lista)==0 or lista[-1] < numero:
        lista.append(numero)
        continue
    
    pos = 0
    while numero > lista[pos]:
        pos += 1
        
        lista.insert(pos,numero)

print(lista)


    
    
