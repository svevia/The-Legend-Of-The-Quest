'''Fonction du début du jeu où le joueur choisi sa classe est son pseudo
C'est à partir de cette fonction que le joueur est crée ainsi que la plupart des class,
Ensuite ces classe sont retournés dans les binds pour être utilisé dans toutes
les fonctions du jeu'''

import pygame,time,random
from pygame.locals import *
from module.statistiques import *
from module.worldmap_v1 import *
from module.menu_auberge_combat import *
from module.generation_map import *
from module.population import *
from module.objet import *
from module.story import *
from module.compagnon import *



#Première génération de la carte qui va donc initialiser les biomes
def genere(fen1,personnage,GestionPop,item,comp):
    
    #choisis aléatoirement une carte
    personnage.cartenum = random.randint(1,2)
    
    varA,varB,varC,varG,varR,varP,varQ,varZ,varM = GenerationMap(fen1,GestionPop,0,0,0,personnage)
    carte = world(fen1,personnage,item,comp)
    carte.varA,carte.varB,carte.varC,carte.varG,carte.varR,carte.varP,carte.varQ,carte.varZ,carte.varM = varA,varB,varC,varG,varR,varP,varQ,varZ,varM
    return carte


#Fonction actualisant le menu action lorsque le joueur écrit son nom ou clic sur la case à cocher
def MAJ_classe(fen1,case,position_case,font,textepseudo,fond,name,couleur):
    fen1.blit(fond, (0,0))
    fen1.blit(case, position_case)
    texte1 = font.render("Desactiver la cinématique",1,(206,206,206))
    fen1.blit(texte1, (435,670))
    fen1.blit(textepseudo,(350,100))
    block = font.render(name,1,(255, 255, 255))
    rect = block.get_rect()
    rect = rect.move(460, 100)
    fen1.blit(block, rect)
    pygame.draw.rect(fen1,couleur,(450,90,260,40),2)
    pygame.display.flip()



def ChoixClasse(fen1):
    pygame.init()

    fen1 = pygame.display.set_mode((1024,768),pygame.NOFRAME)
    pygame.display.set_caption("Classe")
    font = pygame.font.SysFont(None, 32)
    textepseudo = font.render("Pseudo:",True,(255, 255, 255))
    fond = pygame.image.load("img/menuClasse.png").convert()

    name = ""
    personnage = ""
    couleur = (255,255,255) #couleur du cadre autour du pseudo, change si oubli lors de la validation


    item = objet()
    GestionPop = pop()
    auberge = CombatAuberge()
    story = quete()
    
    case = pygame.image.load("img/case-a-coche.png").convert_alpha()
    position_case = case.get_rect()
    position_case = position_case.move(350, 650)
    MAJ_classe(fen1,case,position_case,font,textepseudo,fond,name,couleur)
    

    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_1: #paladin
                    if name != "":
                        personnage = Stats(str(name),"paladin",70,70,8,10,10,7)
                        comp = compagnon(0,0,personnage)
                        carte = genere(fen1,personnage,GestionPop,item,comp)
                        return personnage,carte,auberge,GestionPop,item,story,comp
                    else:
                        couleur = (255,10,10)
                        MAJ_classe(fen1,case,position_case,font,textepseudo,fond,name,couleur)
                        
                elif event.key == K_2: #mage
                    if name != "":
                        personnage = Stats(str(name),"mage",50,50,15,5,5,3)
                        comp = compagnon(0,0,personnage)
                        carte = genere(fen1,personnage,GestionPop,item,comp)
                        return personnage,carte,auberge,GestionPop,item,story,comp
                    else:
                        couleur = (255,10,10)
                        MAJ_classe(fen1,case,position_case,font,textepseudo,fond,name,couleur)
                        
                elif event.key == K_3: #voleur
                    if name != "":
                        personnage = Stats(str(name),"voleur",60,60,12,15,7,5)
                        comp = compagnon(0,0,personnage)
                        carte = genere(fen1,personnage,GestionPop,item,comp)
                        return personnage,carte,auberge,GestionPop,item,story,comp
                    else:
                        couleur = (255,10,10)
                        MAJ_classe(fen1,case,position_case,font,textepseudo,fond,name,couleur)

                    
                elif event.key == K_BACKSPACE:
                        name = name[:-1]
                        MAJ_classe(fen1,case,position_case,font,textepseudo,fond,name,couleur)
                        
                elif event.unicode.isalpha() and len(name) <= 12: #Vérifie si le joueur à écrit une lettre et si la taille du pseudo est <12
                        name += event.unicode
                        MAJ_classe(fen1,case,position_case,font,textepseudo,fond,name,couleur)
                elif event.key == K_SPACE and len(name) <= 12:
                        name += " "
                        MAJ_classe(fen1,case,position_case,font,textepseudo,fond,name,couleur)

            if event.type == MOUSEBUTTONDOWN and event.button == 1: #Vérifie si le joueur à cliquer sur la case pour désactiver la cinématique
                position = pygame.mouse.get_pos()
                if position_case.collidepoint(position) == True:
                    if story.cinematique == True:
                        story.cinematique = False
                        case = pygame.image.load("img/case_coche.png").convert_alpha()
                        MAJ_classe(fen1,case,position_case,font,textepseudo,fond,name,couleur)
                    elif story.cinematique == False:
                        story.cinematique = True
                        case = pygame.image.load("img/case-a-coche.png").convert_alpha()
                        MAJ_classe(fen1,case,position_case,font,textepseudo,fond,name,couleur)


                        

