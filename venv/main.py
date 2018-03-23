import pygame

import graphics
import units

graphics.init()


import event

ava = units.Ava(25, 25)
ava.facing = "right"
graphics.register(ava)

def quit(e):
    global run
    if e.type == pygame.QUIT:
        run = False
    elif e.type == pygame.KEYUP:
        if ((e.key == pygame.K_F4) and
                (e.mod and pygame.KMOD_ALT)):
            run = False


event.register(ava.handler)
event.register(quit)

clock = pygame.time.Clock()
run = True
frame = 0
while run:
    clock.tick(30)
    #for e in pygame.event.get():
    #    if e.type == pygame.QUIT:
    #        run = False
    #    elif e.type == pygame.KEYUP:
    #        if (e.key == pygame.K_F4) and (e.mod and pygame.KMOD_ALT):
    #            run = False
    #    elif e.type == pygame.KEYDOWN:
    #        if e.key == pygame.K_UP:
    #            ava.facing = "up"
    #        elif e.key == pygame.K_DOWN:
    #            ava.facing = "down"
    #        elif e.key == pygame.K_LEFT:
    #            ava.facing = "left"
    #        elif e.key == pygame.K_RIGHT:
    #            ava.facing = "right"

    event.update()
    ava.update()
    graphics.update()


pygame.display.quit()