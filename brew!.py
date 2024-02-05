import os
import sys

import pygame
from tkinter import *
from  tkinter import messagebox

import time
from time import sleep
from pygame import *

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#IMPORTS AND GLOBAL VALUES



HEIGHT, WIDTH = 450, 1100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BREW!")
FPS = 60
GREEN = (5,100,44)
keys_pressed = pygame.key.get_pressed()
rectangle1 = pygame.Rect(0,0,20,20)
RED = (255,30,70)

pf_dest = [535, 290]
tamper_dest = [390, 80]
global beans_amount
beans_amount = 0



clock = time.Clock()

#LOADING AND SCALING IMAGES ####

POURING_COFFEE1_IMAGE = pygame.image.load(resource_path('pouring.png'))
POURING_COFFEE1 = pygame.transform.scale(POURING_COFFEE1_IMAGE,(55,85))

POURING_COFFEE2_IMAGE = pygame.image.load(resource_path('pouring2.png'))
POURING_COFFEE2 = pygame.transform.scale(POURING_COFFEE2_IMAGE,(55,85))

PLUS_COFFEE_IMAGE = pygame.image.load(resource_path('PLUS_COFFEE.png'))
PLUS_COFFEE = pygame.transform.scale(PLUS_COFFEE_IMAGE,(20,40))

MINUS_COFFEE_IMAGE = pygame.image.load(resource_path('MINUS_COFFEE.png'))
MINUS_COFFEE = pygame.transform.scale(MINUS_COFFEE_IMAGE,(20,40))


MILLING_IMAGE = pygame.image.load(resource_path('milling1.png'))
MILLING = pygame.transform.scale(MILLING_IMAGE,(20,40))

MILLING_IMAGE2 = pygame.image.load(resource_path('milling2.png'))
MILLING2 = pygame.transform.scale(MILLING_IMAGE2,(20,40))

FORCE_INDICATOR_IMAGE = pygame.image.load(resource_path('force_indicator.png'))
FORCE_INDICATOR = pygame.transform.scale(FORCE_INDICATOR_IMAGE,(40,100))

FORCE_DASH_IMAGE = pygame.image.load(resource_path('force_dash.png'))
FORCE_DASH = pygame.transform.scale(FORCE_DASH_IMAGE,(100,5))

COFFEE_MACHINE_IMAGE = pygame.image.load(resource_path("machine_empty.png"))
COFFEE_M = pygame.transform.scale(COFFEE_MACHINE_IMAGE, (500,500))

GRINDER_IMAGE = pygame.image.load(resource_path("grinder.png"))
GRINDER = pygame.transform.scale(GRINDER_IMAGE, (400,400))

TAMPER_IMAGE = pygame.image.load(resource_path("tamper.png"))
TAMPER = pygame.transform.scale(TAMPER_IMAGE, (100, 100))


GRINDED_AMOUNT_IMAGE = pygame.image.load(resource_path("grinded+amount.png"))
GRINDED_AMOUNT = pygame.transform.scale(GRINDED_AMOUNT_IMAGE, (20, 150))

GRINDING_SCALE_IMAGE = pygame.image.load(resource_path("grinding+scale.png"))
GRINDING_SCALE = pygame.transform.scale(GRINDING_SCALE_IMAGE, (300, 100))


PF_IMAGE = pygame.image.load(resource_path('empty_PF.png'))
PF = pygame.transform.scale(PF_IMAGE,(100,100))

PF_full_IMAGE = pygame.image.load(resource_path('full_PF.png'))
PF_full = pygame.transform.scale(PF_full_IMAGE,(100,100))

EMPTY_GLASS_IMAGE = pygame.image.load(resource_path('empty_glass.png'))
EMPTY_GLASS = pygame.transform.scale(EMPTY_GLASS_IMAGE, (200,180))

FULL_GLASS_IMAGE = pygame.image.load(resource_path('full_glass.png'))
FULL_GLASS = pygame.transform.scale(FULL_GLASS_IMAGE, (200,180))



### DEFINING FUNCTIONS ###

def draw_comand(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x,y))

