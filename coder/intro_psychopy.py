### http://www.djmannion.net/psych_programming/vision/intro/intro.html

import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False,
    color=[1, 1, 1]
)

text = psychopy.visual.TextStim(
    win=win,
    text="Hello, world!",
    color=[-1, -1, -1]
)

text.draw()
win.flip()

# change text to green
text.color = [-1, 0, -1]
# draw text again
text.draw()
win.flip()

psychopy.event.waitKeys()
win.close()


### gratings
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

grating = psychopy.visual.GratingStim(
    win=win,
    units="pix",
    size=[150, 150]
)

grating.draw()
win.flip()
psychopy.event.waitKeys()
win.close()


# Posición y fase de las gratings
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

grating = psychopy.visual.GratingStim(
    win=win,
    units="pix",
    size=[80, 80]
)

grating_vpos = [150, 50, -50, -150]
grating_phase = [0.0, 0.16, 0.33, 0.5]

for i_phase in range(4):

    grating.phase = grating_phase[i_phase]

    grating.pos = [0, grating_vpos[i_phase]]

    grating.draw()

win.flip()
psychopy.event.waitKeys()
win.close()


# Frecuencias: ciclos en una unidad, i.e. pixeles
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

grating = psychopy.visual.GratingStim(
    win=win,
    units="pix",
    size=[150, 150]
)

grating.sf = 5.0 / 150.0    # 5 ciclos en 150 pixeles
grating.draw()
win.flip()
psychopy.event.waitKeys()
win.close()


# orientación de las lineas: y el uso de una más cara gauseana o de circulo
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

grating = psychopy.visual.GratingStim(
    win=win,
    units="pix",
    size=[80, 80]
)

grating.sf = 5.0 / 80.0
grating.mask = "gauss"
#grating.mask = "circle"

orientations = [0.0, 45.0, 90.0, 135.0]
grating_hpos = [-150, -50, 50, 150]

for i_grating in range(4):
    grating.ori = orientations[i_grating]
    grating.pos = [grating_hpos[i_grating], 0]

    grating.draw()

win.flip()
psychopy.event.waitKeys()
win.close()

# Contraste
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

grating = psychopy.visual.GratingStim(
    win=win,
    units="pix",
    size=[80, 80]
)

grating.sf = 5.0 / 80.0
grating.mask = "circle"

contrasts = [0.1, 0.2, 0.4, 0.8]
grating_hpos = [-150, -50, 50, 150]

for i_grating in range(4):
    grating.contrast = contrasts[i_grating]
    grating.pos = [grating_hpos[i_grating], 0]
    grating.draw()

win.flip()
psychopy.event.waitKeys()
win.close()


### Shapes
# lineas
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False,
    color=[1, 1, 1]
)

line = psychopy.visual.Line(
    win=win,
    units="pix",
    lineColor=[-1, -1, -1]
)

line.start = [-200, -200]
line.end = [+200, +200]
line.lineColor = [-1, -1, 1]
line.lineWidth = 5

line.draw()
win.flip()
psychopy.event.waitKeys()
win.close()

### ilusiones: Ponzo illusion
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False,
    color=[1, 1, 1]
)

line = psychopy.visual.Line(
    win=win,
    units="pix",
    lineColor=[-1, -1, -1]
)

bar_horiz_offset = 20
bar_vert_offset = 80

for bar_offset in [-1, +1]:
    line.start = [-bar_horiz_offset, bar_vert_offset * bar_offset]
    line.end = [+bar_horiz_offset, bar_vert_offset * bar_offset]
    line.draw()

pers_far_horiz_offset = 150
pers_near_horiz_offset = 10
pers_vert_offset = 140

for pers_offset in [-1, +1]:
    line.start = [pers_far_horiz_offset * pers_offset, -pers_vert_offset]
    line.end = [pers_near_horiz_offset * pers_offset, +pers_vert_offset]
    line.draw()

win.flip()
win.getMovieFrame()
psychopy.event.waitKeys()
win.close()


# rectangulos y circulos
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False,
    color=[1, 1, 1]
)

rect = psychopy.visual.Rect(
    win=win,
    units="pix",
    width=200,
    height=100,
    fillColor=[1, -1, -1],
    lineColor=[-1, -1, 1]
)

#circle = psychopy.visual.Circle(
#    win=win,
#    units="pix",
#    radius=150,
#    fillColor=[0, 0, 0],
#    lineColor=[-1, -1, -1],
#    edges=128
#)
#circle.draw()

rect.draw()
win.flip()
psychopy.event.waitKeys()
win.close()

# Mondrian pattern
import random
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False,
    color=[1, 1, 1]
)

rect = psychopy.visual.Rect(win=win, units="pix")

n_rect = 500

for i_rect in range(n_rect):
    rect.width = random.uniform(10, 100)
    rect.height = random.uniform(10, 100)
    rect_color = random.uniform(-1, 1)
    rect.fillColor = rect_color
    rect.lineColor = rect_color
    rect.pos = [
        random.uniform(-200, 200),
        random.uniform(-200, 200)
    ]
    rect.draw()

win.flip()
psychopy.event.waitKeys()
win.close()


# Ebbinghaus illusion
import psychopy.visual
import psychopy.event
import psychopy.misc

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False,
    color=[1, 1, 1]
)

circle = psychopy.visual.Circle(
    win=win,
    units="pix",
    fillColor=[-1] * 3,
    lineColor=[-1] * 3,
    edges=128
)

# 'test' circles
circle.radius = 12
test_offset = 100

for offset in [-1, +1]:
    circle.pos = [test_offset * offset, 0]
    circle.draw()

# 'surround' circles
surr_thetas = [0, 72, 144,  216,  288]
surr_r = 50

for i_surr in range(len(surr_thetas)):
    [surr_pos_x, surr_pos_y] = psychopy.misc.pol2cart(
        surr_thetas[i_surr],
        surr_r
    )
    surr_pos_x = surr_pos_x + test_offset
    circle.pos = [surr_pos_x, surr_pos_y]
    circle.radius = 25
    circle.draw()

win.flip()
win.getMovieFrame()
psychopy.event.waitKeys()
win.close()