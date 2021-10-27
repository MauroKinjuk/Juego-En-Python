import pygame

class Menu():   #creo una clase y la llamo menu
    def __init__(self, game):   #creamos una funcion para inicializar que pide por parametro la clase game para usar sus funciones
        self.game = game       #accedemos a las variables de la clase game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2   #variables para guardar la mitad de la ventana en ancho y alto
        self.run_display = True #para que el menu siga ejecutandose
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)    #cursor
        self.offset = - 100 #posicionamos el cursor a la izquierda del texto

    def draw_cursor(self):  #funcion para darle forma al cursor
        self.game.draw_text('X', 15, self.cursor_rect.x, self.cursor_rect.y)    #reutilizamos la funcion para darle forma al texto 

    def blit_screen(self):  #funcion de reset de lienzo ventana y teclas
        self.game.window.blit(self.game.display, (0, 0))    #reseteo el lienzo para que no se superponga
        pygame.display.update() #refresco de la imagen en la ventana
        self.game.reset_keys()  #reseteo las teclas presionadas

class MainMenu(Menu):   #clase de menu principal que hereda las funciones de la clase Menu
    def __init__(self, game):   #defino otra funcion de para inicializar
        Menu.__init__(self, game)   #reutilizo la funcion de la clase menu para reutilizar las variables
        self.state = "Comenzar"    #Creo una variable de estado y la inicializo en "Start"
        self.startx, self.starty = self.mid_w, self.mid_h -10  #posicion de la variable "Start"
        self.controlx, self.controly = self.mid_w, self.mid_h + 30  #posicion de la variable "Control"
        self.soundx, self.soundy = self.mid_w, self.mid_h + 70  #posicion de la variable "sound"
        self.outx, self.outy = self.mid_w, self.mid_h + 110  #posicion de la variable "out"
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)  #Posicion inicial del cursor

    def display_menu(self): #funcion para mostrar el menu
        self.run_display = True #para que el menu siga ejecutandose
        while self.run_display: #mientras la variable de arriba sea true
            self.game.check_events()   #funcion que percibe si tocamos una tecla  
            self.check_input()  #llamamos a la funcion que actualiza la variable de estado
            self.game.display.fill(self.game.BLACK) #relleno el fondo de negro
            self.game.draw_text('Main Menu', 35, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 80) #escribo "Main menu"
            self.game.draw_text("Comenzar", 30, self.startx, self.starty) #escribo "Comenzar"
            self.game.draw_text("Controles", 30, self.controlx, self.controly)    #escribo "Opciones"
            if self.game.sound: #Si el sonido esta activado
                self.game.draw_text("Sonido: si", 30, self.soundx, self.soundy)    #escribo "sound: Si"
            elif not self.game.sound:   #Si el sonido esta desactivado 
                self.game.draw_text("Sonido: no", 30, self.soundx, self.soundy)    #escribo "sound: no"
            self.game.draw_text("Salir", 30, self.outx, self.outy)    #escribo "Salir"
            self.draw_cursor()  #Dibujamos el cursoor
            self.blit_screen()  #mantenemos actualizada la pantalla

    def move_cursor(self):  #funcion que define el movimiento del cursor
        if self.game.DOWN_KEY:  #si se presiona la tecla hacia abajo
            if self.state == 'Comenzar':   #si estamos parados en "Comenzar"
                self.cursor_rect.midtop = (self.controlx + self.offset, self.controly)  #Muevo el cursor abajo
                self.state = 'Controles'  #actualizo la variable de estado a Opciones
            elif self.state == 'Controles':   #si estamos parados en "opciones"
                self.cursor_rect.midtop = (self.soundx + self.offset, self.soundy)  #Muevo el cursor abajo
                self.state = 'Sonido'  #actualizo la variable de estado a Sonido
            elif self.state == 'Sonido':   #si estamos parados en "Sonido"
                self.cursor_rect.midtop = (self.outx + self.offset, self.outy)  #Muevo el cursor abajo
                self.state = 'Out'    #actualizo la variable de estado a Out
            elif self.state == 'Out':   #si estamos parados en "Out"
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)  #Muevo el cursor arriba de todo
                self.state = 'Comenzar'    #actualizo la variable de estado a Comenzar
        elif self.game.UP_KEY:  #si se presiona la tecla hacia arriba
            if self.state == 'Comenzar':   #si estamos parados en "Comenzar"
                self.cursor_rect.midtop = (self.outx + self.offset, self.outy)  #Muevo el cursor abajo de todo
                self.state = 'Out'  #actualizo la variable de estado a Out
            elif self.state == 'Controles':   #si estamos parados en "Opciones"
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)  #Muevo el cursor arriba
                self.state = 'Comenzar'    #actualizo la variable de estado a Comenzar
            elif self.state == 'Sonido':   #si estamos parados en "Sonido"
                self.cursor_rect.midtop = (self.controlx + self.offset, self.controly)  #Muevo el cursor arriba
                self.state = 'Controles'  #actualizo la variable de estado a Opciones
            elif self.state == 'Out':   #si estamos parados en "Out"
                self.cursor_rect.midtop = (self.soundx + self.offset, self.soundy)  #Muevo el cursor arriba
                self.state = 'Sonido'  #actualizo la variable de estado a Sonido

    def check_input(self):  #funcion que cambia el estado de acuerdo con que elijamos en el menu
        self.move_cursor()  #llamo a la funcion de movimiento del cursor
        if self.game.START_KEY: #Si se presiona enter
            if self.state == 'Comenzar':   #si el estado es Comenzar
                self.game.playing = True    #paso la variable de juego a true
            elif self.state == 'Controles':   #si la variable de estado es control
                self.game.curr_menu = self.game.control 
            elif self.state == 'Sonido':    #si la variable de estado es Sonido
                if self.game.sound: #Si el sonido esta activado
                    self.game.sound = False #Desactivo sonido
                elif not self.game.sound:   #Si el sonido esta desactivado 
                    self.game.sound = True  #Activo sonido
            elif self.state == 'Out':   #si la variable de estado es Out
                self.game.running = False
            self.run_display = False    #la funcion display_menu va a parar

