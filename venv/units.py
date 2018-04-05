
import math
import pygame

import graphics
import audio


class Unit(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0.0


class Ava(Unit):
    def __init__(self, x, y):
        super(Ava, self).__init__(x, y)
        self.spritesheet = graphics.load(r"resources\ava_small.png")
        self.rot_sprite = self.spritesheet
        self.direction = 0
        self.speed = 1
        self.moving = False
        self.blocked = False
        self.w = False
        self.a = False
        self.s = False
        self.d = False
        self.left = False
        self.right = False
        self.space = False
        self.new_space = True
        self.sensitivity = 5
        self.step_counter = 0

    def update(self):
        rad = math.radians(self.direction)
        ava_mask = pygame.mask.from_surface(self.rot_sprite.convert_alpha())
        old_x = self.x
        old_y = self.y
        new_x = old_x
        new_y = old_y
        distances = [0, 0, 0, 0]
        while not graphics.background_mask.get_at((int(self.x), int(self.y) - distances[1])):
            distances[1] += 1
        while not graphics.background_mask.get_at((int(self.x), int(self.y) + distances[3])):
            distances[3] += 1
        while not graphics.background_mask.get_at((int(self.x) - distances[2], int(self.y))):
            distances[2] += 1
        while not graphics.background_mask.get_at((int(self.x) + distances[0], int(self.y))):
            distances[0] += 1
        """if self.left:
            self.direction += self.sensitivity
        if self.right:
            self.direction -= self.sensitivity"""
        if self.w:
            new_y -= self.speed * math.sin(rad)
            new_x += self.speed * math.cos(rad)
            if graphics.background.get_at((int(new_x), int(new_y)))[3] != 0:
                new_x = old_x
                new_y = old_y
                if not self.blocked:
                    audio.play_thump()
                    self.blocked = True
            else:
                self.moving = True
                old_x = new_x
                old_y = new_y
                if self.y < 0:
                    self.y = 0
                if self.x < 0:
                    self.x = 0
                if self.y > (graphics.height - 40):
                    self.y = (graphics.height - 40)
                if self.x > (graphics.width - 40):
                    self.x = (graphics.width - 40)
        if self.s:
            new_y += self.speed * math.sin(rad)
            new_x -= self.speed * math.cos(rad)
            if graphics.background.get_at((int(new_x), int(new_y)))[3] != 0:
                new_x = old_x
                new_y = old_y
                if not self.blocked:
                    audio.play_thump()
                    self.blocked = True
            else:
                self.moving = True
                old_x = new_x
                old_y = new_y
                if self.y < 0:
                    self.y = 0
                if self.x < 0:
                    self.x = 0
                if self.y > (graphics.height - 40):
                    self.y = (graphics.height - 40)
                if self.x > (graphics.width - 40):
                    self.x = (graphics.width - 40)
        if self.a:
            new_y -= self.speed * math.cos(rad)
            new_x -= self.speed * math.sin(rad)
            if graphics.background.get_at((int(new_x), int(new_y)))[3] != 0:
                new_x = old_x
                new_y = old_y
                if not self.blocked:
                    audio.play_thump()
                    self.blocked = True
            else:
                self.moving = True
                old_x = new_x
                old_y = new_y
                if self.y < 0:
                    self.y = 0
                if self.x < 0:
                    self.x = 0
                if self.y > (graphics.height - 40):
                    self.y = (graphics.height - 40)
                if self.x > (graphics.width - 40):
                    self.x = (graphics.width - 40)
        if self.d:
            new_y += self.speed * math.cos(rad)
            new_x += self.speed * math.sin(rad)
            if graphics.background.get_at((int(new_x), int(new_y)))[3] != 0:
                new_x = old_x
                new_y = old_y
                if not self.blocked:
                    audio.play_thump()
                    self.blocked = True
            else:
                self.moving = True
                old_x = new_x
                old_y = new_y
        if self.moving or self.space:
            if self.moving:
                self.step_counter += 1
                self.blocked = False
            if (self.step_counter > 20 or self.space):
                self.step_counter = 0
                left_side = 0
                right_side = 0
                norm_dir = abs(self.direction % 360)
                if norm_dir < 45 or norm_dir > 315:
                    left_side = distances[1]
                    right_side = distances[3]
                    print "facing right"
                elif norm_dir < 135:
                    left_side = distances[2]
                    right_side = distances[0]
                    print "facing up"
                elif norm_dir < 225:
                    left_side = distances[3]
                    right_side = distances[1]
                    print "facing left"
                else:
                    left_side = distances[0]
                    right_side = distances[2]
                    print "facing down"
                audio.play_echo(left_side, right_side)
            self.space = False
        self.x = new_x
        self.y = new_y
        if self.y < 0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.y > (graphics.height - 1):
            self.y = (graphics.height - 1)
        if self.x > (graphics.width - 1):
            self.x = (graphics.width - 1)
        self.moving = False

    def render(self, surface):
        orig_center = self.spritesheet.get_rect().center
        self.rot_sprite = pygame.transform.rotate(self.spritesheet, self.direction)
        rot_rect = self.rot_sprite.get_rect()
        rot_rect.center = orig_center
        surface.blit(self.rot_sprite, (self.x + 2 * rot_rect[0], self.y + 2 * rot_rect[1]), rot_rect)

    def handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.w = True
            elif event.key == pygame.K_s:
                self.s = True
            elif event.key == pygame.K_a:
                self.a = True
            elif event.key == pygame.K_d:
                self.d = True
            elif event.key == pygame.K_LEFT:
                self.left = True
            elif event.key == pygame.K_RIGHT:
                self.right = True
            elif event.key == pygame.K_SPACE:
                print self.new_space
                if self.new_space == True:
                    self.space = True
                    self.new_space = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.w = False
            elif event.key == pygame.K_s:
                self.s = False
            elif event.key == pygame.K_a:
                self.a = False
            elif event.key == pygame.K_d:
                self.d = False
            elif event.key == pygame.K_LEFT:
                self.left = False
                self.direction += 90
            elif event.key == pygame.K_RIGHT:
                self.right = False
                self.direction -= 90
            elif event.key == pygame.K_SPACE:
                self.space = False
                self.new_space = True




class George(Unit):
    def __init__(self, x, y):
        super(George, self).__init__(x, y)
        self.spritesheet = graphics.load("C:\Users\Jarom\PycharmProjects\\resources\george.png")
        self.mapping = {
            "down" : [(0, 48 * i, 48, 48) for i in xrange(4)],
            "left" : [(48, 48 * i, 48, 48) for i in xrange(4)],
            "up"   : [(96, 48 * i, 48, 48) for i in xrange(4)],
            "right": [(144, 48 * i, 48, 48) for i in xrange(4)]
        }
        self.facing = "up"
        self.speed = 0.2
        self.moving = False

    def update(self):
        if self.moving:
            self.frame = (self.frame + self.speed) % 4
        else:
            self.frame = 1 - 2 * self.speed
        self.moving = False

    def render(self, surface):
        surface.blit(self.spritesheet, (self.x, self.y, 48, 48), self.mapping[self.facing][int(self.frame)])

    def handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.moving = True
                self.facing = "up"
                self.y -= 3
                if self.y < 0:
                    self.y = 0
            elif event.key == pygame.K_DOWN:
                self.moving = True
                self.facing = "down"
                self.y += 3
                if self.y > (399 - 48):
                    self.y = (399 - 48)
            elif event.key == pygame.K_LEFT:
                self.moving = True
                self.facing = "left"
                self.x -= 3
                if self.x < 0:
                    self.x = 0
            elif event.key == pygame.K_RIGHT:
                self.moving = True
                self.facing = "right"
                self.x += 3
                if self.x > (599 - 48):
                    self.x = (599 - 48)
