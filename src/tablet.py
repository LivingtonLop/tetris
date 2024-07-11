import pygame
from config import BLACK, COLUMN_TABLET, ROW_TABLET,SIZE_CELL

class Tablet:
    
    def __init__(self) -> None:

        self.tablet:list = [[BLACK for _ in range(COLUMN_TABLET)]for _ in range(ROW_TABLET)]

    def render(self,screen:pygame):
        for y in range(ROW_TABLET):
            for x in range(COLUMN_TABLET):
                pygame.draw.rect(screen, BLACK, (x * SIZE_CELL, y * SIZE_CELL, SIZE_CELL, SIZE_CELL), 1)
                if self.tablet[y][x] != BLACK:
                    pygame.draw.rect(screen, self.tablet[y][x], (x * SIZE_CELL, y * SIZE_CELL, SIZE_CELL, SIZE_CELL))

    def confirmrowcompleteTable(self)->int:
        row_complete:int = 0
        
        for y in range(ROW_TABLET):
            
            if all(self.tablet[y][x] != BLACK for x in range(COLUMN_TABLET)):
                row_complete += 1
                
                for mover_y in range(y, 0, -1):
                    self.tablet[mover_y] = self.tablet[mover_y - 1]
                self.tablet[0] = [BLACK for _ in range(COLUMN_TABLET)]
                
        return row_complete