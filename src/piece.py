import random
import pygame
from config import getDataonJSON, SIZE_CELL
from config import  DIR_FILENAME_TO_COLORS as file_colors


class Piece:

    def __init__(self, pos_x:int, pos_y:int, form_random: list) -> None:
        
        self.list_color:list = getDataonJSON(dir_filename=file_colors)["colors"]
        
        self.x:int = pos_x
        self.y:int = pos_y
        self.form:list = form_random
        self.rotate:int = 0
        self.color:tuple= random.choice(self.list_color)
        
    def render(self,screen:pygame):
        for y, row in enumerate(self.form):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, self.color, (self.x * SIZE_CELL + x * SIZE_CELL, self.y * SIZE_CELL + y * SIZE_CELL, SIZE_CELL, SIZE_CELL))

    def rotatePiece(self):
        self.form = list(zip(*self.form[::-1]))
