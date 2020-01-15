#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A PsychoPy experiment is now divided in three sections. In the 
# Setup section we read files and open windows. These things are slow 
# and therefore should not be done while the experiment is running.
# in the Experiment section we do the actual presenting of stimuli
# en in the Closing section we do what has to be done after the 
# experiment if finished.
 
## Setup Section
from psychopy import core, visual
 
win = visual.Window([300,300], monitor="testMonitor")
 
# The following block of code prepares a text stimulus called message
# a string variable contains text, it must be enclosed in quotation marks
myText = "nr:   grade:\n"
# a list variable contains a number of variables
grades = [7.1, 4.5, 6.3, 5.8, 8.2]

# do something for every item in the list
for studentNumber, grade in enumerate(grades):
    # extend the text with one line, "\n" tells PsychoPy to start en new line
    myText += str(studentNumber) + " ,      " + str(grade) + "\n"
 
# write myText to a TextStim object called message and draw this to the window
message = visual.TextStim(win, text=myText)
message.draw()
 
## Experiment Section
win.flip()
core.wait(5.0)
 
## Closing Section
win.close()
core.quit()



#### 
# Type the following experiment in the PsychoPy editor. You need not copy the comments. Save it and execute.
#   Present the average grade on the screen. For calculating the average grade you can use: average = sum(grades)/len(grades). 
#   For adding a text to the myText string you can use myText += "\naverage: " + str(average). Where would this code go?

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A PsychoPy experiment is now divided in three sections. In the 
# Setup section we read files and open windows. These things are slow 
# and therefore should not be done while the experiment is running.
# in the Experiment section we do the actual presenting of stimuli
# en in the Closing section we do what has to be done after the 
# experiment if finished.
 
## Setup Section
from psychopy import core, visual
 
win = visual.Window([300,300], monitor="testMonitor")
 
# The following block of code prepares a text stimulus called message
# a string variable contains text, it must be enclosed in quotation marks
myText = "nr:   grade:\n"
# a list variable contains a number of variables
grades = [7.1, 4.5, 6.3, 5.8, 8.2]
average = sum(grades)/len(grades)

# do something for every item in the list
for studentNumber, grade in enumerate(grades):
    # extend the text with one line, "\n" tells PsychoPy to start en new line
    myText += str(studentNumber) + " ,      " + str(grade) + "\n"

myText += "average: " + str(average)

# write myText to a TextStim object called message and draw this to the window
message = visual.TextStim(win, text = myText)
message.draw()
 
## Experiment Section
win.flip()
core.wait(5.0)
 
## Closing Section
win.close()
core.quit()



#### 
#   Add a third column to the screen, indicating whether the student has passed or failed the test.

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A PsychoPy experiment is now divided in three sections. In the 
# Setup section we read files and open windows. These things are slow 
# and therefore should not be done while the experiment is running.
# in the Experiment section we do the actual presenting of stimuli
# en in the Closing section we do what has to be done after the 
# experiment if finished.
 
## Setup Section
from psychopy import core, visual
 
win = visual.Window([300,300], monitor="testMonitor")
 
# The following block of code prepares a text stimulus called message
# a string variable contains text, it must be enclosed in quotation marks
myText = "nr:   grade:   aprove:\n"
# a list variable contains a number of variables
grades = [7.1, 4.5, 6.3, 5.8, 8.2]
#average = sum(grades)/len(grades)
final = [i >= 6 for i in grades]

# do something for every item in the list
for studentNumber, (grade, aprove) in enumerate(zip(grades, final)):
    # extend the text with one line, "\n" tells PsychoPy to start en new line
    myText += str(studentNumber) + " ,      " + str(grade) + " ,      " + str(aprove) + "\n"

#myText += "average: " + str(average)

# write myText to a TextStim object called message and draw this to the window
message = visual.TextStim(win, text = myText)
message.draw()
 
## Experiment Section
win.flip()
core.wait(5.0)
 
## Closing Section
win.close()
core.quit()


###
# Funciones

def showText(window, myText): 
    message = visual.TextStim(window, text=myText)
    message.draw()
    window.flip()

win = visual.Window([400,300], monitor="testMonitor")
showText (win, "Hello World")