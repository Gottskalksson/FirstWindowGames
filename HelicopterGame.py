import pygame

pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode((width,height))

def write(text, size):
    font = pygame.font.SysFont("Arial", size)
    rend = font.render(text, 1, (255,100,100))
    x = (width - rend.get_rect().width)/2
    y = (height - rend.get_rect().height)/2
    screen.blit(rend, (x,y))

write("Press space to continue", 20)
pygame.display.update()
