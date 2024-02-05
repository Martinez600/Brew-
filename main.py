import os

import pygame
import time

HEIGHT, WIDTH = 450, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BREW!")
FPS = 60
GREEN = (5,100,44)

COFFEE_MACHINE_IMAGE = pygame.image.load("machine_empty.png")
COFFEE_M = pygame.transform.scale(COFFEE_MACHINE_IMAGE, (500,500))

GRINDER_IMAGE = pygame.image.load("grinder.png")
GRINDER = pygame.transform.scale(GRINDER_IMAGE, (400,400))

TAMPER_IMAGE = pygame.image.load("tamper.png")
TAMPER = pygame.transform.scale(TAMPER_IMAGE, (100, 100))


PF_IMAGE = pygame.image.load('empty_PF.png')
PF = pygame.transform.scale(PF_IMAGE,(100,100))

PF_full_IMAGE = pygame.image.load('full_PF.png')
PF_full = pygame.transform.scale(PF_full_IMAGE,(100,100))
# SPACESHIP2_image = pygame.image.load("2.jpg")
# SPACESHIP2 = pygame.transform.scale(SPACESHIP2_image, (90,40))
SPACESHIP_WIDTH = 40
SPACESHIP_HEIGHT = 20
def draw_window_start():
    WIN.fill(GREEN)

    WIN.blit(COFFEE_M, (0,0))
    WIN.blit(GRINDER, (400, 70))
    WIN.blit(TAMPER, (390, 80))
    WIN.blit(PF, (535, 290))
    # WIN.blit(COFFEE_M,(yellow.x,  yellow.y))
    # WIN.blit(SPACESHIP2, (red.x, red.y))


    pygame.display.update()

def draw_window_grinded():

    WIN.fill(GREEN)

    WIN.blit(COFFEE_M, (0,0))
    WIN.blit(GRINDER, (400, 70))
    WIN.blit(TAMPER, (390, 80))
    WIN.blit(PF_full, (390, 200))
    pygame.display.update()

def draw_window_tamped():

    WIN.fill(GREEN)

    WIN.blit(COFFEE_M, (0,0))
    WIN.blit(GRINDER, (400, 70))
    WIN.blit(TAMPER, (386, 160))
    WIN.blit(PF, (390, 200))
    pygame.display.update()


def draw_window_rd_to_brew():

    WIN.fill(GREEN)

    WIN.blit(COFFEE_M, (0,0))
    WIN.blit(GRINDER, (400, 70))
    WIN.blit(TAMPER, (386, 160))
    WIN.blit(PF, (193, 247))
    pygame.display.update()



def main():
    # red = pygame.Rect(100, 100, SPACESHIP_WIDTH, SPACESHIP_HEIGHT )
    # yellow = pygame.Rect(10, 30, SPACESHIP_WIDTH, SPACESHIP_HEIGHT )

    stage = 1
    clock = pygame.time.Clock()
    run = True
    while run:

        x, y = pygame.mouse.get_pos()
        print(x, y)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if stage == 1 :
                draw_window_start()

            if event.type == pygame.MOUSEBUTTONDOWN and x > 566 and x < 595 and y >224 and y < 250:
                draw_window_grinded()
                stage = 2

            if event.type == pygame.MOUSEBUTTONDOWN and stage == 2 and x > 410 and x < 463 and y >100 and y < 163:
                draw_window_tamped()
                stage = 3

            if event.type == pygame.MOUSEBUTTONDOWN and stage == 3 and x > 400 and x < 463 and y > 240 and y < 270:
                draw_window_rd_to_brew()
                stage = 3



    pygame.quit()

if __name__ == "__main__":
    main()