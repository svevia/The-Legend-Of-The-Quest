import pygame,random,time
import module.bind
from module.menu_action import *
from module.quete import *

class Quete_assaut:

    def __init__(self,fen1,personnage):
        self.bataille = 1
        self.soldat = 1000
        self.ennemi = random.randint(1000,1300)
        self.unite = 100
        self.front1,self.front2,self.front3 = 0,0,0
        self.frontjoueur = 1

        if personnage.classe == "mage":
            self.tete = pygame.image.load("img/heretique/teteHeretique.png").convert_alpha()
        elif personnage.classe == "paladin":
            self.tete = pygame.image.load("img/paladin/tetepaladin.png").convert_alpha()
        elif personnage.classe == "voleur":
            self.tete = pygame.image.load("img/assassin/teteAssassin.png").convert_alpha()

        
        self.placement(fen1)

    def placement(self,fen1):
        pygame.display.set_caption("Placement_assaut")
        fond = pygame.image.load("img/bataille.png").convert()
        pygame.key.set_repeat(300, 300)
        font = pygame.font.SysFont(None, 30)

        
        text_soldat = font.render(str(self.soldat) ,1,(206,206,206))
        text_front1 = font.render(str(self.front1) ,1,(206,206,206))
        text_front2 = font.render(str(self.front2) ,1,(206,206,206))
        text_front3 = font.render(str(self.front3) ,1,(206,206,206))
        text_ennemi = font.render(str(self.ennemi) ,1,(206,206,206))

        
        fen1.blit(fond,(0,0))
        fen1.blit(text_soldat,(550,520))
        fen1.blit(text_front1,(250,360))
        fen1.blit(text_front2,(550,360))
        fen1.blit(text_front3,(850,360))
        fen1.blit(text_ennemi,(480,90))

        if self.bataille < 5:
            fen1.blit(self.tete,(140+300*(self.frontjoueur -1),350))
        else:
            fen1.blit(self.tete,(440,510))
            self.frontjoueur = 0

        pygame.display.flip()


    def placement_ennemi(self,fen1,personnage):
        egalite = lambda x,y,z : abs(x-y)<= abs(z)
        self.efront1,self.efront2,self.efront3 = 0,0,0
        if egalite(self.ennemi,self.soldat,self.ennemi*0.02) == True:
            self.efront1 = int(self.ennemi/3) + random.randint(-int(0.1*self.ennemi),int(0.1*self.ennemi))
            self.ennemi -= self.efront1
            self.efront2 = int(self.ennemi/2) + random.randint(-int(0.1*self.ennemi),0.1*self.ennemi)
            self.ennemi -= self.efront2
            self.efront3 = self.ennemi
            self.ennemi = 0

        elif self.ennemi < self.soldat:
            frontchoisis = random.randint(1,3)
            if frontchoisis == 1:
                self.efront2 = random.randint(0,int(self.ennemi*0.1))
                self.ennemi -= self.efront2
                self.efront3 = random.randint(0,int(self.ennemi*0.1))
                self.ennemi -= self.efront3
                self.efront1 = self.ennemi
                self.ennemi = 0

            if frontchoisis == 2:
                self.efront1 = random.randint(0,int(self.ennemi*0.1))
                self.ennemi -= self.efront1
                self.efront3 = random.randint(0,int(self.ennemi*0.1))
                self.ennemi -= self.efront3
                self.efront2 = self.ennemi
                self.ennemi = 0

            if frontchoisis == 3:
                self.efront1 = random.randint(0,int(self.ennemi*0.1))
                self.ennemi -= self.efront1
                self.efront2 = random.randint(0,int(self.ennemi*0.1))
                self.ennemi -= self.efront2
                self.efront3 = self.ennemi
                self.ennemi = 0

        else: #si l'IA est en large superiorité numérique
            strategie = random.randint(1,2)
            if strategie == 1: #l'IA se place sur tous les fronts
                self.efront1 = int(self.ennemi/3) + random.randint(-int(0.15*self.ennemi),int(0.15*self.ennemi))
                self.ennemi -= self.efront1
                self.efront2 = int(self.ennemi/2) + random.randint(-int(0.15*self.ennemi),int(0.15*self.ennemi))
                self.ennemi -= self.efront2
                self.efront3 = self.ennemi
                self.ennemi = 0
            if strategie ==2: #l'IA concentre ses forces sur 1 seul front
                frontchoisis = random.randint(1,3)
                if frontchoisis == 1:
                    self.efront2 = random.randint(0,int(self.ennemi*0.15))
                    self.ennemi -= self.efront2
                    self.efront3 = random.randint(0,int(self.ennemi*0.15))
                    self.ennemi -= self.efront3
                    self.efront1 = self.ennemi
                    self.ennemi = 0

                if frontchoisis == 2:
                    self.efront1 = random.randint(0,int(self.ennemi*0.15))
                    self.ennemi -= self.efront1
                    self.efront3 = random.randint(0,int(self.ennemi*0.15))
                    self.ennemi -= self.efront3
                    self.efront2 = self.ennemi
                    self.ennemi = 0

                if frontchoisis == 3:
                    self.efront1 = random.randint(0,int(self.ennemi*0.15))
                    self.ennemi -= self.efront1
                    self.efront2 = random.randint(0,int(self.ennemi*0.15))
                    self.ennemi -= self.efront2
                    self.efront3 = self.ennemi
                    self.ennemi = 0



        self.Calcul_Combat(fen1,personnage)
        

    def Calcul_Combat(self,fen1,personnage):
        
        egalite = lambda x,y,z : abs(x-y)<= abs(z)
        #calcul front 1
        if self.frontjoueur != 1:
            if egalite(self.efront1,self.front1,0.10*self.efront1) == True:
                self.perte_efront1 = random.randint(int(self.front1*0.05),int(self.efront1*0.15))
                self.perte_front1 = random.randint(int(self.front1*0.05),int(self.front1*0.15))
            elif self.efront1 + 0.10*self.front1 <= self.front1:
                self.perte_efront1 = random.randint(int(self.efront1*0.6),int(self.efront1*0.8))
                self.perte_front1 = random.randint(int(self.front1*0.05),int(self.front1*0.15))
            else:
                self.perte_efront1 = random.randint(int(self.efront1*0.05),int(self.efront1*0.15))
                self.perte_front1 = random.randint(int(self.front1*0.6),int(self.front1*0.8))

            if self.front1 <= 10 : self.perte_efront1 = 0
            if self.efront1 <= 10 : self.perte_front1 = 0
            
            self.front1 -= self.perte_front1
            self.efront1 -= self.perte_efront1


        if self.frontjoueur != 2:
            if egalite(self.efront2,self.front2,0.10*self.efront2) == True:
                self.perte_efront2 = random.randint(int(self.front2*0.05),int(self.efront2*0.15))
                self.perte_front2 = random.randint(int(self.front2*0.05),int(self.front2*0.15))
            elif self.efront2 + 0.10*self.front2 <= self.front2:
                self.perte_efront2 = random.randint(int(self.efront2*0.6),int(self.efront2*0.8))
                self.perte_front2 = random.randint(int(self.front2*0.05),int(self.front2*0.15))
            else:
                self.perte_efront2 = random.randint(int(self.efront2*0.05),int(self.efront2*0.15))
                self.perte_front2 = random.randint(int(self.front2*0.6),int(self.front2*0.8))

            if self.front2 <= 10 : self.perte_efront2 = 0
            if self.efront2 <= 10 : self.perte_front2 = 0
            
            self.front2 -= self.perte_front2
            self.efront2 -= self.perte_efront2


        if self.frontjoueur != 3:
            if egalite(self.efront3,self.front3,0.10*self.efront3) == True:
                self.perte_efront3 = random.randint(int(self.front3*0.05),int(self.efront3*0.15))
                self.perte_front3 = random.randint(int(self.front3*0.05),int(self.front3*0.15))
            elif self.efront3+ 0.10*self.front3 <= self.front3:
                self.perte_efront3 = random.randint(int(self.efront3*0.6),int(self.efront3*0.8))
                self.perte_front3 = random.randint(int(self.front3*0.05),int(self.front3*0.15))
            else:
                self.perte_efront3 = random.randint(int(self.efront3*0.05),int(self.efront3*0.15))
                self.perte_front3 = random.randint(int(self.front3*0.6),int(self.front3*0.8))

            if self.front3 <= 10 : self.perte_efront3 = 0
            elif self.efront3 <= 10 : self.perte_front3 = 0
            
            self.front3 -= self.perte_front3
            self.efront3 -= self.perte_efront3



        if self.bataille == 5:
            boss = 404
        else:
            boss = random.randint(401,402)




        if self.frontjoueur == 0:
            somme_front = self.front1 + self.front2 + self.front3 + self.soldat
            somme_front_ennemi = self.efront1 + self.efront2 + self.efront3 + self.ennemi
            if egalite(somme_front_ennemi,somme_front,0.10*somme_front_ennemi) == True:
                module.bind.creaCombat(fen1,random.randint(301,303),boss,1,2)
            elif somme_front_ennemi + 0.10*somme_front <= somme_front:
                module.bind.creaCombat(fen1,boss,1,1,1)
            else:
                module.bind.creaCombat(fen1,random.randint(301,303),boss,random.randint(301,303),3)


        if self.frontjoueur == 1:
            if egalite(self.efront1,self.front1,0.10*self.efront1) == True:
                module.bind.creaCombat(fen1,random.randint(301,303),boss,1,2)
            elif self.efront1 + 0.10*self.front1 <= self.front1:
                module.bind.creaCombat(fen1,boss,1,1,1)
            else:
                module.bind.creaCombat(fen1,random.randint(301,303),boss,random.randint(301,303),3)


        if self.frontjoueur == 2:
            if egalite(self.efront2,self.front1,0.10*self.efront2) == True:
                module.bind.creaCombat(fen1,random.randint(301,303),boss,1,2)
            elif self.efront2 + 0.10*self.front2 <= self.front2:
                module.bind.creaCombat(fen1,boss,1,1,1)
            else:
                module.bind.creaCombat(fen1,random.randint(301,303),boss,random.randint(301,303),3)


        if self.frontjoueur == 3:
            if egalite(self.efront3,self.front3,0.10*self.efront3) == True:
                module.bind.creaCombat(fen1,random.randint(301,303),boss,1,2)
            elif self.efront3 + 0.10*self.front3 <= self.front3:
                module.bind.creaCombat(fen1,boss,1,1,1)
            else:
                module.bind.creaCombat(fen1,random.randint(301,303),boss,random.randint(301,303),3)
            

    def Affichage_rapport(self,fen1,personnage,carte,item,comp,story):
        
        if self.frontjoueur == 1:
            if personnage.BatailleVictoire == 1:
                self.perte_efront1 = random.randint(int(self.efront1*0.6),int(self.efront1*0.8))
                self.perte_front1 = random.randint(int(self.front1*0.05),int(self.front1*0.15))

            else:
                self.perte_efront1 = random.randint(int(self.efront1*0.05),int(self.efront1*0.15))
                self.perte_front1 = random.randint(int(self.front1*0.6),int(self.front1*0.8))

                            
            self.front1 -= self.perte_front1
            self.efront1 -= self.perte_efront1




        if self.frontjoueur == 2:
            if personnage.BatailleVictoire == 1:
                self.perte_efront2 = random.randint(int(self.efront2*0.6),int(self.efront2*0.8))
                self.perte_front2 = random.randint(int(self.front2*0.05),int(self.front2*0.15))

            else:
                self.perte_efront2 = random.randint(int(self.efront2*0.05),int(self.efront2*0.15))
                self.perte_front2 = random.randint(int(self.front2*0.6),int(self.front2*0.8))

                            
            self.front2 -= self.perte_front2
            self.efront2 -= self.perte_efront2


        if self.frontjoueur == 3:
            if personnage.BatailleVictoire == 1 :
                self.perte_efront3 = random.randint(int(self.efront3*0.6),int(self.efront3*0.8))
                self.perte_front3 = random.randint(int(self.front3*0.05),int(self.front3*0.15))

            else:
                self.perte_efront3 = random.randint(int(self.efront3*0.05),int(self.efront3*0.15))
                self.perte_front3 = random.randint(int(self.front3*0.6),int(self.front3*0.8))

                            
            self.front3 -= self.perte_front3
            self.efront3 -= self.perte_efront3
            

        self.ennemi = self.efront1 + self.efront2 + self.efront3 + self.ennemi
        self.soldat = self.front1 + self.front2 + self.front3 + self.soldat
        
        fond = pygame.image.load("img/rapport.png").convert()
        font = pygame.font.SysFont(None, 25)
        pygame.display.set_caption("Rapport_assaut")
        fen1.blit(fond,(0,0))


        text_front1 = font.render(str(self.front1) + " (-" + str(self.perte_front1) + ")" ,1,(206,206,206))
        text_front2 = font.render(str(self.front2) + " (-" + str(self.perte_front2) + ")" ,1,(206,206,206))
        text_front3 = font.render(str(self.front3) + " (-" + str(self.perte_front3) + ")" ,1,(206,206,206))


        text_efront1 = font.render(str(self.efront1) + " (-" + str(self.perte_efront1) + ")" ,1,(206,206,206))
        text_efront2 = font.render(str(self.efront2) + " (-" + str(self.perte_efront2) + ")" ,1,(206,206,206))
        text_efront3 = font.render(str(self.efront3) + " (-" + str(self.perte_efront3) + ")" ,1,(206,206,206))



        fen1.blit(fond,(0,0))
        fen1.blit(text_front1,(230,360))
        fen1.blit(text_front2,(530,360))
        fen1.blit(text_front3,(830,360))

        fen1.blit(text_efront1,(180,90))
        fen1.blit(text_efront2,(480,90))
        fen1.blit(text_efront3,(780,90))
        fen1.blit(self.tete,(140+300*(self.frontjoueur -1),350))

        if self.bataille < 4:
            text_suivant = font.render("1.Passer à la phase " + str(self.bataille + 1),1,(206,206,206))
        elif self.bataille == 4:
            text_suivant = font.render("1.Passer à la phase finale",1,(206,206,206))
        else:text_suivant = font.render("",1,(206,206,206))
            
        fen1.blit(text_suivant,(450,500))

        pygame.display.flip()
        
        if self.frontjoueur == 0:
            font = pygame.font.SysFont(None, 32)
            if personnage.BatailleVictoire == 1:
                personnage.bataille = 1
                story.activation_quetes[7] = 2
                texte1 = font.render("Nous avons réussi ! Regardez ils s'enfuient !",1,(206,206,206))
                pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
                fen1.blit(texte1,(10,580))
                pygame.display.flip()
                time.sleep(3)
                Action(fen1)
                quete = quest_ID(fen1,7,personnage,item,story,comp,carte)


            if personnage.BatailleVictoire == 0:
                story.activation_quetes[7] = 2
                personnage.bataille = 0
                texte1 = font.render("Oh non ! c'est impossible ! Nous devons fuir au plus vite !",1,(206,206,206))
                pygame.draw.rect(fen1,(3,34,76),(0,568,1024,200))
                fen1.blit(texte1,(10,580))
                pygame.display.flip()
                time.sleep(3)
                carte.reprise(fen1,personnage,item,comp)
                quete = quest_ID(fen1,7,personnage,item,story,comp,carte)
     
        self.front1,self.front2,self.front3 = 0,0,0
        if self.soldat <= 50 : self.unite = 10
        else:self.unite = round((self.soldat/100))*10 #nombres de soldats ajoutés à chaque clic pour le positionnement



        
