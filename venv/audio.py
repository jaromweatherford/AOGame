import pygame.mixer

pygame.mixer.init(channels=2)

closer = None
close = None
medium = None
far = None
thump = None
chan_left = None
chan_right = None


def init():
    global closer, close, medium, far, thump, chan_left, chan_right
    #closer = pygame.mixer.Sound(r"resources/solonearstep.ogg")
    #close = pygame.mixer.Sound(r"resources/solohalfnear.ogg")
    #medium = pygame.mixer.Sound(r"resources/solohalffar.ogg")
    #far = pygame.mixer.Sound(r"resources/solofarstep.ogg")
    closer = pygame.mixer.Sound(r"resources/closer.ogg")
    close = pygame.mixer.Sound(r"resources/close2.ogg")
    medium = pygame.mixer.Sound(r"resources/medium2.ogg")
    far = pygame.mixer.Sound(r"resources/far2.ogg")
    thump = pygame.mixer.Sound(r"resources/thump.ogg")
    chan_left = pygame.mixer.Channel(0)
    chan_right = pygame.mixer.Channel(1)

def play_thump():
    global thump
    thump.play()

def play_echo(left=1.0, right=1.0):
    global closer, close, medium, far, chan_left, chan_right
    print "left side: ", left
    print "right side: ", right
    print
    print
    chan_left.set_volume(1.0, 0)
    chan_right.set_volume(0, 1.0)
    if left < 20:
        chan_left.play(closer)
    elif left < 60:
        chan_left.play(close)
    elif left < 150:
        chan_left.play(medium)
    else:
        chan_left.play(far)
    if right < 20:
        chan_right.play(closer)
    elif right < 60:
        chan_right.play(close)
    elif right < 150:
        chan_right.play(medium)
    else:
        chan_right.play(far)