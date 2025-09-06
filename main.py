import random

# Largura
WIDTH = 800
# Altura
HEIGHT = 400
# Quadrado
TILE_SIZE = 50

STATE = "MENU"
score = 0
level = 1
music_enable = True

# CORES
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_ASPHALT = (60, 60, 60)
COLOR_SIDEWALK = (180, 180, 180)
COLOR_LANE_LINE = (255, 255, 255, 100)
COLOR_MENU_BUTTON = (100, 100, 255)

# Sprite
FRAME_CAT0 = "cat"
FRAME_CAT1 = "cat_walk1"
FRAME_CAT2 = "cat_walk2"
CAT_INICIAL_POSITION = 380, 380
# CAT_INICIAL_POSITION = 540, 30 # for tests


# BOTOES
play_again_button = Rect((WIDTH / 2 - 100, HEIGHT / 2), (200, 50))
exit_button = Rect((WIDTH / 2 - 100, HEIGHT / 2 + 60), (200, 50))
play = Rect((WIDTH / 2 - 100, HEIGHT / 2), (200, 50))
back_menu_button = Rect((WIDTH / 2 - 100, HEIGHT / 2 + 120), (200, 50))

game_over_bg = Actor("gameoverbackground")
game_over_bg.pos = (WIDTH / 2, HEIGHT / 2)


def draw_game_over():
    game_over_bg.draw()
    screen.draw.text(
        "GAME OVER",
        center=(WIDTH / 2, HEIGHT / 2 - 100),
        fontsize=60,
        color=COLOR_WHITE,
    )
    screen.draw.filled_rect(play_again_button, COLOR_MENU_BUTTON)
    screen.draw.text(
        "PLAY AGAIN", center=play_again_button.center, fontsize=30, color=COLOR_WHITE
    )
    screen.draw.filled_rect(exit_button, COLOR_MENU_BUTTON)
    screen.draw.text("EXIT", center=exit_button.center, fontsize=30, color=COLOR_WHITE)
    screen.draw.filled_rect(back_menu_button, COLOR_MENU_BUTTON)
    screen.draw.text(
        "BACK TO MENU", center=back_menu_button.center, fontsize=30, color=COLOR_WHITE
    )


win_bg = Actor("winbackground")
win_bg.pos = pos = (WIDTH / 2, HEIGHT / 2)


def draw_win_screen():
    win_bg.draw()
    screen.draw.text(
        "YOU WIN!", center=(WIDTH / 2, HEIGHT / 2 - 100), fontsize=60, color=COLOR_WHITE
    )
    screen.draw.filled_rect(play_again_button, COLOR_MENU_BUTTON)
    screen.draw.text(
        "PLAY AGAIN", center=play_again_button.center, fontsize=30, color=COLOR_WHITE
    )
    screen.draw.filled_rect(exit_button, COLOR_MENU_BUTTON)
    screen.draw.text("EXIT", center=exit_button.center, fontsize=30, color=COLOR_WHITE)
    screen.draw.filled_rect(back_menu_button, COLOR_MENU_BUTTON)
    screen.draw.text(
        "BACK TO MENU", center=back_menu_button.center, fontsize=30, color=COLOR_WHITE
    )


menu_bg = Actor("menubackground")
menu_bg.pos = (WIDTH / 2, HEIGHT / 2)
volume_option_button = Actor("volume1")
volume_images = ["volume0", "volume1"]


def draw_menu_screen():
    menu_bg.draw()
    volume_option_button.draw()
    volume_option_button.pos = 700, 50

    screen.draw.text(
        "CAT AND RAT",
        center=(WIDTH / 2, HEIGHT / 2 - 100),
        fontsize=60,
        color=COLOR_WHITE,
    )
    screen.draw.filled_rect(play, COLOR_MENU_BUTTON)
    screen.draw.text("PLAY", center=play.center, fontsize=30, color=COLOR_WHITE)
    screen.draw.filled_rect(exit_button, COLOR_MENU_BUTTON)
    screen.draw.text("EXIT", center=exit_button.center, fontsize=30, color=COLOR_WHITE)


# Classes

TILE_SIZE_MOVE = 1


