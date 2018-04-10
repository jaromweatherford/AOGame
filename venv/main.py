import pygame

import graphics
import audio
import units

graphics.init()


import event

audio.init()

ava = units.Ava(25, 25)
ava.facing = "right"
graphics.register(ava)

run = True
cover = True

def handle(e):
    global run, cover
    if e.type == pygame.QUIT:
        run = False
    elif e.type == pygame.KEYUP:
        if ((e.key == pygame.K_F4) and
                (e.mod and pygame.KMOD_ALT)):
            run = False
        elif e.key == pygame.K_b:
            cover = not cover
            print "cover: ", cover


event.register(ava.handler)
event.register(handle)

clock = pygame.time.Clock()
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
    graphics.update(cover)




pygame.display.quit()