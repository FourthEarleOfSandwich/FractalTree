# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pygame as py
import random as rand
py.init()
screen = py.display.set_mode((800, 800))
py.display.set_caption("Fractal Tree")
#colors
white = (255, 255, 255)
black = (0, 0, 0)
#startingvalues
startingX = screen.get_width() / 2
startingY = screen.get_height() / 2
startLen = 200
def branch(len, xLoc, yLoc, orientationUp):
    py.time.wait(10)
    py.display.update()
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
    if len < 5:
        return
    nextLineLen = len * 0.7
    if orientationUp:
        py.draw.line(screen, white, (xLoc + nextLineLen, yLoc), (xLoc, yLoc))

        branch(nextLineLen, xLoc + nextLineLen, yLoc, False)
        py.draw.line(screen, white, (xLoc - nextLineLen, yLoc), (xLoc, yLoc))
        branch(nextLineLen, xLoc - nextLineLen, yLoc, False)


    elif orientationUp == False:
        py.draw.line(screen, white, (xLoc, yLoc + nextLineLen), (xLoc, yLoc))

        branch(nextLineLen, xLoc, yLoc + nextLineLen, True)
        py.draw.line(screen, white, (xLoc, yLoc - nextLineLen), (xLoc, yLoc))
        branch(nextLineLen, xLoc, yLoc - nextLineLen, True)




#Screen loop
running = True
while running:
    screen.fill(black)
    py.draw.line(screen, white, (startingX, startingY + startLen), (startingX, startingY))
    branch(startLen, startingX, startingY, True)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    py.display.update()







