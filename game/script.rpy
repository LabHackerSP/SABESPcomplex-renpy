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

# The game starts here.
label start:
  a "Muito bem, vamos começar."
  
  "Você está sentado ao lado de algumas dezenas de jornalistas, a maior parte do Estado de São Paulo, alguns do resto do país e meia meia dúzia de gringos."
  "Seu nome é Frederico Bambelo, as pessoas te chamam de Fred Bamba e você é repórter investigativo por vocação. Rodou toda a velha mídia – dois anos na Folha de São Paulo, três na editora Abril, especiais para o Estado e para a Carta Capital."
  "Hoje, já está há dois anos na Folha de São Paulo e não aguenta mais ter que vir para eventos como esse e escutar senhores como esse que está na sua frente dizendo absurdos como o seguinte:"
  
  a "Fenômenos inesperados da natureza acontecem em todos os lugares, nessas horas somente empresas como a Sabesp apresentam soluções sérias e verdadeiras."
  
  "O assessor retirou essa frase de uma das peças oficiais de publicidade da empresa, que tenta se recuperar em meio a uma das maiores crises de sua história. Com os níveis dos reservatórios críticos e nenhuma recuperação dos mananciais, você sabe que é uma questão de tempo até o colapso."
  
  a "A Sabesp investiu R$ 9,3 bilhões entre 1995 e 2013, em medidas para aumentar a segurança do abastecimento de água. Os recursos permitiram aumentar a disponibilidade de mananciais, a capacidade de produção, o transporte de água tratada..."
  a "...e a integração entre os sistemas produtores, além de ter ampliado a capacidade de reservação e de distribuição de água à população e, importante, com redução nas perdas. No período, a capacidade de produção subiu 57,2 para 73,3 metros cúbicos por segundo."
  
  "Droga. Tudo propaganda. Você sabe que XX dados contraXXX. Sabia também que seu jornal nunca publicaria essas informações. Enquanto ouvia, fazia anotações em seu laptop e controlava a ansiedade. Precisava fazer alguma coisa. Começou a abrir páginas de veículos independentes como A Pública, Outras Palavras, Jornalistas Livres, XX, XXXX."
  
  "Uma tela de diálogo apareceu sobre seu navegador."

  jump navegador

label navegador:
  c "Cara, vou te falar, você está certo."
  f "Que merda é essa? Fred se perguntou assustado. Fui hackeado."
  c "Fred. Fica calmo. Eu vim falar com você. Me escuta. É sobre a Sabesp."
   
  "Bom, é o seguinte. Você foi hackeado. Talvez a pessoa esteja te enrolando enquanto esvazia sua conta bancária importando bonecas eróticas da China, vai saber. Ou talvez ela tenha informações sérias sobre a Sabesp."

  menu:
    "Tira a bateria do lap":
      "Você segura a bateria assustado, respirando rápido. Olha ao redor, ninguém percebeu. Antes do fôlego diminuir, seu celular toca."      
      c "Amigo, eu posso te dar documentos."
      menu:
        "Tira a bateria do cel":
          jump go1_lapquebrado
        "Continua conversando":
          jump conversa
    "Continua conversando":
      jump conversa
      
label conversa:
  #olha para o lado, no canto da sala um computador na mesa

  f "Quem é você?"
  c "Eu vou te ajudar a encontrar informações. Olha pra sua esquerda, tá vendo aquele computador na mesa?"
  f "Sim."
  c "Ele está conectado ao sistema interno deles. Eu só tenho acesso como usuário, preciso acessar como administrador. Mas já tem muita coisa, vamos denunciar esses fdps. Vai lá discretamente, senta e faz login. Dá uma fuçada. Tem um monte de documento,  eu não sei o que pode te ajudar. Dá uma olhada, alguma coisa vai servir pra você."

  #chegando perto do comp

  "Você tropeça em alguém e se desculpa, está nervoso"
  
label login:
  c "O usuário é o meu nome no feminino e a senha é o seu de trás pra frente."
  
  $ login = renpy.input("Login: ")
  $ senha = renpy.input("Senha: ")
  if login != "cadelaraposa" or senha != "derf":
    "Login incorreto!"
    jump login

  python:
    pygame.init()
    terminal = complex.Game('level1a')
    terminal_label = 'term_level1a'
    
label login_sub:
  $ button_show = True
  c "É isso! Você conseguiu seu primeiro desafio. Está vendo este botão que apareceu ali? É o símbolo do terminal. Clique nele para acessar a etapa de programação deste jogo"
  jump login_sub
    
label term_level1a:
  python:
    pygame.init()
    ret = terminal.main()
    button_show = False
  
  if ret == 1:
    c "Ah, você está como usuário, não como admin. Eu quebrei a senha de um dos diretores, vou te deixar entrar também. Mas ele ainda não tem acesso a essa pasta Atlantis, tou louco para saber o que tem aí dentro."
    c "Vou te dar permissão de admin, pera… Merda, cara. Fudeu. Policia aqui. Me deixa um beijo."
    
  if ret == 2:
    c "Merda, cara. Fudeu. Policia aqui. Me deixa um beijo."
    
  if ret > 0:
    f "Alô, alô, Cão, tudo bem??" 
    "..."
    
    python:
      pygame.init()
      terminal = complex.Game('level1b')
      terminal_label = 'term_level1b'
      
    jump level1b
    
  return
  
label level1b:
  $ button_show = True
  "Merda. Boa sorte, tomara que fuja. Mas você não pode fazer nada por ele agora. O jeito é continuar voltar para o terminal."
  jump level1b
  
label term_level1b:
  python:
    pygame.init()
    ret = terminal.main()
  return
      
label go1_lapquebrado:
  "Você está com uma bateria em cada mão, um pouco confuso. Alguém percebe, você tenta disfarçar e derruba o próprio computador. Leva um tempo até você se recuperar e o resto da história é medíocre."
   
  "Você utiliza apenas dados do release oficial e conteúdo da internet para fazer a matéria do dia seguinte. Com um pouco de sorte, ninguém percebe como o texto está fraco."
   
  "Nessa noite você sai para beber com amigos e não fica bêbado. Estranha, bebe mais, e não fica bêbado. Bebe pra caralho e nada. Vai para casa com prejuízo e nenhum samba."
   
  "Acordo com uma ressaca enorme e um enjôo ainda maior. De repente, toda a noite passada volta com tudo e você corre para vomitar no trono de porcelana. Enquanto está ali, se espanta, são.. letras? Sim, você vomitou letras, letras que dizem PERDEU"
