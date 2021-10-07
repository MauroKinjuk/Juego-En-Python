import pygame
import sys
import random

#Constantes
ANCHO = 1250 #ancho de mi pantalla en px
ALTO = 720 #alto de mi pantalla en px
color_rojo = (255,0,0) 
color_negro = (0,0,0)
color_azul = (0,0,255)

#jugador
jugador_size = 50 #tamaño
jugador_pos = [ANCHO / 2, ALTO - jugador_size * 1.5] #spawn

#Enemigo(s)
enemigo_size = 50 #tamaño
enemigo_pos = [ANCHO - enemigo_size, random.randint(0 + enemigo_size, ALTO - (enemigo_size*3))] #spawn

#ventana
ventana = pygame.display.set_mode((ANCHO,ALTO)) #establezco las medidas de la ventana con las variables que defini antes

game_over = False #variable para el bucle
FPS = pygame.time.Clock() #fotogramas por segundo (los regulo abajo de todo)

#Funciones
def detectar_colision(jugador_pos,enemigo_pos):
	jx = jugador_pos[0] #posicion del jugador en X
	jy = jugador_pos[1] #posicion del jugador en Y
	ex = enemigo_pos[0] #posicion del enemigo en X
	ey = enemigo_pos[1] #posicion del enemigo en Y

	if (ex >= jx and ex <(jx + jugador_size)) or (jx >= ex and jx < (ex + enemigo_size)): #si se interceptan (eje X)
		if (ey >= jy and ey <(jy + jugador_size)) or (jy >= ey and jy < (ey + enemigo_size)): #si se interceptan (eje Y)
			return True
		return False

while not game_over: #bucle
	for event in pygame.event.get():
		if event.type == pygame.QUIT: #condicion para que la ventana no se cierre si no toco la cruz
			sys.exit()

		if event.type == pygame.KEYDOWN: #movimiento
			x = jugador_pos[0] 
			y = jugador_pos[1] 
			if event.key == pygame.K_LEFT: #izquierda
				x -= jugador_size
			if event.key == pygame.K_RIGHT: #derecha
				x += jugador_size
			if event.key == pygame.K_UP: #arriba
				y -= jugador_size
			if event.key == pygame.K_DOWN: #abajo
				y += jugador_size
			jugador_pos[0] = x
			jugador_pos[1] = y

	ventana.fill(color_negro) #fondo

	if enemigo_pos[0] >= 0 and enemigo_pos[0] < ANCHO: #si el enemigo esta dentro de la pantalla
		enemigo_pos[0] -= 20 #se resta posicion en X (va de izquierda a derecha)
	else: #si el enemigo sale de la pantalla
		enemigo_pos[1] = random.randint(0 + enemigo_size, ALTO - (enemigo_size*3)) #vuelve a una posicion Aleatoria sobre el eje Y
		enemigo_pos[0] = ANCHO-1  #vuelve todo a la derecha en X (si no pongo el -1 no vuelve)
		
	#Colisiones
	if detectar_colision(jugador_pos,enemigo_pos):
		game_over = True

	#Dibujar enemigo
	pygame.draw.rect(ventana, color_azul,
			(enemigo_pos[0],enemigo_pos[1],
			enemigo_size, enemigo_size))

	#Dibujar jugador
	pygame.draw.rect(ventana, color_rojo,
			(jugador_pos[0],jugador_pos[1],
			jugador_size,jugador_size))

	FPS.tick(35)
	pygame.display.update()