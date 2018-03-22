import pygame

pygame.key.set_repeat(20, 20)

listeners = []


def register(listener):
    global listeners
    if listener not in listeners:
        listeners.append(listener)

def remove(listener):
    global listeners
    if listener in listeners:
        listeners.remove(listener)


def update():
    global listeners

    for e in pygame.event.get():
        for l in listeners:
            l(e)