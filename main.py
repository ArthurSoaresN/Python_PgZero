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

TILE_SIZE_MOVE = 1

class Cat:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.frame_timer = 0.0
        self.animation_speed = 0.2
        self.is_moving = False
        self.actor = Actor(FRAME_CAT0)
        self.actor.pos = (self.x, self.y) # É mais simples atribuir a posição assim

    # Removi os métodos move, getPosition e setPosition que não estavam sendo usados
    # Se precisar deles depois, podemos adicioná-los novamente.
    
    def moveUP(self):
        self.actor.y -= TILE_SIZE_MOVE
        self.actor.angle = 0
        
    def moveDOWN(self):
        self.actor.y += TILE_SIZE_MOVE
        self.actor.angle = 180
    
    def moveRIGHT(self):
        self.actor.x += TILE_SIZE_MOVE
        self.actor.angle = 270

    def moveLEFT(self):
        self.actor.x -= TILE_SIZE_MOVE
        self.actor.angle = 90

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
            
    def update(self, dt): # Apenas uma função update agora
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
   
def check_boundaries():
    # --- EIXO Y (VERTICAL) - Clamping ---
    # Se a parte de cima do gato passar do topo da tela (y < 0)
    if hero.actor.top < 0:
        # Trava a parte de cima do gato em 0
        hero.actor.top = 0
    
    # Se a parte de baixo do gato passar da base da tela (y > HEIGHT)
    if hero.actor.bottom > HEIGHT:
        # Trava a parte de baixo do gato no limite da altura
        hero.actor.bottom = HEIGHT

    # --- EIXO X (HORIZONTAL) - Wrapping ---
    # Se a parte direita do gato sumir pela esquerda da tela (x < 0)
    if hero.actor.right < 0:
        # Move a parte esquerda do gato para a borda direita da tela
        hero.actor.left = WIDTH
    
    # Se a parte esquerda do gato sumir pela direita da tela (x > WIDTH)
    if hero.actor.left > WIDTH:
        # Move a parte direita do gato para a borda esquerda da tela
        hero.actor.right = 0

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

    moving_this_frame = False

    if keyboard.up or keyboard.w:
        hero.moveUP()
        moving_this_frame = True
    
    if keyboard.down or keyboard.s:
        hero.moveDOWN()
        moving_this_frame = True
    
    if keyboard.right or keyboard.d:
        hero.moveRIGHT()
        moving_this_frame = True
    
    if keyboard.left or keyboard.a:
        hero.moveLEFT()
        moving_this_frame = True

    hero.is_moving = moving_this_frame

    check_boundaries()
