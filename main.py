import pygame
from enemy import Enemy
from player import Player
from logic import check_collision, check_level
from game import Game   #importamos la clase Game del archivo game


#Inicializador
pygame.init()
clock = pygame.time.Clock()
g = Game()  #creamos una variable para inicializar la clase Game

#Pantalla del juego
carpincho = pygame.image.load("carpincho/izquierda/1.png") #Agrego imagen para la pantalla de game over
background = pygame.transform.scale(pygame.image.load("bg.png"), (g.DISPLAY_W, g.DISPLAY_H)) #Seteo el fondo, escalandolo al tamaño de la pantalla
pygame.display.set_caption("Carpinchometro") 

#Grupos de sprites
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

def main():
    #Parametros basicos
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
        g.window.blit(background, (0,0))  #Background

        #Defino y dibujo las palabras en pantalla
        lives_label = main_font.render(f"Vidas: {player.lives}", 1, (255,255,255))
        level_label = main_font.render(f"Nivel: {player.level}", 1, (255,255,255))
        g.window.blit(lives_label,(10,10)), g.window.blit(level_label, (g.DISPLAY_W - lives_label.get_width() - 10, 10))

        #Agrego los enemigos
        enemy_group.update(0.1)
        enemy_group.draw(g.window)
        
        #Agrego al jugador
        player_group.update(0.1, g.window)
        player_group.draw(g.window)

        #Refresco la pantalla
        pygame.display.update()

    def gameover_window():
        #Dibujo en pantalla
        g.window.blit(background, (0,0)) #Fijo el fondo
        death_label = lost_font.render("No has podido evitar al carpincho",1,(30,30,30)) #Muestro mensaje de muerte
        score_label = lost_font.render(f"Has llegado al nivel: {player.level+1}",1,(30,30,30)) #Muestro hasta que nivel llego el jugador
        restart_label = lost_font.render("Toca cualquier flecha para reiniciar",1,(30,30,30)) #Muestro instrucciones para reinicio
        g.window.blit(carpincho,(300,500))
        g.window.blit(death_label,(50,g.DISPLAY_H // 2-100)), g.window.blit(score_label,(180,g.DISPLAY_H//2-50)), g.window.blit(restart_label,(30,g.DISPLAY_H//2))
        #Refresco la pantalla
        pygame.display.update()

    #to.do: si se agrega sonido hacer que dependa de la variable g.sound (boolean)
    while g.running:
        clock.tick(FPS)
        g.curr_menu.display_menu()  #despliego el menu

        while g.playing and player.lives > 0:
            redraw_window()

            #Detecto cuando se presionan las teclas del jugador
            if(g.diestro):
                player.get_input()
            if(g.zurdo):
                player.get_input_wasd()

            #Checkeo las colisiones
            check_collision(player, enemy_group)    #Le paso el jugador y el grupo de enemigos
            check_level(player, enemy_group)    #Compruebo cuando el jugador pasa la pantalla

            #Detecto cuando se cierra la pantalla
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    g.running, g.playing = False, False  
                    g.curr_menu.run_display = False 
                 
        while(player.lives <= 0): #Check si el jugador tiene 0 vidas, si es asi, el if con el juego no va ocurrir
            gameover_window() #Muestro la pantalla de game over
            if event.type == pygame.KEYDOWN: 
                player.lives = 2
                player.level = 0
                player.rect.x = (800 // 2) - 95 #Coloco al jugador en el centro de la pantalla
                player.rect.y = 600 - 170
                enemy_group.empty() #Elimino enemigos para evitar que el juego empieze con enemigos ya en el medio de la pantalla
                new_enemy = Enemy()
                enemy_group.add(new_enemy) #Agrego nuevos enemigos para que funcione todo correctamente
                g.playing = False
            
            #Detecto cuando se cierra la pantalla
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:  
                    g.running, g.playing = False, False  
                    g.curr_menu.run_display = False 
            
main()