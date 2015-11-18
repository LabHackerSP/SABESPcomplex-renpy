# -*- coding: utf-8 -*-

from renpygame.locals import *
import renpygame as pygame
import sys, os, string, renpy, codecs
from backports import configparser
# local
import cli, pygtext

# event constants
USEREVENT_BLINK_CURSOR = USEREVENT
USEREVENT_CUSTOM_QUIT = USEREVENT+1

class Game:
  def __init__(self, basedir='sabesp', mode=''):
    # pasta base (root) da fase, default para sabesp
    self.basedir = os.path.abspath(os.path.join(renpy.config.basedir, 'complex', basedir))
    # pasta virtual, subdiretório da base
    self.curdir = ''
    self.events = ''
    self.mode = mode
    self.filecheck = []
    self.nfilecheck = []
    
    self.users = []
    self.objectives = []

    pygame.init()
    self.font = pygame.font.SysFont('monospace', 24)

    # modulos
    sys.stdout = self.stdout = pygtext.Pygfile(self.font, parent=self)      
    self.terminal = cli.Cli(self)
    
  # carrega arquivo .info da pasta
  def loadconf(self, init=False):
    # procura arquivo .info# na pasta virtual atual onde # é o mode passado ao init
    path = os.path.join(self.basedir, self.curdir, '.info'+self.mode)
    
    self.objectives = []
    if os.path.exists(path):
      config = configparser.ConfigParser()
      config.readfp(codecs.open(path, "r", "utf8"))
      if config.has_section('General'):
        # usuário inicial da fase
        if init == True and config.has_option('General', 'user'): self.player = config.get('General', 'user')
        # MOTD da pasta
        if config.has_option('General', 'motd'): print(config.get('General', 'motd').encode('UTF-8'))
      #if reset == True: self.users = []
      if config.has_section('Users'):
        self.users = []
        for u in config.options('Users'):
          # lista de usuários para comando login
          self.users = self.users + [ [ u, config.get('Users', u) ] ]
      if config.has_section('Objectives'):
        # objetivos que retornam exit values
        for u in config.options('Objectives'):
          cmd = u.split(' ')
          # existência de arquivo
          if cmd[0] == 'filecheck': self.filecheck = [ cmd[1], config.get('Objectives', u) ]
          # não-existência de arquivo
          elif cmd[0] == 'nfilecheck': self.nfilecheck = [ cmd[1], config.get('Objectives', u) ]
          # comando digitado no terminal
          else: self.objectives = self.objectives + [ [ u, config.get('Objectives', u) ] ]
  
  # comando de texto escrito lentamente
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
    
    self.loadconf(True)

    while True:
      # escutar eventos pygame
      self.events = pygame.event.get()
      for event in self.events:
        if event.type == QUIT:
          return 0
        elif event.type == USEREVENT_CUSTOM_QUIT: # usado para objetivos
          return int(event.code)
        elif event.type == USEREVENT_BLINK_CURSOR: # cursor piscante
          self.terminal.cursor = '_' if self.cursor_state else ' '
          self.cursor_state = not self.cursor_state
      self.terminal.updateinput(self.events)
      # processo de blitting da imagem
      # clear the image to black
      self.screen.fill((0,0,0))
      # show it on the screen
      self.stdout.display(self.screen)
      pygame.display.flip()
