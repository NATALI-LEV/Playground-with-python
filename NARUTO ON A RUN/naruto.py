import os
import sys
import pygame

WIDTH = 623
HEIGHT = 150

pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption('Naruto')

class Naruto:
  
    def __init__(self):
        self.width = 44
        self.height = 44
        self.x = 10
        self.y = 80
        self.texture_num = 0
        self.dy = 3
        self.gravity = 1.2
        self.onground = True
        self.jumping = False
        self.jump_stop = 10
        self.falling = False
        self.fall_stop = self.y
        self.set_texture()
        self.set_sound()
        self.show()

    def update(self, loops):
        # jumping
        if self.jumping:
            self.y -= self.dy
            if self.y <= self.jump_stop:
                self.fall()
        
        # falling
        elif self.falling:
            self.y += self.gravity * self.dy
            if self.y >= self.fall_stop:
                self.stop()

        # walking
        elif self.onground and loops % 4 == 0:
            self.texture_num = (self.texture_num + 1) % 3
            self.set_texture()
        

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

    def set_texture(self):
        path = os.path.join(f'assets/images/naruto_stand.png')
        self.texture = pygame.image.load(path)
        self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

    def set_sound(self):
        path = os.path.join('assets/sounds/jump.wav')
        self.sound = pygame.mixer.Sound(path)

    def jump(self):
        self.sound.play()
        self.jumping = True
        self.onground = False

    def fall(self):
        self.jumping = False
        self.falling = True

    def stop(self):
        self.falling = False
        self.onground = True
  
class BG:

  def __init__(self, x):
    self.width = WIDTH
    self.height = HEIGHT
    self.x = x
    self.y = 0
    self.set_texture()
    self.show()

  def update(self, dx):
    self.x += dx
    if self.x <= -WIDTH:
      self.x = WIDTH

  def show(self):
    screen.blit(self.texture, (self.x, self.y))

  def set_texture(self):
    path = os.path.join('assets/images/background.png')
    self.texture = pygame.image.load(path)
    self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

class Game:

  def __init__(self):
    self.bg = [BG(x=0), BG(x=WIDTH)]
    self.naruto = Naruto()
    self.speed = 0.5
  
def main():
  
  game = Game()  
  clock = pygame.time.Clock()

  while True:
    
    for bg in game.bg:
      bg.update(-game.speed)
      bg.show()
    
    game.naruto.show()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
    clock.tick(400)
    pygame.display.update()

main()