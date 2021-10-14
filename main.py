import pygame, sys, random, os
from enemy import *
from player import *

#Inicializador
pygame.init()
clock = pygame.time.Clock()

#Pantalla del juego
screen_width = 800  #Ancho
screen_height = 600 #Alto
screen = pygame.display.set_mode((screen_width, screen_height)) 
background = pygame.transform.scale(pygame.image.load("bg.png"), (screen_width, screen_height)) #Seteo el fondo, escalandolo al tamaño de la pantalla
pygame.display.set_caption("Carpinchometro")

#Grupos de sprites
moving_sprites = pygame.sprite.Group()

def main():
    #Parametros basicos
    run = True  #Mantiene la ventana abierta mientras sea True
    FPS = 60    #Seteo la velocidad de fotogramas
    level = 1
    hearths = 2

    #Parametros enemigo
    enemies = []

    #Fuentes
    main_font = pygame.font.SysFont("comicsans", 50)    #Fuente Principal
    lost_font = pygame.font.SysFont("comicsans", 60)    #Fuente de Muerte

    #Enemigo
    enemy = Enemy(screen_width, random.randrange(0, (screen_height - 190)))
    moving_sprites.add(enemy)  #Para agregar el enemigo

    #Coloco al jugador
    player = Player((screen_width // 2) - 95, (screen_height - 210))
    moving_sprites.add(player)

    #Colisiones
    #sprites_hits = pygame.sprite.spritecollide(player, enemy, True)

    while run:

        #Dibujo en pantalla
        screen.blit(background, (0,0))  #Background

        #Parametros de sprites
        moving_sprites.draw(screen) #Hago que se dibuje el sprite
        moving_sprites.update(0.2)  #Hago que el sprite se mueva a cierta velocidad

        #Detecto cuando se cierra la pantalla
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Detecto cuando se presionan las teclas del jugador
        player.get_input()

        #Spawn del enemigo
        if len (enemies) == 0:
              enemies.append(enemy)
              
        for enemy in enemies[:]:
            enemy.animate() #llamo a la funcion que anima y mueve al enemigo


            

        pygame.display.update()
        clock.tick(FPS)

main()