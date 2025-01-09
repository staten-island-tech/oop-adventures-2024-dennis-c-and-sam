import pygame
import random

# Initialize Pygame
pygame.init()

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define Screen Dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shop Interface")

# Define Item Class
class Item:
    def __init__(self, name: str, description: str, price: int):
        self.name = name
        self.description = description
        self.price = price

# Define Player Class
class Player:
    def __init__(self, inventory: list, money: int, speed: int):
        self.inventory = inventory
        self.money = money
        self.speed = speed

    def buy(self, item):
        if self.money >= item.price:
            self.inventory.append(item)
            self.money -= item.price
            return True
        return False

# Create a few sample items
item_dict = [
    ("speed_potion", "Increases speed", 5),
    ("ladder", "Allows you to jump over one wall", 10),
    ("dash", "Makes you dash in a certain direction", 5)
]

# Randomly select items for sale
shop_items = [Item(*random.choice(item_dict)) for _ in range(3)]

# Create a player
mc = Player(inventory=[], money=100, speed=10)

# Function to draw the shop interface
def draw_shop():
    screen.fill(WHITE)
    
    # Draw title
    font = pygame.font.Font(None, 40)
    title_text = font.render("Welcome to the Shop!", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 20))
    
    # Display available items
    item_y = 100
    for idx, item in enumerate(shop_items):
        item_text = font.render(f"{item.name}: {item.description} - Price: {item.price}", True, BLACK)
        pygame.draw.rect(screen, GREEN, (100, item_y, 600, 50))
        screen.blit(item_text, (120, item_y + 10))
        pygame.draw.rect(screen, RED, (700, item_y, 50, 50))  # Button for buying
        buy_text = font.render("Buy", True, WHITE)
        screen.blit(buy_text, (710, item_y + 15))
        item_y += 60
    
    # Display player's money
    money_text = font.render(f"Money: ${mc.money}", True, BLACK)
    screen.blit(money_text, (10, 10))

# Function to handle mouse click events
def handle_click(mouse_pos):
    global shop_items
    item_y = 100
    for idx, item in enumerate(shop_items):
        buy_button_rect = pygame.Rect(700, item_y, 50, 50)
        if buy_button_rect.collidepoint(mouse_pos):
            if mc.buy(item):
                shop_items.pop(idx)
                print(f"You bought {item.name}! Remaining money: {mc.money}")
                break
        item_y += 60

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                handle_click(event.pos)

    # Draw the shop interface
    draw_shop()
    
    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
