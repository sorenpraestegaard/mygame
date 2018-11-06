import pygame
import math
from random import randint
from gamelib import Game
import numpy as np

def draw_game():
    if game.state == 0:
        pygame.draw.rect(screen, (30,30,30), pygame.Rect(380, 280, 80, 50))
        screen.blit(myfont.render("MENU", 1, (255,255,255)), (400, 300))
    elif game.state == 1:
        screen.fill((0,10,20))

        for y in reversed(range(0,5)):
            for x in range(0, 5):
                screen.blit(game.level.get_tile_image(x,y), (100 + x*50 + y*50,300 + x*50 - y*50))

        #pygame.draw.rect(screen, (10,123,50), pygame.Rect(game.x, game.y, 50, 50))
        
        if game.moving:
            sprite = game.sprites[3+int(pygame.time.get_ticks()/200)%3]
        else:
            sprite = game.sprites[int(pygame.time.get_ticks()/300)%3]
        mx,my = pygame.mouse.get_pos()
        ang = math.atan2(my - game.y,mx - game.x)
        if game.left:
            screen.blit(pygame.transform.rotate(pygame.transform.flip(sprite, True, False),-math.degrees(ang)), (game.x, game.y))
        else:
            screen.blit(pygame.transform.rotate(sprite,-math.degrees(ang)), (game.x, game.y))

            m = game.to_world_pos(np.array(pygame.mouse.get_pos()))
            #print(m)
            screen.blit(myfont.render("Mouse World pos: {},{}".format(m[0][0],m[1][1]), 1, (255,255,255)), (20,10))
    elif game.state == 2:
        pygame.draw.rect(screen, (30,30,30), pygame.Rect(380, 280, 80, 50))
        screen.blit(myfont.render("PAUSE", 1, (255,255,255)), (400, 300))

pygame.init()
screen = pygame.display.set_mode((800, 600))#, pygame.FULLSCREEN)
# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

done = False

game = Game()

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            game.toggle_pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if game.started():
                game.end_game()
            else:
                game.start_game()

    pressed = pygame.key.get_pressed()

    game.tick(pygame, pressed)
    draw_game()

    pygame.display.flip()
    clock.tick(60)
