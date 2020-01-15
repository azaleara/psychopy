import os
import sys
import random
import numpy as np
import psychopy.visual
import psychopy.event
import psychopy.gui
import psychopy.core


gui = psychopy.gui.Dlg()

gui.addField("Subject ID:")
gui.addField("Repeat num:")

gui.show()

subj_id = gui.data[0]
rep_num = gui.data[1]

data_path = subj_id + "_rep_" + rep_num + ".tsv"

if os.path.exists(data_path):
    sys.exit("Data path " + data_path + " already exists!")

exp_data = []

bg_colour = [-1, -1, -0.25]

oval_radius_pix = [10, 18]
oval_fill_colour = [-1, 0.25, -1]
n_ovals_per_dim = 40
oval_col_ori_change = -30
oval_row_ori_change = +30
oval_edge_contrast = 1.0
oval_line_width = 3.0
oval_n_edges = 128

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False,
    color=bg_colour
)

oval = psychopy.visual.Circle(
    win=win,
    radius=oval_radius_pix,
    units="pix",
    edges=oval_n_edges,
    fillColor=oval_fill_colour,
)

vertices = oval.verticesPix.tolist()

right_vertices = vertices[:(n_edges / 2 + 1)]

left_vertices = []

for vertex in right_vertices:
    left_vertices.append([-vertex[0], vertex[1]])

left_side = psychopy.visual.ShapeStim(
    win=win,
    vertices=left_vertices,
    closeShape=False,
    units="pix",
    lineWidth=oval_line_width,
    lineColor=[-oval_edge_contrast] * 3
)

right_side = psychopy.visual.ShapeStim(
    win=win,
    vertices=right_vertices,
    closeShape=False,
    units="pix",
    lineWidth=oval_line_width,
    lineColor=[+oval_edge_contrast] * 3
)

offsets = range(-180, 181, n_ovals_per_dim)

oval_line_contrasts = [0, 0.25, 0.5, 0.75, 1.0]
n_oval_line_contrasts = len(oval_line_contrasts)

n_trials_per_line_contrast = 10

trial_oval_line_contrasts = oval_line_contrasts * n_trials_per_line_contrast
random.shuffle(trial_oval_line_contrasts)

instructions = psychopy.visual.TextStim(
    win=win,
    wrapWidth=350,
)

instructions.text = """
Press a key from 1 to 5 to rate your sense of motion for the stimulus on a
given trial.\n
\n
Press any key to begin.
"""

instructions.draw()
win.flip()

psychopy.event.waitKeys()

pre_duration_s = 0.5
stim_duration_s = 0.5

min_iti_s = 2.0

clock = psychopy.core.Clock()

for trial_oval_line_contrast in trial_oval_line_contrasts:

    left_side.lineColor = [-trial_oval_line_contrast] * 3
    right_side.lineColor = [+trial_oval_line_contrast] * 3

    clock.reset()

    while clock.getTime() < pre_duration_s:
        win.flip()

    while clock.getTime() < (pre_duration_s + stim_duration_s):

        row_count = 0

        for y_offset in offsets:

            ori = row_count * oval_row_ori_change

            for x_offset in offsets:

                ori = ori + oval_col_ori_change

                for stim in [oval, left_side, right_side]:
                    stim.pos = [x_offset, y_offset]
                    stim.ori = ori
                    stim.draw()

            row_count = row_count + 1

        win.flip()

    win.flip()

    keys = psychopy.event.waitKeys(
        keyList=["1", "2", "3", "4", "5", "q"],
        timeStamped=clock
    )

    for key in keys:

        if key[0] == "q":
            sys.exit("User quit")

        key_num = int(key[0])
        rt = key[1]

    trial_data = [trial_oval_line_contrast, key_num, rt]

    exp_data.append(trial_data)

    while clock.getTime() < min_iti_s:
        win.flip()

np.savetxt(data_path, exp_data, delimiter="\t")

win.close()