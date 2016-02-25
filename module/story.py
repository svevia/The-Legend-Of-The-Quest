import pygame,time
from module.menu_action import *
from module.quete import *


'''Cette class gère l'histoire générale du jeu, elle affiche la cinématique de début et sauvegarde
l'atat de chacunes de suqêtes ainsi que les objectifs en cours'''



class quete:
    def __init__(self):
        self.cinematique = True
        self.activation_quetes = [0,0,0,0,0,0,0,0,0,0,0] #liste contenant l'état de chaques quêtes (0:inactive, 1:en réalisation, 2:à rendre, 3 :finit)
        self.objectif_quetes = [0,0,0,0,0,0,0,0,0,0,0] #liste contenant les objectifs restant pour chaques quêtes (monstres à tuer...)
                                         #si 0: la quête correspondante est inactive ou terminée
        
    def Affichage_cine(self,fen1,personnage,carte,item,comp):

        
        #Cette fonction affiche la cinématique du début de jue, celle-ci n'est pas
        #identique pour chaques classes
        
        self.font = pygame.font.SysFont(None, 32)
        pygame.display.set_caption("Cinématique")
        self.fond = pygame.image.load('img/map/noir.png')


        self.texte1 = self.font.render("Vous voilà revenu dans le village de votre enfance.",1,(206,206,206))
        self.texte2 = self.font.render("Mais quelque chose est différent...",1,(206,206,206))
        self.texte3 = self.font.render("Il y a une odeur âcre dans l'air, une odeur de soufre.",1,(206,206,206))
        self.texte4 = self.font.render("La peur se lit dans les yeux des habitants, d'habitude serain.",1,(206,206,206))

        self.affichage_texte_cine(fen1)

        if personnage.classe == "paladin":
            self.texte1 = self.font.render("L'entrainement au combat que vos parents vous ont fait subir vous sera sûrement très utile...",1,(206,206,206))
            self.texte2 = self.font.render(personnage.pseudo + ", faites votre possible pour aider les habitants de cette région !",1,(206,206,206))
            self.texte3 = self.font.render("Mais attention car elle est dangereuse en ces temps troublés.",1,(206,206,206))
            self.texte4 = self.font.render("Les soldats impériaux sont au front : vous n'aurez aucun soutient, aucune aide....",1,(206,206,206))

        elif personnage.classe == "mage":
            self.texte1 = self.font.render("Vous ressentez une aura magique très puissante dans ces lieux.",1,(206,206,206))
            self.texte2 = self.font.render(personnage.pseudo + ", trouvez et comprenez ce qu'il se passe ici !",1,(206,206,206))
            self.texte3 = self.font.render("Mais attention la région est dangereuse en ces temps troublés.",1,(206,206,206))
            self.texte4 = self.font.render("Vos frères et soeurs sont tombés aux mains de l'Eglise, vous êtes seul !",1,(206,206,206))

        elif personnage.classe == "voleur":
            self.texte1 = self.font.render("Vous remarquez tout de suite que quelque chose ne va pas !",1,(206,206,206))
            self.texte2 = self.font.render(personnage.pseudo + ", c'est à vous de rechercher la cause de ces perturbations.",1,(206,206,206))
            self.texte3 = self.font.render("Affûtez vos lames et n'oubliez jamais que vous ne pouvez vous fier qu'à elles...",1,(206,206,206))
            self.texte4 = self.font.render("La confrérie ne vous viendra pas en aide, vous combatterez seul avec vos lames !",1,(206,206,206))


        time.sleep(4)
        self.affichage_texte_cine(fen1)
        time.sleep(4)

        
        carte.affichage(fen1,personnage,item,comp)
        self.fond.set_alpha(255)
        fen1.blit(self.fond, (0,0))
        carte.contour(fen1,personnage)
        pygame.display.flip()
        self.fond_alpha = self.fond.get_alpha()
        while self.fond_alpha > 0:
            carte.affichage(fen1,personnage,item,comp)
            self.fond.set_alpha(self.fond_alpha - 15)
            fen1.blit(self.fond, (0,0))
            self.fond_alpha = self.fond.get_alpha()
            carte.contour(fen1,personnage)
            pygame.display.flip()
            time.sleep(0.1)


    def affichage_texte_cine(self,fen1):
        #cette fonction affiches progressivement les textes pendants la cinématique
        pygame.display.set_caption("Cinématique")
        fen1.blit(self.fond, (0,0))
        pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
        fen1.blit(self.texte1,(10,580))
        pygame.display.flip()
        time.sleep(2)
        fen1.blit(self.texte2,(10,610))
        pygame.display.flip()
        time.sleep(2)
        fen1.blit(self.texte3,(10,640))
        pygame.display.flip()
        time.sleep(2)
        fen1.blit(self.texte4,(10,670))
        pygame.display.flip()


    def verification_quetes(self,fen1,personnage,item,comp,carte):
        #vérifie si certaines quêtes ont été terminé à la fin de chaques combat
        #Si c'est le cas, les textes de ces quêtes sont affichés en conséquences
        for i in range (0,len(self.activation_quetes)):
            if self.activation_quetes[i] == 1 and self.objectif_quetes[i] == 0:
                quete = quest_ID(fen1,i,personnage,item,self,comp,carte)
                pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
                fen1.blit(quete.textfinit,(10,580))
                pygame.display.flip()
                time.sleep(3)
                self.activation_quetes[i] = 2
                carte.affichage(fen1,personnage,item,comp)
        carte.reprise(fen1,personnage,item,comp)

    def echec_quetes(self,fen1,personnage,item,comp,carte):
        if self.activation_quetes[5] == 1 and comp.ami == 0:
                quete = quest_ID(fen1,5,personnage,item,self,comp,carte)
                pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
                fen1.blit(quete.textEchec,(10,580))
                pygame.display.flip()
                time.sleep(2)
                self.activation_quetes[i] = 0
                carte.affichage(fen1,personnage,item,comp)
        carte.reprise(fen1,personnage,item,comp)




                        

    
