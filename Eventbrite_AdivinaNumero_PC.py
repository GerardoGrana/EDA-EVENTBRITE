#import itertools
#import os

#numbers = '1542'
#y = ''
#for c in itertools.product(numbers, repeat=4):
    #pin = y+''.join(c)
    #print (pin)
    #os.system("./xyz "+pin)

import random
import time

print ('Saludos humano, estoy aquí para proponerte un desafío...')
time.sleep(2)
print ('...Una demostración de mis capacidades psíquicas.')
time.sleep(2)
print ('Solo debes escribir un número de 4 dígitos y yo lo adivinaré!')
time.sleep(2)


while True:
    try:
        userInput = int(input('Ingresa tu número '))
        if not 1000 <= userInput <= 9999:
            raise ValueError('Valor fuera del intervalo permitido')
        break
    except ValueError:
        print ('Solo enteros de 4 dígitos')
        pass

pensador= userInput
adivinador = 1000

while pensador:
    adivinador 
    if adivinador != pensador:
        adivinador= adivinador + 1
        #print (adivinador)
    if adivinador == pensador:
        break
if adivinador == pensador:
    print ('Te he ganado humano, el número que escribiste es ' + str(adivinador))


#from itertools import *
#for valor in count (1000, 1):
#    print (valor, end='')
#    if valor == 1050: break


#contador = 0 
#for elemento in cycle("Python"):
#    print(elemento, end = ' ')
#    contador += 1
#    if contador == 12: break

#print ()
#contador = 0
#for elemento in cycle([10, 12, 14]):
#    print(elemento, end = ' ')
#    contador += 1
#    if contador == 5: break
