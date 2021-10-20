import csv
import random

resp = ['b','d','b','b','a','a','c','b','c','b','a','c','c','b','c','b','c','d','c','c','b','d','c','a','d','d','a','d','a','a']


repet = []

def opciones(n):
    print(data[n][0])
    print('a - ' + data[n][2])
    print('b - ' + data[n][3])
    print('c - ' + data[n][4])
    print('d - ' + data[n][5])

def mezclar(nivel):
    repet = []
    while len(repet)< 5:
        x = random.randint(0,9) + nivel*10
        if x in repet:
            continue
        repet.append(x)
    return repet

file = open('PreguntasCompu.csv')

readfile = csv.reader(file)

data = list(readfile)

nivel = 'fácil'

print('Nivel ' + nivel)

while True:
    if nivel == 'fácil':
        niv = 0
        repet = mezclar(niv)
        for n in range(0,5):
            print(repet)
            opciones(repet[0])
            ans = input('Respuesta: ')
            if ans == resp[repet[0]]:
               print('bien') 
            
        break
