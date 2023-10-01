import pygame
import math

pygame.init()

WIDTH, HEIGHT =  1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar Simulation")
background = pygame.image.load('stars.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

class Planet:
    AU = 149.6e6 * 1000 # astronomical units - distance of earth to the sun
    G = 6.67428e-11 # gravity
    SCALE = 250 / AU  # 1AU equals to 100 pixels
	TIMESTEP = 3600*24 # 1 day

    def __init__(self, x, y, radius, color, mass):
        self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.mass = mass
  
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
          
        #moving in circle
        self.x_vel = 0 
		self.y_vel = 0

def main():
    run = True
    WIN.blit(background, (0, 0))
    pygame.display.update() 
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
    pygame.quit()
    
main()