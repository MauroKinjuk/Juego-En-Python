import pygame, sys
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
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

def main():
    #Parametros basicos
    run = True  #Mantiene la ventana abierta mientras sea True
    FPS = 60    #Seteo la velocidad de fotogramas
    level = 1   #Nivel
    hearths = 2 #Vidas
    health_player = 100 #Vida jugador

    speed_enemy = 3

    #Defino y añado el grupo de enemigos y jugador
    player = Player(health_player)
    player_group.add(player)
    enemy = Enemy(speed_enemy)
    enemy_group.add(enemy)

    #Fuentes
    main_font = pygame.font.SysFont("comicsans", 50)    #Fuente Principal
    lost_font = pygame.font.SysFont("comicsans", 60)    #Fuente de Muerte

    #Metodo para refrescar la pantalla
    def redraw_window():
        #Dibujo en pantalla
        screen.blit(background, (0,0))  #Background

        #Defino y dibujo las palabras en pantalla
        lives_label = main_font.render(f"Vidas: {hearths}", 1, (255,255,255))
        level_label = main_font.render(f"Nivel: {level}", 1, (255,255,255))
        screen.blit(lives_label,(10,10)), screen.blit(level_label, (screen_width - lives_label.get_width() - 10, 10))

        #Agrego los enemigos
        enemy_group.update(0.15)
        enemy_group.draw(screen)
        
        #Agrego al jugador
        player_group.update(0.2)
        player_group.draw(screen)

        #Refresco la pantalla
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        #Detecto cuando se presionan las teclas del jugador
        player.get_input()

        #Detecto cuando se cierra la pantalla
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()    

        #Agrego colisiones
        colision = pygame.sprite.spritecollide(player, enemy_group, False, pygame.sprite.collide_mask)

        for i in colision:

            #Si el nivel es mayor a 0
            if level > 0:
                level -= 1  #Resto 1 nivel
                if speed_enemy > 3: #Si la velocidad del enemigo es mayor a 3
                    speed_enemy -= 1

            if health_player > 0:
                    health_player -= 50
                    if health_player == 0:
                        hearths -= 1
                        health_player = 100
            else:
                hearths -= 1
                health_player = 100
                if hearths <= 0:
                    pygame.quit()
            
            print (health_player)

            enemy_group.remove(i)   #Remuevo i del grupo de enemigos
            new_enemy = Enemy(speed_enemy)     #Nueva variable para spawn de enemigos
            enemy_group.add(new_enemy)  #Agrego el nuevo spawn al grupo de enemigos
            enemy_group.update(0.15)    #Le hago un update



main()