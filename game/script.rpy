# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define e = Character('Eileen', color="#c8ffc8")

init python:
  from complex import complex
  import pygame_sdl2 as pygame

# The game starts here.
# - El juego comienza aquí.
label start:

    e "aaaaa!"
    
    python:
      pygame.init()
      terminal = complex.Game('level1')
      terminal.main()
      
    e "bbbbb!"
    
    return
