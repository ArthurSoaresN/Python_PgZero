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

# Classes

class Cat:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        self.current_frame = 0
        self.frame_timer = 0.0
        self.animation_speed = 0.2
        self.is_moving = False
        self.actor = Actor(FRAME_CAT0, (self.x, self.y))

    def moveUP(self):
        self.actor.y -= TILE_SIZE
        self.is_moving = True
        songs.play('move')
    
    def moveDOWN(self):
        self.actor.y += TILE_SIZE
        self.is_moving = True
    
    def moveRIGHT(self):
        self.actor.x += TILE_SIZE
        self.is_moving = True
    
    def moveLEFT(self):
        self.actor.x -= TILE_SIZE
        self.is_moving = True
    
    def update(self, dt):
        """Atualiza a lógica e a animação do gato."""
        self.animate(dt)
        if not self.is_moving:
            self.actor.image = FRAME_CAT0
    
    def animate(self, dt):
        """Gerencia a animação de sprite de caminhar."""
        if not self.is_moving:
            return

        self.frame_timer += dt
        
        if self.frame_timer >= self.animation_speed:
            # Alterna entre os dois sprites de caminhar
            if self.actor.image == FRAME_CAT1:
                self.actor.image = FRAME_CAT2
            else:
                self.actor.image = FRAME_CAT1
            
            self.frame_timer = 0.0
        
    def draw(self):
        """Desenha o gato na tela."""
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

hero = Cat(380, 380)
var0cg = hero

def init_game():
    global hero, score, fase, STATE
    hero = Cat(380, 380)
    score = 0
    STATE = 'PLAYING'
    music.play('backsong')

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

def on_key_down(key):
    """Gerencia eventos de teclado."""
    if key == keyboard.W or key == keyboard.UP:
        hero.moveUP()
    elif key == keyboard.S or key == keyboard.DOWN:
        hero.moveDOWN()
    elif key == keyboard.A or key == keyboard.LEFT:
        hero.moveLEFT()
    elif key == keyboard.D or key == keyboard.RIGHT:
        hero.moveRIGHT()
    
    hero.is_moving = True

def on_key_up(key):
    """Quando o jogador solta a tecla, o gato para de se mover."""
    hero.is_moving = False