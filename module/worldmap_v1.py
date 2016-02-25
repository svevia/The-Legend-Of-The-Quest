#Importation des bibliothèques nécessaires
import pygame,random,os
from pygame.locals import *
from PIL import Image
from module.combat import *
from module.population import *
from module.menu_action import *
from module.event import *
from module.generation_map import *
from module.compagnon import *
from module.quete import *
import module.bind


'''
Class carte du jeu, c'est elle qui permet d'afficher la carte auparavant généré par generation_map.py
Cette class gère:
-le déclenchement aléatoire des combats
-le déclenchement aléatoire des events
-La gestion jours/nuit (un affichage d'une image noir +/- transparente)
-La collision avec le bord de la carte (le joueur ne peut pas marcher sur l'eau)
-L'affichage du biome où est le joueur
-La perte de points de vie si le joueur marche sur le biome contamine
-Le repérage du joueur sur la mini-map
-l'affichage de la jauge de vie, d'XP et du HUD(head-up display)
-la gestion de la console permettant d'executer des commandes depuis l'interface graphique
-le menu pause
'''


class world:
    #création de l'objet "carte" qui contient toutes les varibales nécessaire au gestion sur la carte
    def __init__(self,fen1,personnage,item,comp):
        pygame.init()
        self.debutEvent = random.randint(200000,500000) #déclenche un event quand arrive à 0
        self.debutCombat = random.randint(100,250) #déclenche un combat quand arrive à 0
        self.compteur = 0 # 0 =jour et 10 = nuit
        self.inverse = 0 # 0 = jour et 1 = nuit
        self.vitesse = 4
        self.nuit = 0 #reutiliser cette valeur pour les events
        self.tour = 10000 #temps en ms avant compteur -1
        self.next = pygame.time.get_ticks() + self.tour
        self.liste_event = [1,2,3,4,5,6,7] #Nombre d'event aléatoire possibles
        self.repousse = 0
        self.historique_console = [] #historique des commandes tapés dans la console depuis le dernier chargement
        self.cooldown_contamine = 30 #nombre de pas avant de perdre des points de vie dans le biome contamine

        #chargement des images du perso dans une liste en fonction de la classe
        self.fichier = []
        if personnage.classe == "paladin":
            self.tete = pygame.image.load("img/paladin/tetepaladin.png").convert_alpha()
            for i in range(1,33):
                self.fichier.append(pygame.image.load("img/paladin/Paladin"+str(i)+".png").convert_alpha())

        if personnage.classe == "mage":
            self.tete = pygame.image.load("img/heretique/teteHeretique.png").convert_alpha()
            for i in range(1,33):
                self.fichier.append(pygame.image.load("img/heretique/Heretique"+str(i)+".png").convert_alpha())

        if personnage.classe == "voleur":
            self.tete = pygame.image.load("img/assassin/teteAssassin.png").convert_alpha()
            for i in range(1,33):
                self.fichier.append(pygame.image.load("img/assassin/Assassin"+str(i)+".png").convert_alpha())




            
        map = open('module/map' + str(personnage.cartenum) + '.txt','r') #ouvre le fichiers texte gérant la carte
        self.texte = map.readlines() #importe tous ce fichiers dans la liste self.texte
        map.close

        #récupération de la taille de la carte
        carte_pil = Image.open("img/map/map.png")
        self.taille = carte_pil.size

        #diviseur entre la taille de la map et de la minimap (combien de fois la grande map a été divisé pour obtenir la petite
        self.multiple_x = self.taille[0] / 1024
        self.multiple_y = self.taille[1] / 768

        #affiche la carte en supprimant le blanc autour de celle-ci
        self.fond = pygame.image.load('img/map/map.png').convert()
        self.fond.set_colorkey((255,255,255))

        #cette image est utilisé pour faire des flash rouge quand le joueur perd de la vie dans le biome contamine
        self.rouge = pygame.image.load('img/map/perte_vie.png').convert()
        self.rouge.set_alpha(100)

        #le HUD (contour de la courte + boussole
        self.HUD = pygame.image.load('img/map/HUD.png').convert_alpha()

        #Affiche un fond bleu derrière la carte pour faire un effet de mer à la fin de la carte
        self.eau = pygame.Surface(fen1.get_size())
        self.eau = self.eau.convert()
        self.eau.fill((21, 96, 189))
        
        self.minimap = pygame.image.load('img/map/minimap.png').convert()

        #Cette image est afficher avec un ratio de transparence variant pour la gestion jour/nuit
        self.noir = pygame.image.load('img/map/noir.png')
        self.noir.set_alpha(0)

        #liste des images du personnage pour l'animation du mouvement
        self.pos = 1
        self.perso = self.fichier[self.pos]

        #positionnement et deplacement automatique du fond
        self.position_fond = self.fond.get_rect() #gestion de la postion sur la carte par rect()
        self.cote_perso = [(470,352) ,(560,352),(470,440),(560,440)]

        #récupération de la position par rapport au bord de la carte
        self.positionx = -self.position_fond.x + 464
        self.positiony = -self.position_fond.y + 336
        

    def animation(self,fen1,VX, VY,personnage,item,GestionPop,story,comp):
        X,Y=512,384

        self.pos = self.pos + 1
        #collision du perso avec le bord de la carte
        #vérifie si une des 4 extrémités du perso est en dehors de la carte
        if VY < 0: #vers le bas
            if self.position_fond.collidepoint(self.cote_perso[3]) != True:
                VY=0
        elif VX < 0: #vers la droite
            if self.position_fond.collidepoint(self.cote_perso[1]) != True:
                VX=0
        elif VX > 0: #vers la gauche
            if self.position_fond.collidepoint(self.cote_perso[2]) != True:
                VX=0
        elif VY > 0: #vers le haut
            if self.position_fond.collidepoint(self.cote_perso[0]) != True:
                VY=0

        #animation du perso à chaque pas => changement d'image
        if self.pos not in range(0,8) and VY < 0 :
            self.pos = 0
        elif self.pos not in range(8,16) and VX < 0 :
            self.pos = 8
        elif self.pos not in range(16,24) and VX > 0 :
            self.pos = 16
        elif self.pos not in range(24,32) and VY > 0 :
            self.pos = 24
        elif VX == 0 and VY == 0:
            self.pos = 1


        #------------------------------------gestion jour / nuit---------------------------------#
        caption = pygame.display.get_caption()
        if pygame.time.get_ticks() >= self.next and caption[1]=="WorldMap":
            self.next = pygame.time.get_ticks() + self.tour
            if self.compteur <= 10 and self.inverse == 1:
                self.compteur -= 1
                self.noir.set_alpha(15*int(self.compteur)) #augmentation de la transparence du fond noir = éclaircir la carte
            elif self.compteur >= 0 and self.inverse == 0:
                self.compteur += 1
                self.noir.set_alpha(15*int(self.compteur)) #reduction de la transparence du fond noir = assombrir la carte
            if self.compteur == 10 or self.compteur ==0:
                self.inverse = 1-self.inverse
            if self.compteur == 5:
                self.nuit = 1-self.nuit #il fait inversion de la varibale "nuit" quand le compteur est à 5, cette varibale est utilisé pour les evenmenet aléatoire utilisant le jour /nuit
                
        #------------------------------------------------------------------------------------------#
            
        #récupération de la position par rapport au bord de la carte
        self.positionx = -self.position_fond.x + 464
        self.positiony = -self.position_fond.y + 336
        self.mouvement(fen1,VX, VY,personnage,item,GestionPop,story,comp)

    def pause(self,fen1): #Affiche le menu pause permettant d'aller vers la plupart de smenus de la carte
        pygame.key.set_repeat(300, 300)
        pygame.display.set_caption("Pause")
        font = pygame.font.SysFont(None, 25)
        pygame.draw.rect(fen1, (35,51,67), [750, 0, 275, 800])

        text1 = font.render("1.Personnage",1,(206,206,206))
        text2 = font.render("2.Inventaire",1,(206,206,206))
        text3 = font.render("3.Quêtes",1,(206,206,206))
        text4 = font.render("4.Sauvegarder",1,(206,206,206))
        text5 = font.render("5.Charger",1,(206,206,206))
        text6 = font.render("6.Quitter",1,(206,206,206))
        text7 = font.render("7.Aide",1,(206,206,206))

        fen1.blit(text1,(800,50))
        fen1.blit(text2,(800,150))
        fen1.blit(text3,(800,250))
        fen1.blit(text4,(800,350))
        fen1.blit(text5,(800,450))
        fen1.blit(text6,(800,550))
        fen1.blit(text7,(800,650))


        text_version = font.render("Version 1.4",1,(206,206,206))
        fen1.blit(text_version,(900,750))
        pygame.display.flip()


    def Console(self,fen1): #Affichage de la console
        pygame.key.set_repeat(0,30)
        pygame.display.set_caption("Console")
        font = pygame.font.SysFont(None, 30)
        pygame.draw.rect(fen1, (0,0,0), [0, 468, 1024, 300])
        pygame.draw.line(fen1, (255,255,255), [0, 508], [1024,508], 3)
        texte_commande = font.render(str(self.commande),1,(255, 255, 255))
        fen1.blit(texte_commande,(10,480))
        texte_erreur = font.render(str(self.erreur),1,(255, 0, 0))
        fen1.blit(texte_erreur,(10,620))

        pygame.display.flip()
        if self.help == 1 : self.ConsoleHelp(fen1)


    def ConsoleHelp(self,fen1): #en tapant "help" dans la console, affiche une liste non exhaustive des commandes
        font = pygame.font.SysFont(None, 25)
        textAide1 = font.render("- creaCombat(fen1) : déclenche un combat aléatoire",1,(255, 255, 255))
        textAide2 = font.render("- creaCombat(fen1,ID1,ID2,ID3,nbrMonstre) : déclenche un combat spécifique",1,(255, 255, 255))
        textAide3 = font.render("- creaComp(fen1,ID,1): Ajoute le compagnon ID",1,(255, 255, 255))
        textAide4 = font.render("- creaComp(fen1,effet = 0):Supprime votre compagnon",1,(255, 255, 255))
        textAide5 = font.render("- Choix_Event(fen1,carte,personnage,item,comp,story) : déclenche un event aléatoire",1,(255, 255, 255))
        textAide6 = font.render("- carte.vitesse = x : Augmente ou diminue la vitesse du perso, par defaut x = 4",1,(255, 255, 255))
        textAide7 = font.render("- carte.repousse = x , repousse les ennemis pendant x combats",1,(255, 255, 255))
        textAide8 = font.render("- personnage.principale = x : Augmente ou diminue la force du perso",1,(255, 255, 255))
        textAide9 = font.render("- personnage.argent = x : L'argent du personnage devient la valeur de x",1,(255, 255, 255))        

        fen1.blit(textAide1,(10,520))
        fen1.blit(textAide2,(10,545))
        fen1.blit(textAide3,(10,570))
        fen1.blit(textAide4,(10,595))
        fen1.blit(textAide5,(10,620))
        fen1.blit(textAide6,(10,645))
        fen1.blit(textAide7,(10,670))
        fen1.blit(textAide8,(10,695))
        fen1.blit(textAide9,(10,720))
        pygame.display.flip()


    def aide(self,fen1):
        pygame.key.set_repeat(300, 300)
        pygame.display.set_caption("Aide")
        menu_aide = pygame.image.load('img/aide.png').convert()
        fen1.blit(menu_aide,(0,0))
        pygame.display.flip()

    
    #Fonction permettant de regénérer la carte pour augmenter la zone de la contamination
    def regenere(self,fen1,GestionPop,personnage):
        
        varA,varB,varC,varG,varR,varP,varQ,varZ,varM = GenerationMap(fen1,GestionPop,self.varA,self.varB,self.varC,personnage)
        self.varA,self.varB,self.varC,self.varG,self.varR,self.varP,self.varQ,self.varZ,self.varM = varA,varB,varC,varG,varR,varP,varQ,varZ,varM
        
        self.fond = pygame.image.load("img/map/map.png").convert()
        self.fond.set_colorkey((255,255,255))
        self.minimap = pygame.image.load("img/map/minimap.png" ).convert()


    #Fonction detectant le biome où est le joueur
    def DetectionBiome(self,fen1):
        font = pygame.font.SysFont(None, 25)

        #Nombre de carrés (128*128) depuis le bord de la map
        nbrbiome_x = int(self.positionx / 128)
        nbrbiome_y = int(self.positiony / 128)
        
        #correspondance entre la position actuel et la lettre dans le fichier texte
        ligne = self.texte[nbrbiome_y]
        self.lettre = ligne[nbrbiome_x]

        #Attribution à chaque lettre de son équivalent en biome
        #VarA, VarB et VarC sont définit lors de la génération de la map, ce sont les concordance lettre/Biome
        if self.lettre == "A":
            self.biome = self.varA
        elif self.lettre == "B":
            self.biome = self.varB
        elif self.lettre == "C":
            self.biome = self.varC
        elif self.lettre == "G":
            self.biome = self.varG
        elif self.lettre == "V":
            self.biome = "village"
        elif self.lettre == "S":
            self.biome = "village"
        elif self.lettre == "N":
            self.biome = "village"
        elif self.lettre == "D":
            self.biome = "village"
        elif self.lettre == "R":
            self.biome = self.varR
        elif self.lettre == "P":
            self.biome = self.varP
        elif self.lettre == "Q":
            self.biome = self.varQ
        elif self.lettre == "Z":
            self.biome = self.varZ
        elif self.lettre == "M":
            self.biome = self.varM

        #modification couleur d'affichage du texte du biome en fonction du fond (couleur du biome)
        self.txtbiome = font.render(self.biome ,1,(255,255,255))

        


    def mouvement(self,fen1,VX,VY,personnage,item,GestionPop,story,comp):
        fontpseudo = pygame.font.SysFont(None, 25)
        if personnage.temps_vitesse > 0:
            personnage.temps_vitesse -= 1
        if personnage.temps_vitesse == 0:
            self.vitesse = 4
        self.DetectionBiome(fen1)





        #---------------------------------------perte de vie dans le biome contamine--------------------#
        #si le joueur est dans le biome contamine, il perd progressivement de la vie
        if self.biome == "contaminée" and story.activation_quetes[7] != 3:
            if self.cooldown_contamine == 0:
                self.cooldown_contamine = 30 #tous les 30 pas, le joueur perd de la vie
                if personnage.vie > 1: #le joueur ne peut pas mourir avec cette perte de vie
                    personnage.vie -= int(0.02*personnage.viemax) #perte de 2% de la vie max
                    fen1.blit(self.rouge, (0,0)) #affiche un flash rouge
                    pygame.display.flip()
                    time.sleep(0.2)
                    if personnage.vie <= 0:
                        personnage.vie = 1
            else:
                self.cooldown_contamine -= 1


        #-------------------------------------------------------------------------------------------------#
                
        #déplacement du fond de la valeur VX et VY
        self.perso = self.fichier[self.pos]
        self.position_fond = self.position_fond.move(VX, VY)
        fen1.blit(self.eau, (0,0))
        fen1.blit(self.fond, (self.position_fond))
        fen1.blit(self.perso, (512,384))
        fen1.blit(self.noir, (0,0))

        self.contour(fen1,personnage)


        #si des compétences sont disponible alors affichage de l'image
        if personnage.competence > 0:
            up = pygame.image.load('img/map/up.png').convert_alpha()
            fen1.blit(up, (950,700))
            
        pygame.display.flip()
        

        
        if self.lettre == "V":
            self.regenere(fen1,GestionPop,personnage)
            if  story.activation_quetes[0] == 0:
                quete = quest_ID(fen1,0,personnage,item,story,comp,self)
            if  story.activation_quetes[0] == 2:
                quete = quest_ID(fen1,0,personnage,item,story,comp,self)
            Action(fen1)
            
        elif self.lettre == "S":
            self.regenere(fen1,GestionPop,personnage)
            Action(fen1)
            if  story.activation_quetes[1] == 1:
                quete = quest_ID(fen1,1,personnage,item,story,comp,self)
            elif  story.activation_quetes[2] == 1:
                if item.inventaireLook(0) >= 1:
                    quete = quest_ID(fen1,2,personnage,item,story,comp,self)
                else:
                    Action(fen1)

        elif self.lettre == "N":
            self.regenere(fen1,GestionPop,personnage)
            Action(fen1)
            if  story.activation_quetes[3] == 1:
                quete = quest_ID(fen1,3,personnage,item,story,comp,self)
            elif  story.activation_quetes[4] == 1:
                if item.inventaireLook(4) >= 3 and item.inventaireLook(1) >= 1:
                    quete = quest_ID(fen1,4,personnage,item,story,comp,self)
                else:
                    Action(fen1)
            elif story.activation_quetes[5] == 2 or story.activation_quetes[5] == 0 and story.activation_quetes[4] == 3:
                   quete = quest_ID(fen1,5,personnage,item,story,comp,self)

                
        elif self.lettre == "D":
            self.regenere(fen1,GestionPop,personnage)
            Action(fen1)
            if story.activation_quetes[6] == 1:
                quete = quest_ID(fen1,6,personnage,item,story,comp,self)

        elif self.lettre == "G":
            if story.activation_quetes[8] == 1:
                quete = quest_ID(fen1,8,personnage,item,story,comp,self)
                module.bind.creaCombat(fen1,408,1,1,1) #déclenche le combat contre le boss finale
                
                

