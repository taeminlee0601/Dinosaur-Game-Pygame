<<<<<<< HEAD:dinosaurgame.py
import pygame
import os
import time

WIDTH,HEIGHT = 900, 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Dinosaur Game")

FPS = 60
JUMP_HEIGHT = 1

WHITE = 255,255,255
BLACK = 0,0,0
RED = 255,0,0

GROUND = pygame.Rect(0, HEIGHT - 100, WIDTH, HEIGHT/3)
PLAYER = pygame.Rect(WIDTH/4 - 10, HEIGHT - 175 , 20, 75)

def jump(key_pressed):
    if key_pressed[pygame.K_SPACE] and PLAYER.y == HEIGHT - 175:
        jump_animation()

def jump_animation():
    upwards = True
    for i in range(0,301):
        time.sleep(0.001)
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, GROUND)
        if PLAYER.y > HEIGHT - 325 and upwards:
            PLAYER.y -= JUMP_HEIGHT
            pygame.draw.rect(screen, RED, PLAYER)
            pygame.display.update()
        elif PLAYER.y == HEIGHT - 325 and upwards:
            upwards = False
            pygame.draw.rect(screen, RED, PLAYER)
            pygame.display.update()
        elif PLAYER.y >=  HEIGHT - 325 and not upwards:
            PLAYER.y += JUMP_HEIGHT
            pygame.draw.rect(screen, RED, PLAYER)
            pygame.display.update()
    
        

def draw_window():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, GROUND)
    pygame.draw.rect(screen, RED, PLAYER)
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

        key_pressed = pygame.key.get_pressed()

        jump(key_pressed)

    pygame.quit()


if __name__ == "__main__":
=======
from pickle import FALSE
import pygame
import os
import time

WIDTH,HEIGHT = 900, 500

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Dinosaur Game")

FPS = 60
JUMP_HEIGHT = 1

WHITE = 255,255,255
BLACK = 0,0,0
RED = 255,0,0

GROUND = pygame.Rect(0, HEIGHT - 100, WIDTH, HEIGHT/3)
PLAYER = pygame.Rect(WIDTH/4 - 10, HEIGHT - 175 , 20, 75)

def jump(key_pressed):
    if key_pressed[pygame.K_SPACE] and PLAYER.y == HEIGHT - 175:
        jump_animation()

def jump_animation():
    upwards = True
    for i in range(0,301):
        time.sleep(0.001)
        screen.fill(WHITE)
        pygame.draw.rect(screen, BLACK, GROUND)
        if PLAYER.y > HEIGHT - 325 and upwards:
            PLAYER.y -= JUMP_HEIGHT
            pygame.draw.rect(screen, RED, PLAYER)
            pygame.display.update()
        elif PLAYER.y == HEIGHT - 325 and upwards:
            upwards = False
            pygame.draw.rect(screen, RED, PLAYER)
            pygame.display.update()
        elif PLAYER.y >=  HEIGHT - 325 and not upwards:
            PLAYER.y += JUMP_HEIGHT
            pygame.draw.rect(screen, RED, PLAYER)
            pygame.display.update()
    
        

def draw_window():
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, GROUND)
    pygame.draw.rect(screen, RED, PLAYER)
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

        key_pressed = pygame.key.get_pressed()

        jump(key_pressed)

    pygame.quit()


if __name__ == "__main__":
>>>>>>> 40c4a77308cd0288b1137c3efe68a4e853291eeb:Dinosaur Game/dinosaurgame.py
    main()