class Cat:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.frame_timer = 0.0
        self.animation_speed = 0.2
        self.is_moving = False
        self.actor = Actor(FRAME_CAT0)
        self.actor.pos = (self.x, self.y)
        self.direction = "up"

    def setDirection(self, new_direction: str):
        self.direction = new_direction

    def moveUP(self):
        self.actor.y -= TILE_SIZE_MOVE
        self.actor.angle = 0
        self.direction = "up"

    def moveDOWN(self):
        self.actor.y += TILE_SIZE_MOVE
        self.actor.angle = 180
        self.direction = "down"

    def moveRIGHT(self):
        self.actor.x += TILE_SIZE_MOVE
        self.actor.angle = 270
        self.direction = "right"

    def moveLEFT(self):
        self.actor.x -= TILE_SIZE_MOVE
        self.actor.angle = 90
        self.direction = "left"

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
        if self.is_moving:
            self.animate(dt)
        else:
            self.actor.image = FRAME_CAT0
            if self.direction == "up":
                self.actor.angle = 0
            elif self.direction == "down":
                self.actor.angle = 180
            elif self.direction == "right":
                self.actor.angle = 270
            elif self.direction == "left":
                self.actor.angle = 90

    def draw(self):
        self.actor.draw()


cars_imagens = ["car1", "car2", "car3", "car4"]
streets_right_direction = [(-100, 290), (-100, 210), (-100, 130)]
streets_left_direction = [(900, 295), (900, 210), (900, 125)]
all_cars = []


class Car:
    def __init__(self, via: int, x_start: int = None):

        self.via = via

        if self.via == 1:  # LEFT
            x, y = streets_left_direction[0]
        elif self.via == 2:  # RIGHT
            x, y = streets_right_direction[1]
        elif self.via == 3:  # LEFT
            x, y = streets_left_direction[2]

        self.x = x
        self.y = y
        self.image = random.choice(cars_imagens)
        self.actor = Actor(self.image)
        self.actor.pos = (self.x, self.y)
        self.speed = 0

        if x_start != None and x_start > 1000:
            self.actor.x = x_start

    def setSpeed(self, new_speed):
        self.speed = new_speed

    def moving(self):
        base_speed = 5

        if self.via == 2:
            self.actor.angle = 180
            self.actor.x += base_speed + self.speed
            if self.actor.left > WIDTH:
                self.actor.right = 0
                self.actor.image = random.choice(cars_imagens)
        else:
            self.actor.x -= base_speed + self.speed
            if self.actor.right < 0:
                self.actor.left = WIDTH
                self.actor.image = random.choice(cars_imagens)

    def update(self):
        self.moving()

    def draw(self):
        self.actor.draw()


MIN_CAR_DISTANCE = 200


def create_cars():
    all_cars.clear()

    patern = random.randint(1, 3)

    if patern == 1:
        car1 = Car(1)
        car2 = Car(2)
        car3 = Car(3)
        car4 = Car(3, x_start=1500)
        car5 = Car(1, x_start=600)
        all_cars.extend([car1, car2, car3, car4, car5])
    elif patern == 2:
        car1 = Car(2)
        car2 = Car(1, x_start=1400)
        car3 = Car(3)
        car4 = Car(2, x_start=400)
        car5 = Car(3, x_start=1500)
        car2.setSpeed(2)
        all_cars.extend([car1, car2, car3, car4])
    else:
        car1 = Car(1)
        car2 = Car(1, x_start=1300)
        car3 = Car(1, x_start=1000)
        car4 = Car(2)
        car5 = Car(3)
        car5.setSpeed(2)
        all_cars.extend([car1, car2, car3, car4, car5])


def check_collisions():
    global STATE, score, level
    for car in all_cars:
        if hero.actor.colliderect(car.actor):
            STATE = "GAME_OVER"
            if music_enable:
                sounds.crash.play()
                sounds.motor.stop()
            hero.setDirection("up")

    if hero.actor.colliderect(rat):
        score += 10
        level += 1
        hero.actor.pos = CAT_INICIAL_POSITION

        if level >= 4:
            STATE = "WIN"
            if music_enable:
                sounds.motor.stop()
                sounds.win.play()
        else:
            new_speed_bonus = level - 1
            for car in all_cars:
                car.setSpeed(new_speed_bonus)


def on_mouse_down(pos, button):

    global STATE, music_enable

    if STATE == "MENU":

        if play.collidepoint(pos):
            init_game()

        if exit_button.collidepoint(pos):
            exit()

        if volume_option_button.collidepoint(pos):
            music_enable = not music_enable
            if music_enable:
                volume_option_button.image = volume_images[1]
            else:
                volume_option_button.image = volume_images[0]

    elif STATE == "GAME_OVER" or STATE == "WIN":
        if play_again_button.collidepoint(pos):
            init_game()  # Reinicia o jogo

        if exit_button.collidepoint(pos):
            if music_enable:
                sounds.motor.stop()
                sounds.win.stop
            exit()  # Fecha o jogo

        if back_menu_button.collidepoint(pos):
            if music_enable:
                sounds.motor.stop()
                sounds.win.stop()
            STATE = "MENU"

    """
    # FUNÇÃO AUXILIAR
    x, y = pos
    # Imprime os valores de x e y
    print(f"Clique em X: {x}, Y: {y}")
    """

    if button == mouse.LEFT and hero.actor.collidepoint(pos):
        print("aw")
        if music_enable:
            sounds.catcrash.play()
    else:
        print("You missed me")


