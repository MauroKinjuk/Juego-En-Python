import pygame
import os, time, random
from pygame import mixer #Mixer para el audio
pygame.font.init() #Importo para pdoer usar fuentes

#Voy a crear las propiedades de la ventana
WIDTH, HEIGHT = 800, 600 #El tamaño de X e Y
WIN = pygame.display.set_mode(((WIDTH, HEIGHT)))
pygame.display.set_caption("Un jueguito") #Seteo el titulo de la ventana

#Cargo las imagenes del personaje
TOM_1 = pygame.transform.scale(pygame.image.load(os.path.join("images/tom", "tom-1.png")), (120, 120))
TOM_2 = pygame.image.load(os.path.join("images/tom", "tom-2.png"))
TOM_2 = pygame.image.load(os.path.join("images/tom", "tom-3.png"))

#Cargo imagenes del enemigo
ENEMY_1 = pygame.transform.scale(pygame.image.load(os.path.join("images/enemy", "enemy-1.png")), (120, 120))
ENEMY_2 = pygame.transform.scale(pygame.image.load(os.path.join("images/enemy", "enemy-2.png")), (120, 120))
ENEMY_3 = pygame.transform.scale(pygame.image.load(os.path.join("images/enemy", "enemy-3.png")), (120, 120))
ENEMY_4 = pygame.transform.scale(pygame.image.load(os.path.join("images/enemy", "enemy-4.png")), (120, 120))

#Cargo lasers o disparos
LASER_BLUE = pygame.image.load(os.path.join("images/disparos", "pixel_laser_blue.png"))
LASER_GREEN = pygame.image.load(os.path.join("images/disparos", "pixel_laser_green.png"))
LASER_RED = pygame.image.load(os.path.join("images/disparos", "pixel_laser_red.png"))
LASER_YELLOW = pygame.image.load(os.path.join("images/disparos", "pixel_laser_yellow.png"))

#Cargo la imagen del fondo
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("images/background", "background-2.png")), (WIDTH*2, HEIGHT)) #Escalo la imagen de BG al tamaño de la pantalla

#Colores (RED, GREEN, BLUE) (RGB)
FONT_RED = (252, 3, 69)

#Cargo la musica
pygame.init()
pygame.mixer.music.set_volume(0.2) #Seteo el volumen
backgroud_music = mixer.music.load("music/battle.wav")
mixer.music.play(-1)

#Clase del personaje
class Character:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.character_img = None
        self.laser_img = None
        self.laser = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.character_img, (self.x, self.y))

    def get_width(self):
        return self.character_img.get_width()   #Obtengo el tamaño del personaje

    def get_height(self):
        return self.character_img.get_height()  #Obtengo el tamaño del personaje

class Player(Character):
    def __init__(self, x, y, health = 100): #Default vida maxima
        super().__init__(x, y, health=health) #Inicializa todo lo que esta en Character
        self.character_img = TOM_1
        self.laser_img = LASER_RED #Le asigno un laser o disparo al jugador
        self.mask = pygame.mask.from_surface(self.character_img) #Crea una mascara de pixel (Permite hacer colisiones)
        self.max_healt = health #Lo utilizamos para saber cual es la vida maxima que tenga el jugador

class Enemy(Character):

    #Hago un mapa de colores de enemigos con sus disparos
    COLOR_MAP = {
                "blue": (ENEMY_1, LASER_BLUE),
                "green": (ENEMY_2, LASER_GREEN),
                "yellow": (ENEMY_3, LASER_YELLOW)
                }

    def __init__(self, x, y, color, health = 100):
        super().__init__(x, y, health)
        self.character_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.character_img) #Crea una mascara de pixel (Permite hacer colisiones)

    def move(self, vel):    #El movimiento para enemigos
        self.y += vel

def main():
    run = True #Mantiene la ventana abierta mientras este en True
    FPS = 60 #Los fps
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    enemies = []
    enemy_vel = 1
    wave_lenght = 5 #El tamaño para la ola de enemigos

    player_vel = 5 #Velocidad max en la que se va a mover un personaje al presionar una tecla

    player = Player(350, 420) #Posiciono el personaje X,Y

    clock = pygame.time.Clock()

    def redraw_window(): 
        WIN.blit(BACKGROUND, (0,0)) #Coloco el BG
         
        #Escribo el texto de nivel y vida
        lives_label = main_font.render(f"Vidas: {lives}", 1, FONT_RED)
        level_lebel = main_font.render(f"Nivel: {level}", 1, FONT_RED)
        WIN.blit(lives_label, (10 , 10)), WIN.blit(level_lebel, (WIDTH - lives_label.get_width() - 10, 10)) #Ancho de la pantalla - ancho de la palabra - 10
        
        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN) #Llamo al personaje

        pygame.display.update() #Updatea la pantalla

    while run:
        clock.tick(FPS)
        redraw_window() #llamo a la funcion para updatear la pantalla

        if len(enemies) == 0:   #Compruebo que cuando no hay mas enemigos subo el nivel
            level += 1
            wave_lenght += 5
            for i in range(wave_lenght):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1000, -100), random.choice(["blue", "green", "yellow"]))
                enemies.append(enemy)
            
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #Cuando el usuario preciona el boton de cerrar (X)
                run = False #Cambio para que se cierre la ventana
        
        keys = pygame.key.get_pressed() #Declaro la variable que detecta las teclas presionadas
        if keys[pygame.K_a] or keys[pygame.K_LEFT] and player.x - player_vel > 0: #Tecla a que va hacia la izquierda
            player.x -= player_vel 
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player.x +  player_vel + player.get_width() < WIDTH: #Derecha (Despues del and compruebo que el character no pase los bordes de las ventanas)
            player.x += player_vel
        if keys[pygame.K_w] or keys[pygame.K_UP] and player.y - player_vel > 0: #Arriba
            player.y -= player_vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN] and player.y +  player_vel + (player.get_height() + 30) < HEIGHT: #Abajo
            player.y += player_vel

        #Movimiento enemigos
        for enemy in enemies:
            enemy.move(enemy_vel)


main() #Llamo a la funcion Main par iniciar el juego