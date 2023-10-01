##Solar System simulation in Python(rotation):
This Python project offers a captivating planet simulation, providing a visual representation of celestial bodies' movements within our solar system. The simulation includes the Sun, Earth, Mars, Mercury, and Venus, each with accurate initial conditions such as mass, velocity, and orbit.

##Key Features:
Astronomy and Math basics.
Realistic planetary motion using Newton's law of universal gravitation.
Visualization of orbits and distances from the Sun.
Adjustable time step for dynamic simulation control.
An intuitive and interactive graphical interface using Pygame.

remember:
rotations, gravity, and distances are essential elements in simulating planetary motion. Rotations create day-night cycles, gravity governs celestial body interactions, and distances determine positions and orbits. These factors come together to create dynamic and realistic planetary simulations.

This code simulates a basic planetary system using Python and Pygame. It includes several physics and math formulas. Here's a list of the key formulas being used in the code:

Newton's Law of Universal Gravitation:

Formula: F = (G * m1 * m2) / r^2
Explanation: Calculates the Attraction/gravitational force between two objects with masses m1 and m2, separated by a distance r. F is the gravitational force, G is the gravitational constant.
Distance Calculation:

Formula: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
Explanation: Calculates the distance between two points (x1, y1) and (x2, y2) using the Pythagorean theorem.
Angle Calculation:

Formula: theta = atan2(y, x)
Explanation: Calculates the angle (theta) between the x-axis and a line connecting two points with coordinates (x, y).
Velocity Update Using Force:

Formula: F = m * a
Explanation: Newton's second law relates force (F), mass (m), and acceleration (a). In this case, it is used to update the velocity of the planets based on the total force acting on them.
Position Update Using Velocity:

Formula: x = x + (v * t)
Explanation: Updates the position (x) of an object based on its velocity (v) and a given time step (t).
Scaling Factor for Simulation:

Formula: Scaled_position = Real_position * SCALE + (WIDTH / 2, HEIGHT / 2)
Explanation: Scales real-world positions to fit the screen and center them on the screen.


note : The background picture was taken by my loving partner at a night full of stars and northen lights in Vik , iceland  

