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

init:
  image bg laptop1 = "laptop1.png"
  image bg laptop2 = "laptop2.png"
  image bg laptop3 = "laptop3.png"
  image bg black = "#000000"

init python:
  import pygame_sdl2 as pygame
  from complex import complex
  
  button_show = False
  terminal_label = "terminal"
  
  def overlay_button():
    if button_show:
      ui.imagebutton("terminal_idle.png","terminal_hover.png",clicked=ui.callsinnewcontext(terminal_label),xpos=.01,ypos=.01)# or ui.jumps
  config.overlay_functions.append(overlay_button)

# The game starts here.
label start:
  scene bg laptop1

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
  scene laptop2
  
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
    terminal = complex.Game('level1','1')
    terminal_label = 'term_level1a'
    button_show = True
    
label level1a:
  c "É isso! Você conseguiu seu primeiro desafio. Está vendo este botão que apareceu ali? É o símbolo do terminal. Clique nele para acessar a etapa de programação deste jogo"
  jump level1a
    
label term_level1a:
  python:
    pygame.init()
    ret = terminal.main()
  
  if ret > 0:
    $ button_show = False
    scene bg laptop3
  
    if ret == 1:
      c "Ah, você está como usuário, não como admin. Eu quebrei a senha de um dos diretores, vou te deixar entrar também. Mas ele ainda não tem acesso a essa pasta Atlantis, tou louco para saber o que tem aí dentro."
      c "Vou te dar permissão de admin, pera… Merda, cara. Fudeu. Policia aqui. Me deixa um beijo."
      
    if ret == 2:
      scene bg laptop3
      c "Merda, cara. Fudeu. Policia aqui. Me deixa um beijo."
    
    f "Alô, alô, Cão, tudo bem??" 
    "..."
    "Merda. Boa sorte, tomara que fuja. Mas você não pode fazer nada por ele agora. O jeito é continuar voltar para o terminal."
    
    python:
      pygame.init()
      terminal = complex.Game('level1','2')
#      terminal.mode = '2'
      terminal_label = 'term_level1b'
      button_show = True
      
    jump level1b
    
  return
  
label level1b:
  "Deve ter algo nas pastas quais você tem acesso pra desmascarar a Sabesp."
  jump level1b
  
label term_level1b:
  python:
    pygame.init()
    ret = terminal.main()
    
  if ret == 1:
    $ button_show = False
    "Atlantis! Você sabe que precisa copiar este arquivo e não tem ninguém para te ensinar. A ansiedade começa a crescer e você quase desespera, mas sente o peso do seu telefone no bolso e se lembra do google. Você abre o celular e pesquisa. Agora te vira, negão, negona. Você precisa aprender o comando necessário para mover um arquivo."
    
    python:
      pygame.init()
      terminal = complex.Game('level1b','1')
      terminal_label = 'term_level1c'
      button_show = True
      
    jump level1c
      
  return
  
label level1c:
  "Você conecta seu pendrive no computador e a pasta 'pendrive' aparece na raiz do sistema."
  jump level1c
  
label term_level1c:
  python:
    pygame.init()
    ret = terminal.main()
    
  if ret == 1:
    jump copiado
    
  if ret == 2:
    $ terminal.mode = '2'
    jump movido
    
  if ret == 3:
    $ terminal.mode = '1'
    jump movido2
      
  return
  
label movido:
  "Ih, merda, ao mover ficou um buraco. Não dá para excluir o arquivo deles, é um rastro muito óbvio. Mover era o comando errado, agora você precisa copiar o arquivo de volta para a pasta original ou alguém vai perceber."
  jump movido
  
label movido2:
  "Você tirou o arquivo do seu pendrive... tenta mais uma vez, vai."
  jump movido2
  
label copiado:
  $ button_show = False
  "Pronto, com esse arquivo copiado você já consegue colocar o dedo na cara da Sabesp e exigir respostas sobre esses 85 milhões. É o suficiente. Se você quiser sair e escapar de qualquer problema possível, faça logout no sistema. Mas por outro lado, você tem a sensação de que perdeu alguma pista em algum lugar."
  
  menu:
    "Log out e matéria dedo na cara":
      jump go2_materia
    "Descobrir a senha":
      # terminal 3
      python:
        pygame.init()
        terminal = complex.Game('level1b','3')
        #terminal.mode = '3'
        terminal_label = 'term_level1d'
        button_show = True
      jump level1d
      
label level1d:
  "Tem alguma pista no arquivo de precrise sobre a senha da diretoria. Leia de novo.."
  jump level1d
        
label term_level1d:
  python:
    pygame.init()
    ret = terminal.main()
    
  if ret == 1:
    $ button_show = False
    jump copiado2
    
  return
      
