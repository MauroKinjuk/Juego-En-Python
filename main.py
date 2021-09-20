import pygame
import os, time, random
pygame.font.init() #Importo para pdoer usar fuentes

#Voy a crear las propiedades de la ventana
WIDTH, HEIGHT = 800, 600 #El tamaño de X e Y
WIN = pygame.display.set_mode(((WIDTH, HEIGHT)))
pygame.display.set_caption("Un jueguito") #Seteo el titulo de la ventana

#Cargo las imagenes del personaje
TOM_1 = pygame.transform.scale(pygame.image.load(os.path.join("images/tom", "tom-1.png")), (120, 120))
TOM_2 = pygame.image.load(os.path.join("images/tom", "tom-2.png"))
TOM_2 = pygame.image.load(os.path.join("images/tom", "tom-3.png"))

#Cargo la imagen del fondo
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("images/background", "background-2.png")), (WIDTH*2, HEIGHT)) #Escalo la imagen de BG al tamaño de la pantalla

#Colores (RED, GREEN, BLUE) (RGB)
FONT_RED = (252, 3, 69)

#Clase del personaje
class Character:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.character_img = None
        self.cool_down_counter = 0
        

    def draw(self, window):
        window.blit(self.character_img, (self.x, self.y))

class Player(Character):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health=health)
        self.character_img = TOM_1
        self.mask = pygame.mask.from_surface(self.character_img) #Crea una mascara de pixel (Permite hacer colisiones)
        self.max_healt = health #Lo utilizamos para saber cual es la vida maxima que tenga el jugador



def main():
    run = True #Mantiene la ventana abierta mientras este en True
    FPS = 60 #Los fps
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    clock = pygame.time.Clock()

    player_vel = 5 #Velocidad max en la que se va a mover un personaje al presionar una tecla

    character = Player(350, 420) #Posiciono el personaje X,Y

    def redraw_window(): 
        WIN.blit(BACKGROUND, (0,0)) #Coloco el BG
         
        #Escribo el texto de nivel y vida
        lives_label = main_font.render(f"Vidas: {lives}", 1, FONT_RED)
        level_lebel = main_font.render(f"Nivel: {level}", 1, FONT_RED)
        WIN.blit(lives_label, (10 , 10)), WIN.blit(level_lebel, (WIDTH - lives_label.get_width() - 10, 10)) #Ancho de la pantalla - ancho de la palabra - 10
        
        character.draw(WIN) #Llamo al personaje

        pygame.display.update() #Updatea la pantalla

    while run:
        clock.tick(FPS)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #Cuando el usuario preciona el boton de cerrar (X)
                run = False #Cambio para que se cierre la ventana
        
        keys = pygame.key.get_pressed() #Declaro la variable que detecta las teclas presionadas
        if keys[pygame.K_a] or keys[pygame.K_LEFT] and character.x - player_vel > 0: #Tecla a que va hacia la izquierda
            character.x -= player_vel 
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and character.x +  player_vel + 50 < WIDTH: #Derecha (Despues del and compruebo que el character no pase los bordes de las ventanas)
            character.x += player_vel
        if keys[pygame.K_w] or keys[pygame.K_UP] and character.y +  player_vel + 50 > 0: #Arriba
            character.y -= player_vel
        if keys[pygame.K_s] or keys[pygame.K_DOWN] and character.y +  player_vel + 50 < (HEIGHT - 100): #Arriba
            character.y += player_vel

        redraw_window() #llamo a la funcion para updatear la pantalla

main() #Llamo a la funcion Main par iniciar el juego