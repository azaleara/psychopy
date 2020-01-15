import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

img = psychopy.visual.ImageStim(
    win=win,
    image="/Users/azaleareyesaguilar/Desktop/coder/all.png",
    units="pix"
)

size_x = img.size[0]
size_y = img.size[1]
img.size = [size_x * 1.5, size_y * 1.5]
#img.opacity = 0.5

img.draw()
win.flip()
# para salvar screenshot de la ventana de psychopy 
#win.getMovieFrame()
#win.saveMovieFrames("name.png")
psychopy.event.waitKeys()
win.close()


#### Dots
import random
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

n_dots = 200
dot_xys = []

for dot in range(n_dots):
    dot_x = random.uniform(-200, 200)
    dot_y = random.uniform(-200, 200)
    dot_xys.append([dot_x, dot_y])

dot_stim = psychopy.visual.ElementArrayStim(
    win=win,
    units="pix",
    nElements=n_dots,
    elementTex=None,
    elementMask="circle",
    xys=dot_xys,
    sizes=10
)

dot_stim.draw()
win.flip()
psychopy.event.waitKeys()
win.close()

# con gratings 
import random
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

n_dots = 200
dot_xys = []

for dot in range(n_dots):
    dot_x = random.uniform(-200, 200)
    dot_y = random.uniform(-200, 200)
    dot_xys.append([dot_x, dot_y])

dot_stim = psychopy.visual.ElementArrayStim(
    win=win,
    units="pix",
    nElements=n_dots,
    elementTex="sin",
    elementMask="gauss",
    sfs=5.0 / 2.5,
    xys=dot_xys,
    sizes=20
)

dot_stim.draw()
win.flip()
psychopy.event.waitKeys()
win.close()

# orietaciones al azar (random)
import random
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

n_dots = 200
dot_xys = []
dot_oris = []

for dot in range(n_dots):
    dot_x = random.uniform(-200, 200)
    dot_y = random.uniform(-200, 200)
    dot_xys.append([dot_x, dot_y])
    dot_oris.append(random.uniform(0, 180))

dot_stim = psychopy.visual.ElementArrayStim(
    win=win,
    units="pix",
    nElements=n_dots,
    elementTex="sin",
    elementMask="gauss",
    sfs=5.0 / 2.5,
    xys=dot_xys,
    sizes=20,
    oris=dot_oris
)

dot_stim.draw()
win.flip()
psychopy.event.waitKeys()
win.close()


### Dinámica - tiempo
# reloj 
import psychopy.core

clock = psychopy.core.Clock()

for iteration in range(2):
    psychopy.core.wait(1.0)
    print clock.getTime()

### un ejemplo
import psychopy.visual
import psychopy.event
import psychopy.core

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

clock = psychopy.core.Clock()
text = psychopy.visual.TextStim(win=win)

grating = psychopy.visual.GratingStim(
    win=win,
    size=[200, 200],
    mask="circle",
    units="pix",
    sf=5.0 / 200.0
)

text.text = "Press any key to show the grating"

text.draw()
win.flip()
psychopy.event.waitKeys()
clock.reset()

while clock.getTime() < 0.5:
    grating.draw()
    win.flip()

text.text = "Press any key to finish"
text.draw()
win.flip()
psychopy.event.waitKeys()
win.close()


# ejemplo con 30 frames 
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

text = psychopy.visual.TextStim(win=win)

grating = psychopy.visual.GratingStim(
    win=win,
    size=[200, 200],
    mask="circle",
    units="pix",
    sf=5.0 / 200.0
)

text.text = "Press any key to show the grating"
text.draw()
win.flip()
psychopy.event.waitKeys()

for frame in range(30):
    grating.draw()
    win.flip()

text.text = "Press any key to finish"
text.draw()
win.flip()
psychopy.event.waitKeys()
win.close()


# estímulos dinámicos
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
keep_going = True

while keep_going:
    grating.phase = np.mod(clock.getTime() / 0.5, 1)
    grating.draw()
    win.flip()
    keys = psychopy.event.getKeys()
    if len(keys) > 0:
        keep_going = False

win.close()


# control de los estímulos 
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