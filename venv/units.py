
import math
import pygame

import graphics


class Unit(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0.0


class Ava(Unit):
    def __init__(self, x, y):
        super(Ava, self).__init__(x, y)
        self.spritesheet = graphics.load("resources\Ava.png")
        self.rot_sprite = self.spritesheet
        self.direction = 0
        self.speed = 2
        self.w = False
        self.a = False
        self.s = False
        self.d = False
        self.left = False
        self.right = False
        self.space = False
        self.sensitivity = 5

    def update(self):
        rad = math.radians(self.direction)
        ava_mask = pygame.mask.from_surface(self.rot_sprite.convert_alpha())
        old_x = self.x
        old_y = self.y
        new_x = old_x
        new_y = old_y
        if self.left:
            self.direction += self.sensitivity
        if self.right:
            self.direction -= self.sensitivity
        if self.w:
            new_y -= self.speed * math.sin(rad)
            new_x += self.speed * math.cos(rad)
            overlap = graphics.background_mask.overlap(ava_mask, (int(new_x), int(new_y)))
            if overlap:
                new_x = old_x
                new_y = old_y
            else:
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
            overlap = graphics.background_mask.overlap(ava_mask, (int(new_x), int(new_y)))
            if overlap:
                new_x = old_x
                new_y = old_y
            else:
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
            overlap = graphics.background_mask.overlap(ava_mask, (int(new_x), int(new_y)))
            if overlap:
                new_x = old_x
                new_y = old_y
            else:
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
            overlap = graphics.background_mask.overlap(ava_mask, (int(self.x), int(self.y)))
            if overlap:
                new_x = old_x
                new_y = old_y
            else:
                old_x = new_x
                old_y = new_y
        if self.space:
            center_x = self.spritesheet.get_rect().center[1]
            center_y = self.spritesheet.get_rect().center[0]
            top_dist = 0
            while not graphics.background_mask.get_at((center_x + int(self.x), center_y + int(self.y) - top_dist)):
                top_dist += 1
            print "TOP: ", top_dist
            bot_dist = 0
            while not graphics.background_mask.get_at((center_x + int(self.x), center_y + int(self.y) + bot_dist)):
                bot_dist += 1
            print "BOTTOM: ", bot_dist
            print "HEIGHT: ", bot_dist + top_dist
            left_dist = 0
            while not graphics.background_mask.get_at((center_x + int(self.x) - left_dist, center_y + int(self.y))):
                left_dist += 1
            print "LEFT: ", left_dist
            right_dist = 0
            while not graphics.background_mask.get_at((center_x + int(self.x) + right_dist, center_y + int(self.y))):
                right_dist += 1
            print "RIGHT: ", right_dist
            print "WIDTH: ", left_dist + right_dist
        self.x = new_x
        self.y = new_y
        if self.y < 0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.y > (graphics.height - 40):
            self.y = (graphics.height - 40)
        if self.x > (graphics.width - 40):
            self.x = (graphics.width - 40)

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
                self.space = True
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
            elif event.key == pygame.K_RIGHT:
                self.right = False
            elif event.key == pygame.K_SPACE:
                self.space = False




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
