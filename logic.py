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

        player.rect.x = (800 // 2) - 95 #Coloco al jugador en el centro de la pantalla
        player.rect.y = 600 - 170
        #Le resto un nivel al jugador
        if player.level >= 1:
            player.level -= 1

        enemy_group.empty()   #Se remueve el enemigo
        new_enemy = Enemy()    #Se crea un nuevo enemigo
        enemy_group.add(new_enemy)  #Se agrega el nuevo enemigo al grupo de enemigos

        #Cambio la velocidad del enemigo
        for enemy in enemy_group:
            if player.level > 0:
                enemy.speed = player.level
            else:
                enemy.speed = 1

#Funcion que detecta cuando el jugador se va de la pantalla, y aumenta el nivel
def check_level(player, enemy_group):

    #Si el jugador se va de la pantalla
    if player.rect.y <= 0-150:
        #Remuevo a todos los enemigos y los vuelvo a spawnear
        enemy_group.empty()
        new_enemy = Enemy()
        enemy_group.add(new_enemy)
        
        #Cambio la velocidad del enemigo
        for enemy in enemy_group:
            enemy.speed = player.level + 1

        #Coloco al jugador en su spawn
        player.rect.x = (800 // 2) - 95
        player.rect.y = 600 - 170  
        #Aumento el nivel y la vida
        player.health = 100
        player.level += 1