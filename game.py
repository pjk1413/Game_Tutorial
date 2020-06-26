import pygame
import random
#import image_load

pygame.init()

#Variables
scWidth = 640
scHeight = 400

#Display
screenSize = (scWidth, scHeight)
win = pygame.display.set_mode(screenSize)

pygame.display.set_caption("Skelly Boi")

#Image load
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
walkUp = [pygame.image.load('U1.png'), pygame.image.load('U2.png'), pygame.image.load('U3.png'), pygame.image.load('U4.png'), pygame.image.load('U5.png'), pygame.image.load('U6.png'), pygame.image.load('U7.png'), pygame.image.load('U8.png'), pygame.image.load('U9.png')]
walkDown = [pygame.image.load('D1.png'), pygame.image.load('D2.png'), pygame.image.load('D3.png'), pygame.image.load('D4.png'), pygame.image.load('D5.png'), pygame.image.load('D6.png'), pygame.image.load('D7.png'), pygame.image.load('D8.png'), pygame.image.load('D9.png')]

shootRight = [pygame.image.load('SR1.png'), pygame.image.load('SR2.png'), pygame.image.load('SR3.png'), pygame.image.load('SR4.png'), pygame.image.load('SR5.png'), pygame.image.load('SR6.png'), pygame.image.load('SR7.png'), pygame.image.load('SR8.png'), pygame.image.load('SR9.png'), pygame.image.load('SR10.png'), pygame.image.load('SR11.png'), pygame.image.load('SR12.png')]
shootLeft = [pygame.image.load('SL1.png'), pygame.image.load('SL2.png'), pygame.image.load('SL3.png'), pygame.image.load('SL4.png'), pygame.image.load('SL5.png'), pygame.image.load('SL6.png'), pygame.image.load('SL7.png'), pygame.image.load('SL8.png'), pygame.image.load('SL9.png'), pygame.image.load('SL10.png'), pygame.image.load('SL11.png'), pygame.image.load('SL12.png'), pygame.image.load('SL13.png')]
shootUp = [pygame.image.load('SU1.png'), pygame.image.load('SU2.png'), pygame.image.load('SU3.png'), pygame.image.load('SU4.png'), pygame.image.load('SU5.png'), pygame.image.load('SU6.png'), pygame.image.load('SU7.png'), pygame.image.load('SU8.png'), pygame.image.load('SU9.png'), pygame.image.load('SU10.png'), pygame.image.load('SU11.png'), pygame.image.load('SU12.png'), pygame.image.load('SU13.png')]
shootDown = [pygame.image.load('SD1.png'), pygame.image.load('SD2.png'), pygame.image.load('SD3.png'), pygame.image.load('SD4.png'), pygame.image.load('SD5.png'), pygame.image.load('SD6.png'), pygame.image.load('SD7.png'), pygame.image.load('SD8.png'), pygame.image.load('SD9.png'), pygame.image.load('SD10.png'), pygame.image.load('SD11.png'), pygame.image.load('SD12.png'), pygame.image.load('SD13.png')]

magicRight = [pygame.image.load('SC1.png'), pygame.image.load('SC2.png'), pygame.image.load('SC3.png'), pygame.image.load('SC4.png'), pygame.image.load('SC5.png'), pygame.image.load('SC6.png'), pygame.image.load('SC7.png')]

aL = pygame.image.load('aL.png')
aR = pygame.image.load('aR.png')
aU = pygame.image.load('aU.png')
aD = pygame.image.load('aD.png')

#coffeThrow = [aL, pygame.transform.rotate(aL, 90), pygame.transform.rotate(aL, 180), pygame.transform.rotate(aL, 270)]

open = pygame.image.load('open_screen.png')
bg = pygame.image.load('bg/street.png')
char = pygame.image.load('standing.png')

#arrowL = pygame.image.load('arrowL.png')
#arrowR = pygame.image.load('arrowR.png')

clock = pygame.time.Clock()

class menu(object):
    def __init__(self):
        self.selector = 0
        self.menu = True

