import pygame
from sys import exit

pygame.init()
Screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("gugu run")
clock = pygame.time.Clock()
test__font = pygame.font.Font(None, 50)

sky = pygame.image.load("graphics/sky.png")
ground = pygame.image.load("graphics/ground.png")
text_surface = test__font.render("gugu run", False, (64, 64, 64))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    Screen.blit(sky, (0, 0))
    Screen.blit(ground, (0, 300))
    Screen.blit(text_surface, (320, 100))
    pygame.display.update()
    clock.tick(60)