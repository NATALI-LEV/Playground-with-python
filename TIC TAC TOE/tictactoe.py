import sys
import pygame
import numpy as np

from constants import *

pygame.init()
screen = pygame.display.set_mode( (WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill( BG_COLOR )

class Board:
  def __init__(self):
    self.squares = np.zeros( ( ROWS , COLS) )
    
    
  
  def mark_sqr(self, row, col, player):
    self.squares[row][col] = player


class Game:
    
  def __init__(self):
      self.board = Board()
      self.player = 1
      self.show_lines()

  def show_lines(self):
    pygame.draw.line(screen, LINE_COLOR, (SQSIZE,0), (SQSIZE,HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (WIDTH-SQSIZE,0), (WIDTH-SQSIZE,HEIGHT), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (0,SQSIZE), (WIDTH,SQSIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0,HEIGHT-SQSIZE), (WIDTH,HEIGHT-SQSIZE), LINE_WIDTH)
  

def main():

  game = Game()
  board = game.board

  while True:

    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit

      if event.type == pygame.MOUSEBUTTONDOWN:
        pos = event.pos
        row = pos[1] // SQSIZE
        col = pos[0] // SQSIZE
        
        board.mark_sqr(row, col, 1)

    pygame.display.update()
  
main()