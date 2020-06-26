import pygame

shootRight = [pygame.image.load('SR1.png'), pygame.image.load('SR2.png'), pygame.image.load('SR3.png'), pygame.image.load('SR4.png'), pygame.image.load('SR5.png'), pygame.image.load('SR6.png'), pygame.image.load('SR7.png'), pygame.image.load('SR8.png'), pygame.image.load('SR9.png'), pygame.image.load('SR10.png'), pygame.image.load('SR11.png'), pygame.image.load('SR12.png'), pygame.image.load('SR13.png')]
shootLeft = [pygame.image.load('SL1.png'), pygame.image.load('SL2.png'), pygame.image.load('SL3.png'), pygame.image.load('SL4.png'), pygame.image.load('SL5.png'), pygame.image.load('SL6.png'), pygame.image.load('SL7.png'), pygame.image.load('SL8.png'), pygame.image.load('SL9.png'), pygame.image.load('SL10.png'), pygame.image.load('SL11.png'), pygame.image.load('SL12.png'), pygame.image.load('SL13.png')]

class Characters(object):
    def __init__(self, name, health):
        
