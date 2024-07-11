import pygame
import random
from piece import Piece
from tablet import Tablet
from config import WIDTH,HEIGHT,DIR_FILENAME_TO_PIECES, WHITE,getDataonJSON
class Game:
    def __init__(self):
        self.list_pieces = getDataonJSON(DIR_FILENAME_TO_PIECES)["pieces"]
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tetris")
        self.reloj = pygame.time.Clock()
        self.tablet = Tablet()
        self.piece = Piece(5,0,random.choice(self.list_pieces))
        self.execute:bool = True

    def run(self):
        while self.execute:
            self.events()
            self.update()
            self.render()
            self.reloj.tick(60)
        pygame.quit()

    def events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.execute = False
            
            
            
    def update(self):
        pass
       
    def render(self):
        self.screen.fill((WHITE))
        self.tablet.render(self.screen)
        self.piece.render(self.screen)
        pygame.display.update()