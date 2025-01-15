import pygame
import os

# Constants
TILE_SIZE = 64
WIDTH = TILE_SIZE * 8
HEIGHT = TILE_SIZE * 8

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Maze Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
tiles = {
    'empty': pygame.Surface((TILE_SIZE, TILE_SIZE)),
    'wall': pygame.Surface((TILE_SIZE, TILE_SIZE)),
    'goal': pygame.Surface((TILE_SIZE, TILE_SIZE)),
    'door': pygame.Surface((TILE_SIZE, TILE_SIZE)),
    'key': pygame.Surface((TILE_SIZE, TILE_SIZE))
}

tiles['empty'].fill(WHITE)
tiles['wall'].fill(BLACK)
tiles['goal'].fill((0, 255, 0))
tiles['door'].fill((255, 0, 0))
tiles['key'].fill((0, 0, 255))

# Maze layout
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 2, 0, 1],
    [1, 0, 1, 0, 1, 1, 3, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 4, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Player and positions
player_pos = [1, 1]

def can_move_to(pos):
    row, col = pos
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
        return False
    return maze[row][col] != 1  # Only block movement if the tile is a wall

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            new_pos = player_pos[:]
            if event.key == pygame.K_UP:
                new_pos[1] -= 1
            elif event.key == pygame.K_DOWN:
                new_pos[1] += 1
            elif event.key == pygame.K_LEFT:
                new_pos[0] -= 1
            elif event.key == pygame.K_RIGHT:
                new_pos[0] += 1

            if can_move_to(new_pos):
                player_pos = new_pos

    # Draw the maze
    screen.fill(WHITE)
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            tile = tiles['empty']
            if maze[row][col] == 1:
                tile = tiles['wall']
            elif maze[row][col] == 2:
                tile = tiles['goal']
            elif maze[row][col] == 3:
                tile = tiles['door']
            elif maze[row][col] == 4:
                tile = tiles['key']
            screen.blit(tile, (col * TILE_SIZE, row * TILE_SIZE))

    # Draw the player
    pygame.draw.rect(screen, (0, 255, 0), (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.flip()

pygame.quit()