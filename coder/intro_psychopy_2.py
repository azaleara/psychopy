# registro de respuestas
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

keys = psychopy.event.waitKeys()
print keys
win.close()

# Determinar qué teclas puedes ser usadas para responder
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

keys = psychopy.event.waitKeys(keyList=["left", "right"])
win.close()

# Registrar tiempo de reacción
import psychopy.visual
import psychopy.event
import psychopy.core

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

clock = psychopy.core.Clock()
keys = psychopy.event.waitKeys(timeStamped=clock)
print keys
win.close()


###
import os

data_path = "p1000_exp_cond_1_rep_1.tsv"
data_path_exists = os.path.exists(data_path)
print data_path_exists

# para no sobre escribir 
import os
import sys

data_path = "p1000_exp_cond_1_rep_1.tsv"
data_path_exists = os.path.exists(data_path)

# we will pretend that it does exist
data_path_exists = True

if data_path_exists:
    sys.exit("Filename " + data_path + " already exists!")

# oeganizar los datos 
import random
import pprint

data = []

for trial in range(10):
    data.append(
        [
            random.uniform(0, 180),
            random.choice(["left", "right"])
        ]
    )

pprint.pprint(data)

# otro para organizar
import random
import pprint

data = []

for trial in range(10):
    data.append(
        [
            random.uniform(0, 180),
            random.choice(["left", "right"])
        ]
    )

pprint.pprint(data)
coded_data = []

for data_row in data:

    if data_row[1] == "left":
        data_row[1] = 1
    elif data_row[1] == "right":
        data_row[1] = 2
    coded_data.append(data_row)

pprint.pprint(coded_data)

# guardar los datos 
import random
import numpy as np
import pprint

data = []

for trial in range(10):
    data.append(
        [
            random.uniform(0, 180),
            random.choice([1, 2])
        ]
    )

pprint.pprint(data)

np.savetxt(
    "p1000_exp_cond_1_run_2.tsv",
    data,
    delimiter="\t"
)

# para verificar los datos 
import numpy as np
import pprint

data = np.loadtxt(
    "p1000_exp_cond_1_run_2.tsv",
    delimiter="\t"
)

pprint.pprint(data.tolist())