label copiado2:
  "Cara, você, um hacker. Rá, vamos ver agora, Sabesp. Com esse documento na mão você tem uma bela de uma matéria. E agora, acha que já tem o suficiente ou ainda vai dar um jeito de abrir aquele atlantis.dir e conhecer todos os segredos do projeto?"
  "Você precisa decidir rápido."
  
  menu:
    "Ficar até hackear Atlantis":
      jump go3_prisao
    "Sair do comp e discretamente sentar em seu lugar":
      jump sentar
      
label sentar:
  "Você já tem conteúdo suficiente para o maior furo da sua vida e também acha que já abusou da sorte. Discretamente se levanta e deixa aquele computador em paz." 
  "Pouco depois, três homens de terno negro entram na sala e se dirigem para o computador onde você estava. Procuram ao redor e não sabem o que fazer. Um deles leva a mão até a orelha esquerda e começa a falar alguma coisa, mais ou menos ao mesmo tempo em que a coletiva termina. Todos os jornalistas se levantam ao mesmo tempo e você aproveita a movimentação para sair logo dali."
  "Promoção da escassez? Que jogo político é esse? Então a seca foi promovida pelo governo estadual? Naquela noite você redige a matéria com fogo nos dedos, certo de que está prestes a desmacarar um grande cartel."
  "O texto está primoroso e o documento oficial te respalda para fazer a crítica olhando no olho. Você prepara o email para seu editor, mas exita. Não entende porque, mas exita. Será que seu editor publicaria essa matéria? Será que a Folha de São Paulo, o maior jornal do país, compraria uma briga com o governo de SP?"
  "Então, você se lembra daqueles grupos independentes, A Pública, Ponte, Jornalistas Livres, Outras Palavras. Com certeza eles publicariam, mas teriam alcance suficiente? Hora de tomar uma decisão."
  
  menu:
    "enviar para a Folha de São Paulo":
      jump go4_folha
    "enviar para A Pública":
      jump go5_publica
  
label go1_lapquebrado:
  scene bg black #trocar
  
  "Você está com uma bateria em cada mão, um pouco confuso. Alguém percebe, você tenta disfarçar e derruba o próprio computador. Leva um tempo até você se recuperar e o resto da história é medíocre."
  "Você utiliza apenas dados do release oficial e conteúdo da internet para fazer a matéria do dia seguinte. Com um pouco de sorte, ninguém percebe como o texto está fraco."
  "Nessa noite você sai para beber com amigos e não fica bêbado. Estranha, bebe mais, e não fica bêbado. Bebe pra caralho e nada. Vai para casa com prejuízo e nenhum samba."
  "Acordo com uma ressaca enorme e um enjôo ainda maior. De repente, toda a noite passada volta com tudo e você corre para vomitar no trono de porcelana. Enquanto está ali, se espanta, são.. letras? Sim, você vomitou letras, letras que dizem PERDEU"
  $ renpy.full_restart()
  
label go2_materia:
  scene bg black #trocar
  
  "A direção da Sabesp lhe responde que Atlantis é uma pesquisa sobre alternativas para a crise hídrica. Você pede dados dessa pesquisa e recebe dados genéricos como resposta. É tudo obviamente uma farsa. Uma semana depois, você publica a matéria que é capa do caderno Cotidiano. Após a edição de seu texto por seu chefe, Atlantis é publicado como um belo programa de resgate das águas paulistas."
  "Naquela noite você tenta bater uma punheta antes de dormir, mas brocha um GAME OVER."
  $ renpy.full_restart()
  
label go3_prisao:
  scene bg black #trocar
  
  "De repente, três homens de terno negro entram na sala e se dirigem rapidamente até você. Fudeu. Assustado, não tem tempo de fazer nada antes de ouvir:"
   
  p "Venha com a gente, senhor. Por favor."
   
  "Você pensa em responder alguma coisa, levanta o dedo para se defender e.. desiste. Não fala coisa alguma. A sensação de impotência está estampada na sua cara, que se levanta e acompanha os homens."
  "No dia seguinte, seu próprio jornal estampa a matéria: jornalista preso por suspeita de invadir sistema do governo estadual. Após alguns meses você vai a julgamento e as provas são irrefutáveis, você foi pego em flagrante e agora vai amargar alguns anos horríveis em uma prisão genérica."
  "A comida é horrível e você demora até se acostumar com o código de honra e força que rege a vida na cela. Com o tempo você adota uma parede e todo dia marca nela um tracinho novo."
  "Seus colegas de cárcere pensam que você está contando os dias de prisão, mas nenhum deles entende que na verdade você está, aos poucos, com muita paciência, escrevendo uma mensagem no concreto, hábito de jornalista, escrevendo uma mensagem para as gerações futuras, elas precisam saber a verdade, todos precisam saber que você GAME OVER."
  $ renpy.full_restart()

