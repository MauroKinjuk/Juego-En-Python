import pygame
import os, time, random
pygame.font.init() #Importo para pdoer usar fuentes

#Voy a crear las propiedades de la ventana
WIDTH, HEIGHT = 800, 600 #El tamaño de X e Y
WIN = pygame.display.set_mode(((WIDTH, HEIGHT)))
pygame.display.set_caption("Un jueguito") #Seteo el titulo de la ventana

#Cargo las imagenes del personaje
TOM_1 = pygame.image.load(os.path.join("images/tom", "tom-1.png"))
TOM_2 = pygame.image.load(os.path.join("images/tom", "tom-2.png"))
TOM_2 = pygame.image.load(os.path.join("images/tom", "tom-3.png"))

#Cargo la imagen del fondo
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("images/background", "background.jpg")), (WIDTH, HEIGHT)) #Escalo la imagen de BG al tamaño de la pantalla

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
        pygame.draw.rect(window, FONT_RED, (self.x, self.y, 50, 50))


def main():
    run = True #Mantiene la ventana abierta mientras este en True
    FPS = 60 #Los fps
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    clock = pygame.time.Clock()

    character = Character(350, 350) #Posiciono el personaje

    def redraw_window(): 
        WIN.blit(BACKGROUND, (0,0)) #Coloco el BG

        #Escribo el texto de nivel y vida
        lives_label = main_font.render(f"Nivel: {lives}", 1, FONT_RED)
        level_lebel = main_font.render(f"Nivel: {level}", 1, FONT_RED)
        WIN.blit(lives_label, (10 , 10)), WIN.blit(level_lebel, (WIDTH - lives_label.get_width() - 10, 10)) #Ancho de la pantalla - ancho de la palabra - 10
        
        character.draw(WIN) #Llamo al personaje

        pygame.display.update() #Updatea la pantalla

    while run:
        clock.tick(FPS)
        redraw_window() #llamo a la funcion para updatear la pantalla

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: #Cuando el usuario preciona el boton de cerrar (X)
                run = False #Cambio para que se cierre la ventana

main()