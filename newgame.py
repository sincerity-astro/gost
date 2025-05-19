from pygame import *
import pygame
from random import randint
from time import time

lost = 0


class GameSprite(sprite.Sprite):
    def __init__ (self, imagee, x, y, speed, size1, size2):
        super().__init__()
        self.image = transform.scale(image.load(imagee), (size1, size2))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.red = 0
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keypress = key.get_pressed()
        if keypress[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keypress[K_RIGHT] and self.rect.x < 890:
            self.rect.x += self.speed
        if keypress[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keypress[K_DOWN] and self.rect.y < 590:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= 1000:
            self.rect.x = 0
            self.rect.y = randint(50, 950)
class Enemy2(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 700:
            self.rect.y = 0
            self.rect.x = randint(50, 650)
class Button(GameSprite):
    def update(self, player):
        if sprite.collide_rect(self, player) and self.red == 0:
            self.image = transform.scale(image.load('ng55.png'), (50, 50))
            button = Button('ng44.png', randint(50, 950), randint(50, 650), 0, 50, 50)
            buttonsred.add(button)
            self.red = 1


window = display.set_mode((1000, 700))
display.set_caption('Полминуты!')
background = transform.scale(image.load('ng1.jpg'), (1000, 700))



player = Player('ng66.png', 350, 200, 10, 60, 70)

monsters1 = sprite.Group()
for i in range(3):
    enemy = Enemy('ng33.png', 0, 0, randint(1, 5), 70, 70)
    monsters1.add(enemy)
monsters2 = sprite.Group()
for i in range(3):
    enemy = Enemy2('ng33.png', 0, 0, randint(1, 5), 70, 70)
    monsters2.add(enemy)

buttonswhite = sprite.Group()
for i in range(5):
    button = Button('ng44.png', randint(50, 950), randint(50, 650), 0, 50, 50)
    buttonswhite.add(button)

buttonsred = sprite.Group()

font.init()
font1 = font.SysFont('Arial', 36)



clock = pygame.time.Clock()
FPS = 60

game = True
win = True

starttime = time()
curtime = starttime
texttime = font1.render('Время: 0', 1, (255, 255, 255))

while game == True:
    if win == True:
        window.blit(background, (0,0))
        window.blit(texttime, (50, 20))
        player.reset()
        player.move()
        monsters1.draw(window)
        monsters1.update()
        monsters2.draw(window)
        monsters2.update()
        buttonswhite.draw(window)
        buttonswhite.update(player)
        buttonsred.draw(window)
        buttonsred.update(player)
        newtime = time()
        textscore = font1.render('Счет: '+str(lost), 1, (255, 255, 255))
        window.blit(textscore, (30, 40))
        if sprite.spritecollide(player, monsters1, False):
            win = False
        if sprite.spritecollide(player, monsters2, False):
            win = False
        spisoc1 = sprite.groupcollide(monsters1, buttonsred, True, True)
        for i in spisoc1:
            lost += 1
            enemy = Enemy2('ng33.png', 0, 0, randint(1, 5), 100, 100)
            monsters1.add(enemy)
        spisoc2 = sprite.groupcollide(monsters2, buttonsred, True, True)
        for i in spisoc2:
            lost += 1
            enemy = Enemy2('ng33.png', 0, 0, randint(1, 5), 100, 100)
            monsters2.add(enemy)
        if newtime - curtime > 1:
            curtime = newtime
            texttime = font1.render('Время: '+str(int(curtime - starttime)), 1, (255, 255, 255))
            window.blit(texttime, (10, 20))
        if curtime - starttime >= 30 and lost <= 5:
            win = False
        if lost >= 5 and (curtime - starttime <= 30):
            textfinish = font1.render('ура победа', 1, (255, 255, 255))
            window.blit(textfinish, (500, 50))
    if win == False:
        textend = font1.render('о нееет', 1, (255, 255, 255))
        window.blit(textend, (500, 50))
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)