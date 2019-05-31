
import random
import time


#bienvenida
print ('Bienvenido a adivina el número, presiona ENTER para continuar')
input()
print('En este momento estoy pensando un número de 4 dígitos...')
time.sleep(2)
print('Para adivinarlo te voy a dar pistas...')
time.sleep(2)
print ('Sabrás cuantos números están BIEN y cuantos están REGULAR')
time.sleep(3)
print ()

número= random.randint(1000, 9999)
pensador= list(str(número))

#piensa número
número= random.randint(1000, 9999)
pensador= list(str(número))
print ('Ya está, lo he pensado. Ingresa un número entero de 4 dígitos')


#realizar intento

while pensador:
    bien = 0
    regular = 0
    adiv=input()
    adivinador= list (adiv)
    for pIndex, pVal in enumerate(adivinador):
        for aIndex, aVal in enumerate(pensador):
            if pVal==aVal and pIndex==aIndex:
                bien = bien + 1
            elif pVal==aVal and pIndex != aIndex:
                regular = regular + 1           

    if adivinador != pensador:
        print (str(bien) + ' están BIEN y ' + str(regular) +' están REGULAR')
        time.sleep(2)
        print('Seguí intentando')

    if adivinador == pensador:
        break
        
if adivinador == pensador:
    print('GANASTE!') 
