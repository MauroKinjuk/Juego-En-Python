import pygame
from enemy import Enemy
from player import Player
from logic import check_collision, check_level

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

    #Defino y añado el grupo de enemigos y jugador
    player = Player()
    player_group.add(player)
    enemy = Enemy()
    enemy_group.add(enemy)

    #Fuentes
    main_font = pygame.font.SysFont("comicsans", 50)    #Fuente Principal
    lost_font = pygame.font.SysFont("comicsans", 60)    #Fuente de Muerte

    #Metodo para refrescar la pantalla
    def redraw_window():
        #Dibujo en pantalla
        screen.blit(background, (0,0))  #Background

        #Defino y dibujo las palabras en pantalla
        lives_label = main_font.render(f"Vidas: {player.lives}", 1, (255,255,255))
        level_label = main_font.render(f"Nivel: {player.level}", 1, (255,255,255))
        screen.blit(lives_label,(10,10)), screen.blit(level_label, (screen_width - lives_label.get_width() - 10, 10))

        #Agrego los enemigos
        enemy_group.update(0.15)
        enemy_group.draw(screen)
        
        #Agrego al jugador
        player_group.update(0.2, screen)
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
                run = False

        #Checkeo las colisiones
        check_collision(player, enemy_group)    #Le paso el jugador y el grupo de enemigos
        check_level(player, enemy_group)    #Compruebo cuando el jugador pasa la pantalla

main()