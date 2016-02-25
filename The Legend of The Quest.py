import pygame,time,os
from sys import exit
from pygame.locals import *
from module.bind import *
from module.menu_classe import *


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0) #permet de placer la fenêtre en haut à gauche de l'écran

pygame.init()

fen1 = pygame.display.set_mode((1024,768),pygame.NOFRAME) #pour retirer les bordures
pygame.display.set_caption("Depart")
fond = pygame.image.load("img/NewGame.png").convert()
fen1.blit(fond, (0,0))
pygame.display.flip()


continuer = 1
#Boucle infinie
while continuer == 1:

    '''L'ensemble de la gestion du transferts entre chaques menus est géré en externe, dans le module bind.py,
        c'est un fichiers unique qui de ce fait est le centre névralgique du programme,
        c'est de là que tous les menus sont appelés, c'est égalemet là la plupart des class
        sont crées. L'attribution des touches du clavier en fonction du menu où nous sommes
        se fait par l'intermediaire du titre de page (le caption)
        Ce titre est modifié pour chaque menus et de ce fait nous permet de savoir en permanence
        où le joueur est exactement est donc de le rediriger en fonction de ses actions sur le clavier.'''


#Choix valables sur toutes les pages
    caption = pygame.display.get_caption()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(1)

    
       #attribution des Bind en fonctions des titres

        if caption[1]=="Depart":
            BindDepart(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="Action":
            BindAction (fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="Auberge":
            BindAuberge(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="Combat auberge":
            BindLancerCombatAuberge(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="Combat d'ivrognes":
            BindCombatAuberge(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="Victoire Auberge":
            BindVictoireAuberge(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="Parie":
            BindParie(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="WorldMap":
            BindWorldMap(fen1,event)
            pygame.event.clear()
        elif caption[1]=="Console":
            BindConsole(fen1,event)
            pygame.event.clear()
        elif caption[1]=="MiniMap":
            BindMiniMap(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="Inventaire":
            BindInventaire(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="Forgeron_craft":
            BindForgeron_craft(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1] == "Alchimiste":
            BindAlchimiste(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="Vente":
            BindVente(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)            
        elif caption[1]=="Save":
            BindSave(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="Load":
            BindLoad(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)   

        elif caption[1]=="Pause":
            BindPause(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)  

        elif caption[1]=="Quetes":
            BindQuetes(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)

        elif caption[1]=="Aide":
            BindAide(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)

        elif caption[1]=="Combat":
            BindCombat(fen1,event)
            pygame.event.clear()
        elif caption[1]=="Combat2":
            BindCombat2(fen1,event)
            pygame.event.clear()
        elif caption[1]=="Choix":
            BindChoix(fen1,event)
            pygame.event.clear()
        elif caption[1]=="Victoire":
            BindVictoire(fen1,event)
            pygame.event.clear()
        elif caption[1]=="Défaite":
            BindDefaite(fen1,event)
            pygame.event.clear()

        elif caption[1]=="No CD retour":
            BindRetour(fen1,event)
            pygame.event.clear()
        elif caption[1]=="Attaque Speciale 1":
            BindASDirect(fen1,event)
            pygame.event.clear()
        elif caption[1]=="Attaque Speciale Multi":
            BindASChoix(fen1,event)
            pygame.event.clear()
        elif caption[1]=="Choix Speciale 1":
            BindAS_1_Multi(fen1,event)
            pygame.event.clear()
        elif caption[1]=="Choix Speciale 2":
            BindAS_2_Multi(fen1,event)
            pygame.event.clear()
        
        elif caption[1]=="Competences":
            BindCompetence(fen1,event)
            pygame.event.clear()

        elif caption[1]=="Event-taxe":
            BindEventTaxe(fen1,event)
            pygame.event.clear()
        elif caption[1]=="Event-messager":
            BindEventMessager(fen1,event)
            pygame.event.clear()
        elif caption[1]=="Event-Compagnon":
            BindEventCompagnon(fen1,event)
            pygame.event.clear()

        elif caption[1]=="Invent":
            BindInvent(fen1,event)
            pygame.event.clear()
        elif caption[1]=="Invent combat":
            BindInventCombat(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="Invent full combat":
            BindInventaireFull(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)  
        elif caption[1]=="Invent looter objet":
            BindInventaireLooter(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        
        elif caption[1]=="Choix_potion":
            BindChoixPotion(fen1,event)
            pygame.event.clear()
        elif caption[1] == "Choix_donner_ressources":
            BindChoixRessources(fen1,event)
            pygame.event.clear()
        elif caption[1] == "Choix quête 5":
            BindChoixQuete5(fen1,event)
            pygame.event.clear()
        elif caption[1] == "Choix quête 6":
            BindChoixQuete6(fen1,event)
            pygame.event.clear()
        elif caption[1] == "Placement_assaut":
            BindPlacementAssaut(fen1,event)
            pygame.event.clear()
        elif caption[1] == "Rapport_assaut":
            BindRapportAssaut(fen1,event)
            pygame.event.clear()
            
            
            
        elif caption[1]=="Menu Esclave":
            BindMenuEsclave(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)
        elif caption[1]=="Verification":
            BindAchatEsclave(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)

        elif caption[1]=="Auberge Compagnon":
            BindAubergeCompagnon(fen1,event)
            pygame.event.clear()
            time.sleep(0.2)




            
