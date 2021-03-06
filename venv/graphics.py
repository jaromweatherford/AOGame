import pygame
from pygame.locals import *

pygame.display.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

width = 640
height = 400

assets = {}

renderables = []

picture = None
screen = None
background_mask = None
background = None
pixel_array = None

def update(cover):
    global screen, background, renderables, picture, width, height

    screen.fill((0, 0, 0))
    if not cover:
        if background:
            screen.blit(background, (0, 0))
        for r in renderables:
            r.render(screen)
    else:
        screen.blit(picture, (0, 0))
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
    global screen, background, background_mask, pixel_array, picture
    background = load(r"resources\room04.png")
    picture = load(r"resources\jao1.png")
    pygame.display.init()
    screen = pygame.display.set_mode((width, height))
    background_mask = pygame.mask.from_surface(background.convert_alpha())
    pixel_array = pygame.PixelArray(background.copy())


def cover():
    global picture
    screen.blit(picture, (0, 0))


def load(file):
    global assets
    if file in assets:
        return assets[file]
    else:
        image = pygame.image.load(file)
        assets[file] = image
        return image

