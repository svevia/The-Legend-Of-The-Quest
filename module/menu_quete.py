import pygame
from module.quete import *


'''Ce menu rescence toutes les quêtes actives du joueur, c'est à dire:
-sois les quêtes que le joueur est entrain de réaliser (story.activation_quetes[i] == 1)
-sois les quêtes que le joueur a finit mais n'a pas rendu (story.activation_quetes[i] == 2)


Dans les autres cas, sois la quête est terminée sois elle n'est pasne ncore active, donc ce
menu n'affichera pas ces quêtes
'''


def Menu_quete(fen1,story,personnage,item,comp,carte):
    pygame.display.set_caption("Quetes")
    pygame.key.set_repeat(300, 300)
    fond = pygame.image.load("img/MenuQuete.png").convert()
    font_titre = pygame.font.SysFont(None, 32)
    font_desc = pygame.font.SysFont(None, 25)
    fen1.blit(fond, (0,0))
    pygame.display.flip()
    hauteur = 200


    #Cette boucle fait le tour de toutes les quêtes et affiche uniquement les quêtes qui sont actives
    #les quetes sont actives lorsque la valeur dans la liste story.activation_quetes[ID] a pour valeur 1
    #si la valeur est à 2, la quête est terminé mais pas encore rendue
    for i in range(0,len(story.activation_quetes)):
        if story.activation_quetes[i] == 1:
            quete = quest_ID(fen1,i,personnage,item,story,comp,carte)
            texte_titre = font_titre.render(quete.titre,1,(74,112,139))
            texte_desc = font_desc.render(quete.desc,1,(206,206,206))
            fen1.blit(texte_titre,(200,hauteur))
            fen1.blit(texte_desc,(200,hauteur+30))
            pygame.draw.line(fen1, (218,165,32), [80, hauteur+80], [950,hauteur+80], 3) #séparateur entre chaques quête de couleur or
            pygame.display.flip()
            hauteur += 120
            
        if story.activation_quetes[i] == 2:
            quete = quest_ID(fen1,i,personnage,item,story,comp,carte)
            texte_titre = font_titre.render(quete.titre,1,(74,112,139))
            texte_desc = font_desc.render(quete.rendre,1,(206,206,206))
            fen1.blit(texte_titre,(200,hauteur))
            fen1.blit(texte_desc,(200,hauteur+30))
            pygame.draw.line(fen1, (218,165,32), [80, hauteur+80], [950,hauteur+80], 3) #séparateur entre chaques quête de couleur or
            pygame.display.flip()
            hauteur += 120
