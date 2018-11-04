from random import randint
import math
from level import Level

class Game:
        def __init__(self, pygame):
                self.state = 0
                #State 0: Menu
                #State 1: Game
                #State 2: Pause
                self.x = 100
                self.y = 100
                self.points = 0
                self.target = [250, 250]
                self.moving = False
                self.left = False
                self.level = Level()
                try:
                        #.convert() converterer billedet til det format, der
                        #er valgt med pyamge.display.setmode(). Hurtigere tegning hver gang
                        self.sheet = pygame.image.load("spritesheet-demo.png").convert()
                        
                except pygame.error:
                        pass

                rects = ((0,0,22,25), (22,0,22,25), (44,0,21,25), (65,0,25,25), (90,0,17,25), (107,0,22,25))
                self.sprites = []
                for r in rects:
                        image = pygame.Surface(pygame.Rect(r).size).convert()
                        image.blit(self.sheet, (0, 0), pygame.Rect(r))
                        self.sprites.append(image)


        def tick(self, pg, pressed):
                self.moving = False
                if self.state == 1:
                        if pressed[pg.K_UP]: 
                                self.y -= 3
                                self.moving = True
                                print('UP' + str(pygame.time.get_ticks()))
                        if pressed[pg.K_DOWN]: 
                                self.y += 3
                                self.moving = True
                        if pressed[pg.K_LEFT]: 
                                self.x -= 3
                                self.moving = True
                                self.left = True
                        if pressed[pg.K_RIGHT]: 
                                self.x += 3
                                self.moving = True
                                self.left = False
                        if math.sqrt((self.target[0] - self.x)**2 + (self.target[1] - self.y)**2) < 40:
                                self.points += 1
                                self.target = [randint(0,800), randint(0,600)]
        
        def start_game(self):
                if self.state == 0:
                        self.state = 1     
                        self.points = 0
                        self.x = 100
                        self.y = 100
                        self.target = [randint(0,800), randint(0,600)]

        def end_game(self):
                if self.state > 0:
                        self.state = 0

        def toggle_pause(self):
                if self.state == 1:
                        self.state = 2
                else:
                        self.state = 1

        def started(self):
                if self.state > 0:
                        return True
                else:
                        return False