#recolle la carte sans redonner accès aux bind de celle-ci : le personnage est statique => utile pour les events dans le déplacement des persos
    def affichage(self,fen1,personnage,item,comp):
        fen1.blit(self.eau, (0,0))
        fen1.blit(self.fond, (self.position_fond))
        fen1.blit(self.perso, (512,384))
        fen1.blit(self.noir, (0,0))
        self.jauge(fen1,personnage)

        #si des compétences sont disponible alors affichage de l'image
        if personnage.competence > 0:
            up = pygame.image.load('img/map/up.png').convert_alpha()
            fen1.blit(up, (950,700))



    def contour(self,fen1,personnage): #Fonction permettant de coller les images de contour sur la carte (HUD, pseudo,jauges...)
        fontpseudo = pygame.font.SysFont(None, 25)
        self.jauge(fen1,personnage)
        fen1.blit(self.HUD, (0,0))
        self.DetectionBiome(fen1)
        if self.biome != "contaminée" :
            fen1.blit(self.txtbiome,(920,175))
        else:
            fen1.blit(self.txtbiome,(900,175))
        textpseudo = fontpseudo.render(personnage.pseudo + " Niv. "+ str(personnage.niveau) ,1,(255,255,255))
        fen1.blit(textpseudo, (50,25))
        fen1.blit(self.tete, (255,5))



    def jauge(self,fen1,personnage): #cette fonction est appelée dans la fonction contour() c'est elle qui gère l'affichage des jauges sur la carte
        font = pygame.font.SysFont(None, 20)
        pygame.draw.rect(fen1, (153,153,153), [0, 755, 1024, 12])
        if personnage.niveau == 1:
            xp_max = 300
            xp = personnage.xp
            pygame.draw.rect(fen1, (255,185,15), [0, 755, (1024/personnage.xpmax)*personnage.xp, 12])
        else:
            xp_precedant = (personnage.xpmax-(personnage.xpbase + (personnage.niveau - 1)*250))
            xp_max = (personnage.xpmax - xp_precedant)
            xp = personnage.xp-xp_precedant
            pygame.draw.rect(fen1,(255,185,15), [0, 755, (1024/xp_max)*xp, 12])

        textxp = font.render("XP "+str(personnage.xp) + "/" + str(personnage.xpmax) ,1,(0,0,0))            

        pygame.draw.rect(fen1, (153,153,153), [11,4, 229, 11])
        pygame.draw.rect(fen1, (255,0,0), [11, 4, (229/personnage.viemax)*personnage.vie, 11])

        textvie = font.render("VIE "+str(personnage.vie) + "/" + str(personnage.viemax) ,1,(255,255,255))     


        fen1.blit(textvie, (100,4))
        fen1.blit(textxp, (500,755))
    
    #affichage de la mini map
    def mini(self,fen1,personnage,item):
        pygame.display.set_caption("MiniMap")
        pygame.key.set_repeat(500, 500)

        #positionnement du curseur par rapport à la position
        position_mini = (self.positionx / self.multiple_x , self.positiony / self.multiple_y)
        curseur = pygame.image.load('img/map/curseur.png').convert_alpha()
        
        fen1.blit(self.minimap, (0,0))
        fen1.blit(curseur, position_mini)

        pygame.display.flip()

        
       #fonction permettant de revenir sur la carte à l'ezndoit exact où nous l'avons laissé sans stopper la gestion jour/nuit
    def reprise(self,fen1,personnage,item,comp):
        fontpseudo = pygame.font.SysFont(None, 25)
        self.DetectionBiome(fen1)
        
        while self.biome == "village":
            self.position_fond = self.position_fond.move(30,0)
            self.positionx = -self.position_fond.x + 464
            self.positiony = -self.position_fond.y + 336
            self.DetectionBiome(fen1)
            
        pygame.display.set_caption("WorldMap")
        fen1.blit(self.eau, (0,0))
        fen1.blit(self.fond, self.position_fond)
        fen1.blit(self.perso, (512,384))
        fen1.blit(self.noir, (0,0))
        self.contour(fen1,personnage)
        if personnage.competence > 0:
            up = pygame.image.load('img/map/up.png').convert_alpha()
            fen1.blit(up, (950,700))
        pygame.display.flip()
        pygame.key.set_repeat(1, 60)

    #récupération de la carte après le chargement d'une sauvergarde (recharge les images et replace le perso au bon endroit)
    def chargement(self,fen1,personnage,item,comp):
        fontpseudo = pygame.font.SysFont(None, 25)
        self.historique_console = []
        self.fichier = []

        #charge les images en fonction de la class du joueur
        if personnage.classe == "paladin":
            self.tete = pygame.image.load("img/paladin/tetepaladin.png").convert_alpha()
            for i in range(1,33):
                self.fichier.append(pygame.image.load("img/paladin/Paladin"+str(i)+".png").convert_alpha())

        if personnage.classe == "mage":
            self.tete = pygame.image.load("img/heretique/teteHeretique.png").convert_alpha()
            for i in range(1,33):
                self.fichier.append(pygame.image.load("img/heretique/Heretique"+str(i)+".png").convert_alpha())

        if personnage.classe == "voleur":
            self.tete = pygame.image.load("img/assassin/teteAssassin.png").convert_alpha()
            for i in range(1,33):
                self.fichier.append(pygame.image.load("img/assassin/Assassin"+str(i)+".png").convert_alpha())

        self.DetectionBiome(fen1)

        self.pos = 1

        #recharge tous les villages
        pygame.display.set_caption("WorldMap")
        self.fond = pygame.image.load("img/map/map.png").convert()
        self.fond.set_colorkey((255,255,255))
        self.minimap = pygame.image.load("img/map/minimap.png").convert()
        self.noir = pygame.image.load('img/map/noir.png')
        self.rouge = pygame.image.load('img/map/perte_vie.png').convert()
        self.eau = pygame.Surface(fen1.get_size())
        self.eau = self.eau.convert()
        self.eau.fill((21, 96, 189))
        self.HUD = pygame.image.load('img/map/HUD.png').convert_alpha()
        self.noir.set_alpha(15*int(self.compteur))
        self.rouge.set_alpha(100)
        self.perso = self.fichier[self.pos]
        #si le joueur était dans un village pendant la save, il y est renvoyé
        if self.biome == "village":
            Action(fen1)
        else:
            self.reprise(fen1,personnage,item,comp)


