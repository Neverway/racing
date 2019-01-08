import pygame

# This is important and needs to be first
pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Windows resolution
game_display = pygame.display.set_mode((display_width, display_height))

# Windows name
pygame.display.set_caption('Serpent')

# Game clock(FPS)
clock = pygame.time.Clock()

# Load sprites
chara = pygame.image.load('Sprites/knight.png')

# Spawn player
def  char(x, y):
    game_display.blit(chara, (x, y))


x = (display_width * 0.45)
y = (display_height * 0.8)

x_change = 0


# Game loop
dead = False

while not dead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -2
            elif event.key == pygame.K_RIGHT:
                x_change = 2


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    x += x_change

    game_display.fill(black)
    char(x, y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
