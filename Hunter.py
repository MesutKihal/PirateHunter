import pygame
from process import Play
import sys

def run_game():
    pygame.init()
    width = 1024
    height = 512
    fps = 60
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pirate Hunter")
    clock = pygame.time.Clock()
    bg = pygame.image.load('sea_bg.png')
    wheel = pygame.image.load('wheel.png')
    door = pygame.image.load('door.png')
    pirate_ = pygame.image.load('pirate.png')
    flag = pygame.image.load('flag.png')
    title = pygame.image.load('title.jpg')
    font = pygame.font.SysFont('rod', 72)
    font2 = pygame.font.SysFont('newcourier', 22)
    start_color = (100,100,100)
    exit_color = (100,100,100)

    button_width = 300
    button_height = 70
    start_x = 362
    start_y = 221
    exit_x = 362
    exit_y = 301
    def draw_screen():
        screen.blit(bg, (0,0))
        pygame.draw.rect(screen, start_color, (start_x, start_y, button_width, button_height))
        screen.blit(wheel, (start_x + button_width,start_y))
        pygame.draw.rect(screen, exit_color, (exit_x, exit_y, button_width, button_height))
        screen.blit(door, (exit_x + button_width, exit_y))
        screen.blit(start_text, (399, start_y))
        screen.blit(exit_text, (422, exit_y))
        screen.blit(title, (287, 81))
        screen.blit(pirate_, (182,81))
        screen.blit(flag, (0,409))
        screen.blit(credit, (51,425))
        pygame.display.update()

    
    while True:
        clock.tick(fps) 
        start_text = font.render('START', True, (255,255,255))
        exit_text = font.render('EXIT', True, (255,255,255))
        credit = font2.render('Developed By:  Mesut Kihal', True, (0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                if start_x < mouse[0] < start_x + button_width and start_y < mouse[1] < start_y + button_height:
                    start_color = (150,150,150)
                    Play()
                    break
                elif exit_x < mouse[0] < exit_x + button_width and exit_y < mouse[1] < exit_y + button_height:
                    exit_color = (150,150,150)
                    break
        draw_screen()
        start_color = (100,100,100)
        exit_color = (100,100,100)
    pygame.quit()
run_game()