label go4_folha:
  scene bg black #trocar
  
  "Mesmo já sendo de madrugada, seu editor te responde em pouco tempo, com uma linha apenas:"
   
  e "Fred.. como você conseguiu esse documento?"
  f "Consegui com uma fonte anônima chamada Cão Raposa, que eu não vou revelar quem é"
  e "Então, infelizmente não poderemos publicar esse texto. Inclusive, Fred, provavelmente esse conteúdo é ilegal. Recebemos hoje mesmo um contato do governo estadual dizendo que o sistema deles foi hackeado durante a coletiva desta tarde e que qualquer material publicado com aquele conteúdo teria sérias implicações para o jornal."
  e "Nunca imaginei que você teria relação com isso. Me desculpe. Eu fiz o que deveria fazer, acabei de enviar seu email para eles. Não posso ser cúmplice. Desculpe mesmo. Estou te avisando por companheirismo, porque nos conhecemos há anos. Mas você cometeu um erro primário, deveria saber que não aceitaríamos conteúdo ilegal."
   
  "Merda. Merdamerdamerdamerda. Você pensa em fugir, em pegar seus bens mais valiosos colocar tudo numa mochila e fugir para a casa daquela gringa que se mudou para Ibitipoca e foi ser guia turístico quando você visitou o parque há alguns meses."
  "Britney. É isso. Britney, você lembra dela, loira, gostosona, foi sua guia no último passeio, vocês se amassaram numa curva especialmente linda do rio e ela sempre deixou claro que te receberia por lá sempre que você quisesse voltar. É isso. Britney vai te salvar." 
  "Enquanto você divaga sobre seu caso norte americando, ouve um carro estacionando bruscamente em sua porta. Olha pela janela e lá estão os mesmos três homens de terno preto que você viu esta tarde na coletiva. Em pouco tempo eles derrubam a porta de sua casa e te levam embora."
   
  p "Você é burro?"
  p2 "Não conhece a hashtag #podemostirarseacharmelhor?"
  p3 "Shh, não conversem com os mortos"
   
  "Seu corpo nunca é encontrado. Os peixes da represa Guarapiranga começam comendo as partes moles do seu rosto. Um fenômeno estranho faz com que um cardume especialmente voraz de manjubinhaa coma a sua pele da bochecha num padrão de mordidas que desenha sua pele, parece, espera, é isso, parece que na sua bochecha esquerda elas escreveram, com os dentes, as palavras GAME OVER."
  $ renpy.full_restart()

label go5_publica:
  scene bg black #trocar
  
  "Um sexto sentido pulsa no fundo da sua cabeça. Talvez a Folha de São Paulo esteja envolvida demais com o governo do estado para publicar essa matéria. Talvez seja melhor tentar outro caminho. É, parece que é isso. Chega dessa vida de jornalismo institucional, trabalhar como proletário da notícia para a velha mídia. Hora de mudar."
  "Você manda a matéria para A Pública e no dia seguinte recebe a resposta positiva. \"Sim, adoramos, vamos publicar! Como você conseguiu esse orçamento?\". A matéria sai impecável e joga merda no ventilador. O governo do estado precisa se explicar em uma série de coletivas."
  "A resposta oficial diz que \"promoção de escassez\" foi um erro de grafia, o que deveria estar escrito era \"prevenção de escassez\". Farto material de pesquisa corrobora essa afirmação. E afinal, que interesse teria o governo em promover a falta dágua?"
  "Incrivelmente, essa versão cola junto à velha mídia. Você perde o emprego na Folha de São Paulo e se desespera ao perceber que a versão oficial passa a ser a versão comprada pelos veículos tradicionais. Sua investigação continua por conta própria, mas há pouco que você consegue descobrir sem o acesso facilitado que te permitiu o Cão Raposa."
  "No fim das contas, você balança levemente a estrutura da Sabesp mas não consegue nenhuma mudança substancial. Bom, pelo menos agora você se tornou um profissional independente com disponibilidade para seguir as pautas que te interessarem." 
  "O dinheiro é uma merda. A repercussão de seu trabalho é quase nenhuma. Seu impacto no governo estadual tendeu ao zero. Bom, o que você queria? Mudar o mundo com o jornalismo? Faz me rir. Pelo menos agora você dorme melhor e isso é a única coisa que impede as enormes palavras GAME OVER de se formarem sobre sua cabeça quando você dorme e sonha com um mundo diferente. Parabéns por ter se transformado em outra coisa antes que fosse tarde demais."
  $ renpy.full_restart()

