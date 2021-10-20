import csv
import random

resp = ['b','d','b','b','a','a','c','b','c','b','a','c','c','b','c','b','c','d','c','c','b','d','c','a','d','d','a','d','a','a']


repet = []

contador = 0

def opciones(n):
    print('')
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

def respC(n):
    if n == 'a':
        x = 2
    elif n == 'b':
        x = 3
    elif n == 'c':
        x = 4
    elif n == 'd':
        x = 5
    return x

def level(niv):
    contador = 0
    repet = mezclar(niv)
    for n in range(0,5):
        opciones(repet[n])
        ans = input('Respuesta: ')
        if ans == resp[repet[n]]:
            print('Respuesta correcta')
            contador += 1
        else:
            print('Respuesta incorrecta')
            opcionC = respC(resp[repet[n]])
            print('Respuesta correcta: ' + resp[repet[n]] + ' - ' + data[repet[n]][opcionC])

        if contador == 1:
            print('Llevas ' + str(contador) + ' punto')
        else:
            print('Llevas ' + str(contador) + ' puntos')

    return contador

def plevel(niv):
    if niv == 0:
        nivel = 'Nivel fácil'
    elif niv == 1:
        nivel = 'Nivel medio'
    elif niv == 2:
        nivel = 'Nivel difícil'
    return nivel

def cambioNivel(buenas,nivel,puntuacion):
    nivel = 0
    if buenas >= 4 and nivel == 0:
        print('Puntuación total: ' +  str(puntuacion))
        print('Felicidades, avanzas al siguiente nivel')
        nivel += 1
        
    elif buenas >= 4 and nivel == 1:
        print('Puntuación total: ' +  str(puntuacion))
        print('Felicidades, avanzas al siguiente nivel')
        nivel += 1
        
    elif buenas >= 4 and nivel == 2:
        print('Puntuación total: ' +  str(puntuacion))
        print('Felcidades, has completado con éxito los 3 niveles')
    return nivel

file = open('PreguntasCompu.csv')

readfile = csv.reader(file)

data = list(readfile)

nivel = 0

while True:

    print('')
    print(plevel(nivel))

    buenas = level(nivel)

    puntuacion = contador + buenas

    if buenas < 4 and nivel != 0:
        puntuacion = contador - buenas
        print('Puntuación total: ' +  str(puntuacion))
        repetir = input("¿Quieres volver a jugar?(si o no): ")
        repetir.lower()
        if repetir == 'si':
            continue
        elif repetir == 'no':
            break

    elif buenas < 4:
        print('Puntuación total: ' +  str(puntuacion))
        repetir = input("¿Quieres volver a jugar?(si o no): ")
        repetir.lower()
        if repetir == 'si':
            continue
        elif repetir == 'no':
            break

    nivel += cambioNivel(buenas,nivel,puntuacion)