def draw_result(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x, y))
    WIN.fill(GREEN)
    WIN.blit(COFFEE_M, (0, 0))
    WIN.blit(FULL_GLASS, (134, 274))
    WIN.blit(GRINDER, (400, 70))
    WIN.blit(TAMPER, (tamper_dest[0], tamper_dest[1]))
    WIN.blit(PF, (pf_dest[0], pf_dest[1]))
    WIN.blit(img, (x, y))
    pygame.draw.rect(WIN,RED,rectangle1)


    pygame.display.update()

def draw_coffee_amount(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    WIN.blit(img, (x,y))
    WIN.fill(GREEN)
    WIN.blit(COFFEE_M, (0, 0))
    WIN.blit(EMPTY_GLASS, (134, 274))
    WIN.blit(GRINDER, (400, 70))
    WIN.blit(TAMPER, (tamper_dest[0], tamper_dest[1]))
    WIN.blit(PF, (pf_dest[0], pf_dest[1]))
    WIN.blit(img, (x,y))
    draw_comand(
        "Now something for control freaks. ",
        text_font, (0, 0, 0), 20, 30)
    draw_comand(
        "Use + and - buttons to chose amount of water for brewing (ml).",
        text_font, (0, 0, 0), 20, 60)
    draw_comand(
        "If decided, turn the machine on.",
        text_font, (0, 0, 0), 20, 90)
    pygame.draw.rect(WIN, RED, rectangle1)
    pygame.display.update()
def tamping_force(pf_x, pf_y):
    global FI_dest
    FI_dest = [310, 210]
    going_down = True
    while True:

        if FI_dest[1] == 310:
            going_down = False
        if FI_dest[1] == 210:
            going_down = True

        if going_down == True:
            FI_dest[1] += 1

        else:
            FI_dest[1] -= 1



        WIN.fill(GREEN)

        WIN.blit(COFFEE_M, (0, 0))
        WIN.blit(GRINDER, (400, 70))
        WIN.blit(TAMPER, (390, 80))
        WIN.blit(PF, (pf_x, pf_y))
        WIN.blit(EMPTY_GLASS, (134, 274))
        WIN.blit(FORCE_INDICATOR,(420,220))
        WIN.blit(FORCE_DASH,(390,FI_dest[1]))
        draw_comand("Try to get the right force (green spot).", text_font2, (0, 0, 0), 20, 30)
        pygame.draw.rect(WIN, RED, rectangle1)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:


                return FI_dest[1], False



def grinded_amount(pf_x, pf_y):
    global GA_dest
    GA_dest = [710, 20]

    going_left = True
    while True:

        if GA_dest[0] == 970:
            going_left = False
        if GA_dest[0] == 710:
            going_left = True

        if going_left == True:
            GA_dest[0] += 2

        else:
            GA_dest[0] -= 2

        WIN.fill(GREEN)

        WIN.blit(COFFEE_M, (0, 0))
        WIN.blit(GRINDER, (400, 70))
        WIN.blit(TAMPER, (390, 80))
        WIN.blit(PF, (pf_x, pf_y))
        WIN.blit(EMPTY_GLASS, (134, 274))
        WIN.blit(GRINDING_SCALE,(690,120))
        WIN.blit(GRINDED_AMOUNT,(GA_dest[0],70))
        draw_comand("pick your coffee amount (grams).", text_font2, (0, 0, 0), 700, 230)
        draw_comand("click at the right moment", text_font2, (0, 0, 0), 700, 260)
        pygame.draw.rect(WIN, RED, rectangle1)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("dziala")

                return GA_dest[0], False

def draw_window_start(pf_x, pf_y):


    WIN.fill(GREEN)

    WIN.blit(COFFEE_M, (0,0))
    WIN.blit(GRINDER, (400, 70))
    WIN.blit(TAMPER, (390, 80))
    WIN.blit(PF, (pf_x, pf_y))
    WIN.blit(EMPTY_GLASS,(134,274))

    draw_comand("Let's prepare the perfect espresso... or whatever you like ", text_font, (0, 0, 0), 20, 20)
    draw_comand("(there will be points tho)!", text_font, (0, 0, 0), 20, 50)
    draw_comand("First things first,", text_font2, (0, 0, 0), 700, 200)
    draw_comand("grind some coffee!", text_font2, (0, 0, 0), 700, 230)

    pygame.draw.rect(WIN, RED, rectangle1)
    pygame.display.update()
    return pf_x, pf_y

def draw_window_grinded(x, y):


    for i in range (0,100):
        WIN.fill(GREEN)
        WIN.blit(COFFEE_M, (0,0))
        WIN.blit(EMPTY_GLASS, (134, 274))
        WIN.blit(GRINDER, (400, 70))
        WIN.blit(TAMPER, (390, 80))
        WIN.blit(PF, (pf_dest[0], 290))

        if i %3 == 0:
            WIN.blit(MILLING,(570, 290))
        else:
            WIN.blit(MILLING2, (570, 290))

        i+=1
        pygame.draw.rect(WIN, RED, rectangle1)
        pygame.display.update()



    for pf_dest[0] in range (pf_dest[0], 395, -1):
        pf_dest[0] = pf_dest[0] -1

        WIN.fill(GREEN)


        WIN.blit(COFFEE_M, (0,0))
        WIN.blit(EMPTY_GLASS, (134, 274))
        WIN.blit(GRINDER, (400, 70))
        WIN.blit(TAMPER, (390, 80))
        WIN.blit(PF_full, (pf_dest[0], 290))
        draw_comand("Use the force! ehm.. use tamper to tamp the coffee in portafilter", text_font2, (0, 0, 0), 20, 30)
        pygame.draw.rect(WIN, RED, rectangle1)
        pygame.display.update()

    return pf_dest[0]



def draw_window_tamped():




    for x in range (tamper_dest[1],260):


        tamper_dest[1] = tamper_dest[1] +1
        WIN.fill(GREEN)


        WIN.blit(COFFEE_M, (0,0))
        WIN.blit(EMPTY_GLASS, (134, 274))
        WIN.blit(GRINDER, (400, 70))
        draw_comand("Put the portafilter into group head, it is a metal piece that poors water on portafilter." , text_font2, (0, 0, 0), 20, 30)
        draw_comand("Actually, no explanation needed, just click the portafilter, its automated", text_font2, (0, 0, 0), 20, 60)


        WIN.blit(TAMPER, (tamper_dest[0], tamper_dest[1]))

        if tamper_dest[1] < 240:
            WIN.blit(PF_full, (pf_dest[0], pf_dest[1]))
        else:
            WIN.blit(PF, (pf_dest[0], pf_dest[1]))
        pygame.draw.rect(WIN, RED, rectangle1)
        pygame.display.update()
    return tamper_dest[0], tamper_dest[1]




def draw_window_rd_to_brew():


    for z in range (tamper_dest[1],160,-1):

        tamper_dest[1] = tamper_dest[1] -1
        WIN.fill(GREEN)


        WIN.blit(COFFEE_M, (0,0))
        WIN.blit(EMPTY_GLASS, (134, 274))
        WIN.blit(GRINDER, (400, 70))
        WIN.blit(TAMPER, (tamper_dest[0], tamper_dest[1]))
        WIN.blit(PF, (pf_dest[0], pf_dest[1]))
        pygame.draw.rect(WIN, RED, rectangle1)
        pygame.display.update()


    for x in range (pf_dest[0], 193, -1):
        pf_dest[0] -= 1
        if pf_dest[1] > 247:
            pf_dest[1] -=1

        WIN.fill(GREEN)

        WIN.blit(COFFEE_M, (0,0))
        WIN.blit(EMPTY_GLASS, (134, 274))
        WIN.blit(GRINDER, (400, 70))
        WIN.blit(TAMPER, (tamper_dest[0], tamper_dest[1]))
        WIN.blit(PF, (pf_dest[0], pf_dest[1]))
        pygame.draw.rect(WIN, RED, rectangle1)
        pygame.display.update()

    return tamper_dest[0], tamper_dest[1], pf_dest[0], pf_dest[1]


# def COFFEE_AMOUNT_CHOOSING():
#


### POURING COFFEE ###
def pouring_cofee():

    for i in range (0,70):

        if i < 25:

            WIN.fill(GREEN)
            WIN.blit(COFFEE_M, (0,0))
            WIN.blit(EMPTY_GLASS, (134, 274))
            WIN.blit(GRINDER, (400, 70))
            WIN.blit(TAMPER, (tamper_dest[0], tamper_dest[1]))
            WIN.blit(PF, (pf_dest[0], pf_dest[1]))
            if i %3 == 0:
                WIN.blit(POURING_COFFEE1,(210, 325))
            else:
                WIN.blit(POURING_COFFEE2, (210, 325))

            i+=1

            pygame.draw.rect(WIN, RED, rectangle1)
            pygame.display.update()
            pygame.time.wait(35)

        elif i < 69:
            WIN.fill(GREEN)
            WIN.blit(COFFEE_M, (0, 0))
            WIN.blit(FULL_GLASS, (134, 274))
            WIN.blit(GRINDER, (400, 70))
            WIN.blit(TAMPER, (tamper_dest[0], tamper_dest[1]))
            WIN.blit(PF, (pf_dest[0], pf_dest[1]))
            if i % 3 == 0:
                WIN.blit(POURING_COFFEE1, (210, 325))
            else:
                WIN.blit(POURING_COFFEE2, (210, 325))

            i += 1
            pygame.draw.rect(WIN, RED, rectangle1)
            pygame.display.update()
            pygame.time.wait(35)

        else:
            WIN.fill(GREEN)
            WIN.blit(COFFEE_M, (0, 0))
            WIN.blit(FULL_GLASS, (134, 274))
            WIN.blit(GRINDER, (400, 70))
            WIN.blit(TAMPER, (tamper_dest[0], tamper_dest[1]))
            WIN.blit(PF, (pf_dest[0], pf_dest[1]))
            pygame.draw.rect(WIN, RED, rectangle1)
            pygame.display.update()
            pygame.time.wait(35)


def points():
    beans_amount = 0
    if FI_dest[1] > 270 and FI_dest[1] < 300:
        tamped_force = 1
        draw_result("Tamped gooooood", text_font2, (0, 0, 0),200, 60)
    if FI_dest[1] >= 300:
        draw_comand("Tamped too soft", text_font2, (0, 0, 0), 200, 60)
        tamped_force = 0
    if FI_dest[1] <=270:
        draw_comand("Tamped too hard", text_font2, (0, 0, 0), 200, 60)
        tamped_force = 2

    if GA_dest[0] > 709 and GA_dest[0] < 740:
        beans_amount = 5
    if GA_dest[0] > 739 and GA_dest[0] < 800:
        beans_amount = 10
    if GA_dest[0] > 799 and GA_dest[0] < 870:
        beans_amount = 15
    if GA_dest[0] > 869 and GA_dest[0] < 935:
        beans_amount = 20
    if GA_dest[0] > 934 and GA_dest[0] < 971:
        beans_amount = 25





    coffe_ratio =  coffee_amount / beans_amount


    if coffe_ratio > 2.2:
        if tamped_force == 1:
            draw_result("Coffee is watery, and has zero taste (too much water for this amount of coffee beans. Tamped good tho.", text_font2, (0, 0, 0), 20, 60)

        if tamped_force == 0:
            draw_result("Coffee is watery, and has zero taste (too much water for this amount of coffee beans. Tamped too hard.", text_font2, (0, 0, 0), 20, 60)

        if tamped_force == 2:
            draw_result("Coffee is watery, and has zero taste (too much water for this amount of coffee beans. Tamped too weak as well.", text_font2, (0, 0, 0), 20, 60)




    if coffe_ratio < 1.5:
        if tamped_force == 1:
            draw_result("Coffee is too strong, bitter, (too much coffee beans for this amount of water). Tamped good tho.", text_font2, (0, 0, 0), 20, 90)
        if tamped_force == 0:
            draw_result("Coffee is too strong, bitter, (too much coffee beans for this amount of water). Tamped too hard.", text_font2, (0, 0, 0), 20, 90)
        if tamped_force == 2:
            draw_result("Coffee is too strong, bitter, (too much coffee beans for this amount of water). Tamped too weak as well.", text_font2, (0, 0, 0), 20, 90)

    if coffe_ratio <= 2.2 and coffe_ratio >= 1.5:
        if tamped_force == 1:
            draw_result("Perfect cup of espresso! Ratio just on point. Tamped good as well.", text_font2, (0, 0, 0), 20, 90)
        if tamped_force == 0:
            draw_result("Perfect cup of espresso! Ratio just on point. Tamped too hard tho.", text_font2, (0, 0, 0), 20, 90)
        if tamped_force == 2:
            draw_result("Perfect cup of espresso! Ratio just on point. Tamped too weak tho.", text_font2, (0, 0, 0), 20, 90)




### MAIN FUNCTION OF APP ###
def main():

    pygame.init()
    global coffee_amount
    coffee_amount = 0
    global tamped_force
    tamped_force = 0


    global text_font
    text_font = pygame.font.SysFont("Arial", 30, bold=True, italic=True)

    global text_font2
    text_font2 = pygame.font.SysFont("Arial", 20, bold=True, italic=True)
    stage = 1
    clock = pygame.time.Clock()
    run = True
    sec = 0
    started = False
    tamp_force = 0
    tamping = True
    GRINDED_COFFEE_AMOUNT = 0

    interuptor = True
    grinder_value = 1

### RUNNING LOOP ###

    while run:
        x, y = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed(num_buttons=3)






### CALLING EVENTS ###

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN and stage == 6 and x > 155 and x < 173 and y > 229 and y < 251:
                coffee_amount = coffee_amount -1
                draw_coffee_amount(str(coffee_amount), text_font, (0, 0, 0), 170, 195)

            if event.type == pygame.MOUSEBUTTONDOWN and stage == 6 and x > 183 and x < 203 and y > 229 and y < 251:
                coffee_amount = coffee_amount +1
                draw_coffee_amount(str(coffee_amount), text_font, (0, 0, 0), 170, 195)



            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and x < 20 and y < 20:
                global pf_dest
                pf_dest = [535, 290]
                tamper_dest = [390, 80]
                beans_amount = 0
                main()


            if stage == 1 :
                draw_window_start(pf_dest[0], pf_dest[1])
                stage = 2


            if event.type == pygame.MOUSEBUTTONDOWN and stage == 2 and x > 566 and x < 595 and y > 224 and y < 250:
                grinded_amount(pf_dest[0], pf_dest[1])

                stage = 3

            if event.type == pygame.MOUSEBUTTONDOWN and x > 566 and x < 595 and y > 224 and y < 250 and stage == 3:
                draw_window_grinded(pf_dest[0], pf_dest[1])

                stage = 4

            if event.type == pygame.MOUSEBUTTONDOWN and stage == 4 and x > 410 and x < 463 and y >100 and y < 163:

                tamping_force(pf_dest[0], pf_dest[1])

                draw_window_tamped()
                stage = 5


            if event.type == pygame.MOUSEBUTTONDOWN and stage == 5 and x > 407 and x < 475 and y > 324 and y < 366:
                draw_window_rd_to_brew()

                draw_coffee_amount(str(coffee_amount), text_font, (0, 0, 0), 170, 195)

                stage = 6

            if event.type == pygame.MOUSEBUTTONDOWN and stage == 6 and x > 220 and x < 255 and y > 195 and y < 235:
                if coffee_amount > 70:
                    messagebox.showerror("nope", "Yo, that's too much coffee for so tiny glass!")

                if coffee_amount < 0:
                    messagebox.showerror("nope", "That would be magic, we don't do magic here")

                if coffee_amount >= 0 and coffee_amount < 10:
                    messagebox.showerror("nope", "That is not enough to get the taste!")

                if coffee_amount>=10 and coffee_amount <= 70:
                    pouring_cofee()

                    stage = 7

                if stage == 7:
                    points()












    pygame.quit()

if __name__ == "__main__":
    main()