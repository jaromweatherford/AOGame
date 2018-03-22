import pygame
from pygame.locals import *

pygame.display.init()

width = 640
height = 400

assets = {}

renderables = []

screen = None
background_mask = None
background = None

def update():
    global screen, background, renderables, width, height


    screen.fill((0, 0, 0))
    if background:
        screen.blit(background, (0, 0))
    for r in renderables:
        r.render(screen)

    pygame.display.flip()


def register(renderable):
    global renderables
    if renderable not in renderables:
        renderables.append(renderable)


def remove(renderable):
    global renderables
    if renderable in renderables:
        renderables.remove(renderable)


def init():
    global screen, background, background_mask
    background = load("resources\\room03-1.png")
    pygame.display.init()
    screen = pygame.display.set_mode((width, height))
    background_mask = pygame.mask.from_surface(background.convert_alpha())


def load(file):
    global assets
    if file in assets:
        return assets[file]
    else:
        image = pygame.image.load(file)
        assets[file] = image
        return image
