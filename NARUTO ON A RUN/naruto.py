import os
import sys
import pygame
import random

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
        self.gravity = 0.3
        self.onground = True
        self.jumping = False
        self.jump_stop = 2
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
        elif self.onground and loops % 200 == 0:
            self.texture_num = (self.texture_num + 1) % 3
            self.set_texture()
        

    def show(self):
        screen.blit(self.texture, (self.x, self.y))

    def set_texture(self):
        path = os.path.join(f'assets/images/naruto{self.texture_num}.png')
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

class Pain:
  def __init__(self, x):
      self.width = 34
      self.height = 44
      self.x = x
      self.y = 80
      self.set_texture()
      self.show()

  def update(self, dx):
      self.x += dx

  def show(self):
        screen.blit(self.texture, (self.x, self.y))

  def set_texture(self):
    path = os.path.join('assets/images/pain.png')  
    self.texture = pygame.image.load(path)
    self.texture = pygame.transform.scale(self.texture, (self.width, self.height))

class collision:
  pass

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
    self.obstacles = []
    self.speed = 0.5
  
  def tospawn(self, loops):
        return loops % 100 == 0

  def spawn_pain(self):
    # list with pain
    if len(self.obstacles) > 0:
      prev_pain = self.obstacles[-1]
      x = random.randint(prev_pain.x + self.naruto.width + 84, WIDTH + prev_pain.x + self.naruto.width + 84)

   # empty list
    else:
      x = random.randint(WIDTH + 100, 1000)

  # create the new pain
    pain = Pain(x)
    self.obstacles.append(pain)
        
def main():
  
  game = Game() 
  naruto = game.naruto 
  clock = pygame.time.Clock()
  loops = 0

  while True:
    
    loops += 1
    
    for bg in game.bg:
      bg.update(-game.speed)
      bg.show()
    
    naruto.update(loops)
    naruto.show()
    
    if game.tospawn(loops):
      game.spawn_pain()
      
    for pain in game.obstacles:
      pain.update(-game.speed)
      pain.show()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          if naruto.onground:
            naruto.jump()
                  
    clock.tick(400)
    pygame.display.update()

main()