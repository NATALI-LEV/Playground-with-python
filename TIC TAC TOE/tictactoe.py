import sys
import pygame
import numpy as np

from constants import *

pygame.init()
screen = pygame.display.set_mode( (WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill( BG_COLOR )

class Board:
  ########################
  def __init__(self):
    self.squares = np.zeros( ( ROWS , COLS) )
    self.empty_sqrs = self.squares
    self.marked_sqrs = 0
    
  def final_state(self):
    #return 0 if there is no win yet
    
    pass
    
    
    
    
    
  def mark_sqr(self, row, col, player):
    self.squares[row][col] = player
    self.marked_sqrs +=1

  def empty_sqr(self, row, col):
    return self.squares[row][col] == 0

  def get_empty_sqrs(self):
    empty_sqrs = []
    for row in range(ROWS):
        for col in range(COLS):
          if self.empty_sqrs(row, col):
            empty_sqrs.append((row,col))
            
    return empty_sqrs
 
  def isfull(self):
      return self.marked_sqrs[row][col] == 9
    
  def isempty(self):
      return self.marked_sqrs == 0
    
class Game:
    #######################
  def __init__(self):
      self.board = Board()
      self.player = 1 # 1 - cross , 2 - circles
      self.show_lines()

  def show_lines(self):
    pygame.draw.line(screen, LINE_COLOR, (SQSIZE,0), (SQSIZE,HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (WIDTH-SQSIZE,0), (WIDTH-SQSIZE,HEIGHT), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (0,SQSIZE), (WIDTH,SQSIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0,HEIGHT-SQSIZE), (WIDTH,HEIGHT-SQSIZE), LINE_WIDTH)
  
  def draw_fig(self, row, col):
    if self.player == 1:
      start_descending = (col * SQSIZE + OFFSET , row * SQSIZE + OFFSET)
      end_descending = (col * SQSIZE + SQSIZE - OFFSET , row * SQSIZE + SQSIZE - OFFSET)
      pygame.draw.line(screen, CROSS_COLOR, start_descending, end_descending, CROSS_WIDTH)
      start_ascending =  (col * SQSIZE + OFFSET , row * SQSIZE + SQSIZE - OFFSET)
      end_ascending = (col * SQSIZE + SQSIZE - OFFSET , row * SQSIZE + OFFSET)
      pygame.draw.line(screen, CROSS_COLOR, start_ascending, end_ascending, CROSS_WIDTH)
    elif self.player == 2:
      center = (col * SQSIZE + SQSIZE //2 , row * SQSIZE + SQSIZE //2)
      pygame.draw.circle(screen, CIRCLE_COLOR, center, RADIUS, CIRCLE_WIDTH)

  def next_turn(self):
    self.player = self.player % 2 + 1 

def main():
  ########################
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
        

        if board.empty_sqr(row,col):
          board.mark_sqr(row, col, game.player)
          game.draw_fig(row, col)
          game.next_turn()


          #print(board.squares)

    pygame.display.update()
  
main()