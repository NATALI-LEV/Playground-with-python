# Naruto Jumping Game

This is a simple jumping game implemented in Python using the Pygame library. In this game, you control the character "Naruto" and your goal is to jump over obstacles to score points. The game continues until you collide with an obstacle or press the "R" key to restart.

## Prerequisites

Before you can run the game, you need to have Python and the Pygame library installed on your computer. You can install Pygame using pip:

    ```bash
        pip install pygame


## Game Features

- **Naruto Character:** Play as Naruto with a jumping animation.
- **Obstacles:** Dodge obstacles represented by the "Pain" character.
- **Scoring System:** Keep track of your score as you progress.
- **High Score:** View and aim to beat your highest score.
- **Background:** Enjoy a visually appealing background with music and sound effects.

## How to Play

1. **Run the Game:** Execute the Python script in your terminal or IDE.
2. **Jumping:** Use the "SPACE" key to make Naruto jump.
3. **Avoid Obstacles:** Navigate Naruto to avoid colliding with the obstacles (Pain character) to keep the game going.
4. **Scoring:** Your score increases as you successfully jump over obstacles.
5. **Game Over:** If Naruto collides with an obstacle, the game ends, and your final score is displayed.
6. **Restart:** Press the "R" key to restart the game and try to beat your previous score.

## Game Controls

- **Jumping:** Press the "SPACE" key to make Naruto jump.
- **Restart:** Press the "R" key to restart the game when it's over.

## Game Logic

- Naruto can jump and must avoid obstacles to survive.
- The game speed gradually increases, making it more challenging as you progress.
- Your highest score is tracked and displayed.
- Special sound effects play when you reach certain score milestones.

## Code Structure

The code is organized into several classes:

- `Naruto`: Represents Naruto and controls his movement and animation.
- `Pain`: Represents the obstacles (Pain character) and their movement.
- `Collision`: Detects collisions between Naruto and Pain.
- `BG`: Manages the scrolling background.
- `Score`: Handles scoring and displays the high score.
- `Game`: The main game class that orchestrates the game loop and interactions.

## Contributions

Feel free to contribute to this game by adding new features, improving the graphics, or optimizing the code. Pull requests are welcome!

Enjoy playing Naruto Jumping Game!
