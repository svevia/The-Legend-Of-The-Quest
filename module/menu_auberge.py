import pygame
from module.bind import *
from module.statistiques import *


#Menu de l'auberge
def Auberge(fen1,personnage,item,carte):
    fond = pygame.image.load("img/menuAuberge.png").convert()
    pygame.display.set_caption("Auberge")
    
    fondtext = pygame.font.SysFont(None, 22)

    #Affiche les textes de l'auberge, avec la vie et l'or du personnage
    text1 = fondtext.render("Bienvenu à l'auberge, aventurier !" ,1,(206,206,206))
    text2 = fondtext.render("Vous voulez une chopine ? Un steak ?" ,1,(206,206,206))
    text3 = fondtext.render("Buvez une bière et récupérer 1 point de vie pour 5 pièces d'or.",1,(206,206,206))
    text4 = fondtext.render("Mangez un steak et récupérer 5 points de vie pour 20 pièces d'or.",1,(206,206,206))
    text5 = fondtext.render("Prendre une chambre pour la nuit pour 50 pièces et récupérer toute votre vie.",1,(206,206,206))
    text6 = fondtext.render("Votre vie est de : " + str(personnage.vie) + " / " + str(personnage.viemax), 1, (206,206,206))
    text7 = fondtext.render("Votre or est de : " + str(personnage.argent),1,(206,206,206))

    #Place les textes
    fen1.blit(fond,(0,0))
    fen1.blit(text1,(450,230))
    fen1.blit(text2,(450,260))
    fen1.blit(text3,(450,290))
    fen1.blit(text4,(450,320))
    fen1.blit(text5,(450,350))
    fen1.blit(text6,(450,380))
    fen1.blit(text7,(450,410))



    #Permet la navigation dans le menu, gérer par les binds ("boutons")
    #Les textes affichés dépendent de la vie et de l'argent
    textretour = fondtext.render("1.Retour au menu action",1, (206,206,206))

    if personnage.vie == personnage.viemax :
        textbiere = fondtext.render("Votre vie est au maximum !",1, (206,206,206))
    elif personnage.argent < 5 :
        textbiere = fondtext.render("Vous n'avez pas asser d'argent pour une bière !",1, (206,206,206))  
    else :
        textbiere = fondtext.render("2.Boire une bière",1, (206,206,206))

    
    if personnage.vie == personnage.viemax :
        textsteak = fondtext.render("",1,(206,206,206))
    elif personnage.vie > personnage.viemax - 5 and personnage.vie != personnage.viemax :
        textsteak = fondtext.render("Vous n'avez pas besoin de manger un steak !",1,(206,206,206))
    elif personnage.argent < 5 :
        textsteak = fondtext.render("Vous n'avez pas asser d'argent pour un steak !",1, (206,206,206))  
    else :
        textsteak = fondtext.render("3.Manger un steak",1, (206,206,206))

    if personnage.vie == personnage.viemax :
        textchambre = fondtext.render("",1,(206,206,206))
    elif personnage.argent < 50:
        textchambre = fondtext.render("Aucune chambre de libre !",1,(206,206,206))
    else :
        textchambre = fondtext.render("4.Prendre une chambre",1, (206,206,206))

    textcombatauberge = fondtext.render("5.Combats d'ivrognes",1, (206,206,206))


    if carte.lettre == "V":
        biome_autour = carte.varA
    elif carte.lettre == "S":
        biome_autour = carte.varB
    elif carte.lettre == "D" or carte.lettre == "N":
        biome_autour = carte.varC

    if biome_autour == "desert" and personnage.karus == 1:
        textComp = fondtext.render("6.Aller voir le galakran",1, (206,206,206))
    elif biome_autour == "marais" and personnage.iriszia == 1:
        textComp = fondtext.render("6.Aller voir l'elfette",1, (206,206,206))
    elif biome_autour == "plaine" and personnage.archimage == 1:
        textComp = fondtext.render("6.Aller voir le mage",1, (206,206,206))
    else : textComp = fondtext.render("",1, (206,206,206))



    #Place les "boutons"
    fen1.blit(textretour,(100,230))    
    fen1.blit(textbiere,(100,260))
    fen1.blit(textsteak,(100,290))
    fen1.blit(textchambre,(100,320))
    fen1.blit(textcombatauberge,(100,350))
    fen1.blit(textComp,(100,380))


    
    pygame.display.flip()


#Fonctions ajoutant de la vie contre de l'argent (1/5 et 5/20)    
def biere(fen1,personnage,item,carte):
    if personnage.vie < personnage.viemax and personnage.argent >= 5 :
        personnage.vie += 1
        personnage.argent -= 5
        Auberge(fen1,personnage,item,carte)

        
def steak(fen1,personnage,item,carte):
    if personnage.vie <= personnage.viemax - 5 and personnage.argent >= 20 :
        personnage.vie += 5
        personnage.argent -= 20
        Auberge(fen1,personnage,item,carte)

def chambre(fen1,personnage,item,carte):
    pygame.display.set_caption("Cinematique")
    fond = pygame.image.load("img/menuAuberge.png").convert()
    if personnage.vie < personnage.viemax  and personnage.argent >= 50 :
        personnage.vie = personnage.viemax
        personnage.argent -= 50
        noir = pygame.image.load('img/map/noir.png')
        noir.set_alpha(0)
        fen1.blit(noir, (0,0))
        pygame.display.flip()
        noir_alpha = noir.get_alpha()
        while noir_alpha < 255:
            fen1.blit(fond,(0,0))
            noir.set_alpha(noir_alpha + 15)
            fen1.blit(noir, (0,0))
            noir_alpha = noir.get_alpha()
            pygame.display.flip()
            time.sleep(0.1)
        time.sleep(2)
        while noir_alpha > 0:
            fen1.blit(fond,(0,0))
            noir.set_alpha(noir_alpha - 15)
            fen1.blit(noir, (0,0))
            noir_alpha = noir.get_alpha()
            pygame.display.flip()
            time.sleep(0.1)

        Auberge(fen1,personnage,item,carte)

