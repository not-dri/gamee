import pygame
from sys import exit

pygame.init()
Screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("gugu run")
clock = pygame.time.Clock()
test__font = pygame.font.Font(None, 50)

sky = pygame.image.load("graphics/sky.png").convert_alpha()
ground = pygame.image.load("graphics/ground.png").convert_alpha()
text_surface = test__font.render("gugu run", False, (64, 64, 64))

snail_surface = pygame.image.load("graphics/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))
snail_x_pos = 600

player_surf = pygame.image.load("graphics/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    Screen.blit(sky, (0, 0))
    Screen.blit(ground, (0, 300))
    Screen.blit(text_surface, (320, 70))
    snail_rect.left -= 3
    if snail_rect.right < 0:
        snail_rect.left = 800
    Screen.blit(snail_surface, snail_rect)
    Screen.blit(player_surf, player_rect)

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print("collision")

    pygame.display.update()
    clock.tick(60)