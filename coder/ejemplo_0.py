import os
import sys
import numpy as np
import psychopy.visual
import psychopy.event
import psychopy.gui
import psychopy.core

gui = psychopy.gui.Dlg()

gui.addField("Sujeto ID:")
gui.addField("Condición. num.:")
gui.addField("Sesión num_rep:")

gui.show()

subj_id = gui.data[0]
cond_num = gui.data[1]
rep_num = gui.data[2]

data_path = subj_id + "_cond_" + cond_num + "_rep_" + rep_num + ".tsv"

if os.path.exists(data_path):
    sys.exit("Data path " + data_path + " already exists!")

responses = []

sfm_size_pix = 200
sfm_dot_size_pix = 5
sfm_n_dots = 1000
sfm_dot_shape = "gauss"

if cond_num == "1":
    sfm_speed_rev_per_s = 0.2
elif cond_num == "2":
    sfm_speed_rev_per_s = 0.1
else:
    sys.exit("Unknown condition number")

sfm_y_pos = np.random.uniform(-sfm_size_pix / 2, +sfm_size_pix / 2, sfm_n_dots)

sfm_x_phase = np.random.uniform(0, 2 * np.pi, sfm_n_dots)

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

sfm_stim = psychopy.visual.ElementArrayStim(
    win=win,
    units="pix",
    nElements=sfm_n_dots,
    elementTex=None,
    elementMask=sfm_dot_shape,
    sizes=sfm_dot_size_pix
)

instructions = psychopy.visual.TextStim(
    win=win,
    wrapWidth=350,
)

instructions.text = """
Aprieta la tecla de la flecha izquierda cuando veas la figura rotar a la izquierda.\n
Aprieta la tecla de la flecha derecha cuando veas la figura rotar a la derecha.\n
\n
Presiona cualquier tecla para comenzar.
"""

instructions.draw()
win.flip()

psychopy.event.waitKeys()

duration_s = 120.0
clock = psychopy.core.Clock()

while clock.getTime() < duration_s:
    phase_offset = (clock.getTime() * sfm_speed_rev_per_s) * (2 * np.pi)
    sfm_xys = []
    for i_dot in range(sfm_n_dots):
        dot_x_pos = np.cos(sfm_x_phase[i_dot] + phase_offset) * sfm_size_pix / 2.0
        sfm_xys.append([dot_x_pos, sfm_y_pos[i_dot]])
    sfm_stim.xys = sfm_xys
    sfm_stim.draw()
    win.flip()
    keys = psychopy.event.getKeys(
        keyList=["left", "right"],
        timeStamped=clock
    )
    for key in keys:
        if key[0] == "left":
            key_num = 1
        else:
            key_num = 2
        responses.append([key_num, key[1]])

np.savetxt(data_path, responses, delimiter="\t")
win.close()

