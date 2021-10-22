import pygame, sys
from enemy import Enemy

def check_collision(player, enemy_group):

    #Voy a explicar las colisiones aca, de manera detallada, asi se entiende de una mejor manera

    colision = pygame.sprite.spritecollide(player, enemy_group, False, pygame.sprite.collide_mask)

    for i in colision:
        if player.health > 0:   #Si colisionan y el jugador tiene vida
            player.health -= 50 #Le resto 50 de vida
            if player.health == 0:  #Si la vida es 0
                player.health = 100 #Vuelvo a poner la vida a 100
                player.lives -= 1  #Le resto una vida al jugador
        
        if player.lives == 0:  #Si el jugador no tiene corazones
            sys.exit()  #Se cierra el juego

        player.rect.x = (800 // 2) - 95 #Coloco al jugador en el centro de la pantalla
        player.rect.y = 600 - 170   

        enemy_group.empty()   #Se remueve el enemigo
        new_enemy = Enemy()    #Se crea un nuevo enemigo
        enemy_group.add(new_enemy)  #Se agrega el nuevo enemigo al grupo de enemigos
        enemy_group.update(0.15)    #Se actualiza el grupo de enemigos

#Funcion que detecta cuando el jugador se va de la pantalla, y aumenta el nivel
def check_level(player, enemy_group):
    if player.rect.y <= 0-150:  #Si el jugador se va de la pantalla
        #Coloco al jugador en su spawn
        player.rect.x = (800 // 2) - 95
        player.rect.y = 600 - 170  
        #Aumento el nivel
        player.level += 1

        #Remuevo a todos los enemigos y los vuelvo a spawnear
        enemy_group.empty()
        new_enemy = Enemy()
        enemy_group.add(new_enemy)
        enemy_group.update(0.15)