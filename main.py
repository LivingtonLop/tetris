
#modules
import pygame
import random

pause = False
#Configure this must be in file.env o Enviorement Variable
WIDTH : int = 600 #px
HEIGHT : int = 600 #px
WIDTH_TABLET = 300
SIZE_CELL : int = 30 #px
COLUMN_TABLET :int = WIDTH_TABLET//SIZE_CELL
ROW_TABLET :int = HEIGHT//SIZE_CELL

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)

boton_x = 370
boton_y = 50

img_retry = pygame.image.load("retry.png")
img_retry = pygame.transform.scale(img_retry, (100, 100))

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
screen = pygame.display.set_mode((WIDTH,HEIGHT))
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
                pygame.draw.rect(screen, piece.color, (piece.x * SIZE_CELL + x * SIZE_CELL, piece.y * SIZE_CELL + y * SIZE_CELL, SIZE_CELL, SIZE_CELL))

#Draw tablet
def draw_tablet(screen, tablet):
    for y in range(ROW_TABLET):
        for x in range(COLUMN_TABLET):
            pygame.draw.rect(screen, BLACK, (x * SIZE_CELL, y * SIZE_CELL, SIZE_CELL, SIZE_CELL), 1)
            if tablet[y][x] != BLACK:
                pygame.draw.rect(screen, tablet[y][x], (x * SIZE_CELL, y * SIZE_CELL, SIZE_CELL, SIZE_CELL))

#draw collision
def collision(tablet, piece):
    for y, fila in enumerate(piece.form):
        for x, celda in enumerate(fila):
            if celda:
                if (piece.y + y >= ROW_TABLET or piece.x + x < 0 or piece.x + x >= COLUMN_TABLET or tablet[piece.y + y][piece.x + x] != BLACK):
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

#verificate pieces row
def verificate_delete_row_complete(tablet):
    row_complete = 0
    for y in range(ROW_TABLET):
        if all(tablet[y][x] != BLACK for x in range(COLUMN_TABLET)):
            row_complete += 1
            # Eliminar la fila completa y desplazar las superiores hacia abajo
            for mover_y in range(y, 0, -1):
                tablet[mover_y] = tablet[mover_y - 1]
            tablet[0] = [BLACK for _ in range(COLUMN_TABLET)]
            
    return row_complete

#show menu
def show_score(screen, score, coor):
    font = pygame.font.SysFont('Arial', 24)
    text = font.render(f'Puntuación: {score}', True, BLACK)
    screen.blit(text, coor)

# def reiniciar_juego():
#     [[BLACK for _ in range(COLUMN_TABLET)] for _ in range(ROW_TABLET)]
#     new_piece()
    



# Función principal del juego
def main():
    tablet = [[BLACK for _ in range(COLUMN_TABLET)] for _ in range(ROW_TABLET)]
    piece_now = new_piece()
    score = 0
    #clock
    clock = pygame.time.Clock()
    time_down = 1000 
    time_prev = pygame.time.get_ticks()

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    mouse_x, mouse_y = evento.pos
                    if boton_x <= mouse_x <= boton_x + img_retry.get_width() and boton_y <= mouse_y <= boton_y + img_retry.get_height():
                        print("si")
                        
                    
            if not pause:
                #keyboards
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        piece_now.x -= 1
                        if collision(tablet=tablet,piece= piece_now):
                            piece_now.x += 2
                    if evento.key == pygame.K_RIGHT:
                        piece_now.x += 1
                        if collision(tablet=tablet,piece=  piece_now):
                            piece_now.x -= 2
                    if evento.key == pygame.K_DOWN:
                        piece_now.y += 1
                        if collision(tablet=tablet,piece=  piece_now):
                            piece_now.y -= 1
                    if evento.key == pygame.K_UP:
                        rotate_piece(piece_now)
                        if collision(tablet=tablet,piece=  piece_now):
                            for _ in range(3):
                                rotate_piece(piece_now)

        if not pause:
            time_now = pygame.time.get_ticks() 
            if time_now - time_prev >= time_down:
                piece_now.y +=1
                if collision(tablet=tablet, piece=piece_now):
                    piece_now.y -= 1
                    add_piece(tablet=tablet,piece=piece_now)

                    row_del = verificate_delete_row_complete(tablet=tablet)
                    score += row_del*100

                    piece_now = new_piece()

                    if collision(tablet=tablet, piece=piece_now):
                        ejecutando = False

                time_prev = time_now

        screen.fill(WHITE)
            
        draw_tablet(screen, tablet)
        draw_piece(screen, piece_now)
        show_score(screen=screen,score=score, coor=(350,10))
        screen.blit(img_retry,(boton_x,boton_y))

        pygame.display.update()
        
        clock.tick(60)

    
    

main()
pygame.quit()