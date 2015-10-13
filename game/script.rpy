# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")

init python:
  import pygame_sdl2 as pygame
  from complex import complex
  
  button_show = False
  
  def overlay_button():
    if button_show:
      ui.imagebutton("image_idle.png","image_hovered.png",clicked=ui.callsinnewcontext("terminal"),xpos=.5)# or ui.jumps
  config.overlay_functions.append(overlay_button)
  
label terminal:
    python:
      pygame.init()
      terminal.main()
      
    return

# The game starts here.
label start:
    e "reset!!!"
    
    python:
      pygame.init()
      terminal = complex.Game('level1')

    jump the_label

label the_label:
    e "aaaaa!"
      
    e "bbbbb!"

    $ button_show = True
    
    jump the_label