#Player Properties
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.hitbox = (self.x + 18, self.y + 10, 30, 60)
        self.hitbox = (self.x + 18, self.y + 15, 30, 48)
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.up = False
        self.down = False
        self.shooting = False
        self.shootCount = 0
        self.magic = False
        self.magicCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x,self.y))
                self.walkCount += 1
            elif self.up:
                win.blit(walkUp[self.walkCount // 3], (self.x,self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(walkDown[self.walkCount // 3], (self.x,self.y))
                self.walkCount += 1
        elif self.standing and self.shooting is False:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            elif self.up:
                win.blit(walkUp[0], (self.x, self.y))
            else:
                win.blit(walkDown[0], (self.x, self.y))
        elif self.shooting is True:
            if self.shootCount >= 36:
                self.shootCount = 0
                self.shooting = False
            if self.right:
                win.blit(shootRight[self.shootCount // 3], (self.x, self.y))
                self.shootCount += 1
            if self.left:
                win.blit(shootLeft[self.shootCount // 3], (self.x, self.y))
                self.shootCount += 1
            if self.up:
                win.blit(shootUp[self.shootCount // 3], (self.x, self.y))
                self.shootCount += 1
            if self.down:
                win.blit(shootDown[self.shootCount // 3], (self.x, self.y))
                self.shootCount += 1
        elif self.magic is True:
            win.blit(magicRight[self.magicCount // 3], (self.x, self.y))
            self.magicCount += 1
        self.hitbox = (self.x + 18, self.y + 15, 30, 48)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

class enemy(object):

    fallDown = [pygame.image.load('EF1.png'), pygame.image.load('EF2.png'), pygame.image.load('EF3.png'), pygame.image.load('EF4.png'), pygame.image.load('EF5.png'), pygame.image.load('EF6.png'), pygame.image.load('EF6.png'), pygame.image.load('EF6.png'), pygame.image.load('EF6.png')]
    walkLeft = [pygame.image.load('LE1.png'), pygame.image.load('LE2.png'), pygame.image.load('LE3.png'), pygame.image.load('LE4.png'), pygame.image.load('LE5.png'), pygame.image.load('LE6.png'), pygame.image.load('LE7.png'), pygame.image.load('LE8.png'), pygame.image.load('LE9.png')]

    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.end = False
        self.walkCount = 0
        self.vel = 3
        self.exist = True
        self.right = False
        self.hitbox = (self.x + 18, self.y + 15, 30, 48)
        self.death = False
        self.deathHit = False
        self.deathCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.deathHit is False:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x,self.y))
            self.walkCount += 1
            self.x -= self.vel
            self.hitbox = (self.x + 18, self.y + 15, 30, 48)
            if self.death is True:
                win.blit(self.fallDown[self.deathCount // 3], (self.x, self.y))
                self.deathCount += 1
        elif self.deathHit is True:
            win.blit(self.fallDown[self.deathCount // 3], (self.x, self.y))
            self.deathCount += 1
            self.x += self.vel
            if self.deathCount > 26:
                self.deathHit = False
                self.deathCount = 0
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
#projectile class
class projectile(object):
    def __init__(self, x, y, direction, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 15 * facing
        self.pause = True
        self.start = False
        self.direction = direction
        self.width = 64
        self.OC_X = 0

    def draw(self, win):
        if self.direction == 'x' and facing == -1:
            win.blit(aL, (self.x, self.y - 30))
        elif self.direction == 'x' and facing == 1:
            win.blit(aR, (self.x - 30, self.y - 30))
        elif self.direction == 'y' and facing == -1:
            win.blit(aU, (self.x - 30, self.y - 30))
        elif self.direction == 'y' and facing == 1:
            win.blit(aD, (self.x - 30, self.y - 30))

#Jump Properties
isJump = False
jumpCount = 10
shooting = False
run = True
timer = 1000
counter = 0
difficulty = 10

def redrawGameWindow():

    if newMenu.menu is True:
        win.blit(open, (0,0))
    else:
        win.blit(bg, (0,0))
        for bullet in bullets:
            bullet.draw(win)
        if shooting is False:
            man.draw(win)
        for enemy in goblins:
            enemy.draw(win)
    pygame.display.update()

#Main loop
man = player(300, 300, 64, 64)
#goblin = enemy(300, 300, 64, 64)
pDir = man.x
createEnemy = True
coolDown = 0

newMenu = menu()
bulletFire = False
bullets = []
goblins = []
while run:
    randomInt = random.randint(1, difficulty * 5)
    if coolDown > 0:
        coolDown += 1
    if coolDown > 3:
        coolDown = 0

    if randomInt == difficulty * 2:
        createEnemy = True

    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        for goblin in goblins:
            if (bullet.x + bullet.width) > goblin.hitbox[0] and (bullet.x + bullet.width) < goblin.hitbox[0] + goblin.hitbox[2]:
                if (bullet.y) > goblin.hitbox[1] and bullet.y < goblin.hitbox[1] + goblin.hitbox[3]:
                    bullets.pop(bullets.index(bullet))
                    goblins.pop(goblins.index(goblin))
                    goblin.death = True
        if bullet.x < scWidth and bullet.x > -2 and bullet.direction == 'x':
            bullet.x += bullet.vel
        elif bullet.y < scHeight and bullet.y > 250 and bullet.direction == 'y':
            bullet.y += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))



    for goblin in goblins:
        if goblin.x < 0:
            goblins.pop(goblins.index(goblin))

    if createEnemy is True:
        randomNum = random.randint(250, 350)
        goblins.append(enemy(scWidth, randomNum, 64, 64))
        createEnemy = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_s]:
        newMenu.menu = False

    if keys[pygame.K_x]:
        for goblin in goblins:
            goblin.deathHit = True
        man.magicMove = True

    if keys[pygame.K_z]:
        man.shooting = True
        if man.left:
            facing = -1
        elif man.right:
            facing = 1
        elif man.up:
            facing = -1
        elif man.down:
            facing = 1

    if (man.shootCount // 3) == 9 and coolDown == 0:
        coolDown = 10
        if len(bullets) < 3:
            if man.left is True or man.right is True:
                pDir = 'x'
            else:
                pDir = 'y'
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height //2), pDir, facing))
            bulletFire = False

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.up = False
        man.down = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < screenSize[0] - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.up = False
        man.down = False
        man.standing = False
    elif keys[pygame.K_UP] and man.y > 240: #and man.y < screenSize[1]/2
        man.y -= man.vel
        man.right = False
        man.left = False
        man.up = True
        man.down = False
        man.standing = False
    elif keys[pygame.K_DOWN] and man.y < scHeight - man.height: # and man.y < screenSize[1]
        man.y += man.vel
        man.right = False
        man.left = False
        man.up = False
        man.down = True
        man.standing = False
    else:
        man.walkCount = 0
        man.standing = True

    if not (man.isJump):
        if keys[pygame.K_SPACE]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
