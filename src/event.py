import pygame

from resources_game import ResourcesGame

class Event(ResourcesGame):
    def __init__(self):
        super().__init__()
        
    def eventMouse(self, event:pygame):
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if self.btn_retry.x <= mouse_x <= self.btn_retry.x + self.btn_retry.img.get_width() and self.btn_retry.y <= mouse_y <= self.btn_retry.y + self.btn_retry.img.get_height():
                        
                    if self.show_message("Reinicio","Usted quiere reiniciar la partida?",True):
                        self.reboot_game()
                        self.pause = False

                if self.btn_pause.x <= mouse_x <= self.btn_pause.x + self.btn_pause.img.get_width() and self.btn_pause.y <= mouse_y <= self.btn_pause.y + self.btn_pause.img.get_height():    
                    self.show_message("Pausado","El juego esta pausado, toca nuevamente para seguir con la partida",False)

                    self.pause = not self.pause

    def eventKeyboard(self, event:pygame):
        
        if not self.pause:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    self.piece.x -= 1
                    if self.collision():
                        self.piece.x += 2
                        if self.collision():
                            self.piece.x -= 2

                if event.key == pygame.K_RIGHT:
                    self.piece.x += 1
                    if self.collision():
                        self.piece.x -= 2
                        if self.collision():
                            self.piece.x += 2
                
                if event.key == pygame.K_DOWN:
                    self.piece.y += 1
                    if self.collision():
                        self.piece.y -= 1

                if event.key == pygame.K_UP:
                    self.piece.rotatePiece()
                    if self.collision():
                        for _ in range(3):
                            self.piece.rotatePiece()
                
                # if event.key == pygame.K_RETURN:
                #     y = len(self.tablet.tablet) - self.piece.y
                #     self.piece.y+= y-1
                #     if self.collision():
                #         self.piece.y -= 1