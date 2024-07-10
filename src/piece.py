import random
from config import getDataonJSON
from config import  DIR_FILENAME_TO_COLORS as file_colors

class Piece:

    def __init__(self, pos_x:int, pos_y:int, form_random: list) -> None:
        
        self.list_color:list = getDataonJSON(dir_filename=file_colors)["colors"]
        
        self.x:int = pos_x
        self.y:int = pos_y
        self.form:list = form_random
        self.rotate:int = 0
        self.color = random.choice(self.list_color)
        