# Hero
hero = Cat(380, 380)
# Villains
create_cars()
var0cg = hero
# RAT
RAT_FRAMES_LEFT = ["rat", "rat1"]
RAT_FRAMES_RIGHT = ["rat_right", "rat1_right"]
rat = Actor(RAT_FRAMES_LEFT[0])
rat.pos = (380, 30)
rat_speed_x = 1
rat_frame_timer = 0.0
RAT_ANIMATION_SPEED = 0.08
RAT_RIGHT_LIMIT = 460
RAT_LEFT_LIMIT = 300


def update_rat(dt):
    global rat_speed_x, rat_frame_timer

    rat.x += rat_speed_x

    if rat.right > RAT_RIGHT_LIMIT or rat.left < RAT_LEFT_LIMIT:
        rat_speed_x *= -1

    active_frames = []
    if rat_speed_x > 0:
        active_frames = RAT_FRAMES_RIGHT
    else:
        active_frames = RAT_FRAMES_LEFT

    rat_frame_timer += dt
    if rat_frame_timer >= RAT_ANIMATION_SPEED:
        if rat.image == active_frames[0]:
            rat.image = active_frames[1]
        else:
            rat.image = active_frames[0]

        rat_frame_timer = 0.0


def init_game():
    global score, level, STATE
    score = 0
    level = 1
    hero.actor.pos = CAT_INICIAL_POSITION
    create_cars()
    if music_enable:
        sounds.motor.play(-1)
    STATE = "PLAYING"


def check_boundaries():
    if hero.actor.top < 0:
        hero.actor.top = 0

    if hero.actor.bottom > HEIGHT:
        hero.actor.bottom = HEIGHT

    if hero.actor.right < 0:
        hero.actor.left = WIDTH

    if hero.actor.left > WIDTH:
        hero.actor.right = 0


cover = Actor("cover")
cover.pos = 160, 125
sidewalk_above = Actor("sidewalk")
sidewalk_below = Actor("sidewalk")
sidewalk_above.topleft = 0, 0
sidewalk_below.topleft = 0, HEIGHT - TILE_SIZE
three = Actor("three")
three.pos = 80, 360
hydrant = Actor("hydrant")
hydrant.pos = 690, 25


def draw():

    #  =========================== SCENARIO ===========================

    sidewalk_above.draw()
    sidewalk_below.draw()
    STREET_HEIGHT = 310  # altura da via
    STREET_WIDTH = 800  # largura da via
    STREET_Y = 50
    STREET_X = 0
    screen.draw.filled_rect(
        Rect(STREET_X, STREET_Y, STREET_WIDTH, STREET_HEIGHT), COLOR_ASPHALT
    )  # street

    LINE_Y = 80
    LINE_X = 0
    LINE_WIDTH = 50  # largura faixa
    STREET_HEIGHT = 5  # altura faixa

    for j in range(4):
        new_line_y = LINE_Y * j + TILE_SIZE + 35
        for i in range(6):
            new_line_x = LINE_X + (i * 150)
            screen.draw.filled_rect(
                Rect(new_line_x, new_line_y, LINE_WIDTH, STREET_HEIGHT), COLOR_WHITE
            )
        j += 100

    cover.draw()
    screen.draw.filled_rect(Rect(0, 85, 800, 5), COLOR_WHITE)
    screen.draw.filled_rect(Rect(0, 325, 800, 5), COLOR_WHITE)

    # =================================================================

    rat.draw()
    hero.draw()
    three.draw()
    hydrant.draw()

    for car in all_cars:
        car.draw()

    screen.draw.text(
        f"Score: {score}   Level: {level}", (10, 10), fontsize=30, color=COLOR_WHITE
    )

    if STATE == "GAME_OVER":
        draw_game_over()
    elif STATE == "WIN":
        draw_win_screen()
    elif STATE == "MENU":
        draw_menu_screen()


def update(dt):
    if STATE == "PLAYING":
        update_rat(dt)
        for car in all_cars:
            car.update()

        # === HERO MOVIE ===
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

        # PHYSIC
        check_boundaries()
        check_collisions()
