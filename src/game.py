import pygame

from event import  Event

from config import WIDTH,HEIGHT, WHITE

class Game (Event):
    def __init__(self):
        super().__init__()
 
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tetris")
        
        self.reloj = pygame.time.Clock()
        self.time_d = 1000
        self.time_p = pygame.time.get_ticks()
    
    def run(self):
        while self.execute:
            self.events()
            self.update()
            self.render()
            self.reloj.tick(60)
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.execute = False
            
            self.eventMouse(event=event)
            self.eventKeyboard(event=event)
            
    def update(self):
        if not self.pause:
            time_now = pygame.time.get_ticks()
            if time_now - self.time_p >= self.time_d:
                self.piece.y += 1
                if self.collision():
                    self.piece.y -=1
                    self.add_piece()

                    self.score = self.tablet.confirmrowcompleteTable()
                    self.piece = self.new_piece()

                    if self.collision():
                        if self.show_message("Game Over", "Loser, you want retry?, press 'yes', or If want also press 'no' to close game", True):
                            self.reboot_game()
                        else:
                            self.execute = False

                self.time_p = time_now
       
    def render(self):
        self.screen.fill((WHITE))
        self.tablet.render(self.screen)
        self.piece.render(self.screen)
        
        self.show_score(self.screen,(350,10))

        self.btn_pause.render(self.screen)
        self.btn_retry.render(self.screen)

        pygame.display.update()