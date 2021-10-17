import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
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

        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    #Funcion que devuelve el tamaño de las imagenes
    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    #Funcion que cambia cuando el personaje se mueve
    def animate(self):
        self.is_animating = True

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
        if keys[pygame.K_DOWN] and self.rect.y + self.speed + self.get_height() < 600:    #Cambiar cuando tenga la pantalla
            self.animate()
            self.rect.y += self.speed

        self.player_level()

    #Funcion que detecta cuando el jugador pasa la pantalla de arriba
    def player_level(self):
        if self.rect.y - self.speed <= -190:    #Detecto cuando deja la pantalla
            #Lo mando de nuevo al inicio
            self.rect.x = (400 - 95)
            self.rect.y = 600 - 210

    #Funcion update que actualiza el sprite
    def update(self, speed):
        if self.is_animating == True:
            self.current_sprite += speed
            
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]

            self.mask = pygame.mask.from_surface(self.image)