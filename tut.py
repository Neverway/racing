import pygame

# This is important and needs to be first
pygame.init()

# Resolution edits
display_width = 640
display_height = 480

# Define colors
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



def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

    # Left right movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -0.15
                if event.key == pygame.K_RIGHT:
                    x_change = 0.15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

    # Up Down movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -0.15
                if event.key == pygame.K_DOWN:
                    y_change = 0.15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0


        x += x_change
        y += y_change

        game_display.fill(black)
        char(x, y)
        pygame.display.update()
    clock.tick(30)

game_loop()
pygame.quit()
quit()
