import pygame
import random
import os
import sys
import subprocess



# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generator with Timer and Exit")

# Constants
CELL_SIZE = 20
COLS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VISITED = (200, 200, 200)
PATH = (0, 0, 255)
BACKGROUND = (0, 0, 0)
PLAYER_COLOR = (255, 0, 0)
EXIT_COLOR = (0, 255, 0)
TIMER_COLOR = (0, 0, 255)  # Blue color for the timer

# Directions: Up, Right, Down, Left
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Maze grid structure
maze = [[0] * COLS for _ in range(ROWS)]
visited = [[False] * COLS for _ in range(ROWS)]

# Define the exit position (to be determined later)
exit_x, exit_y = -1, -1

# Timer variables
start_time = pygame.time.get_ticks()  # Get the starting time in milliseconds
countdown_time = 90000  # 30 seconds countdown (in milliseconds)

class Item:
    def __init__(self, name: str, description: str, price: int):
        self.name = name
        self.description = description
        self.price = price

class Player:
    def __init__(self, inventory: list, money: int):
        self.inventory = inventory
        self.money = money

    def use(self, item):
        if item in self.inventory:
            print(f"You have used {item.name}.")
            self.inventory.remove(item)


def carve_maze(x, y):
    visited[y][x] = True
    maze[y][x] = 1

    # Randomize directions to carve the maze
    random.shuffle(DIRECTIONS)
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx * 2, y + dy * 2
        if 0 <= nx < COLS and 0 <= ny < ROWS and not visited[ny][nx]:
            maze[y + dy][x + dx] = 1  # Carve the wall between cells
            carve_maze(nx, ny)


def draw_maze():
    for y in range(ROWS):
        for x in range(COLS):
            color = WHITE if maze[y][x] == 0 else BLACK
            pygame.draw.rect(WINDOW, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_player(player_x, player_y):
    pygame.draw.rect(WINDOW, PLAYER_COLOR, (player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_exit():
    pygame.draw.rect(WINDOW, EXIT_COLOR, (exit_x * CELL_SIZE, exit_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def find_exit():
    global exit_x, exit_y
    # Try to place the exit far away from the start (top-left corner)
    while True:
        # Randomly pick an empty space
        x = random.randint(1, COLS - 2)  # Avoid edges to make sure it's not out of bounds
        y = random.randint(1, ROWS - 2)

        # The exit must be in an open space (part of the path)
        if maze[y][x] == 1 and (x != 0 or y != 0):  # Exclude the starting position
            exit_x, exit_y = x, y
            break


def draw_timer():
    global countdown_time
    # Calculate the remaining time in seconds
    elapsed_time = pygame.time.get_ticks() - start_time
    remaining_time = max(countdown_time - elapsed_time, 0)
    remaining_seconds = remaining_time // 1000  # Convert milliseconds to seconds

    # Display the remaining time in blue
    font = pygame.font.SysFont(None, 55)
    text = font.render(f"Time: {remaining_seconds}s", True, TIMER_COLOR)  # Blue timer color
    WINDOW.blit(text, (WIDTH - 150, 10))

    return remaining_time


def main():
    global exit_x, exit_y, start_time, countdown_time
    
    start_x, start_y = 0, 0
    carve_maze(start_x, start_y)

    # Find a valid exit that is far from the start position
    find_exit()

    # Initial player position
    player_x, player_y = start_x, start_y

    # Set the clock to control the speed of the block
    clock = pygame.time.Clock()

    inventory = []
    money = 0
    if os.path.exists("player_state.txt"):
        with open("player_state.txt", "r") as f:
            lines = f.readlines()
            money = int(lines[0].strip())
            for line in lines[1:]:
                name, description, price = line.strip().split(",")
                inventory.append(Item(name, description, int(price)))

    mc = Player(inventory=inventory, money=money)

    # Main game loop
    running = True
    win=False
    while running:
        WINDOW.fill(BACKGROUND)  # Fill the window with the background color

        # Draw the maze first
        draw_maze()

        # Draw the player (red block) last to ensure it's on top of the maze walls
        draw_player(player_x, player_y)

        # Draw the exit (green square)
        draw_exit()

        # Draw the countdown timer in blue
        remaining_time = draw_timer()

        # Check if the player reaches the exit
        if player_x == exit_x and player_y == exit_y:
            win=True
            font = pygame.font.SysFont(None, 55)
            text = font.render("You Win!", True, (0, 255, 0))
            WINDOW.blit(text, (WIDTH // 3, HEIGHT // 3))
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds before closing
            subprocess.Popen(["python", "shop.py", str(mc.money)])
            running = False


        # Check if the timer has run out
        if remaining_time <= 0:
            # Display a "You Lose!" message
            font = pygame.font.SysFont(None, 55)
            text = font.render("You Lose!", True, (255, 0, 0))
            WINDOW.blit(text, (WIDTH // 3, HEIGHT // 3))
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds before closing
            running = False  # End the game


        # Check if the timer has run out
        if remaining_time <= 0:
            font = pygame.font.SysFont(None, 55)
            text = font.render("You Lose!", True, (255, 0, 0))
            WINDOW.blit(text, (WIDTH // 3, HEIGHT // 3))
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait for 2 seconds before closing
            running = False

        player_speed = 1

        speed_potion_duration = 0        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Use items based on key presses

        if keys[pygame.K_1]:
            item = mc.use("speed_potion")
            if item:
                player_speed = 1.5  # Increase player speed
                speed_potion_duration = 5000  # Speed potion lasts for 5 seconds
        elif keys[pygame.K_2]:
            item = mc.use("speed_potion_2")
            if item:
                player_speed = 2  # Increase player speed
                speed_potion_duration = 5000  # Speed potion lasts for 5 seconds
        elif keys[pygame.K_3]:
            item = mc.use("speed_potion_long")
            if item:
                player_speed = 1.5  # Increase player speed
                speed_potion_duration = 10000  # Speed potion lasts for 10 seconds

        # Handle speed potion duration
        if speed_potion_duration > 0:
            speed_potion_duration -= clock.get_time()
            if speed_potion_duration <= 0:
                player_speed = 1  # Reset player speed

        # Get key presses to control the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0 and maze[player_y][player_x - 1] == 1:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < len(maze[0]) - 1 and maze[player_y][player_x + 1] == 1:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0 and maze[player_y - 1][player_x] == 1:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < len(maze) - 1 and maze[player_y + 1][player_x] == 1:
            player_y += player_speed



        clock.tick(10)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()