import pygame
import time

pygame.init()

WIDTH = 500
HEIGHT = 500

display_surface=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

img = pygame.image.load("balloons.jpg")
image = pygame.transform.scale(img, (WIDTH, HEIGHT))

while(True):
    font = pygame.font.SysFont("Calibri",80)
    text = font.render("Happy",True,(0,0,0))
    text1 = font.render("Birthday",True,(0,0,0))
    display_surface.fill((255,255,255)) #WHITE
    display_surface.blit(image,(0,0))
    display_surface.blit(text,(210,180))
    display_surface.blit(text1,(180,265))
    pygame.display.update()
    time.sleep(4)

pygame.quit()