import pygame
from module.compagnon import *


def compagnonAuberge(fen1,personnage,item,carte,comp,story):
    fond = pygame.image.load("img/menuAuberge.png").convert()
    fen1.blit(fond,(0,0))
    pygame.display.set_caption("Auberge Compagnon")
    
    fondtext = pygame.font.SysFont(None, 25)


    if carte.lettre == "V":
        biome_autour = carte.varA
    elif carte.lettre == "S":
        biome_autour = carte.varB
    elif carte.lettre == "D" or carte.lettre == "N":
        biome_autour = carte.varC


    if biome_autour == "desert":
        compagnonAuberge = compagnon(0,16,personnage)
        personnage.nouveauCompagnonID = 16

        text1 = fondtext.render("Bonjour aventurier. Je me nomme Karsus et je suis un fier guerrier Galakran !",1,(206,206,206))
        text2 = fondtext.render("Malheureusement, mon peuple connait une époque sombre, dirigé par des fourbes...",1,(206,206,206))
        text3 = fondtext.render("Ils contrôlent notre peuple pour leur seul profit afin d'assouvir leur soif de pouvoir !",1,(206,206,206))
        text4 = fondtext.render("Je recherche donc un compagnon pour une quête plus épique et surtout plus... lucrative !",1,(206,206,206))
        text5 = fondtext.render("Et un jour je pourrai libérer mon peuple du joug de ces scélérats.",1,(206,206,206))

    elif biome_autour == "marais":
        compagnonAuberge = compagnon(0,17,personnage)
        personnage.nouveauCompagnonID = 17

        text1 = fondtext.render("Bonjour mon chère ami. Je suis Iriszia, une puissante guerrière du peuple des elfes !",1,(206,206,206))
        text2 = fondtext.render("J'ai décidé de partir à l'aventure pour protéger mon peuple de la contamination.",1,(206,206,206))
        text3 = fondtext.render("Il paraît que vous aussi, vous cherchez à détruire cette abomination ?",1,(206,206,206))
        text4 = fondtext.render("Je vous propose donc de me joindre à vous, en échange d'un peu d'or, biensur !",1,(206,206,206))
        text5 = fondtext.render("Vous verrez que je manie l'épée avec une grande dextérité et mes ennemis meurent lentement...",1,(206,206,206))

    elif biome_autour == "plaine":
        compagnonAuberge = compagnon(0,18,personnage)
        personnage.nouveauCompagnonID = 18

        text1 = fondtext.render("Salutation jeune homme. Mon nom ? Il n'a pas d'importance. Il n'a plus d'importance !",1,(206,206,206))
        text2 = fondtext.render("Et cela, depuis très longtemps maintenant. Tout ce que vous avez besoin de savoir, c'est que",1,(206,206,206))
        text3 = fondtext.render("je suis un grand sorcier ! Mes pouvoirs dépassent l'entendement : je peux guérir des",1,(206,206,206))
        text4 = fondtext.render("plaies mortelles, ou en infliger... J'accepte de vous accompagner, en échange de pièces",1,(206,206,206))
        text5 = fondtext.render("d'or : cela coûte cher d'entretenir ma longue chevelure ! Oui, car chez les sorciers, la ",1,(206,206,206))
        text6 = fondtext.render("longueur de la chevelure montre la force de ceux-ci : je vous l'ai dit, je suis puissant !",1,(206,206,206))
        
        fen1.blit(text6,(150,300))



    fen1.blit(text1,(150,150))
    fen1.blit(text2,(150,180))
    fen1.blit(text3,(150,210))
    fen1.blit(text4,(150,240))
    fen1.blit(text5,(150,270))


    if personnage.argent >= 500 and (story.activation_quetes[5] == 0 or story.activation_quetes[5] == 3):
        if comp.ami == 1 : text7 = fondtext.render("1.Engager ce compagnon pour 500 d'or et laisser partir votre ancien camarade.",1,(206,206,206))
        else : text7 = fondtext.render("1.Engager ce compagnon pour 500 pièces d'or.",1,(206,206,206))
        text8 = fondtext.render("2.Retourner à l'auberge.",1,(206,206,206))
        fen1.blit(text8,(150,360))
    elif story.activation_quetes[5] == 1 or story.activation_quetes[5] == 2 :
        text7 = fondtext.render("1.Vous avez déjà le scientifique... Retournez à l'auberge",1,(206,206,206))
    else : text7 = fondtext.render("1.Vous n'avez pas asser d'argent, retourner à l'auberge.",1,(206,206,206))

    fen1.blit(text7,(150,330))
    

    pygame.display.flip()
