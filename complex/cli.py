# -*- coding: utf-8 -*-

from renpygame.locals import *
import argparse, sys, os, subprocess, string
import renpygame as pygame

class Cli:
  def __init__(self, parent=None):
    self.parent = parent
    sys.stdout = parent.stdout
    self.cmdbuf = []
    self.cmdbuf_index = 0
    self.prompt = '> '
    self.value = ''
    self.shift = False
    self.ctrl = False
    self.parser = Parser(self)
    
    # transformação para shift
    inkey   = '123457890-=/;\'[]\\'
    shifted = '!@#$%&*()_+?:\"{}|'
    try:
      self.table = str.maketrans(inkey,shifted)
    except:
      self.table = string.maketrans(inkey,shifted)
  
  # retorna string de prompt
  def makeprompt(self, cursor):
    return ''.join([self.parent.player, '@', self.makepath(), self.prompt, self.value, ('_' if cursor else ' ')])
    
  # retorna pasta atual
  def makepath(self, path='', absolute=False):
    return os.path.normpath(os.path.join(self.parent.basedir if absolute else '', self.parent.curdir, path))
    
  # muda pasta atual
  def chpath(self, path):
    tgtdir = os.path.normpath(os.path.join(self.parent.curdir, path))
    if os.path.isdir(os.path.join(self.parent.basedir, tgtdir)):
      self.parent.curdir = tgtdir
    else:
      raise
  
  # chama comando do parser
  def parse(self, inp):
    spl = inp.split(' ')
    command = spl[0]
    args = spl[1:]
    if command == '': command = 'emptyline'
    else: command = 'do_' + command
    try:
      function = getattr(self.parser, command)
    except:
      #print('Comando não reconhecido')
      # se o comando não existe no parser, manda pro shell
      function = getattr(self.parser, 'shell')
      function(inp)
    else:
      function(args)
  
  # recebe evento pygame e atualiza entrada de texto
  def updateinput(self, events):
    '''Update the input based on passed events'''
    for event in events:
      if event.type == KEYUP:
        if event.key == K_LSHIFT or event.key == K_RSHIFT: self.shift = False
        if event.key == K_LCTRL or event.key == K_RCTRL: self.ctrl = False
      if event.type == KEYDOWN:
        if event.key == K_RETURN:
          # add input to buffer, send input to terminal, clear input
          self.cmdbuf = [ self.value ] + self.cmdbuf
          self.cmdbuf_index = 0
          print(self.makeprompt(False))
          #self.terminal.onecmd(self.stdout.value)
          self.parse(self.value)
          self.value = ''
        elif event.key == K_UP:
          self.cmdbuf_index += 1 if self.cmdbuf_index < len(self.cmdbuf) else 0
          self.value = self.cmdbuf[self.cmdbuf_index - 1] if len(self.cmdbuf) > 0 else ''
        elif event.key == K_DOWN:
          self.cmdbuf_index -= 1 if self.cmdbuf_index > 0 else 0
          self.value = self.cmdbuf[self.cmdbuf_index - 1] if self.cmdbuf_index > 0 else ''
        elif event.key == K_BACKSPACE: self.value = self.value[:-1]
        elif event.key == K_LSHIFT or event.key == K_RSHIFT: self.shift = True
        elif event.key == K_LCTRL or event.key == K_RCTRL: self.ctrl = True
        if self.ctrl:
          # ctrl-c clears input line
          if event.key == K_c: self.value = ''
        elif not self.shift:
          if event.key in range(32,126): self.value += chr(event.key)
        elif self.shift:
          if event.key in range(32,126): self.value += chr(event.key).translate(self.table).upper()
    #if len(self.value) > self.maxlength and self.maxlength >= 0: self.value = self.value[:-1]
    
class Login(Cli):
  def __init__(self, parent, old_cli, login):
    Cli.__init__(self, parent)
    self.login = login
    self.old_cli = old_cli
  
  def makeprompt(self, cursor):
    return "Senha: " + ('_' if cursor else ' ')
    
  def parse(self, inp):
    self.parent.terminal = self.old_cli
    for u in self.parent.users:
      if self.login == u[0] and inp == u[1]:
        self.parent.player = u[0]
        return
    print('Usuário ou senha incorretas!')
    
class Parser(object):
  def __init__(self, parent=None):
    self.parent = parent
    self.game = self.parent.parent
  
  def do_exit(self, args):
    pygame.event.post(pygame.event.Event(pygame.QUIT))
  
  #slowtext
  #isso é mais pra debug, tirar no jogo final
  def do_slowtext(self, args):
    self.parent.parent.slowtext(' '.join(args) + '\n')
  
  #change directory
  #checa por .pass dentro do diretório para 'senha'
  def do_cd(self, args):
    if len(args) < 1:
      #implementar cd sem argumento
      return
    cdpath = self.parent.makepath(args[0])
    abspath = self.parent.makepath(args[0], True)
    lockfile = os.path.join(abspath, '.lock')
    if os.path.isfile(lockfile):
      with open(lockfile, 'r') as f:
        user = f.read().split('\n')[0]
      if self.game.player != user:
        print('Este diretório é acessivel apenas a: ' + user)
        return
    if cdpath[0:2] != '..':
      try:
        self.parent.chpath(args[0])
      except:
        print('cd: O diretório \"%s\" não existe.' % args[0])
        
  # comando de login
  def do_login(self, args):
    inp = Login(self.game, self.parent, args[0])
    self.game.terminal = inp
  
  def emptyline(self, args):
    pass
    
  # manda comando como shell
  def shell(self, line):
    try:
#      output = subprocess.check_output(line, shell=True, timeout=2, stderr=subprocess.STDOUT, cwd=self.parent.makepath(absolute=True))
      output = subprocess.check_output(line, shell=True, stderr=subprocess.STDOUT, cwd=self.parent.makepath(absolute=True))
    except subprocess.CalledProcessError as exc:
      print(exc.output.decode('UTF-8'))
    else:
      print(output.decode('UTF-8'))
