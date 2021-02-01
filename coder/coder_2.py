#!/usr/bin/env python
# -*- coding: utf-8 -*-
# There is little experiment if the participant cannot give any input.
# Here we changed assignment 2 a bit so that it waits for a keys, rather
# than waiting 5 s. Note that we need to import the event module from
# PsychoPy to make this work.

from psychopy import core, visual, event
  
## Setup Section
win = visual.Window([400,300], monitor="testMonitor")
textString = "Presiona cualquier tecla para comenzar"
message = visual.TextStim(win, text=textString)
 
## Experiment Section
message.draw()
win.flip()
c = event.waitKeys() # read a character
message = visual.TextStim(win, text=textString + c[0])
message.draw()
win.flip()
event.waitKeys()
 
## Closing Section
win.close()
core.quit()