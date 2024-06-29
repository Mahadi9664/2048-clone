import pygame
import random
import math

pygame.init()

FPS = 60

width, height = 800, 800
rows = 4
cols = 4

rect_height = height//rows
rect_width = width//rows

outline_color = (187, 173, 160)
outline_thickness = 10
background_color = (205, 192, 180)
font_color = (119, 110, 101)

font = pygame.font.SysFont("helvetica", 60, bold= True)
move_vel = 20

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("2048")

def main():
    clock = pygame.time.clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        pygame.quit()

if __name__ == "__main__":
    main(window)