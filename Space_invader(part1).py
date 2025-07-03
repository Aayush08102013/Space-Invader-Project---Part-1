import math
import random
import pygame

# Constants:
# screen:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
# player:
PLAYER_START_X = 370
PLAYER_START_Y = 380
# Enemy:
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
# Bullet:
BULLET_SPEED_Y = 10
# Collision distance:
COLLISION_DISTANCE = 27

# intialize the game:
pygame.init()

# Create a screen:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background:
backgorund = pygame.image.load('C:/Users/aayus/OneDrive/Desktop/Coding with Codlingal/.idea/Pygame/bg2.jpg')

# Caption and Icon:
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('C:/Users/aayus/OneDrive/Desktop/Coding with Codlingal/.idea/Pygame/ufo.jpeg')
pygame.display.set_icon(icon)

# Player:
playerImg = pygame.image.load('C:/Users/aayus/OneDrive/Desktop/Coding with Codlingal/.idea/Pygame/player.jpg')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy:
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

# Creating enemies:

for _i in range (num_of_enemies):
    enemyImg.append(pygame.image.load('C:/Users/aayus/OneDrive/Desktop/Coding with Codlingal/.idea/Pygame/enemy.jpg'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet:
bulletImg = pygame.image.load('C:/Users/aayus/OneDrive/Desktop/Coding with Codlingal/.idea/Pygame/bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = 'ready'

# Score:
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over text:
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Function to show the score:
def show_score(x, y):
    # Display the current score on the screen:
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

# Function to display the Game over text:
def game_over_text():
    over_text = over_font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

# Function to draw the player and enemy:

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Function to draw a bullet
def fire_bullet():
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

# Function to check for collision:
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

