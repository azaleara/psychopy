# comentarios
#python3 # para correr en terminal 

print("Hello World")

#expresiones. Orden: 
#1)parentesis, 
#2)multiplicación y división
#3)suma y resta
2 + 2
6 - 3
3 * 2
6 / 2
(3 + 2) * 7
3 + 2 * 7

# tipos de datos
print("Hello World") # string: e.g.'Hello' + ' ' + 'Azalea' + '!' * 10
print(123)           # integer number
print(3.14)          # real number or float
print(False)         # boolean False, the opposite of True

str(89)
int('1234')
float('3.14')

#operadores de comparación 
== 
!=
<
>
<=
>=

#Booleanos
False and False
False and True
True and False
True and True
# ahora con or 

# others
not True
not False

# variables
anio = 2021
nacimiento = 1999
curso = "psychopy"
password = "chilaquil"
answer = True

anio > 2020 and curso == "psychopy"

a = 123
b = 456
c = a + b
print(c) # output 579

s = "Hello"
t = " "
u = "Mundo"
w = s + t + u 
print(w) # output: "Hello World"



# Modules
import math
y = math.cos(0.0)
print(y)


### psychopy
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# The first line is called the hash bang. It helps operating systems 
# understand what to do with this script. The second line describes 
# the encoding of this file. UTF-8 is the only one used nowadays.
# It supports all alphabeths, even runes and linear B.
 
# Import the PsychoPy libraries that you want to use
from psychopy import core, visual

# Create a window
win = visual.Window([400,300], monitor="testMonitor")
 
# Create a stimulus for a certain window
message = visual.TextStim(win, text="Hello World!")

# Draw the stimulus to the window.
message.draw()
 
# Flip backside of the window.
win.flip()
 
# Pause 5 s, so you get a chance to see it!
core.wait(5.0)

# Close the window
win.close()
 
# Close PsychoPy
core.quit()

####
message1 = visual.TextStim(win, text="Hello Azalea")
message1.draw()
win.flip()
core.wait(1.0)

### Listas
presentationTime = [3.5, 5.5, 7.5]
presentationText = ["Apple", "Spam", "Ham"]

firstValue = presentationTime[0]
lastValue = presentationTime[2]

# esta es una manera de comenzar con una lista vacia e irla llenando
responseTime = []
responseTime.append(3.5)
responseTime.append(5.5)
responseTime.append(7.5)

# otro ejemplo de empezar con una lista vacía pero irla llenando con (dos) valores 
trialResponseTime = []
trialResponseTime.append([2.5, 3.5])
trialResponseTime.append([12.5, 13.5])
trialResponseTime.append([22.5, 23.5])
print(trialResponseTime)


# Control Statements
# for, while, if else

# for

#crear windows y estímulos 
win = visual.Window([200,300], monitor="testMonitor")
stimuli = ["manzana", "plátano", "naranja", "guayaba"]

for stimulus in stimuli:
    message = visual.TextStim(win, text=stimulus)
    message.draw()
    win.flip()
    core.wait(1.0) 

# otra manera donde enumeras por el índice del estímulo 
for i, stimulus in enumerate(stimuli):
    message = visual.TextStim(win, text=str(i)+" es "+stimulus)
    message.draw()
    win.flip()
    core.wait(1.0) 

# while: The condition indicates what must be true for the loop to continue and 
# the indented part is the body of the loop. All the code that is indented will be repeated.

from psychopy import event

i = 0
c = None
while c == None:   # loop until a key is pressed
    message = visual.TextStim(win, text=str(i)+" press a key")
    message.draw()
    win.flip()
    c = event.waitKeys(maxWait = 2.0)
    i = i + 1


# if-else-statement fuera del ambiente de psychopy
result = 7
if result >= 8.5:
    message = visual.TextStim(win, text="Aprobado: FELICIDADES")
elif result >= 6.5:
    message = visual.TextStim(win, text="Apenas, aprobado")
elif result >= 5.5:
    message = visual.TextStim(win, text="Pues no deberías pasar")
else:
    message = visual.TextStim(win, text="NA")

message.draw()
win.flip()

# bbv C0247200 no de cancelacion 
# https://www.socsci.ru.nl/wilberth/nocms/psychopy/print.php