class ControlMenu(Menu):
    def __init__(self, game):   #Funcion para inicializar el menu de controles
        Menu.__init__(self, game)
        self.state = 'Diestro'  #defino una variable de estado y la inicializo como diestro
        self.diestrox, self.diestroy = self.mid_w, self.mid_h - 100 #coordenadas en X e Y de la escritura "diestro"
        self.zurdox, self.zurdoy = self.mid_w, self.mid_h + 70  #coordenadas en X e Y de la escritura "zurdo"
        self.cursor_rect.midtop = (self.diestrox + self.offset, self.diestroy)  #coordenadas en X e Y del cursor

    def display_menu(self): #Funcion para lanzar el menu de controles
        self.run_display = True #variable para el bucle
        while self.run_display:
            self.game.check_events()    #llamo a la funcion que espera que se ingrese algo por teclado 
            self.check_input()  #llamo a la funcion que verifica que se ingreso en el menu
            self.game.display.fill((0, 0, 0))   #relleno el fondo de negro
            self.game.draw_text('Controles', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 150)    #escribo el titulo del menu de controles
            self.game.draw_text("Diestro", 25, self.diestrox, self.diestroy)    #Escribo la opcion de diestro
            flechitaspng = pygame.image.load("images/FlechasPng.png")   #cargo la imagen de las flechas
            self.game.display.blit(flechitaspng,(self.diestrox - 85 , self.diestroy + 25))  #coloco la imagen de las flechas en pantalla
            self.game.draw_text("Zurdo", 25, self.zurdox, self.zurdoy)  #Escribo la opcion de zurdo 
            wasdpng = pygame.image.load("images/wasdPng.png")   #cargo la imagen de las teclas wasd
            self.game.display.blit(wasdpng,(self.zurdox - 85 , self.zurdoy + 25))   #coloco la imagen de las teclas wasd en pantalla
            self.draw_cursor()     #dibujo el cursor
            self.blit_screen()  #actualizo para mostrar todo por pantalla

    def check_input(self):  #funcion que verifica que se ingreso en el menu
        if self.game.BACK_KEY:  #si se presiona la tecla de borrar
            self.game.curr_menu = self.game.main_menu   #volvemos al menu principal
            self.run_display = False    #la variable para el bucle de este menu pasa a false
        elif self.game.UP_KEY or self.game.DOWN_KEY:    #si tocamos la flecha hacia arriba
            if self.state == 'Diestro': #si la variable de estado esta en diestro
                self.state = 'Zurdo'    #pasamos a zurdo
                self.cursor_rect.midtop = (self.zurdox + self.offset, self.zurdoy)  #muevo el cursor a zurdo
            elif self.state == 'Zurdo': #si la variable de estado esta en zurdo
                self.state = 'Diestro'  #pasamos a diestro
                self.cursor_rect.midtop = (self.diestrox + self.offset, self.diestroy)  #muevo el cursor a diestro
        elif self.game.START_KEY:   #si tocamos la tecla enter 
            if self.state == 'Diestro': #si la variable de estado esta en diestro
                self.game.diestro = True    #paso la variable de controles para diestro a True
                self.game.zurdo = False    #paso la variable de controles para zurdo a False
                self.game.curr_menu = self.game.main_menu   #volvemos al menu principal
                self.run_display = False    #la variable para el bucle de este menu pasa a false
            elif self.state == 'Zurdo': #si la variable de estado esta en zurdo
                self.game.zurdo = True    #paso la variable de controles para zurdo a True
                self.game.diestro = False    #paso la variable de controles para diestro a False
                self.game.curr_menu = self.game.main_menu   #volvemos al menu principal
                self.run_display = False    #la variable para el bucle de este menu pasa a false
                

