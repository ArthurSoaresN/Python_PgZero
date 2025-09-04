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

cat = Actor('cat')
CAT_INICIAL_POSITION = [380, 380]
cat.pos = CAT_INICIAL_POSITION

# CORES
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_ASPHALT = (60, 60, 60)
COLOR_SIDEWALK = (180, 180, 180)
COLOR_LANE_LINE = (255, 255, 255, 100) # Faixa de pedestres
COLOR_MENU_BUTTON = (100, 100, 255)

# Classes

class Cat:
    pass

FRAME_CAT1 = ''
FRAME_CAT2= ''

def on_mouse_down(pos, button):

    """Gerencia eventos de clique do mouse e armazena a posição."""
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

def draw():

    screen.draw.filled_rect(Rect(0, 0, WIDTH, TILE_SIZE), COLOR_SIDEWALK) # sidewalk from above
    screen.draw.filled_rect(Rect(0, HEIGHT - TILE_SIZE, WIDTH, TILE_SIZE), COLOR_SIDEWALK) # sidewalk from below

    STREET_HEIGHT = 300 # altura da via
    STREET_WIDTH = 800 # largura da via
    STREET_Y = 50
    STREET_X = 0
    screen.draw.filled_rect(Rect(STREET_X, STREET_Y, STREET_WIDTH, STREET_HEIGHT), COLOR_ASPHALT)

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

    
        

    screen.draw.text(f"Score: {score}   Fase: {fase}", (10, 10), fontsize=30, color=COLOR_WHITE)
    cat.draw()

def update():
    pass