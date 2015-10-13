# -*- coding: utf-8 -*-

from renpygame.locals import *
import renpygame as pygame
import sys, os, string, renpy
from backports import configparser
# local
import cli, pygtext

# event constants
USEREVENT_BLINK_CURSOR = USEREVENT

class Game:
  def __init__(self, basedir='sabesp'):
    # pasta base da fase, default para sabesp
    self.basedir = os.path.abspath(os.path.join(renpy.config.basedir, 'complex', basedir))
    self.curdir = ''
    
    # carrega arquivo .info da pasta
    config = configparser.ConfigParser()
    config.readfp(open(os.path.join(self.basedir,'.info')))
    self.player = config.get('General', 'user')
    self.users = []
    for u in config.options('Users'):
      self.users = self.users + [ [ u, config.get('Users', u) ] ]

    pygame.init()
    self.font = pygame.font.SysFont('monospace', 18)

    # modulos    
    sys.stdout = self.stdout = pygtext.Pygfile(self.font, parent=self)      
    self.terminal = cli.Cli(self)
  
  def slowtext(self, text):
    self.stdout.prompt_enable = False
    for c in text:
      self.stdout.write(c)
      self.stdout.display(self.screen)
      pygame.display.flip()
      pygame.time.wait(20 if c != '.' else 500)
    self.stdout.prompt_enable = True

  def main(self):
    # defaults pygame
    pygame.init()
    pygame.display.init()
    self.screen = pygame.display.set_mode((800, 600))
    pygame.key.set_repeat(200,50)
    self.cursor_state = True
    pygame.time.set_timer(USEREVENT_BLINK_CURSOR, 500)

    while True:
      # watch for events
      events = pygame.event.get()
      for event in events:
        if event.type == QUIT:
          return
        elif event.type == USEREVENT_BLINK_CURSOR:
          self.terminal.cursor = '_' if self.cursor_state else ' '
          self.cursor_state = not self.cursor_state
      self.terminal.updateinput(events)
      # clear the image to black
      self.screen.fill((0,0,0))
      # show it on the screen
      self.stdout.display(self.screen)
      pygame.display.flip()
