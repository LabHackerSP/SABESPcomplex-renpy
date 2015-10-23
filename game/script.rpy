# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define a = Character('Assessor de Imprensa', color="#c8f367")
define f = Character('Fred', color="#c8ffc8")
define c = Character('Cão Raposa', color="#f8c8ff")
define p1 = Character('Polícia', color="#c84fc8")
define p2 = Character('Polícia 2', color="#c84ff8")
define p3 = Character('Polícia 3', color="#c84f68")
define e = Character('Editor', color="#c80fc8")

init python:
  import pygame_sdl2 as pygame
  from complex import complex
  
  button_show = False
  terminal_label = "terminal"
  
  def overlay_button():
    if button_show:
      ui.imagebutton("image_idle.png","image_hovered.png",clicked=ui.callsinnewcontext(terminal_label),xpos=.5)# or ui.jumps
  config.overlay_functions.append(overlay_button)
  
label terminal:
    python:
      pygame.init()
      ret = terminal.main()
    
    "O resultado foi [ret]."      
      
# checagem
    return

# The game starts here.
label start:
    python:
      pygame.init()
      terminal = complex.Game('level1')
      
#    python:
#        povname = renpy.input("What is your name?")
#        povname = povname.strip()
#
#        if not povname:
#             povname = "Pat Smith"

    a "Muito bem, vamos começar."
    
    "Você está sentado ao lado de algumas dezenas de jornalistas, a maior parte do Estado de São Paulo, alguns do resto do país e meia meia dúzia de gringos."
    "Seu nome é Frederico Bambelo, as pessoas te chamam de Fred Bamba e você é repórter investigativo por vocação. Rodou toda a velha mídia – dois anos na Folha de São Paulo, três na editora Abril, especiais para o Estado e para a Carta Capital."
    "Hoje, já está há dois anos na Folha de São Paulo e não aguenta mais ter que vir para eventos como esse e escutar senhores como esse que está na sua frente dizendo absurdos como o seguinte:"
    
    a "Fenômenos inesperados da natureza acontecem em todos os lugares, nessas horas somente empresas como a Sabesp apresentam soluções sérias e verdadeiras."
    
    "O assessor retirou essa frase de uma das peças oficiais de publicidade da empresa, que tenta se recuperar em meio a uma das maiores crises de sua história. Com os níveis dos reservatórios críticos e nenhuma recuperação dos mananciais, você sabe que é uma questão de tempo até o colapso."
    
    a "A Sabesp investiu R$ 9,3 bilhões entre 1995 e 2013, em medidas para aumentar a segurança do abastecimento de água. Os recursos permitiram aumentar a disponibilidade de mananciais, a capacidade de produção, o transporte de água tratada..."
    a "...e a integração entre os sistemas produtores, além de ter ampliado a capacidade de reservação e de distribuição de água à população e, importante, com redução nas perdas. No período, a capacidade de produção subiu 57,2 para 73,3 metros cúbicos por segundo."
    
    "Droga. Tudo propaganda. Você sabe que XX dados contraXXX. Sabia também que seu jornal nunca publicaria essas informações. Enquanto ouvia, fazia anotações em seu laptop e controlava a ansiedade. Precisava fazer alguma coisa. Começou a abrir páginas de veículos independentes como A Pública, Outras Palavras, Jornalistas Livres, XX, XXXX."

    jump the_label

label the_label:
    e "aaaaa!"
      
    e "bbbbb!"

    $ button_show = True
    
    jump the_label
