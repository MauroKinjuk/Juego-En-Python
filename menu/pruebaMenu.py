from game import Game   #importamos la clase Game del archivo game

g = Game()  #creamos una variable para inicializar la clase Game

while g.running:    #bucle que se repite mientras se ejecute el juego
    g.curr_menu.display_menu()  #le pedimos a la variable de menu actual que muestre el menu
    g.game_loop()   #llamamos a la funcion del bucle de juego