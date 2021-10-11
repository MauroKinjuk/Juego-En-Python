#-----------------------------------------
#       TO DO:
#   *Corregir spawn al azar de carpinchos
#   *Agregar Menu  -----LISTO
#   *Animacion carpincho
#   *Mas cosas
#-----------------------------------------

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
#carpi = [
#    pygame.image.load(os.path.join("images/carpincho", "carpincho-1.png")),
#    pygame.image.load(os.path.join("images/carpincho", "carpincho-2.png")),
#    pygame.image.load(os.path.join("images/carpincho", "carpincho-3.png")),
#    pygame.image.load(os.path.join("images/carpincho", "carpincho-4.png")),
#    pygame.image.load(os.path.join("images/carpincho", "carpincho-5.png"))
#    ]

carpi_move = False
#Colores fuentes
FONT_RED = (252, 3, 69)


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
        self.max_health = health #Para saber la vida maxima del jugador

    #Barra de salud
    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.character_img.get_height() + 10, self.character_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.character_img.get_height() + 10, self.character_img.get_width() * (self.health/self.max_health), 10))

class Enemy(Character): #Clase para los carpinchos

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.character_img = CARPI_1
        self.mask = pygame.mask.from_surface(self.character_img) #Mascara del carpincho

    def move(self, vel):
            self.x -= vel

#Def de colisiones
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None #Si las mascaras de los objetos se superponen devuelven posiciones (x, y)

def main():
    run = True  #Mantiene la ventana abierta mientras sea True
    FPS = 60    #Seteo la velocidad de fotogramas
    level = 1   #Nivel
    lives = 5   #Vida
    main_font = pygame.font.SysFont("comicsans", 50)    #Fuente Principal
    lost_font = pygame.font.SysFont("comicsans", 60)    #Fuente de Muerte

    enemies = []
    enemy_vel = 5   #Velocidad del enemigo
    wave_lenght = 1 #Tamaño de la ola

    player_vel = 5
    player = Player( (WIDTH//2)-95, (HEIGHT - 210)) #Posiciono al personaje en X,Y (Si tiene 190px x 190x)
    
    clock = pygame.time.Clock()

    lost = False #Variable que cambia si se pierde
    lost_count = 0

    def redraw_window():
        WIN.blit(BACKGROUND, (0,0)) #Coloco el BG

        #Escribo el texto de la vida
        lives_label = main_font.render(f"Vidas: {lives}", 1, FONT_RED)
        level_label = main_font.render(f"Nivel: {level}", 1, FONT_RED)
        WIN.blit(lives_label, (10, 10)), WIN.blit(level_label, (WIDTH - lives_label.get_width() - 10, 10))  #Ancho de la pantalla - ancho de palabra - 10

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("Te mató el carpincho", 1, FONT_RED)  #Texto si perdemos
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))     #Posiciono el texto

        pygame.display.update() #Updatea la pantalla

    while run:
            clock.tick(FPS)
            redraw_window() #Llamo a la funcion para updatear la pantalla

            #Detecta cuando la vida o vida del jugador es 0
            if lives <= 0 or player.health <= 0:
                lost = True
                lost_count += 1

            #Si perdemos, vamos a tener un tiempo para mostar el mensaje
            if lost:
                if lost_count > FPS * 3:
                    run = False
                else:
                    continue

            if len(enemies) == 0:
                #Comento esto, ya que puede ser util
                #level += 1
                #enemy_vel += 1
                #wave_lenght += 1

                enemy = Enemy(WIDTH, random.randrange(0,(HEIGHT - 380))) #Spawn del enemigo
                enemies.append(enemy)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit() #Utilizo quit para borrar el error del menu al cerrar el juego

            keys = pygame.key.get_pressed() #Declaro la variable que detecta las teclas presionadas
            if keys[pygame.K_a] or keys[pygame.K_LEFT] and player.x - player_vel > 0: #Tecla a que va hacia la izquierda
                player.x -= player_vel 
            if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player.x +  player_vel + player.get_width() < WIDTH: #Derecha (Despues del and compruebo que el character no pase los bordes de las ventanas)
                player.x += player_vel
            if keys[pygame.K_w] or keys[pygame.K_UP]: #Arriba
                player.y -= player_vel
            if keys[pygame.K_s] or keys[pygame.K_DOWN] and player.y +  player_vel + player.get_height() + 15 < HEIGHT: #Abajo
                player.y += player_vel

            #Detectar si el jugador sale de la pantalla arriba
            if player.y - player_vel <= 0:
                level += 1
                player.x = (WIDTH//2)-95
                player.y = HEIGHT - 210
                enemy_vel += 1
                #wave_lenght += 1

            #Movimiento enemigos
            for enemy in enemies[:]:
                enemy.move(enemy_vel)

                #Si colisionas los objetos
                if collide(enemy, player):
                    player.health -= 10
                    player.x = (WIDTH//2)-95
                    player.y = HEIGHT - 210
                    enemies.remove(enemy)
                    if level > 0:
                        level -= 1
                elif enemy.x + enemy.get_width() <= 0:#Si el enemigo se va de la pantalla
                    enemies.remove(enemy)

#Menu principal
def main_menu():
    title_font = pygame.font.SysFont("comicsans", 50)   #Fuente del titulo principal
    run = True

    while run:
        WIN.blit(BACKGROUND, (0,0))
        title_label = title_font.render("Presiona un boton del mouse para iniciar...",1, FONT_RED)
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, HEIGHT/2))  #Posicion texto principal

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:    #Si se preciona cualquier boton del mouse, empieza el juego
                main()

    pygame.quit()
    
main_menu() #Llamo al menu principal para iniciar el juego