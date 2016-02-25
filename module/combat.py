import pygame,random,time
from module.ennemi import *
from module.worldmap_v1 import *
from module.objet import *
from module.menu_inventaire import *
from module.compagnon import *
from module.menu_classe import *
from module.menu_esclaves import *
from module.attaques import *


class gestionCombat:
        
    #Fonction principale lancée aléatoirement depuis la world map
    def __init__(self,fen1,personnage,item,carte,comp,story,a,b,c,nbm):
        self.cooldown = 0
        personnage.up = 0
        self.stunMonstre1 = 0
        self.stunMonstre2 = 0
        self.stunMonstre3 = 0
        self.cooldownPotion = 0
        self.fondtext = pygame.font.SysFont(None, 22)
        
        if comp.ami != 0 : self.Compagnon = pygame.image.load(comp.img)
        
        pygame.key.set_repeat(500, 500)
        
        if a == 0 and b == 0 and c == 0 :
            if carte.biome == "desert" :
                a = random.randint(1,7)
                b = random.randint(1,7)
                c = random.randint(1,7)
            elif carte.biome == "marais" :
                a = random.randint(101,107)
                b = random.randint(101,107)
                c = random.randint(101,107)
            elif carte.biome == "plaine" :
                a = random.randint(201,206)
                b = random.randint(201,206)
                c = random.randint(201,206)
            elif carte.biome == "contaminée" :
                a = random.randint(301,303)
                b = random.randint(301,303)
                c = random.randint(301,303)
            
        
        self.monstre1 = ennemi(a,personnage,story,item)
        self.monstre2 = ennemi(b,personnage,story,item)
        self.monstre3 = ennemi(c,personnage,story,item)

        #Nombre aléatoire de monstre, de 1 à 3:
        if nbm == 0 :
            if personnage.niveau <= 3 :
                self.nombreMonstre = 1
            if (personnage.niveau > 3 and personnage.niveau < 6) :
                self.nombreMonstre = random.randint(1,2)
            if personnage.niveau >= 6 :
                self.nombreMonstre = random.randint(1,3)

        if nbm == 1 : self.nombreMonstre = 1
        if nbm == 2 : self.nombreMonstre = 2
        if nbm == 3 : self.nombreMonstre = 3

        personnage.ennemi = self.nombreMonstre

        #En fonction du nombre de monstre, passe self.monstreVivant à 1 : lorsque tout les self.monstreVivant passe à 0
        #lors de la mort des monstres, victoire du joueur et combat terminé

        self.monstreVivant1 = 0
        self.monstreVivant2 = 0
        self.monstreVivant3 = 0
        
        if self.nombreMonstre == 1 :
            self.monstreVivant1 = 1
        if self.nombreMonstre == 2 :
            self.monstreVivant1 = 1
            self.monstreVivant2 = 1
        if self.nombreMonstre == 3 :
            self.monstreVivant1 = 1
            self.monstreVivant2 = 1
            self.monstreVivant3 = 1

        
        self.fond = pygame.image.load('img/menuCombat.png').convert()
        fen1.blit(self.fond,(0,0))

        #Charge les images du personnage en fonction de la classe et des monstres
        if personnage.classe == "paladin" : self.perso = pygame.image.load("img/PaladinFight.png")
        if personnage.classe == "voleur": self.perso = pygame.image.load("img/AssassinFight.png")
        if personnage.classe == "mage" : self.perso = pygame.image.load("img/HeretiqueFight.png")
        
        self.mstr = pygame.image.load(self.monstre1.img)
        self.mstr2 = pygame.image.load(self.monstre2.img)
        self.mstr3 = pygame.image.load(self.monstre3.img)

        self.maj(fen1,personnage,item,comp,story)
        
        pygame.display.flip()


    #MAJ des informations lors du combat
    def maj(self,fen1,personnage,item,comp,story):
        
        #Affiche le menu du combat
        pygame.display.set_caption("Combat")
        
        textAttaque = self.fondtext.render("1.Attaquer",1,(0,0,0))
        textCompetence = self.fondtext.render("2.Compétences",1,(0,0,0))
        textInventaire = self.fondtext.render("3.Inventaire",1,(0,0,0))
        textFuir = self.fondtext.render("4.Fuir",1,(0,0,0))

        fen1.blit(textAttaque,(120,560))
        fen1.blit(textCompetence,(120,600))
        fen1.blit(textInventaire,(120,640))

        if story.activation_quetes[7] != 1 :
            fen1.blit(textFuir,(120,680))
                  
        #Choix de la cible quand il y a 2 monstres
        if self.nombreMonstre == 2 or self.nombreMonstre == 3 :
            pygame.display.set_caption("Combat2")

        self.statsMonstre(fen1,personnage,item,comp)
        self.statsPersonnage(fen1,personnage,item,comp)
        self.placement(fen1,personnage,item,comp)
        
        pygame.display.flip()


    #Affiche les textes des monstres, donnent leur vie, niveau, nom, leur état (si mort)
    def statsMonstre(self,fen1,personnage,item,comp):
        
        textMonstre1 = self.fondtext.render(self.monstre1.name + " nv " + str(self.monstre1.niveau),1,(0,0,0))

        if self.monstreVivant1 == 1 : textVieMonstre1 = self.fondtext.render("Vie : " + str(self.monstre1.vie) + "/" + str(self.monstre1.viemax),1,(0,0,0))
        else : textVieMonstre1 = self.fondtext.render("Mort",1,(0,0,0))

        fen1.blit(textMonstre1,(700,560))
        fen1.blit(textVieMonstre1,(700,580))

        
        if self.nombreMonstre == 2 or self.nombreMonstre == 3 :
            textMonstre2 = self.fondtext.render(self.monstre2.name + " nv " + str(self.monstre2.niveau),1,(0,0,0))
            
            if self.monstreVivant2 == 1 : textVieMonstre2 = self.fondtext.render("Vie : " + str(self.monstre2.vie) + "/" + str(self.monstre2.viemax),1,(0,0,0))
            else : textVieMonstre2 = self.fondtext.render("Mort",1,(0,0,0))

            fen1.blit(textMonstre2,(700,610))
            fen1.blit(textVieMonstre2,(700,630))

        if self.nombreMonstre == 3 :
            textMonstre3 = self.fondtext.render(self.monstre3.name + " nv " + str(self.monstre3.niveau),1,(0,0,0))
        
            if self.monstreVivant3 == 1 : textVieMonstre3 = self.fondtext.render("Vie : " + str(self.monstre3.vie) + "/" + str(self.monstre3.viemax),1,(0,0,0))
            else : textVieMonstre3 = self.fondtext.render("Mort",1,(0,0,0))

            fen1.blit(textMonstre3,(700,660))
            fen1.blit(textVieMonstre3,(700,680))

        

    #Permet d'afficher un menu de selection de la cible lorsqu'il y a plusieurs ennemis.
    def majMulti(self,fen1,personnage,item,comp):
        fen1.blit(self.fond,(0,0))
        
        pygame.display.set_caption("Choix")

        #Si le monstre est vivant affiche : Attaquer le monstre, sinon affiche : Monstre mort !
        if self.monstreVivant1 == 1 :
            textAttaque = self.fondtext.render("1.Attaquer " + self.monstre1.name,1,(0,0,0))
        else :
            textAttaque = self.fondtext.render(self.monstre1.name + " est mort !",1,(0,0,0))
        fen1.blit(textAttaque,(120,560))
        
        if self.monstreVivant2 == 1 :
            textAttaque2 = self.fondtext.render("2.Attaquer " + self.monstre2.name,1,(0,0,0))
        else :
            textAttaque2 = self.fondtext.render(self.monstre2.name + " est mort !",1,(0,0,0))
        fen1.blit(textAttaque2,(120,600))

        if self.nombreMonstre == 3 :
            if self.monstreVivant3 == 1 :
                textAttaque3 = self.fondtext.render("3.Attaquer " + self.monstre3.name,1,(0,0,0))
            else :
                textAttaque3 = self.fondtext.render(self.monstre3.name + " est mort !",1,(0,0,0))
            fen1.blit(textAttaque3,(120,640))
                
            textRetour = self.fondtext.render("4.Retour",1,(0,0,0))
            fen1.blit(textRetour,(120,680))
        else :
            textRetour = self.fondtext.render("3.Retour",1,(0,0,0))
            fen1.blit(textRetour,(120,640))
            


        self.statsMonstre(fen1,personnage,item,comp)
        self.statsPersonnage(fen1,personnage,item,comp)  
        self.placement(fen1,personnage,item,comp)
        pygame.display.flip()

        

    #Affichage des stats du personnage en combat, sa vie, son XP, son pseudo
    def statsPersonnage(self,fen1,personnage,item,comp):
            textJoueur = self.fondtext.render(personnage.pseudo + " :",1,(0,0,0))
            textVieJoueur = self.fondtext.render("Vie : " + str(personnage.vie) + "/" + str(personnage.viemax),1,(0,0,0))
            textXp = self.fondtext.render("XP : " + str(personnage.xp) + "/" + str(personnage.xpmax),1,(0,0,0))

            fen1.blit(textJoueur,(450,530))
            fen1.blit(textVieJoueur,(450,560))
            fen1.blit(textXp,(450,590))


            if comp.ami != 0 :
                textComp = self.fondtext.render(comp.name + " :",1,(0,0,0))
                if comp.vie > 0 : textVieComp = self.fondtext.render("Vie : " + str(comp.vie) + "/" + str(comp.viemax),1,(0,0,0))
                else : textVieComp = self.fondtext.render("Mort",1,(0,0,0))

                fen1.blit(textComp,(450,650))
                fen1.blit(textVieComp,(450,680))


        
    #Emplacement des images du joueur et des monstres, si ils sont vivants, sinon place une tombe (a la
    #place des monstres)
    def placement(self,fen1,personnage,item,comp):


        if comp.ami == 0 :
            fen1.blit(self.perso,(170,280))#Image du personnage sans compagnon
        else :
            fen1.blit(self.perso,(170,350))#Image du personnage avec compagnon

        
        if comp.ami != 0 and comp.vie > 0:
            fen1.blit(self.Compagnon,(180,185))
        elif comp.ami != 0 and comp.vie <= 0 :
            self.Compagnon = pygame.image.load("img/TombeCompagnon.png")
            fen1.blit(self.Compagnon,(180,185))
        
        
        #Placement du monstre 1
        if self.monstreVivant1 == 1 :
            fen1.blit(self.mstr,(550,170))
        else :
            self.mstr = pygame.image.load("img/Tombe.png")
            fen1.blit(self.mstr,(550,170))

        #Placement du monstre 2
        if self.nombreMonstre == 2 or self.nombreMonstre == 3:
            if self.monstreVivant2 == 1 :    
                fen1.blit(self.mstr2,(700,250))
            else :
                self.mstr2 = pygame.image.load("img/Tombe.png")
                fen1.blit(self.mstr2,(700,250))
                
        #Placement du monstre 3
        if self.nombreMonstre == 3 :       
            if self.monstreVivant3 == 1 :
                fen1.blit(self.mstr3,(585,350))
            else :
                self.mstr3 = pygame.image.load("img/Tombe.png")
                fen1.blit(self.mstr3,(585,350))
                


    #Fonction vérifiant si les conditions pour la victoire sont réunis et permet de gérer le gain d'experience
    #ainsi que le passage de niveau lorsque l'exp est superieur à l'exp max du niveau.
    def victoire(self,fen1,personnage,item,comp,story):
        
            
        #Si tout les monstres meurent, victoire du personnage
        if self.monstreVivant1 == 0 and self.monstreVivant2 == 0 and self.monstreVivant3 == 0 :

            if personnage.temps_force != 0 :
                personnage.temps_force -= 1
                if personnage.temps_force == 0 :
                    personnage.principale -= 5
                    
            if personnage.vendeurEsclave != 0 : personnage.vendeurEsclave -= 1
            if comp.ami != 0 and comp.vie <= 0 : comp.ami = 0
            
            time.sleep(0.8)
            pygame.display.set_caption("Victoire")
            fen1.blit(self.fond, (0,0))
            textVictoire = self.fondtext.render("Victoire",1,(0,0,0))
            fen1.blit(textVictoire,(470,160))


            #Gain d'experience à la mort du monstre si 1 monstre
            if self.nombreMonstre == 1 :
                gainXp = self.monstre1.gainxp
                gainOr = self.monstre1.gold

            #Gain d'experience à la mort du monstre si 2 monstres
            if self.nombreMonstre == 2 :
                gainXp = self.monstre1.gainxp + self.monstre2.gainxp
                gainOr = self.monstre1.gold + self.monstre2.gold

            #Gain d'experience à la mort du monstre si 3 monstres
            if self.nombreMonstre == 3 :
                gainXp = self.monstre1.gainxp + self.monstre2.gainxp + self.monstre3.gainxp
                gainOr = self.monstre1.gold + self.monstre2.gold + self.monstre3.gold
                
            personnage.xp += gainXp
            personnage.argent += gainOr
            
            
            #Passage d'un niveau quand l'xp dépasse l'xpmax, gain de points de compétences, régénération de la vie au max, augmentation de l'xpmax à atteindre
            if personnage.xp >= personnage.xpmax :
                personnage.up = 1
                personnage.niveau += 1
                personnage.competence += 5
                personnage.vie = personnage.viemax
                personnage.xpmax += personnage.xpbase + (personnage.niveau - 1) * 250

                textPassageNiveau = self.fondtext.render("Vous avez gagné un niveau !",1,(0,0,0))
                if story.activation_quetes[7] != 1 :
                    fen1.blit(textPassageNiveau,(300,260))

            self.lootFinCombat(fen1,personnage,item,comp,story)
            
            textGainXp = self.fondtext.render(str(gainXp) + " points d'expérience gagnés.",1,(0,0,0))
            if gainOr > 1 : textGainOr = self.fondtext.render(str(gainOr) + " pièces d'or récupérées.",1,(0,0,0))
            else : textGainOr = self.fondtext.render(str(gainOr) + " pièce d'or récupérée.",1,(0,0,0))

            if story.activation_quetes[7] != 1 :
                if self.inventairePlein == 0 :
                    textRetourMap = self.fondtext.render("1.Carte",1,(0,0,0))
                    fen1.blit(textRetourMap,(300,440))
                else :
                    textInventaire = self.fondtext.render("1.Ouvrir l'inventaire.",1,(0,0,0))
                    textRetourMap = self.fondtext.render("2.Abandonner les objets.",1,(0,0,0))
                    fen1.blit(textInventaire,(300,440))
                    fen1.blit(textRetourMap,(500,440))
                

            if story.activation_quetes[7] == 1:
                fen1.blit(self.fond, (0,0))
                textVictoire = self.fondtext.render("Vous avez gagné la bataille, vous recevez un rapport des autres fronts.",1,(0,0,0))
                textCharger = self.fondtext.render("1.Voir le rapport.",1,(0,0,0))
                
                fen1.blit(textVictoire,(300,200))
                fen1.blit(textCharger,(300,240))

            if story.activation_quetes[7] != 1 :
                fen1.blit(textGainXp,(300,210))
                fen1.blit(textGainOr,(300,310))
            

            
            
              
            

    #Vérifie la mort du joueur
    def mortJoueur(self,fen1,personnage,item,comp,story):
        #Si la vie du joueur <=0 : mort du personnage ===> chargement de la derniere partie 
        if personnage.vie <= 0 :
            if story.activation_quetes[7] == 1:
                time.sleep(0.8)
                pygame.display.set_caption("Défaite")
                fen1.blit(self.fond, (0,0))
                textMort = self.fondtext.render("Vous avez perdu la bataille, vous recevez un rapport des autres fronts.",1,(0,0,0))
                textCharger = self.fondtext.render("1.Voir le rapport.",1,(0,0,0))
            else :
                time.sleep(0.8)
                pygame.display.set_caption("Défaite")
                fen1.blit(self.fond, (0,0))
                textMort = self.fondtext.render("Vous êtes mort",1,(0,0,0))
                textCharger = self.fondtext.render("1.Charger",1,(0,0,0))
            
            fen1.blit(textMort,(300,280))
            fen1.blit(textCharger,(440,330))




    #Vérifie la mort des monstres et du compagnon
    def mort(self,fen1,personnage,item,comp):
        #Lorsque la vie d'un monstre passe en dessous de 0, self.monstreVivant passe a 0 et le monstre est
        #considéré comme mort : son image se retire et le texte "mort" s'affiche à la place de sa vie.
        if self.monstre1.vie <= 0 :
            self.monstreVivant1 = 0
        if self.monstre2.vie <= 0 :
            self.monstreVivant2 = 0
        if self.monstre3.vie <= 0 :
            self.monstreVivant3 = 0



    #Fait toutes les verifications : mort du/des monstre/s, attaque/s du/des monstre/s, mise à jour des stats en combat, victoire du joueur ou la mort du joueur
    def verification(self,fen1,personnage,item,comp,story):
        self.mort(fen1,personnage,item,comp)
        attaqueMonstre(self,fen1,personnage,item,comp)
        self.maj(fen1,personnage,item,comp,story)
        self.victoire(fen1,personnage,item,comp,story)
        self.mortJoueur(fen1,personnage,item,comp,story)



    def verification2(self,fen1,personnage,item,comp,story):
        self.mort(fen1,personnage,item,comp)
        self.maj(fen1,personnage,item,comp,story)
        self.victoire(fen1,personnage,item,comp,story)
        

    def verification3(self,fen1,personnage,item,comp,story):
        self.mort(fen1,personnage,item,comp)
        self.maj(fen1,personnage,item,comp,story)


        

    #Fonction gérant la fuite du personnage en fonction de son taux d'esquive qu'on peut augmenter a chaque niveau.
    #Si la fuite réussit, retour sur la world map sinon le joueur se fait taper normalement par les monstres.            
    def fuite(self,fen1,personnage,item,carte,comp,story):
        fuir = random.randint(0,100)
        if fuir <= personnage.esquive :
            carte.reprise(fen1,personnage,item,comp)
            if comp.ami != 0 and comp.vie <= 0 : comp.ami = 0

            story.echec_quetes(fen1,personnage,item,comp,carte)
                            
            
        else :
            fen1.blit(self.fond, (0,0))
            self.verification(fen1,personnage,item,comp,story)
            pygame.display.flip()


            
                        






    #Menu du choix de la compétence spéciale avec la possibilité de retourner sur le menu principale du combat
    def competenceSpeciale(self,fen1,personnage,item,comp):
        pygame.display.set_caption("No CD retour")

        #Un monstre donc tape le monstre directement, attaque spe disponible
        if self.nombreMonstre == 1 and self.cooldown == 0:
            pygame.display.set_caption("Attaque Speciale 1")

        #Plusieurs monstres, choix de la cible avec le menu de choix, attaque spe disponible
        if (self.nombreMonstre == 2 or self.nombreMonstre == 3) and self.cooldown == 0 :
            pygame.display.set_caption("Attaque Speciale Multi")

            
        fen1.blit(self.fond, (0,0))
        self.placement(fen1,personnage,item,comp)
        self.statsMonstre(fen1,personnage,item,comp)
        self.statsPersonnage(fen1,personnage,item,comp)

        #Attaque spe disponible pour le paladin
        if self.cooldown == 0 and personnage.classe == "paladin" :
            textAttaqueSpeciale1 = self.fondtext.render("1.Attaque puissante",1,(0,0,0))
            textAttaqueSpeciale2 = self.fondtext.render("2.Soin",1,(0,0,0))


        #Attaque spe disponible pour l'assassin
        if self.cooldown == 0 and personnage.classe == "voleur" :
            textAttaqueSpeciale1 = self.fondtext.render("1.Assassinat",1,(0,0,0))
            textAttaqueSpeciale2 = self.fondtext.render("2.Assomer",1,(0,0,0))


        #Attaque spe disponible pour le mage
        if self.cooldown == 0 and personnage.classe == "mage" :
            textAttaqueSpeciale1 = self.fondtext.render("1.Vol de vie",1,(0,0,0))
            textAttaqueSpeciale2 = self.fondtext.render("2.Météore",1,(0,0,0))


        #Attaque spe non dispo, plusieurs tours
        if self.cooldown > 1 : textAttaqueSpeciale1 = self.fondtext.render("Disponible dans " + str(self.cooldown) + " tours",1,(0,0,0))
        #Attaque spe non dispo, 1 tour de cooldown
        if self.cooldown == 1 : textAttaqueSpeciale1 = self.fondtext.render("Disponible dans 1 tour",1,(0,0,0))


        
        textRetour = self.fondtext.render("3.Retour",1,(0,0,0))
        
        fen1.blit(textAttaqueSpeciale1,(120,560))
        
        if self.cooldown == 0 :
            fen1.blit(textAttaqueSpeciale2,(120,600))
            
        fen1.blit(textRetour,(120,640))

        pygame.display.flip()


    def menuInventCombat(self,fen1,personnage,item,comp):
        fen1.blit(self.fond,(0,0))
        
        #Affiche le menu du combat
        pygame.display.set_caption("Invent combat")
        
        textRetour = self.fondtext.render("1.Retour",1,(0,0,0))
        fen1.blit(textRetour,(120,560))

        if item.inventaireLook(0) > 0 and item.inventaireLook(30) > 0 and self.cooldownPotion == 0:
            textPotionJoueur = self.fondtext.render("2.Potion de vie",1,(0,0,0))
            textPotionGroupe = self.fondtext.render("3.Potion de groupe",1,(0,0,0))
            fen1.blit(textPotionJoueur,(120,590))
            fen1.blit(textPotionGroupe,(120,620))

        elif item.inventaireLook(0) == 0 and item.inventaireLook(30) > 0 and self.cooldownPotion == 0:
            textPotionGroupe = self.fondtext.render("2.Potion de groupe",1,(0,0,0))
            fen1.blit(textPotionGroupe,(120,590))

        elif item.inventaireLook(0) > 0 and item.inventaireLook(30) == 0 and self.cooldownPotion == 0:
            textPotionJoueur = self.fondtext.render("2.Potion de vie",1,(0,0,0))
            fen1.blit(textPotionJoueur,(120,590))
        
        elif item.inventaireLook(0) > 0 and self.cooldownPotion == 2:
            textPotionJoueur = self.fondtext.render("Disponible dans 2 tours.",1,(0,0,0))
            fen1.blit(textPotionJoueur,(120,590))
            
        elif item.inventaireLook(0) > 0 and self.cooldownPotion == 1:
            textPotionJoueur = self.fondtext.render("Disponible dans 1 tour.",1,(0,0,0))
            fen1.blit(textPotionJoueur,(120,590))
  

        self.statsMonstre(fen1,personnage,item,comp)
        self.statsPersonnage(fen1,personnage,item,comp)
        self.placement(fen1,personnage,item,comp)
        
        pygame.display.flip()


    def potionVie(self,fen1,personnage,item,comp):
        self.cooldownPotion = 2
        item.objetPerdu(0)

        if personnage.vie <= personnage.viemax - (20 + personnage.alchimiste):
            personnage.vie += (20 + personnage.alchimiste)
        else : personnage.vie = personnage.viemax

    def potionGroupe(self,fen1,personnage,item,comp):
        self.cooldownPotion = 2
        item.objetPerdu(30)

        if personnage.vie <= personnage.viemax - (10 + personnage.alchimiste) :
            personnage.vie += (10 + personnage.alchimiste)
        else : personnage.vie = personnage.viemax

        if comp.ami == 1 :
            if comp.vie <= comp.viemax - (10 + personnage.alchimiste) :
                comp.vie += (10 + personnage.alchimiste)
            else : comp.vie = comp.viemax
        
               


    #Choix de la cible pour l'attaque 1
    def choixCibleAS1(self,fen1,personnage,item,comp):
        self.majMulti(fen1,personnage,item,comp)
        pygame.display.set_caption("Choix Speciale 1")

    #Choix de la cible pour l'attaque 2
    def choixCibleAS2(self,fen1,personnage,item,comp):
        self.majMulti(fen1,personnage,item,comp)
        pygame.display.set_caption("Choix Speciale 2")



            
    #Permet de passer du menu des compétences spéciales au menu principale du combat, recolle un self.fond et replace tout
    def retour(self,fen1,personnage,item,comp,story):
        fen1.blit(self.fond, (0,0))
        self.maj(fen1,personnage,item,comp,story)


    def inventFull(self,fen1,personnage,item,comp):
        fen1.blit(self.fond,(0,0))
        Inventaire(fen1,item,personnage)
        pygame.display.set_caption("Invent full combat")
        textInvent = self.fondtext.render("Selectionner l'objet ou la pile d'objets à supprimer.",1,(206,206,206))
        fen1.blit(textInvent,(250,680))

        textObjetLoot = self.fondtext.render("Objet récupéré : " + str(item.nomObjet(self.objetEnAttente[0],personnage)),1,(206,206,206))
        fen1.blit(textObjetLoot,(250,710))

        textSuppObjet = self.fondtext.render("X : abandonner " + str(item.nomObjet(self.objetEnAttente[0],personnage)),1,(206,206,206))
        fen1.blit(textSuppObjet,(500,710))
            
        pygame.display.flip()


    def etatInvent(self,fen1,personnage,item,comp):
        if item.inventaireRempli() == 0 : 
            pygame.display.set_caption("Invent looter objet")
            textInvent = self.fondtext.render("1.Récupérer " + str(item.nomObjet(self.objetEnAttente[0],personnage)),1,(206,206,206))
            fen1.blit(textInvent,(250,680))
            pygame.display.flip()
        elif item.inventaireRempli() == 1:
            self.inventFull(fen1,personnage,item,comp)
            
    


    def majAnimation(self,fen1,personnage,item,comp,story):
        fen1.blit(self.fond,(0,0))
        self.maj(fen1,personnage,item,comp,story)
        



    def lootFinCombat(self,fen1,personnage,item,comp,story):
        self.inventairePlein = 0
        self.objetEnAttente = []
        self.longueurListe = 0
        self.nombreObjetEnAttente = 0

        if story.activation_quetes[7] != 1 :

            #Permet de gagner une potion à la fin du combat ainsi qu'un objet.
            if item.inventaireRempli() == 0 :
                popo = random.randint(1,5)
                if popo == 1 :
                    textGainPotion = self.fondtext.render("Vous avez récupéré une potion.",1,(0,0,0))
                    fen1.blit(textGainPotion,(300,360))
                    item.loot(0)

            
            
            itemLootMonstre1 = random.randint(2,5)
            itemLootMonstre2 = 0
            itemLootMonstre3 = 0
            
            if self.nombreMonstre == 2 or self.nombreMonstre == 3 :
                itemLootMonstre2 = random.randint(2,5)
            if self.nombreMonstre == 3 :
                itemLootMonstre3 = random.randint(2,5)



            
            if itemLootMonstre1 == 5 :
                    if item.inventaireRempli() == 1 and item.inventaireLook(self.monstre1.loot) >= 1:
                        item.loot(self.monstre1.loot)
                    elif item.inventaireRempli() == 1 and item.inventaireLook(self.monstre1.loot) == 0:
                        self.lootMonstre1 = self.monstre1.loot
                        self.inventairePlein = 1
                        self.objetEnAttente.append(self.monstre1.loot)
                        self.longueurListe += 1
                        self.nombreObjetEnAttente += 1
                    else :
                        item.loot(self.monstre1.loot)

            
            if itemLootMonstre2 == 5 :
                    if item.inventaireRempli() == 1 and item.inventaireLook(self.monstre2.loot) >= 1:
                        item.loot(self.monstre2.loot)
                    elif item.inventaireRempli() == 1 and item.inventaireLook(self.monstre2.loot) == 0:
                        self.lootMonstre2 = self.monstre2.loot
                        self.inventairePlein = 1
                        self.objetEnAttente.append(self.monstre2.loot)
                        self.longueurListe += 1
                        self.nombreObjetEnAttente += 1
                    elif item.inventaireRempli() == 0 :
                        item.loot(self.monstre2.loot)
     
            
            if itemLootMonstre3 == 5 :
                    if item.inventaireRempli() == 1 and item.inventaireLook(self.monstre3.loot) >= 1:
                        item.loot(self.monstre3.loot)
                    elif item.inventaireRempli() == 1 and item.inventaireLook(self.monstre3.loot) == 0:
                        self.lootMonstre3 = self.monstre3.loot
                        self.inventairePlein = 1
                        self.objetEnAttente.append(self.monstre3.loot)
                        self.longueurListe += 1
                        self.nombreObjetEnAttente += 1
                    elif item.inventaireRempli() == 0 :
                        item.loot(self.monstre3.loot)
                        



            if itemLootMonstre1 == 5 or itemLootMonstre2 == 5 or itemLootMonstre3 == 5 :  
                if itemLootMonstre1 == 5 and itemLootMonstre2 != 5 and itemLootMonstre3 != 5 :
                    textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre1.loot,personnage)) + ".",1,(0,0,0))
                    
                elif itemLootMonstre1 != 5 and itemLootMonstre2 == 5 and itemLootMonstre3 != 5 :
                    textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre2.loot,personnage)) + ".",1,(0,0,0))
                elif itemLootMonstre1 != 5 and itemLootMonstre2 != 5 and itemLootMonstre3 == 5 :
                    textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre3.loot,personnage)) + ".",1,(0,0,0))
                    
                elif itemLootMonstre1 == 5 and itemLootMonstre2 == 5 and itemLootMonstre3 != 5 :
                    if self.monstre1.loot == self.monstre2.loot :
                        textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre1.loot,personnage)) + " x2.",1,(0,0,0))
                    else :
                        textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre1.loot,personnage)) + ", " + str(item.nomObjet(self.monstre2.loot,personnage)) + ".",1,(0,0,0))
                        
                elif itemLootMonstre1 == 5 and itemLootMonstre2 != 5 and itemLootMonstre3 == 5 :
                    if self.monstre1.loot == self.monstre3.loot :
                        textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre1.loot,personnage)) + " x2.",1,(0,0,0))
                    else :
                        textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre1.loot,personnage)) + ", " + str(item.nomObjet(self.monstre3.loot,personnage)) + ".",1,(0,0,0))

                elif itemLootMonstre1 != 5 and itemLootMonstre2 == 5 and itemLootMonstre3 == 5 :
                    if self.monstre2.loot == self.monstre3.loot :
                        textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre2.loot,personnage)) + " x2.",1,(0,0,0))
                    else :
                        textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre2.loot,personnage)) + ", " + str(item.nomObjet(self.monstre3.loot,personnage)) + ".",1,(0,0,0))

                elif itemLootMonstre1 == 5 and itemLootMonstre2 == 5 and itemLootMonstre3 == 5 :
                    if self.monstre1.loot == self.monstre2.loot == self.monstre3.loot :
                        textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre1.loot,personnage)) + " x3.",1,(0,0,0))
                    elif self.monstre1.loot == self.monstre2.loot != self.monstre3.loot :
                        textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre1.loot,personnage)) + " x2, " + str(item.nomObjet(self.monstre3.loot,personnage)) + ".",1,(0,0,0))
                    elif self.monstre1.loot == self.monstre3.loot != self.monstre2.loot :
                        textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre1.loot,personnage)) + " x2, " + str(item.nomObjet(self.monstre2.loot,personnage)) + ".",1,(0,0,0))
                    elif self.monstre2.loot == self.monstre3.loot != self.monstre1.loot :
                        textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre1.loot,personnage)) + ", " + str(item.nomObjet(self.monstre2.loot,personnage)) + " x2.",1,(0,0,0))
                    else :
                        textGainLoot = self.fondtext.render("Vous gagnez : " + str(item.nomObjet(self.monstre1.loot,personnage)) + ", " + str(item.nomObjet(self.monstre2.loot,personnage))+ "," + str(item.nomObjet(self.monstre3.loot,personnage)) + ".",1,(0,0,0))

                
                
                
                fen1.blit(textGainLoot,(300,390))



            
            

