import numpy as np
import psychopy.visual
import psychopy.event
import psychopy.core

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

grating = psychopy.visual.GratingStim(
    win=win,
    size=[200, 200],
    mask="circle",
    units="pix",
    sf=5.0 / 200.0
)

clock = psychopy.core.Clock()

n_trials = 5
pre_duration_s = 0.5
stim_duration_s = 0.5
min_iti = 2.0

for trial in range(n_trials):
    clock.reset()
    # wait until the 'pre' time has passed
    while clock.getTime() < pre_duration_s:
        win.flip()
    while clock.getTime() < pre_duration_s + stim_duration_s:
        grating.draw()
        win.flip()
    # clear the window
    win.flip()
    keys = psychopy.event.waitKeys()
    while clock.getTime() < min_iti:
        win.flip()

win.close()