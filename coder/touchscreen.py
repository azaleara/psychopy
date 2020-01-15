from __future__ import print_function

from psychopy import iohub
from psychopy.visual.window import Window
from psychopy.visual.circle import Circle

io = iohub.launchHubServer()
mouse = io.devices.mouse

win = Window(units='pix', fullscr=True)
circle = Circle(win, size=300)
circle.draw()
win.flip()

mouse.clearEvents()

while True:
    e = mouse.getEvents(event_type=(iohub
                                    .EventConstants
                                    .MOUSE_BUTTON_PRESS))

    if e:
        x, y = e[0].x_position, e[0].y_position

        if circle.contains((x, y), units='pix'):
            print('Received button press!')
            break

win.close()
io.quit()