import pygame
import numpy as np
from pygame.draw import *

pygame.init()

FPS = 30
size = 800
xsize = size
ysize = size
screen = pygame.display.set_mode((xsize, ysize))
leftbamboo = pygame.Surface((xsize, ysize), pygame.SRCALPHA)
rightbamboo = pygame.Surface((xsize, ysize), pygame.SRCALPHA)

cgreen = (0, 104, 52)
cpink = (255, 176, 129)
cblack = (0, 0, 0)
cwhite = (255, 255, 255)
transparent = (200, 100, 90, 0)

rect(screen, cpink, (0, 0, xsize, ysize))


def leaf(surf, xa, ya, xb, yb):
    ellipse(surf, cgreen, (xa, ya, xb, yb))


def grect(scr, xa, ya, width, height, x):
    polygon(scr, cgreen, [(xa, ya), (xa+width*np.cos(x), ya+width*np.sin(x)),
                             (xa + width*np.cos(x) - height * np.sin(x), ya + width * np.sin(x) + height * np.cos(x)),
                             (xa - height*np.sin(x), ya + height * np.cos(x))])


def grid(gridxsize, gridysize, xstep, ystep, addit):
    cgray = (128, 128, 128)
    for i in range(1, int(gridxsize / xstep) + 1, 1):
        pygame.draw.line(screen, cgray, (i * xstep, 0), (i * xstep, gridysize), 1)
    for i in range(1, int(gridysize / ystep) + 1, 1):
        pygame.draw.line(screen, cgray, (0, i * ystep), (gridxsize, i * ystep), 1)
    for i in range(addit, int(gridxsize / xstep) + 1, addit):
        pygame.draw.line(screen, cblack, (i * xstep, 0), (i * xstep, gridysize), 1)
    for i in range(addit, int(gridysize / ystep) + 1, addit):
        pygame.draw.line(screen, cblack, (0, i * ystep), (gridxsize, i * ystep), 2)


def duga(scr, xa, ya, xb, yb, angle1, angle2):
    arc(scr, cgreen, (xa, ya, xb, yb), angle1, angle2, 4)


def duga2(scr, xa, ya, xb, yb, angle1, angle2):
    arc(scr, cgreen, (xa, ya, xb, yb), angle1, angle2, 3)


xgridstep = 20
ygridstep = xgridstep

rightmove = size / 200 * 0
rightup = size / 200 * -10
x1 = size / 200 * 100
y1 = size / 200 * 150
w1 = size / 200 * 6
h1 = size / 200 * 24
gap = size / 200 * 4
initial = size / 200 * 8
leftmove = size / 200 * 20
leftup = size / 200 * -10

grect(rightbamboo, x1, y1 + initial, w1, h1 + initial, 0)
grect(rightbamboo, x1, y1 - gap - h1, w1, h1 + initial, 0)
grect(rightbamboo, x1 + w1 + 3 * gap / 4, y1 + gap - 3 * h1, w1, h1 + 3 * gap, np.pi / 12)
grect(rightbamboo, x1 + 2 * w1 + 3.4 * gap, y1 - gap - 3.4 * h1 - 5 * gap, w1 - gap / 2, h1 + 3.5 * gap, np.pi / 8)

x1 = size / 200 * 60
y1 = size / 200 * 165
w1 = size / 200 * 3
h1 = size / 200 * 12
gap = size / 200 * 2
initial = size / 200 * 9
leaflength = size / 8
leafhight = size / 200 * 4

grect(leftbamboo, x1, y1 + initial, w1, h1 + initial, 0)
grect(leftbamboo, x1, y1 - gap - h1, w1, h1 + initial, 0)
grect(leftbamboo, x1 + w1 + gap / 2, y1 - 4 * gap - 2 * h1, w1, h1 + 2 * gap, np.pi / 12)
grect(leftbamboo, x1 + 2 * w1 + 3 * gap, y1 - 6 * gap - 2.7 * h1 - 5 * gap, w1 - gap / 2, h1 + 4.5 * gap, np.pi / 8)

surface = pygame.Surface((int(size / 8 * 3), int(size / 8 * 3)), pygame.SRCALPHA)
rect(surface, transparent, (0, 0, int(size / 8 * 3), int(size / 8 * 3)))
leaf(surface, size / 200 * 20, size / 200 * 20, leaflength, leafhight)
leaf(surface, size / 200 * 20, size / 200 * 28, leaflength, leafhight)
leaf(surface, size / 200 * 22, size / 200 * 36, leaflength, leafhight)
leaf(surface, size / 200 * 23, size / 200 * 44, leaflength, leafhight)
leaf(surface, size / 200 * 22, size / 200 * 56, leaflength, leafhight)

surface2 = pygame.transform.rotate(surface, 75)
surface3 = pygame.transform.rotate(surface, -75)
surface3 = pygame.transform.scale(surface3, (int(size / 8 * 3), int(size / 8 * 3)))
rightbamboo.blit(surface2, (size / 800 * 24, size / 800 * 50))
rightbamboo.blit(surface3, (size / 800 * 506, size / 800 * 164))

threeleaves = pygame.Surface((int(size / 8 * 3), int(size / 8 * 3)), pygame.SRCALPHA)
rect(threeleaves, transparent, (0, 0, int(size / 8 * 3), int(size / 8 * 3)))
leaf(threeleaves, size / 200 * 20, size / 200 * 20, leaflength, leafhight)
leaf(threeleaves, size / 200 * 18, size / 200 * 30, leaflength, leafhight)
leaf(threeleaves, size / 200 * 20, size / 200 * 40, leaflength, leafhight)

