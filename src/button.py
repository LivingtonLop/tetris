import pygame

class Button:
    
    def __init__ (self, pos_x : int, pos_y : int, filename_img: str, scale: tuple):
        self.x : int = pos_x
        self.y : int = pos_y
        self.img = pygame.image.load(filename_img)
        self.scale :tuple = scale
        
    def render (self,screen : pygame):
        self.img = pygame.transform.scale(self.img,self.scale)
        screen.blit(self.img, (self.x, self.y))