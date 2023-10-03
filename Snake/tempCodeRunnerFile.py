import random
from tkinter import *

# Constants for the game
GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 160
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#097969"
FOOD_COLOR = "#DE3163"
BACKGROUND_COLOR = "#B0C4DE"

# Snake class to manage the snake's attributes
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Initialize the snake's body coordinates
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Create rectangles for each part of the snake
        for x, y in self.coordinates:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)

# Food class to manage the food's attributes
class Food:
    def __init__(self):
        # Generate random coordinates for the food
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        # Create an oval for the food
        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food"
        )

# Function to advance the game state
def next_turn(snake, food):
    x, y = snake.coordinates[0]

    # Move the snake's head based on the current direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    # Create a new rectangle to represent the snake's head
    square = canvas.create_rectangle(
        x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR
    )

    snake.squares.insert(0, square)

    # Check if the snake ate the food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text="Score:{}".format(score))
        canvas.delete("food")
        food = Food()
    else:
        # Remove the last part of the snake's tail
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Check for collisions with the walls or itself
    if check_collisions(snake):
        game_over()
    else:
        # Schedule the next turn
        window.after(SPEED, next_turn, snake, food)

# Function to change the snake's direction
def change_direction(new_direction):
    global direction
    if new_direction == "left":
        if direction != "right":
            direction = new_direction
    elif new_direction == "right":
        if direction != "left":
            direction = new_direction
    elif new_direction == "up":
        if direction != "down":
            direction = new_direction
    elif new_direction == "down":
        if direction != "up":
            direction = new_direction

# Function to check for collisions
def check_collisions(snake):
    x, y = snake.coordinates[0]
    
    # Check for collisions with the walls
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    # Check for collisions with itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

# Function to handle the game over state
def game_over():
    canvas.delete(ALL)
    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2 - 50,  # Adjusted vertical position
        font=("consolas", 70),
        text="GAME OVER",
        fill="red",
        tag="gameover",
    )
    
    # Display "Press 'r' to restart"
    canvas.create_text(
        canvas.winfo_width() / 2,
        canvas.winfo_height() / 2 + 50,  # Adjusted vertical position
        font=("consolas", 30),  # Adjusted font size
        text="Press 'r' to restart",
        fill="white",
        tag="restart",
    )
    
    # Bind the 'r' key to restart the game
    window.bind('r', restart_game)

# Function to restart the game
def restart_game(event):
    global score, direction
    
    # Reset score and direction
    score = 0
    direction = "down"
    
    # Clear canvas
    canvas.delete(ALL)
    
    # Create a new label for the score
    label.config(text="Score:{}".format(score))
    
    # Create a new snake and food
    snake = Snake()
    food = Food()
    
    # Start the game loop
    next_turn(snake, food)

# Create the main window
window = Tk()
window.title("Snake game")
window.resizable(False, False)

# Initialize the score and direction
score = 0
direction = "down"

# Create a label to display the score
label = Label(window, text="Score:{}".format(score), font=("consolas", 40))
label.pack()

# Create a canvas for the game
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Get window dimensions and center it on the screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Bind arrow keys to change the snake's direction
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind("<Down>", lambda event: change_direction("down"))

# Create the snake and food objects
snake = Snake()
food = Food()

# Start the game loop
next_turn(snake, food)

# Start the main window's main loop
window.mainloop()
