# -*- coding: utf-8 -*-

from renpygame.locals import *
import argparse, sys, os, subprocess, string
import renpygame as pygame

USEREVENT_CUSTOM_QUIT = USEREVENT+1

class Cli:
  def __init__(self, parent=None):
    self.parent = parent       # objeto do jogo, usado para calls
    sys.stdout = parent.stdout # imita stdout do objeto pai
    self.cmdbuf = []           # buffer de comandos executados
    self.cmdbuf_index = 0
    self.prompt = '> '         # prompt do terminal
    self.value = ''            # variável que guarda texto digitado no terminal
    self.parser = Parser(self) # objeto do parser de comandos
    
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
    
  # muda pasta (virtual) atual
  def chpath(self, path):
    tgtdir = os.path.normpath(os.path.join(self.parent.curdir, path))
    if os.path.isdir(os.path.join(self.parent.basedir, tgtdir)):
      self.parent.curdir = tgtdir
    else:
      raise
  
  # chama comando do parser
  def parse(self, inp):    
    #parsing normal
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
      # inserir whitelist aqui
      function = getattr(self.parser, 'shell')
      function(inp)
    else:
      function(args)
      
    #checa se é objetivo
    for u in self.parent.objectives:
      if " ".join(inp.split()) == u[0]: #ignora espaços repetidos
        # u[0] = string alvo
        # u[1] = código de saída
        self.parent.terminal = AnyKey(self.parent, self, u[1]) # cli falsa que segura até pressionar qualquer tecla
      
    #nfilecheck checa se arquivo não existe
    if len(self.parent.nfilecheck) > 0:
      if not os.path.exists(os.path.join(self.parent.basedir, self.parent.nfilecheck[0])):
        event = pygame.event.Event(USEREVENT_CUSTOM_QUIT, code=self.parent.nfilecheck[1])
        pygame.event.post(event)
      
    #filecheck checa se arquivo existe
    if len(self.parent.filecheck) > 0:
      #print(self.parent.filecheck) # debug
      if os.path.exists(os.path.join(self.parent.basedir, self.parent.filecheck[0])):
        event = pygame.event.Event(USEREVENT_CUSTOM_QUIT, code=self.parent.filecheck[1])
        pygame.event.post(event)
  
  # recebe evento pygame e atualiza entrada de texto
  def updateinput(self, events):
    '''Update the input based on passed events'''
    for event in events:
      if event.type == KEYDOWN:
        if event.key == K_RETURN:
          # add input to buffer, send input to terminal, clear input
          if len(self.cmdbuf) < 1 or self.cmdbuf[0] != self.value: self.cmdbuf = [ self.value ] + self.cmdbuf
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
        if event.mod & KMOD_CTRL:
          # ctrl-c clears input line
          if event.key == K_c: self.value = ''
        elif event.mod & KMOD_SHIFT:
          if event.key == ord(';'): self.value += '?'
          elif event.key in range(32,126): self.value += chr(event.key).translate(self.table).upper()
        else:
          if event.key == ord(';'): self.value += '/'
          elif event.key in range(32,126): self.value += chr(event.key)
    #if len(self.value) > self.maxlength and self.maxlength >= 0: self.value = self.value[:-1]
    
class AnyKey(Cli): # prompt que espera qualquer tecla
  def __init__(self, parent, old_cli, event):
    Cli.__init__(self, parent)
    self.old_cli = old_cli
    pygame.event.clear() # limpa eventos pra não pegar enter anterior
    self.event = pygame.event.Event(USEREVENT_CUSTOM_QUIT, code=event)
    
  # mensagem de qualquer tecla
  def makeprompt(self, cursor):
    return "Pressione qualquer tecla..."
    
  def updateinput(self, events):
    for event in events:
      if event.type == KEYDOWN:
        self.parent.terminal = self.old_cli #volta para prompt quando função retornar
        pygame.event.post(self.event)
        return

class Login(Cli): # prompt de login, deriva de CLI
  def __init__(self, parent, old_cli, login):
    Cli.__init__(self, parent) # executa init padrão de CLI
    self.login = login
    self.old_cli = old_cli
  
  # substitui prompt
  def makeprompt(self, cursor):
    return "Senha: " + ('_' if cursor else ' ')
    
  def parse(self, inp):
    self.parent.terminal = self.old_cli #volta para prompt quando função retornar
    for u in self.parent.users:
      if self.login == u[0] and inp == u[1]:
        self.parent.player = u[0] # se correto, muda usuário do jogo
        return
    print('Usuário ou senha incorretas!')
    
class Parser(object):
  def __init__(self, parent=None):
    self.parent = parent           # pai de parser é cli
    self.game = self.parent.parent # pai de cli é objeto do jogo
  
  def do_exit(self, args):
    pygame.event.post(pygame.event.Event(pygame.QUIT))
  
  #slowtext
  #isso é mais pra debug, tirar no jogo final
  def do_slowtext(self, args):
    self.game.slowtext(' '.join(args) + '\n')
  
  #change directory
  #checa por .lock dentro do diretório para qual usuário pode entrar na pasta
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
      else:
        self.game.loadconf()
        
  # comando de login
  def do_login(self, args):
    if(len(args) > 0):
      inp = Login(self.game, self.parent, args[0]) # roda um outro CLI em baixo pra mudar o prompt
      self.game.terminal = inp
      
  # help
  def do_help(self, args):
    print("ls - lista os arquivos e diretórios")
    print("cd - muda o diretório")
    print("cat - abre um arquivo")
    print("motd - repete a mensagem inicial")
    print("login - entra como outro usuário")
    print("exit - sai do terminal")
    
  def do_motd(self, args):
    #porco
    self.game.loadconf()
  
  def emptyline(self, args):
    pass
    
  # manda comando como shell
  # falta whitelist
  def shell(self, line):
    try:
#      output = subprocess.check_output(line, shell=True, timeout=2, stderr=subprocess.STDOUT, cwd=self.parent.makepath(absolute=True))
      output = subprocess.check_output(line, shell=True, stderr=subprocess.STDOUT, cwd=self.parent.makepath(absolute=True))
    except subprocess.CalledProcessError as exc:
      print(exc.output)#.decode('UTF-8'))
    else:
      print(output)#.decode('UTF-8'))
