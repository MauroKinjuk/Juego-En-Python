import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = []
        self.is_animating = False   #Setea que la animacion sea falso
        self.sprites.append(pygame.image.load("carpincho/izquierda/1.png"))
        self.sprites.append(pygame.image.load("carpincho/izquierda/2.png"))
        self.sprites.append(pygame.image.load("carpincho/izquierda/3.png"))
        self.sprites.append(pygame.image.load("carpincho/izquierda/4.png"))
        self.sprites.append(pygame.image.load("carpincho/izquierda/5.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.speed = 3
        self.health = 100
        self.lives = 2
        self.level = 1

        #Dibuja el enemigo, y hace el spawn
        self.rect = self.image.get_rect()
        self.rect.x = (800 // 2) - 95
        self.rect.y = 600 - 170

    #Funcion que devuelve el tamaño de las imagenes
    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    #Funcion que cambia cuando el personaje se mueve
    def animate(self):
        self.is_animating = True

    #Funcion que agrega la barra de vida
    def health_bar(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.rect.x, self.rect.y + self.get_height() - 10, self.get_width(), 10))
        pygame.draw.rect(screen, (0,255,0), (self.rect.x, self.rect.y + self.get_height() - 10, self.get_width() * (self.health/100), 10))

    #Funcion para obtener las teclas presionadas
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x - self.speed > 0:    #Izquierda
            self.animate()
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x - self.speed < 600: #Cambiar el 600 para cuando tenga la pantalla
            self.animate()
            self.rect.x += self.speed
        if keys[pygame.K_UP]:   #Arriba
            self.animate()
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y + self.speed + (self.get_height() - 20) < 600:    #Cambiar cuando tenga la pantalla
            self.animate()
            self.rect.y += self.speed
        self.player_level()

    #Funcion para obtener las teclas presionadas
    def get_input_wasd(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x - self.speed > 0:    #Izquierda
            self.animate()
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x - self.speed < 600: #Cambiar el 600 para cuando tenga la pantalla
            self.animate()
            self.rect.x += self.speed
        if keys[pygame.K_w]:   #Arriba
            self.animate()
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y + self.speed + (self.get_height() - 20) < 600:    #Cambiar cuando tenga la pantalla
            self.animate()
            self.rect.y += self.speed
        self.player_level()

    #Funcion que detecta cuando el jugador pasa la pantalla de arriba
    def player_level(self):
        if self.rect.y - self.speed <= -190:    #Detecto cuando deja la pantalla
            #Lo mando de nuevo al inicio
            self.rect.x = (400 - 95)
            self.rect.y = 600 - 100

    #Funcion update que actualiza el sprite
    def update(self, speed, screen):
        if self.is_animating == True:
            self.current_sprite += speed
            
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

        self.mask = pygame.mask.from_surface(self.image)
        #Dibujo la barra de vida
        self.health_bar(screen)