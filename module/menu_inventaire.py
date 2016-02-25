import pygame
from pygame.locals import *


#Menu de l'inventaire
def Inventaire(fen1,item,personnage):
    
    fond = pygame.image.load("img/menuInventaire.png").convert()
    pygame.key.set_repeat(500, 500)
    
    fondtext = pygame.font.SysFont(None, 22)

    #Affiche les objets contenues dans l'inventaire.
    text0 = fondtext.render((str(item.affichage(item.ID0,personnage))) ,1,(206,206,206))
    text1 = fondtext.render((str(item.affichage(item.ID1,personnage))) ,1,(206,206,206))
    text2 = fondtext.render((str(item.affichage(item.ID2,personnage))) ,1,(206,206,206))
    text3 = fondtext.render((str(item.affichage(item.ID3,personnage))) ,1,(206,206,206))
    text4 = fondtext.render((str(item.affichage(item.ID4,personnage))) ,1,(206,206,206))
    text5 = fondtext.render((str(item.affichage(item.ID5,personnage))) ,1,(206,206,206))
    text6 = fondtext.render((str(item.affichage(item.ID6,personnage))) ,1,(206,206,206))
    text7 = fondtext.render((str(item.affichage(item.ID7,personnage))) ,1,(206,206,206))
    text8 = fondtext.render((str(item.affichage(item.ID8,personnage))) ,1,(206,206,206))
    text9 = fondtext.render((str(item.affichage(item.ID9,personnage))) ,1,(206,206,206))
    text10 = fondtext.render((str(item.affichage(item.IDArmure,personnage))) ,1,(206,206,206))
    text11 = fondtext.render((str(item.affichage(item.IDCasque,personnage))) ,1,(206,206,206))
    text12 = fondtext.render((str(item.affichage(item.IDPantalon,personnage))) ,1,(206,206,206))
    text13 = fondtext.render((str(item.affichage(item.IDArme,personnage))) ,1,(206,206,206))

    #Place les textes
    fen1.blit(fond,(0,0))
    fen1.blit(text0,(155,240))
    fen1.blit(text1,(310,240))
    fen1.blit(text2,(465,240))
    fen1.blit(text3,(620,240))
    fen1.blit(text4,(775,240))
    fen1.blit(text5,(155,340))
    fen1.blit(text6,(310,340))
    fen1.blit(text7,(465,340))
    fen1.blit(text8,(620,340))
    fen1.blit(text9,(775,340))
    fen1.blit(text10,(310,560))
    fen1.blit(text11,(465,560))
    fen1.blit(text12,(620,560))
    fen1.blit(text13,(465,450))
    
    pygame.display.flip()




#Fonction qui permet de changer le titre de l'inventaire lorsqu'il est appelé
#depuis la worldmap afin de garder le bind du retour sur la map.
def titreInventaireWorldmap(fen1,item):
    pygame.display.set_caption("Inventaire")



#Fonction qui permet de changer le titre de l'inventaire lorsqu'il est appelé
#depuis le combat afin de garder le bind de retour sur le combat.
def titreInventaireCombat(fen1,item):
    pygame.display.set_caption("Invent")




    
