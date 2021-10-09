import pygame
import os, time, random

from pygame import mixer

pygame.font.init() #Importo para pdoer usar fuentes

#Voy a crear las propiedades de la ventana
WIDTH, HEIGHT = 800, 600 #El tamaño de X e Y
WIN = pygame.display.set_mode(((WIDTH, HEIGHT)))
pygame.display.set_caption("Carpinchometro") #Seteo el titulo de la ventana

#Cargo las imagenes del personaje
PLAYER = pygame.image.load(os.path.join("images/carpincho", "carpincho-1.png"))

#Cargo las imagenes del carpincho corriendo (190px x 190px)
CARPI_1 = pygame.image.load(os.path.join("images/carpincho", "carpincho-1.png"))
CARPI_2 = pygame.image.load(os.path.join("images/carpincho", "carpincho-2.png"))
CARPI_3 = pygame.image.load(os.path.join("images/carpincho", "carpincho-3.png"))
CARPI_4 = pygame.image.load(os.path.join("images/carpincho", "carpincho-4.png"))
CARPI_5 = pygame.image.load(os.path.join("images/carpincho", "carpincho-5.png"))


#Cargo imagen del background
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("images/background", "back.png")), (WIDTH, HEIGHT)) #Escalo la imagen del BG para que siempre se adapten a la pantalla
#Clase del personaje
class Character:
    def __init__(self, x, y, health = 100):
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
    def __init__(self, x, y, health=100): #Default vida maxima
        super().__init__(x, y, health=health)
        self.character_img = PLAYER
        self.mask = pygame.mask.from_surface(self.character_img) #Crea mascara de colision sobre el personaje
        self.max_healt = health #Para saber la vida maxima del jugador

class Enemy(Character): #Clase para los carpinchos

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.character_img = CARPI_1
        self.mask = pygame.mask.from_surface(self.character_img) #Mascara del carpincho

    def move(self, vel):
            self.x -= vel

#Colores fuentes
FONT_RED = (252, 3, 69)

def main():
    run = True  #Mantiene la ventana abierta mientras sea True
    FPS = 60    #Seteo la velocidad de fotogramas
    level = 0   #Nivel
    lives = 5   #Vida
    main_font = pygame.font.SysFont("comicsans", 50)    #Fuente

    enemies = []
    enemy_vel = 5   #Velocidad del enemigo
    wave_lenght = 0 #Tamaño de la ola

    player_vel = 5
    player = Player( (WIDTH/2)-95, (HEIGHT - 190)) #Posiciono al personaje en X,Y (Si tiene 190px x 190x)
    
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BACKGROUND, (0,0)) #Coloco el BG

        #Escribo el texto de la vida
        lives_label = main_font.render(f"Vidas: {lives}", 1, FONT_RED)
        level_label = main_font.render(f"Nivel: {level}", 1, FONT_RED)
        WIN.blit(lives_label, (10, 10)), WIN.blit(level_label, (WIDTH - lives_label.get_width() - 10, 10))  #Ancho de la pantalla - ancho de palabra - 10

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        pygame.display.update() #Updatea la pantalla

    while run:
            clock.tick(FPS)

            if len(enemies) == 0:
                level += 1
                wave_lenght += 0

                enemy = Enemy(WIDTH, (HEIGHT / 2) - 95) #Spawn del enemigo
                enemies.append(enemy)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False #Cambio el run a False, para que se cierre el juego

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

            redraw_window() #llamo a la funcion para updatear la pantalla
main()