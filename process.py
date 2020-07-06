import pygame
import random
import time
import sys
from classes import Navy, Cannon, Ship


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
                window.blit(boom, (pirate.x,pirate.y + pirate.height / 4))
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
                window.blit(boom, (pirate.x,pirate.y + pirate.height / 4))
                pygame.display.update()
                time.sleep(0.05)
                replay_menu(score)
                break
        else:
            replay_menu(score)
            break
        drawWindow()
    pygame.quit()


