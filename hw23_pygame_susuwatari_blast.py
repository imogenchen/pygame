#https://www.bilibili.com/video/BV1Zt411T7yv?from=search&seid=8638073701462922993

"""Import and initialise"""
import pygame
import random

pygame.init()

"""Create necessities"""
screen = pygame.display.set_mode((800, 600))
caption = pygame.display.set_caption('Susuwatari Blast!')

clock = pygame.time.Clock()

GREY = (120, 130, 135)

image = pygame.image.load('susuwatari.png')

sprite_list = pygame.sprite.Group()

class Susuwatari(pygame.sprite.Sprite):
    pos = (0,0) 
    x_vel = 1  
    y_vel = 1
    scale = 100 
    
    def __init__(self, pos, x_vel, y_vel):
        super().__init__()
        self.pos = pos
        self.image = image
        self.scale = random.randrange(20, 100)
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale)) 
        self.rect = self.image.get_rect()
        self.rect.x = pos[0] - self.scale/2
        self.rect.y = pos[1] - self.scale/2

    def update(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        if self.rect.x <= 0 or self.rect.x > screen.get_width() - self.scale:
            self.x_vel = -self.x_vel

        if self.rect.y <= 0 or self.rect.y > screen.get_height() - self.scale:
            self.y_vel = -self.y_vel
            
"""The game loop"""
mousedown = False

running = True
while running:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True

        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False

        screen.fill(GREY)
        
        sprite_list.update()
        sprite_list.draw(screen)
        clock.tick(200)
        pygame.display.update()
        
        if mousedown == True:
            mouseposition = pygame.mouse.get_pos()
            x_random_vel = random.randint(-5, 5)
            y_random_vel = random.randint(-5, 5)
            new_susuwatari = Susuwatari(mouseposition, x_random_vel, y_random_vel)
            sprite_list.add(new_susuwatari)
    

pygame.quit()
