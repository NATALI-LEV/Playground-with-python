import pygame
import random
import math
pygame.init()

# Class to store drawing information and constants
class DrawInformation:
    # Color constants
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    PINK = (178, 111, 146)
    RED = (128, 9, 72)
    BACKGROUND_COLOR = WHITE

    # Color gradients
    GRADIENTS = [
        (49, 77, 118),
        (87, 109, 141),
        (151, 165, 186)
    ]

    # Font settings
    FONT = pygame.font.SysFont('comicsans', 30)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)

    # Padding and positioning constants
    SIDE_PAD = 100
    TOP_PAD = 150

    # Initialize DrawInformation object
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualization")
        self.set_list(lst)

    # Set the list data for visualization
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

# Function to draw the visualization
def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1,
                                        draw_info.PINK)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))

    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1,
                                     draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width / 2 - controls.get_width() / 2, 45))

    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | Q - Quick Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 75))

    draw_list(draw_info)
    pygame.display.update()

# Function to draw the bars representing the list elements
def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD // 2, draw_info.TOP_PAD,
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()

# Function to generate a random starting list
def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

# Bubble sort algorithm
def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.PINK, j + 1: draw_info.RED}, True)
                yield True

    return lst

# Insertion sort algorithm
def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            draw_list(draw_info, {i - 1: draw_info.PINK, i: draw_info.RED}, True)
            yield True

    return lst

# Quick sort algorithm
def partition(arr, low, high, draw_info, ascending):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if (arr[j] < pivot and ascending) or (arr[j] > pivot and not ascending):
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_list(draw_info, {i: draw_info.PINK, j: draw_info.RED}, True)
            yield True

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_list(draw_info, {i + 1: draw_info.PINK, high: draw_info.RED}, True)
    yield True
    return i + 1

def quick_sort_helper(arr, low, high, draw_info, ascending):
    if low < high:
        pi = yield from partition(arr, low, high, draw_info, ascending)

        yield from quick_sort_helper(arr, low, pi - 1, draw_info, ascending)
        yield from quick_sort_helper(arr, pi + 1, high, draw_info, ascending)

def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    yield from quick_sort_helper(lst, 0, n - 1, draw_info, ascending)
    return lst

# Main function to control the program flow
def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    # Generate initial random list and create DrawInformation object
    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(1000, 600, lst)
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort  # Default sorting algorithm
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    # Main game loop
    while run:
        clock.tick(45)

        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"
            elif event.key == pygame.K_q and not sorting:
                sorting_algorithm = quick_sort
                sorting_algo_name = "Quick Sort"

    pygame.quit()

if __name__ == "__main__":
    main()
