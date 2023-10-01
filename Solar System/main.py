import pygame
import math

pygame.init()

WIDTH, HEIGHT =  1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar Simulation")

PINK = (255,182,193)
YELLOW = (255, 255, 0)
GREEN = (52, 165, 111)
RED = (188, 39, 50)
GREY = (183, 184, 185)

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
        
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)
 

def main():
    run = True
    WIN.blit(background, (0, 0))
    pygame.display.update() 
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, GREEN, 5.9742 * 10**24)

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)

    mercury = Planet(0.387 * Planet.AU, 0, 8, GREY, 3.30 * 10**23)

    venus = Planet(0.723 * Planet.AU, 0, 14, PINK, 4.8685 * 10**24)

    planets = [sun, earth, mars, mercury, venus]
    
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        for planet in planets:
            planet.draw(WIN)
            
        pygame.display.update() 

                
    pygame.quit()
    
main()