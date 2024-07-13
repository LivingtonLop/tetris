import random
import pygame

import tkinter as tk
from tkinter import messagebox

from button import Button
from piece import Piece
from tablet import Tablet

from config import ROW_TABLET, COLUMN_TABLET, BLACK, DIR_FILENAME_TO_PIECES,DIR_FILENAME_TO_IMG_PAUSE, DIR_FILENAME_TO_IMG_RETRY, getDataonJSON

class ResourcesGame:
    
    def __init__(self):
        
        self.list_pieces = getDataonJSON(DIR_FILENAME_TO_PIECES)["pieces"]
        
        self.tablet = Tablet()
        self.piece = Piece(5,0,random.choice(self.list_pieces))

        self.execute:bool = True
        self.pause:bool = False
        
        self.score:int = 0 
        #btns
        self.btn_pause = Button(370,200,DIR_FILENAME_TO_IMG_PAUSE, (100,100))
        self.btn_retry = Button(370,50,DIR_FILENAME_TO_IMG_RETRY, (100,100))

          
    def collision (self) -> bool:
        response : bool = False
    
        for y, row in enumerate(self.piece.form):
            for x, cell in enumerate (row):
                if cell:
                    if (self.piece.y + y >= ROW_TABLET or self.piece.x + x < 0 or self.piece.x + x >= COLUMN_TABLET or self.tablet.tablet[self.piece.y + y][self.piece.x + x] != BLACK):
                        response =  True
    
        return response
    
    def add_piece(self) -> Tablet:
        for y, row in enumerate(self.piece.form):
            for x, cell in enumerate(row):
                if cell:
                    self.tablet.tablet[self.piece.y + y][self.piece.x + x] = self.piece.color
    
    def new_piece(self)->Piece:    
        return Piece(5,0,random.choice(self.list_pieces))
    
    def show_score(self, screen:pygame, coor:tuple):
        font = pygame.font.SysFont('Arial',24)
        text = font.render(f"Puntuacion: {self.score}", True, BLACK)
        screen.blit(text, coor)

    def reboot_game(self):
        self.tablet.tablet = [[BLACK for _ in range(COLUMN_TABLET)] for _ in range(ROW_TABLET)]
        self.piece = self.new_piece()
        self.score = 0
    
    def show_message(self, title:str, message:str, question:str):
        root = tk.Tk()
        root.withdraw()
        
        response = messagebox.askyesno(title, message) if question else messagebox.showinfo(title, message)

        root.destroy()
        return response