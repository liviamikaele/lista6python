lista = list()

while True:
    a = int(input('Digite um numero:'))
    lista.append(a)

    resp = input('deseja continuar?(s/n)')
    if resp == 'n':
        break

if 5 in lista:
    print('está na lista')
else:
    print('Não está na lista')

print(lista)
print('quantidade de numero',len(lista))
