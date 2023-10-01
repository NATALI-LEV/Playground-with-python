import pygame
import math

pygame.init()

WIDTH, HEIGHT =  1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar Simulation")
background = pygame.image.load('stars.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

def main():
    run = True
    WIN.blit(background, (0, 0))
    pygame.display.update() 

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
    pygame.quit()
    
main()