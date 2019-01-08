import pygame

#This is important and needs to be first
pygame.init()

#Windows resolution
gameDisplay = pygame.display.set_mode((800,600))

#Windows name
pygame.display.set_caption('Car Movement Test')

#Game clock(FPS)
clock = pygame.time.Clock()

#Game loop
dead = False

while not dead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

        print(event)