import math
import random

# Largura
WIDTH = 800
# Altura
HEIGHT = 400
# Quadrado
TILE_SIZE = 50

STATE = 'MENU'
score = 0
fase = 1
music_enable = True

# CORES
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_ASPHALT = (60, 60, 60)
COLOR_SIDEWALK = (180, 180, 180)
COLOR_LANE_LINE = (255, 255, 255, 100) # Faixa de pedestres
COLOR_MENU_BUTTON = (100, 100, 255)

# Sprite
FRAME_CAT0 = 'cat'
FRAME_CAT1 = 'cat_walk1'
FRAME_CAT2 = 'cat_walk2' 
CAT_INICIAL_POSITION = 380, 380

# Musica

# Classes

TILE_SIZE_MOVE = TILE_SIZE/10

class Cat:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.frame_timer = 0.0
        self.animation_speed = 0.2
        self.is_moving = False
        self.actor = Actor(FRAME_CAT0)
        self.actor.x = self.x
        self.actor.y = self.y

    def move(self, dx, dy):
        self.actor.x += dx * TILE_SIZE_MOVE
        self.actor.y += dy * TILE_SIZE_MOVE

    def getPosition(self):
        x1, y1 = self.actor.pos
        position = [x1, y1]
        return position
    
    def setPosition(self, set_x, set_y):
        self.actor.x = set_x
        self.actor.y = set_y

    def moveUP(self):
        self.actor.x = self.actor.x
        self.actor.y -= TILE_SIZE_MOVE
        
    def moveDOWN(self):
        self.actor.x = self.actor.x
        self.actor.y += TILE_SIZE_MOVE
    
    def moveRIGHT(self):
        self.actor.y = self.actor.y
        self.actor.x += TILE_SIZE_MOVE

    def moveLEFT(self):
        self.actor.y = self.actor.y
        self.actor.x -= TILE_SIZE_MOVE

    def update(self, dt):
        self.animate(dt)
        if not self.is_moving:
            self.actor.image = FRAME_CAT0
    
    def animate(self, dt):
        if not self.is_moving:
            return
        self.frame_timer += dt
        
        if self.frame_timer >= self.animation_speed:
            if self.actor.image == FRAME_CAT1:
                self.actor.image = FRAME_CAT2
            else:
                self.actor.image = FRAME_CAT1
            self.frame_timer = 0.0
        
    def update(self, dt):
        self.animate(dt)
        if not self.is_moving:
            self.actor.image = FRAME_CAT0
    
    def draw(self):
        self.actor.draw()


class Car:
    pass

def on_mouse_down(pos, button):

    # Desempacota a tupla 'pos' em x e y
    x, y = pos
    
    # Imprime os valores de x e y
    print(f"Clique em X: {x}, Y: {y}")

    """
    if button == mouse.LEFT and cat.collidepoint(pos):
        print("aw")
        sounds.catcrash.play()
    else:
        print("You missed me")
    """

hero = Cat(380,380)
var0cg = hero

def init_game():
    global hero, score, fase, STATE
    score = 0
    STATE = 'PLAYING'
   

def draw():

    screen.draw.filled_rect(Rect(0, 0, WIDTH, TILE_SIZE), COLOR_SIDEWALK) # sidewalk from above
    screen.draw.filled_rect(Rect(0, HEIGHT - TILE_SIZE, WIDTH, TILE_SIZE), COLOR_SIDEWALK) # sidewalk from below

    STREET_HEIGHT = 300 # altura da via
    STREET_WIDTH = 800 # largura da via
    STREET_Y = 50
    STREET_X = 0
    screen.draw.filled_rect(Rect(STREET_X, STREET_Y, STREET_WIDTH, STREET_HEIGHT), COLOR_ASPHALT) # street

    LINE_Y = 80
    LINE_X = 0
    LINE_WIDTH = 50 # largura faixa
    STREET_HEIGHT = 5 # altura faixa

    for j in range(4):
        new_line_y = LINE_Y * j + TILE_SIZE + 30
        for i in range(6):
            new_line_x = LINE_X + (i * 150)
            screen.draw.filled_rect(Rect(new_line_x, new_line_y, LINE_WIDTH, STREET_HEIGHT), COLOR_WHITE)
        j += 100

    hero.draw()
    screen.draw.text(f"Score: {score}   Fase: {fase}", (10, 10), fontsize=30, color=COLOR_WHITE)

def update(dt):
    hero.update(dt)

    if keyboard.up or keyboard.w:
        hero.moveUP()
        hero.is_moving = True
        hero.update(dt)
    if keyboard.down or keyboard.s:
        hero.moveDOWN()
        hero.is_moving = True
        hero.update(dt)
    if keyboard.right or keyboard.d:
        hero.moveRIGHT()
        hero.is_moving = True
        hero.update(dt)
    if keyboard.left or keyboard.a:
        hero.moveLEFT()
        hero.is_moving = True
        hero.update(dt)
    else:
        hero.is_moving = False
        hero.update(dt)
