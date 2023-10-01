
# Solar System Simulation in Python (Rotation)

This Python project offers an engaging planetary simulation, providing a visually captivating representation of celestial bodies' movements within our solar system. The simulation includes the Sun, Earth&Moon, Mars, Mercury, and Venus, each with accurate initial conditions such as mass, velocity, and orbit.

## Key Features
- **Astronomy and Math Basics**: This project incorporates fundamental principles of astronomy and mathematics to create a realistic simulation of our solar system.
- **Realistic Planetary Motion**: The simulation uses Newton's Law of Universal Gravitation to accurately model the gravitational interactions between celestial bodies.
- **Orbit Visualization**: You can observe the orbits and distances of planets from the Sun, gaining insights into their movements.
- **Adjustable Time Step**: Take control of the simulation's dynamics with an adjustable time step, allowing you to speed up or slow down time.
- **Intuitive Graphical Interface**: The interactive graphical interface built using Pygame makes it easy to explore and enjoy the solar system simulation.

## Key Formulas
### Newton's Law of Universal Gravitation
**Formula**: F = (G * m1 * m2) / r^2
**Explanation**: Calculates the gravitational force (F) between two objects with masses (m1 and m2) separated by a distance (r). G represents the gravitational constant.

### Distance Calculation
**Formula**: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
**Explanation**: Calculates the distance between two points (x1, y1) and (x2, y2) using the Pythagorean theorem.

### Angle Calculation
**Formula**: theta = atan2(y, x)
**Explanation**: Calculates the angle (theta) between the x-axis and a line connecting two points with coordinates (x, y).

### Velocity Update Using Force
**Formula**: F = m * a
**Explanation**: Newton's second law relates force (F), mass (m), and acceleration (a). It's used to update the velocity of the planets based on the total force acting on them.

### Position Update Using Velocity
**Formula**: x = x + (v * t)
**Explanation**: Updates the position (x) of an object based on its velocity (v) and a given time step (t).

### Scaling Factor for Simulation
**Formula**: Scaled_position = Real_position * SCALE + (WIDTH / 2, HEIGHT / 2)
**Explanation**: Scales real-world positions to fit the screen and centers them on the screen.


*Background Picture Credits: Taken by my loving partner during a night full of stars and Northern Lights in Vik, Iceland.*


## Installation
To run the simulation on your local machine, follow these steps:

1. Clone this repository.
   ```sh
   git clone https://github.com/your-username/solar-system-simulation.git


2. Install the required dependencies.
    pip install pygame

3. Run the simulation.
    python main.py


