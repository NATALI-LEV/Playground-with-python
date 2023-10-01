import pygame
import math

pygame.init()

WIDTH, HEIGHT =  1000, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar Simulation")

# Define colors
WHITE = (255, 255, 255)
PINK = (255,182,193)
YELLOW = (255, 255, 0)
GREEN = (52, 165, 111)
RED = (188, 39, 50)
GREY = (183, 184, 185)
GLITER = (230, 232, 250)
# Create a font object
FONT = pygame.font.SysFont("comicsans", 16)

# Load and scale the background image
background = pygame.image.load('stars.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

class Planet:
    AU = 149.6e6 * 1000 # astronomical units - distance of earth to the sun
    G = 6.67428e-11 # gravity
    SCALE = 250 / AU  # 1AU equals to 100 pixels
    TIMESTEP = 3600*24 # 1 day

    def __init__(self, x, y, radius, color, mass ):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
  
        self.orbit = [] # List to store orbit path points
        self.sun = False # Indicates if the planet is the Sun
        self.distance_to_sun = 0
          
        #moving in circle - Velocity components
        self.x_vel = 0 
        self.y_vel = 0
        
    def draw(self, win):
        # Convert planet's position to screen coordinates
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        
        # Draw the orbit path if it has been recorded
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2) # Draw lines between orbit points

        pygame.draw.circle(win, self.color, (x, y), self.radius) # Draw the planet as a circle
		
        # Show the distance to the Sun for all planets except the Sun itself 
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, GLITER)
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))
        
    
    def attraction(self, other):
    #calculates the force of attarction between another object and the current object
    
        #first we calculated the distance between 2 objects
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        #if the other is a sun - store the distance
        if other.sun:
            self.distance_to_sun = distance
        
        #force of attraction/gravitational formula
        force = self.G * self.mass * other.mass / distance**2
        #atan2 = take the y over the x and give us the angle associates with
        theta = math.atan2(distance_y, distance_x)
        # Calculate the force components along x and y axes
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        
        return force_x, force_y
    
    def update_position(self, planets):
        #update position and move by velocity
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            
            fx, fy = self.attraction(planet) #for every planet we calculat the fx, fy 
            total_fx += fx
            total_fy += fy
            
        #calculating the velocity acceleration (F = ma)
        # a = F / m 
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        #update x and y positions by using the velocity and multi by timestep
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        
        # Record the current position in the orbit path
        self.orbit.append((self.x, self.y))
 
class Moon(Planet):
    def __init__(self, earth, radius, color, mass):
        # Initialize the moon with an initial position farther from Earth
        x = earth.x - 0.2 * Planet.AU  # Adjust the x position as needed
        y = earth.y  # Keep the same y position as Earth
        super().__init__(x, y, radius, color, mass)
        self.earth = earth  # Reference to the Earth planet
        self.angle = 0  # Angle to track moon's rotation around Earth
        self.angular_velocity = 0.01 * 12  

    def update_position(self, planets):
        # Update the moon's position relative to Earth (while Earth is orbiting the Sun)
        self.x = self.earth.x + (self.x - self.earth.x) * math.cos(Planet.TIMESTEP)
        self.y = self.earth.y + (self.y - self.earth.y) * math.sin(Planet.TIMESTEP)

        # Calculate the moon's position relative to Earth in a circular orbit
        self.x = self.earth.x + 0.2 * Planet.AU * math.cos(self.angle)
        self.y = self.earth.y + 0.2 * Planet.AU * math.sin(self.angle)

        # Increment the angle for the next frame to simulate moon's rotation
        self.angle += self.angular_velocity  # Adjust the rotation speed as needed

        # Record the current position in the orbit path
        self.orbit.append((self.x, self.y))
        
    def draw(self, win):
    #prevent the moon from drawing its orbit path 
        # Convert moon's position to screen coordinates
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        # Draw the moon as a circle without an orbit path
        pygame.draw.circle(win, self.color, (x, y), self.radius)

        
def main():
    run = True
    WIN.blit(background, (0, 0))
    pygame.display.update() 
    clock = pygame.time.Clock()

    # Create the Sun and planets
    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, GREEN, 5.9742 * 10**24)
    earth.y_vel = 29.783 * 1000 

    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000
    
    mercury = Planet(0.387 * Planet.AU, 0, 8, GREY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000
    
    venus = Planet(0.723 * Planet.AU, 0, 14, PINK, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000
    
# Create the Moon for Earth
    moon = Moon(earth, 4, WHITE, 7.342 * 10**22)
    moon.y_vel = 29.783 * 1000 + 1.02 * 1000  # Adjust the initial velocity as needed
    
    planets = [sun, earth, mars, mercury, venus,moon]
    
    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        WIN.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # Update and draw all planets        
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
            
        pygame.display.update() 
                
    pygame.quit()
    
main()