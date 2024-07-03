
#modules
import pygame
import random

#Configure this must be in file.env o Enviorement Variable
width_window : int = 300 #px
height_window : int = 600 #px
size_cell : int = 30 #px
column_tablet :int = width_window//size_cell
row_tablet :int = height_window//size_cell

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)


#Asset (colores) -> new folder in project like : assets/texture, this project is in 2d, alone colors simples

list_colors :list = [ #para usar random
    (0, 255, 255),  # Cyan
    (0, 0, 255),    # Azul
    (255, 165, 0),  # Naranja
    (255, 255, 0),  # Amarillo
    (0, 255, 0),    # Verde
    (128, 0, 128),  # Morado
    (255, 0, 0)     # Rojo
]

#Assets (pieces) ->  new folder in project like :  assets/pieces.

list_pieces : list = [ #para usar random
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]]   # L
]

#Init screen

pygame.init()
screen = pygame.display.set_mode((width_window,height_window))
pygame.display.set_caption("Tetris")

#Class
class Piece:
    def __init__(self, x : int, y:int,form):
        self.x = x
        self.y = y
        self.form = form
        self.color = random.choice(list_colors)
        self.rotate = 0


#draw piece
def draw_piece(screen, piece):
    for y, row in enumerate(piece.form):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, piece.color, (piece.x * size_cell + x * size_cell, piece.y * size_cell + y * size_cell, size_cell, size_cell))

#Draw tablet
def draw_tablet(screen, tablet):
    for y in range(row_tablet):
        for x in range(column_tablet):
            pygame.draw.rect(screen, BLACK, (x * size_cell, y * size_cell, size_cell, size_cell), 1)
            if tablet[y][x] != BLACK:
                pygame.draw.rect(screen, tablet[y][x], (x * size_cell, y * size_cell, size_cell, size_cell))

#draw collision
def collision(tablet, piece):
    for y, fila in enumerate(piece.form):
        for x, celda in enumerate(fila):
            if celda:
                if (piece.y + y >= row_tablet or piece.x + x < 0 or piece.x + x >= column_tablet or tablet[piece.y + y][piece.x + x] != BLACK):
                    return True
    return False

#add piece
def add_piece(tablet, piece):
    for y, fila in enumerate(piece.form):
        for x, celda in enumerate(fila):
            if celda:
                tablet[piece.y + y][piece.x + x] = piece.color

#generate new instance`s Piece
def new_piece() -> Piece:
    return Piece(5,0,random.choice(list_pieces))

#rotate piece
def rotate_piece(piece):
    piece.form = list(zip(*piece.form[::-1]))



# Función principal del juego
def main():
    tablet = [[BLACK for _ in range(column_tablet)] for _ in range(row_tablet)]
    piece_now = new_piece()
    
    #clock
    clock = pygame.time.Clock()
    time_down = 1000 
    time_prev = pygame.time.get_ticks() 
    
    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            #keyboards
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    piece_now.x -= 1
                    if collision(tablet=tablet,piece= piece_now):
                        piece_now.x += 1
                if evento.key == pygame.K_RIGHT:
                    piece_now.x += 1
                    if collision(tablet=tablet,piece=  piece_now):
                        piece_now.x -= 1
                if evento.key == pygame.K_DOWN:
                    piece_now.y += 1
                    if collision(tablet=tablet,piece=  piece_now):
                        piece_now.y -= 1
                if evento.key == pygame.K_UP:
                    rotate_piece(piece_now)
                    if collision(tablet=tablet,piece=  piece_now):
                        for _ in range(3):
                            rotate_piece(piece_now)


        time_now = pygame.time.get_ticks() 
        if time_now - time_prev >= time_down:
            piece_now.y +=1
            if collision(tablet=tablet, piece=piece_now):
                piece_now.y -= 1
                add_piece(tablet=tablet,piece=piece_now)
                piece_now = new_piece()
                if collision(tablet=tablet, piece=piece_now):
                    print("Game Over")
                    #ejecutando = False

            time_prev = time_now

    
        screen.fill(WHITE)
        draw_tablet(screen, tablet)
        draw_piece(screen, piece_now)
        pygame.display.update()
        
        clock.tick(60)

main()
pygame.quit()