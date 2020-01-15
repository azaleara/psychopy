### Introduccion

# multiplication
print 2 * 3
# division
print 2 / 2
# exponentiation
print 2 ** 4
# subtraction
print 2 - 4

#
print 2.0 ** 3.0

# varibles y módulos
apples = 3
oranges = 2
print apples + oranges
#
import random
rand_val = random.random()
print rand_val

# definir tus propias funciones 
def sum_fruit(fruit_a, fruit_b):
    total_fruit = fruit_a + fruit_b

    return total_fruit

print sum_fruit(fruit_a=apples, fruit_b=oranges)

### strings 
hello_text = "Hello, world!"

print hello_text
print hello_text[0]
print hello_text[0:5]


print hello_text + ", Azalea"
print hello_text * 2

# numero vs string
oranges = "2"
print oranges + oranges
print hello_text.upper()

# logical operators (such as and, or, and not)
fullscreen = False
is_windows = True
print fullscreen or is_windows

oranges = 2
print oranges == 2

### Listas (modificlables) vs Tuples (no-modificables)
apples_list = [2, 4, 6, 5]
apples_list.append(7)
print apples_list

apples_tuple = (2, 4, 6, 5)
apples_tuple.append(7)

### Tuple
fruit = {"apples": 2, "oranges": 3}
print type(fruit)

print fruit.keys()
print fruit.values()
print fruit.items()
print fruit["apples"]

#### arrays
import numpy as np

r_list = range(10)
print type(r_list), r_list

r_array = np.arange(10)
print type(r_array), r_array

data = np.ones(shape=[5, 3])
print data
print data.shape
print data.size
print data.ndim

data1 = np.random.random(size=[5, 3])
print data1
# first row, first column
print data1[0, 0]
# second row, first column
print data1[1, 0]
# second row, last column
print data1[1, -1]
# all rows, first column
print data1[:, 0]
# first row, all columns
print data1[0, :]

### save
np.savetxt("data1.txt", data1)
saved_data1 = np.loadtxt("data1.txt")
print saved_data1

np.savetxt("data2.txt", data1, fmt="%.4f", delimiter=",")  # fmt="%.4f" cuatro decimales


### Control de flujo: if else
# tres condiciones en nuestro experimento: 1, 2 y 3.
# si la condicion es 1, muestra Correcto
# si la condicion es 2, muestra Incorrecto
# si la condicion es 3, muestra No_Respuesta

cond_number = 2

if cond_number == 1:
    print ("Correcto")
elif cond_number == 2:
    print ("Incorrecto")
elif cond_number == 3:
    print ("No Respuesta")
else:
    print ("Condición no esperada")

# Ahora como función
def print_condition(cond_number):
    if cond_number == 1:
        print ("Correcto")
    elif cond_number == 2:
        print ("incorrecto")
    elif cond_number == 3:
        print ("No respuesta")
    else:
        print ("Condición no esperada")

print_condition(cond_number=1)
print_condition(cond_number=2)
print_condition(cond_number=3)
print_condition(cond_number=4)

## For 
trials = range(1, 6)

for trial in trials:
    print (trial)


## while
trial = 1

while trial < 6:
    print (trial)
    trial = trial + 1