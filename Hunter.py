import pygame
import random
import time
import sys

#Classes
class Navy(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.width = 113
        self.height = 66
        self.image = pygame.image.load('navy.png')


    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        pygame.draw.rect(window, (172,228,244), (self.x, self.y, self.width, self.height), 1)
        
class Cannon(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.width = 34
        self.height = 13
        self.image = pygame.image.load('bullet.png')

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        pygame.draw.rect(window, (172,228,244), (self.x, self.y, self.width, self.height), 1)

class Ship(object):
    def __init__(self, x, y, vel):
        self.x = x
        self.y = y
        self.vel = vel
        self.width = 113
        self.height = 66
        self.image = pygame.image.load('pirate_ship.png')

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        pygame.draw.rect(window, (172,228,244), (self.x, self.y, self.width, self.height), 1)

#Game_Logic
def Play():
    global destroyed
    pygame.init()
    #---------------------------------Main-Window-Settings---------------------------------------
    window_width = 1024
    window_height = 512
    fps = 120

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Pirate Hunter')
    clock = pygame.time.Clock()
    bg = pygame.image.load('sea_bg.png')
    boom = pygame.image.load('boom.png')
    destroyed = 0
    score = 0
    level = 0
    hunter = Navy(51, 51, 7)
    pirate = Ship(1536, random.randint(30, 446), 7)
    font = pygame.font.SysFont('rod', 27)
    replay_font = pygame.font.SysFont('verdana', 27)

    #------------------------------------Special-Functions--------------------------------------------
    def replay_menu(score):
        while True:
            clock.tick(fps)
            score_txt = replay_font.render('Score:   ' + str(score), True, (0,0,0))
            replay_text = replay_font.render('If you want to replay Press "R"', True, (0,0,0))
            window.blit(bg, (0,0))
            window.blit(score_txt, (420, 220))
            window.blit(replay_text, (300, 256))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                Play()
                break
    def drawWindow():
        global destroyed
        pygame.display.update()
        window.blit(bg, (0,0))
        window.blit(destroyed_text, (7, 0))
        window.blit(level_text, (210, 0))
        window.blit(score_text, (610, 0))
        hunter.draw(window)
        pirate.draw(window)
            
        for bullet in bullets:
            bullet.draw(window)
                
            if bullet.x < window_width:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
            if bullet.x >= pirate.x and pirate.y <= bullet.y <= pirate.y + pirate.width:
                window.blit(boom, (pirate.x,round(pirate.y + pirate.height / 4)))
                pygame.display.update()
                time.sleep(0.05)
                pirate.x = 1536
                pirate.y = random.randint(0, window_height - pirate.height)
                pygame.mixer.Channel(3).play(pygame.mixer.Sound('explosion.wav'))
                destroyed += 1
        pygame.display.update()

     
    #--------------------------------------Main-Loop----------------------------------------------------     
    bullets = []
    while True:
        clock.tick(fps)
        destroyed_text = font.render('Destroyed ' + str(destroyed), True, (0,0,0))
        level_text = font.render('Level ' + str(level), True, (0,0,0))
        score_text = font.render('Score ' + str(score), True, (0,0,0))
        
        level = (destroyed//7) + 1
        score = level * destroyed * 10
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Channel(2).play(pygame.mixer.Sound('cannon.wav'))
                    if len(bullets) < 2:
                        bullets.append(Cannon(hunter.x + hunter.width, hunter.y + 25, 30))
                    else:
                        bullets.pop(0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and hunter.y >= 50+hunter.vel:
            hunter.y -= hunter.vel

        if keys[pygame.K_DOWN] and hunter.y <= window_height - hunter.height - hunter.vel:
            hunter.y += hunter.vel
                
        if pirate.x > 0:
            pirate.x -= pirate.vel + ((level*2) + 1)
            if pirate.x <= hunter.x + hunter.width and (pirate.y <= hunter.y <= pirate.y + pirate.height or hunter.y <= pirate.y <= hunter.y + hunter.height):
                window.blit(boom, (pirate.x,round(pirate.y + pirate.height / 4)))
                pygame.display.update()
                time.sleep(0.05)
                replay_menu(score)
                break
        else:
            replay_menu(score)
            break
        drawWindow()
    pygame.quit()

#Main_Menu
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
