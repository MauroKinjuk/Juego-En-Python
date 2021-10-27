import pygame
from menu import *


class Game():   #
    def __init__(self):
        pygame.init()   #inicializamos pygame
        self.running, self.playing = True, False    #variables para bucles, la primera implica que el programa corra y la segunda que estamos jugando
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False  #variables para controlar el menu
        self.DISPLAY_W, self.DISPLAY_H = 800, 600   #variables de ancho y alto de la ventana
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))  #creamos el lienzo con el ancho y alto 
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))    #creamos la ventana con el ancho y el alto
        #self.font_name = '8-BIT WONDER.TTF'    #este comando es para trabajar con una fuente descargada
        self.font_name = pygame.font.get_default_font() #definimos una variable con la fuente por defecto
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255) #colores negro y blanco
        self.sound = True
        
        self.main_menu = MainMenu(self) #Creamos una variable de menu principal para para acceder a la clase MainMenu
        self.control = ControlMenu(self)    #Creamos una variable de menu de controles para acceder a la clase ControlMenu
        self.curr_menu = self.main_menu #creamos una variable de menu actual y lo igualamos al menu principal

#todo BORRAR ESTO/////////////////////////////////////////////////////////////////////////
    def game_loop(self):    #funcion de implementacion
        while self.playing: #mientras se este jugando el juego
            self.check_events() #llamamos a la funcion de interaccion con el teclado
            if self.START_KEY:  #si se presiona la tecla enter
                self.playing= False #la variable de juego pasara a false
            self.reset_keys()   #funcion que resetea las entradas por teclado
#///////////////////////////////////////////////////////////////////////////////////////////

    def check_events(self): #funcion de interaccion con las teclas
        for event in pygame.event.get():  #bucle  
            if event.type == pygame.QUIT:   #si se cierra la ventana
                self.running, self.playing = False, False   #las variables de ejecuision y juego pasan a falso
                self.curr_menu.run_display = False  #ponemos la ventana de la variable menu actual en false
            if event.type == pygame.KEYDOWN:    #si se presiona una tecla
                if event.key == pygame.K_RETURN:    #si se presiona enter
                    self.START_KEY = True   #la variable START pasa a true
                if event.key == pygame.K_BACKSPACE: #si se presiona la tecla borrar
                    self.BACK_KEY = True    #la variable BACK pasa a true
                if event.key == pygame.K_DOWN: #si se presiona la flecha abajo
                    self.DOWN_KEY = True    #la variable DOWN pasa a true
                if event.key == pygame.K_UP:    #si se presiona la tecla arriba
                    self.UP_KEY = True  #la variable UP pasa a true

    def reset_keys(self):   #funcion para resetear las teclas y asi no queden como true
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False #paso todas las variables de interaccion con el teclado a false

    def draw_text(self, text, size, x, y ): #funcion para mostrar texto por pantalla (clase, texto que se desea mostrar, tamaño, coordenadas X, coordenadas Y)
        font = pygame.font.Font(self.font_name,size)    #creo una variable para la fuente y el tamaño
        text_surface = font.render(text, True, self.WHITE)  #creo una variable para la superficie del texto
        text_rect = text_surface.get_rect() #creo una variable para el area de la superficie
        text_rect.center = (x,y)    #coloco el area de la superficie en el centro
        self.display.blit(text_surface,text_rect)   #pongo el texto sobre el lienzo