threeleaves1 = pygame.transform.rotate(threeleaves, -70)
threeleaves1 = pygame.transform.scale(threeleaves1, (int(size / 32 * 11), int(size / 32 * 11)))
threeleaves2 = pygame.transform.rotate(threeleaves, 250)
threeleaves2 = pygame.transform.scale(threeleaves2, (int(size / 32 * 13), int(size / 32 * 13)))
rightbamboo.blit(threeleaves1, (size / 200 * 104, size / 200 * 85))
rightbamboo.blit(threeleaves2, (size / 200 * 19, size / 200 * 98))

leaflength = size / 6

threemoreleaves = pygame.Surface((int(size / 8 * 3), int(size / 8 * 3)), pygame.SRCALPHA)
rect(threemoreleaves, transparent, (0, 0, int(size / 8 * 3), int(size / 8 * 3)))
leaf(threemoreleaves, size / 200 * 22, size / 200 * 20, leaflength, leafhight)
leaf(threemoreleaves, size / 200 * 19, size / 200 * 30, leaflength, leafhight)
leaf(threemoreleaves, size / 200 * 20, size / 200 * 40, leaflength, leafhight)

fiveleaves = pygame.Surface((int(size / 8 * 3), int(size / 8 * 3)), pygame.SRCALPHA)
rect(fiveleaves, transparent, (0, 0, int(size / 8 * 3), int(size / 8 * 3)))
leaf(fiveleaves, size / 200 * 20, size / 200 * 20, leaflength, leafhight)
leaf(fiveleaves, size / 200 * 20, size / 200 * 26, leaflength, leafhight)
leaf(fiveleaves, size / 200 * 22, size / 200 * 32, leaflength, leafhight)
leaf(fiveleaves, size / 200 * 23, size / 200 * 38, leaflength, leafhight)
leaf(fiveleaves, size / 200 * 20, size / 200 * 44, leaflength, leafhight)

fiveleaves1 = pygame.transform.rotate(fiveleaves, -80)
fiveleaves1 = pygame.transform.scale(fiveleaves1, (int(size / 16 * 3), int(size / 16 * 3)))
fiveleaves2 = pygame.transform.rotate(fiveleaves, 255)
fiveleaves2 = pygame.transform.scale(fiveleaves2, (int(size / 14 * 3), int(size / 14 * 3)))
leftbamboo.blit(fiveleaves1, (size / 800 * 282, size / 800 * 410))
leftbamboo.blit(fiveleaves2, (size / 800 * 92, size / 800 * 415))

threemoreleaves1 = pygame.transform.rotate(threemoreleaves, 110)
threemoreleaves1 = pygame.transform.scale(threemoreleaves1, (int(size / 16 * 3), int(size / 16 * 3)))
threemoreleaves2 = pygame.transform.rotate(threemoreleaves, 80)
threemoreleaves2 = pygame.transform.scale(threemoreleaves2, (int(size / 16 * 3), int(size / 16 * 3)))
leftbamboo.blit(threemoreleaves1, (size / 200 * 58, size / 200 * 131))
leftbamboo.blit(threemoreleaves2, (size / 200 * 31, size / 200 * 139))

branches = pygame.Surface((xsize, ysize), pygame.SRCALPHA)
rect(branches, transparent, (0, 0, xsize, ysize))
duga(branches, 100, 100, 300, 180, 0.8, 2.4)
branches1 = pygame.transform.rotate(branches, -30)
rightbamboo.blit(branches1, (size / 200 * -62, size / 200 * 78))

rect(branches, transparent, (0, 0, xsize, ysize))
duga(branches, 100, 100, 280, 180, 0.5, 2.5)
branches1 = pygame.transform.rotate(branches, 30)
rightbamboo.blit(branches1, (size / 200 * 62, size / 200 * 18))

rect(branches, transparent, (0, 0, xsize, ysize))
duga(branches, 100, 100, 700, 360, 0.95, 2)
branches1 = pygame.transform.rotate(branches, 30)
rightbamboo.blit(branches1, (size / 200 * 29, size / 200 * 10))

rect(branches, transparent, (0, 0, xsize, ysize))
duga(branches, 100, 100, 700, 360, 1, 2.2)
branches1 = pygame.transform.rotate(branches, -18)
rightbamboo.blit(branches1, (size / 200 * -90, size / 200 * -5))

branches = pygame.Surface((xsize, ysize), pygame.SRCALPHA)
rect(branches, transparent, (0, 0, size, size))
duga2(branches, 100, 100, 160, 160, 0.2, 2.1)
branches1 = pygame.transform.rotate(branches, -0)
leftbamboo.blit(branches1, (size / 200 * -5, size / 200 * 123))

rect(branches, transparent, (0, 0, xsize, ysize))
duga2(branches, 100, 100, 140, 90, 1, 3)
branches1 = pygame.transform.rotate(branches, 16)
leftbamboo.blit(branches1, (size / 200 * 29.5, size / 200 * 74.5))

rect(branches, transparent, (0, 0, xsize, ysize))
duga2(branches, 100, 100, 200, 90, 0.25, 2.75)
branches1 = pygame.transform.rotate(branches, 40)
leftbamboo.blit(branches1, (size / 200 * 23, size / 200 * 6))

rect(branches, transparent, (0, 0, xsize, ysize))
duga2(branches, 100, 100, 190, 190, 0.5, 2.4)
branches1 = pygame.transform.rotate(branches, -24)
leftbamboo.blit(branches1, (size / 200 * -66, size / 200 * 75))


def pandahead(right, down, pandascale):
    pandasize = size * pandascale


screen.blit(leftbamboo, (0 - leftmove, 0 + leftup))
screen.blit(rightbamboo, (0 + rightmove, 0 + rightup))

grid(xsize, ysize, xgridstep, ygridstep, 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while finished is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
