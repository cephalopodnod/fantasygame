import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
pygame.quit()

