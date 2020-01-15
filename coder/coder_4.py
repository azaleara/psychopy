#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from psychopy import core, visual, event
import csv
  
## Setup section, read experiment variables from file
win = visual.Window([400,300], monitor="testMonitor", units="cm", fullscr=False)
stimuli = []
datafile = open("redgreen_stimuli.csv", "rb")
reader = csv.reader(datafile, delimiter=";")
for row in reader:
    if len(row)==2:         # ignore empty and incomplete lines
        size = float(row[0])  # the first element in the row converted to a floating point number
        color = row[1]        # the second element in the row
        stimulus = visual.Rect(win, width=size, height=size)
        stimulus.fillColor = color
        stimuli.append(stimulus)
datafile.close()
  
## Experiment Section, use experiment variables here
for stimulus in stimuli:
    stimulus.draw()
    win.flip()
    core.wait(1.000)
 
## Closing Section
win.close()
core.quit()

##### Audio

#!/usr/bin/env python
from psychopy import core, sound
s = sound.Sound(value="C", secs=0.5) 
 
s.play()
core.wait(4.0)
 
core.quit()


# https://www.socsci.ru.nl/wilberth/nocms/psychopy/print.php