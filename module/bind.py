'''Centre névralgique du programme, c'est cette page qui appel successivement chaque module
pour rediriger l'utilisateur sur les bons menus à chacunes de ses actions.
Ce module regroupe l'ensemble des class du projet afin de pouvoir les placer en paramètre des fonctions
qui sont appelé tout au long du déroulement du jeu.
Chaque fois que le joueur est appelé à effectuer une action via le clavier,
l'action est traité ici et en fonction du menu où se trouve le joueur, le programme redirige
l'utilisateur vers la fonction demandée'''


import pygame,os,random
from sys import exit
from pygame.locals import *
from module.statistiques import *
from module.menu_action import *
from module.menu_classe import *
from module.menu_auberge import *
from module.menu_inventaire import *
from module.sauvegarde import *
from module.menu_competence import *
from module.menu_auberge_combat import *
from module.objet import *
from module.worldmap_v1 import *
from module.combat import *
from module.event import *
from module.animation import *
from module.story import *
from module.marchands import *
from module.menu_esclaves import *
from module.compagnon import *
from module.menu_quete import *
from module.auberge_compagnons import *
from module.attaques import *
from module.item_ID import *
from module.quete_assaut import *


def creaCombat(fen1,ID1=0,ID2=0,ID3=0,num=0): #fonction activant un combat
    global carte,auberge,personnage,GestionPop,item,story,comp,combat
    combat = gestionCombat(fen1,personnage,item,carte,comp,story,ID1,ID2,ID3,num)
    

def creaComp(fen1,ID=1,effet = 1): #fonction gérant les compagnons
    global carte,auberge,personnage,GestionPop,item,story,comp
    comp = compagnon(effet,ID,personnage)
    
    

def BindDepart(fen1,event):
    global carte,auberge,personnage,GestionPop,item,story,comp
    if event.type == KEYDOWN:
        if event.key == K_1:
            personnage,carte,auberge,GestionPop,item,story,comp = ChoixClasse(fen1)
            if story.cinematique == True:
                story.Affichage_cine(fen1,personnage,carte,item,comp)
            save(fen1)
        if event.key == K_2:
            load(fen1)


def BindAction(fen1,event):
    global carte,auberge,personnage,GestionPop,item,story,comp
    if event.type == KEYDOWN:
        if event.key == K_1:
            Auberge(fen1,personnage,item,carte)
        if event.key == K_2:
            personnage.position_pointeur = 0
            Forgeron_craft(fen1,personnage,item)
        if event.key == K_3:
            personnage.position_pointeur = 1
            Vente(fen1,personnage,item)
        if event.key == K_4:
            menuEsclaves(fen1,personnage,comp,item)
        if event.key == K_5:
            Alchimiste(fen1,personnage,item)
        if event.key == K_SEMICOLON:
            carte.reprise(fen1,personnage,item,comp) #après une sauvegarde, donc carte existe déjà, pas besoin de la récréer
            if story.activation_quetes[3] == 0 and story.activation_quetes[2] == 3: #déclenche une quête à la sortie du second village
                quete = quest_ID(fen1,3,personnage,item,story,comp,carte)
        if event.key == K_6:
            sauvegarde(fen1,personnage,carte,auberge,GestionPop,item,story,comp,personnage.save,"action")
        if event.key == K_7:
            load(fen1)
        if event.key == K_8: #Stoppe tous les évenements pygame et arrête la lecture du programme
            pygame.quit()
            exit(1)

        if event.key == K_n:
            compagnonAuberge(fen1,personnage,item,carte,comp)



def BindSave(fen1,event): #sauvergarde uniquement au premier démarrage de l'application, pour créer son personnage, et le sauvegarder à un emplacement donné
    global carte,auberge,personnage,GestionPop,item,story,comp
    if event.type == KEYDOWN:
        if event.key == K_1:
            sauvegarde(fen1,personnage,carte,auberge,GestionPop,item,story,comp,"1","")
            personnage.save = 1
            carte.chargement(fen1,personnage,item,comp)

        if event.key == K_2:
            sauvegarde(fen1,personnage,carte,auberge,GestionPop,item,story,comp,"2","")
            personnage.save = 2
            carte.chargement(fen1,personnage,item,comp)

        if event.key == K_3:
            sauvegarde(fen1,personnage,carte,auberge,GestionPop,item,story,comp,"3","")
            personnage.save = 3
            carte.chargement(fen1,personnage,item,comp)

def BindLoad(fen1,event):
    global carte,auberge,personnage,GestionPop,item,story,comp
    if event.type == KEYDOWN:
        if event.key == K_1:
            carte,personnage,auberge,GestionPop,item,story,comp = Chargement(fen1,"1")
            carte.chargement(fen1,personnage,item,comp)
        if event.key == K_2:
            carte,personnage,auberge,GestionPop,item,story,comp = Chargement(fen1,"2")
            carte.chargement(fen1,personnage,item,comp)
        if event.key == K_3:
            carte,personnage,auberge,GestionPop,item,story,comp = Chargement(fen1,"3")
            carte.chargement(fen1,personnage,item,comp)


#Bind du menu principale de l'auberge : 1 pour retourner sur le menu action, 2 pour prendre une biere (-5or,+1pv),
#3 pour un steak (-20or,+5pv) et 5 pour lancer le menu duel
def BindAuberge(fen1,event):
    if carte.lettre == "V":
        biome_autour = carte.varA
    elif carte.lettre == "S":
        biome_autour = carte.varB
    elif carte.lettre == "D" or carte.lettre == "N":
        biome_autour = carte.varC
        
    if event.type == KEYDOWN:
        if event.key == K_1:
            Action(fen1)
        if event.key == K_2:
            biere(fen1,personnage,item,carte)
        if event.key == K_3:
            steak(fen1,personnage,item,carte)
        if event.key == K_4:
            chambre(fen1,personnage,item,carte)  
        if event.key == K_5:
            auberge.menuDuel(fen1,personnage,item)
        if event.key == K_6:
            if biome_autour == "desert" and personnage.karus == 1 or biome_autour == "marais" and personnage.iriszia == 1 or biome_autour == "plaine" and personnage.archimage == 1:
                compagnonAuberge(fen1,personnage,item,carte,comp,story)


def BindLancerCombatAuberge(fen1,event):
    if event.type == KEYDOWN:
        if event.key == K_1:
            Auberge(fen1,personnage,item,carte)
        if event.key == K_2:
            auberge.gestionCombatAuberge(fen1,personnage,item)

def BindCombatAuberge(fen1,event):
    if event.type == KEYDOWN:
        if event.key == K_1 and auberge.choixAttaque == 1 or event.key == K_2 and auberge.choixAttaque == 2 or event.key == K_3 and auberge.choixAttaque == 3:
            auberge.attaqueCombatAuberge(fen1,personnage,item)
        else : auberge.attaqueRater(fen1,personnage,item)
        
def BindVictoireAuberge(fen1,event):
    if event.type == KEYDOWN:
        if event.key == K_1:
            Auberge(fen1,personnage,item,carte)



def BindConsole(fen1,event):
    global carte,auberge,personnage,GestionPop,item,story,comp,combat
    if event.type == KEYDOWN:
        if event.key == K_BACKSPACE:
            carte.commande = carte.commande[:-1]
            carte.Console(fen1)
            if carte.commande == "":
                if len(carte.historique_console) > 0:
                    carte.positionConsole = len(carte.historique_console)-1
                else:
                    carte.positionConsole = 0
        
        elif event.key == K_RETURN or event.key == K_KP_ENTER:
            carte.historique_console.append(carte.commande)
            carte.positionConsole = len(carte.historique_console)-1
            if carte.commande == "":
                carte.reprise(fen1,personnage,item,comp)
            elif carte.commande == "aide" or carte.commande == "help":
                carte.help = 1
                carte.commande = ""
                carte.erreur = ""
                carte.Console(fen1)
            else:
                try:
                    carte.reprise(fen1,personnage,item,comp)
                    exec(carte.commande)
                    carte.commande = ""
                except NameError:
                    carte.help = 0
                    carte.erreur = "Commande non définie"
                    carte.commande = ""
                    carte.Console(fen1)
                except SyntaxError:
                    carte.help = 0
                    carte.erreur = "Erreur de syntaxe"
                    carte.commande = ""
                    carte.Console(fen1)
                except TypeError:
                    carte.help = 0
                    carte.erreur = "Argument manquant"
                    carte.commande = ""
                    carte.Console(fen1)
                except AttributeError:
                    carte.help = 0
                    carte.erreur = "Erreur d'attribution"
                    carte.commande = ""
                    carte.Console(fen1)
                

        elif event.key == K_UP:
            if len(carte.historique_console) > 0:
                carte.commande = carte.historique_console[carte.positionConsole]
            carte.Console(fen1)
            if carte.positionConsole > 0:
                carte.positionConsole -= 1
                    
        elif event.key == K_ESCAPE:
            carte.reprise(fen1,personnage,item,comp)
        else :
            carte.commande += event.unicode
            carte.Console(fen1)



def BindWorldMap(fen1,event):
    global carte,auberge,personnage,GestionPop,item,story,comp,combat
    if event.type == KEYDOWN:
            if event.key == K_RSHIFT:
                Competence(fen1,personnage,item,GestionPop,comp)
            if event.key == K_LSHIFT:
                carte.aide(fen1)
            if event.key == K_DELETE:
                Action(fen1)
            if event.key == K_ESCAPE:
                carte.pause(fen1)
            if event.key == K_RETURN or event.key == K_KP_ENTER:
                if len(carte.historique_console) > 0:
                    carte.positionConsole = len(carte.historique_console)-1
                else:
                    carte.positionConsole = 0
                carte.commande = ""
                carte.erreur = ""
                carte.help = 0
                carte.Console(fen1)
                time.sleep(0.5)
            if event.key == K_SPACE:
                carte.mini(fen1,personnage,item)
            if event.key == K_F5:
                sauvegarde(fen1,personnage,carte,auberge,GestionPop,item,story,comp,personnage.save,"carte")
            if event.key == K_i:
                Inventaire(fen1,item,personnage)  
                titreInventaireWorldmap(fen1,item)
            if event.key == K_k:
                Menu_quete(fen1,story,personnage,item,comp,carte)



            #Démarrage du combat
            if carte.debutCombat <= 0:
                if carte.repousse <= 0:
                    combat = gestionCombat(fen1,personnage,item,carte,comp,story,0,0,0,0)
                    carte.debutCombat = random.randint(100,250)
                else:
                    carte.repousse -= 1
                    carte.debutCombat = random.randint(100,250)

            elif carte.debutEvent <= 0:
                VX,VY = 0,0
                Choix_Event(fen1,self,personnage,item,comp,story)
                
            else:
                carte.debutCombat -= 1
                carte.debutEvent -= 1

            
                if event.key == K_UP or event.key == K_w:
                    VX, VY = 0, carte.vitesse
                    GestionPop.modifPopulation(fen1,personnage,item)
                    carte.animation(fen1,VX, VY,personnage,item,GestionPop,story,comp)

                        
                if event.key == K_DOWN or event.key == K_s :
                    VX, VY = 0, -carte.vitesse
                    GestionPop.modifPopulation(fen1,personnage,item)
                    carte.animation(fen1,VX, VY,personnage,item,GestionPop,story,comp)

                        
                if event.key == K_LEFT or event.key == K_a:
                    VX, VY = carte.vitesse, 0
                    GestionPop.modifPopulation(fen1,personnage,item)
                    carte.animation(fen1,VX, VY,personnage,item,GestionPop,story,comp)

                        
                if event.key == K_RIGHT or event.key == K_d :
                    VX, VY = -carte.vitesse, 0
                    GestionPop.modifPopulation(fen1,personnage,item)
                    carte.animation(fen1,VX, VY,personnage,item,GestionPop,story,comp)





def BindPause(fen1,event):
    global carte,auberge,personnage,GestionPop,item,story,comp
    if event.type == KEYDOWN:
        if event.key == K_1:
            Competence(fen1,personnage,item,GestionPop,comp)
        if event.key == K_2:
            Inventaire(fen1,item,personnage)  
            titreInventaireWorldmap(fen1,item)
        if event.key == K_3:
            Menu_quete(fen1,story,personnage,item,comp,carte)
        if event.key == K_4:
            sauvegarde(fen1,personnage,carte,auberge,GestionPop,item,story,comp,personnage.save,"carte")            
        if event.key == K_5:
            load(fen1)
        if event.key == K_6: #Stoppe tous les évenements pygame et arrête la lecture du programme
            pygame.quit()
            exit(1)
        if event.key == K_7: #Stoppe tous les évenements pygame et arrête la lecture du programme
             carte.aide(fen1)
        if event.key == K_ESCAPE:
            carte.reprise(fen1,personnage,item,comp)
            
def BindMiniMap(fen1,event):
    if event.type == KEYDOWN:
        if event.key == K_SPACE:
            carte.reprise(fen1,personnage,item,comp)
        if event.key == K_ESCAPE:
            carte.reprise(fen1,personnage,item,comp)


#Bind pour parier de l'or sur un duel à l'auberge : 1 pour lancer le duel et 2 pour parier de l'or           
def BindParie(fen1,event):
    if event.type == KEYDOWN:
        if event.key == K_1:
            auberge.combatAuberge(fen1,personnage,item,carte)
        if event.key == K_2:
            auberge.parie1(fen1,personnage,item)


#Bind pour passer du menu de duel au menu de l'auberge
def BindRetourDuel(fen1,event):
    if event.type == KEYDOWN:
        if event.key == K_1:
            auberge.menuDuel(fen1,personnage,item)


#Bind lors d'un combat contre un seul monstre, 1 taper directement le monstre 1, 4 fuite
def BindCombat(fen1,event):
    if event.type == KEYDOWN:
        if event.key == K_1:
            anim1(combat,fen1,personnage,item,comp,story)
            time.sleep(0.5)
            attaqueJoueurMonstre1(combat,fen1,personnage,item,comp,story)
        if event.key == K_2:
            combat.competenceSpeciale(fen1,personnage,item,comp)
        if event.key == K_3:
            combat.menuInventCombat(fen1,personnage,item,comp)
        if event.key == K_4:
            combat.fuite(fen1,personnage,item,carte,comp,story)




#Bind lors d'un combat contre plusieurs monstres, 1 affiche le menu de selection du monstre a taper.
#Si 2 monstres : BindChoix 1, si 3 monstres : Binchoix 2
#3 fuite
def BindCombat2(fen1,event):
    if event.type == KEYDOWN:
        if event.key == K_1:
            combat.majMulti(fen1,personnage,item,comp)
        if event.key == K_2:
            combat.competenceSpeciale(fen1,personnage,item,comp)
        if event.key == K_3:
            combat.menuInventCombat(fen1,personnage,item,comp)
        if event.key == K_4 and story.activation_quetes[7] != 1 :
            combat.fuite(fen1,personnage,item,carte,comp,story)


#Bind pour le choix de la cible à taper en combat contre 2 ou 3 monstres : 1 monstre 1 et 2 monstre 2
#et 3 soit monstre 3(si 3 monstres) soit retour(si 2 monstres), 4 retour (si 3 monstres)
def BindChoix(fen1,event):
    if event.type == KEYDOWN:
        if event.key == K_1:
            anim1(combat,fen1,personnage,item,comp,story)
            time.sleep(0.5)
            attaqueJoueurMonstre1(combat,fen1,personnage,item,comp,story)
        if event.key == K_2:
            anim2(combat,fen1,personnage,item,comp)
            time.sleep(0.5)
            attaqueJoueurMonstre2(combat,fen1,personnage,item,comp,story)
            
        if personnage.ennemi == 3:
            if event.key == K_3:
                anim3(combat,fen1,personnage,item,comp,story)
                time.sleep(0.5)
                attaqueJoueurMonstre3(combat,fen1,personnage,item,comp,story)

            if event.key == K_4:
                combat.retour(fen1,personnage,item,comp,story)
                
        else:
            if event.key == K_3:
                combat.retour(fen1,personnage,item,comp,story)



#Bind qui relance la map lors de la victoire en combat
def BindVictoire(fen1,event):
    global comp
    
    if event.type == KEYDOWN:
        if event.key == K_1:
            if story.activation_quetes[7] == 1:
                personnage.vie = personnage.viemax
                personnage.BatailleVictoire = 1
                assaut.Affichage_rapport(fen1,personnage,carte,item,comp,story)
            else:
                verificationQueteVictoire(fen1,event)
                            
                if combat.inventairePlein == 0 :
                    if personnage.up == 0 or comp.ami == 0 or comp.vie <= 0:
                        carte.reprise(fen1,personnage,item,comp)

                    else :
                        creaComp(fen1,comp.IDCompagnon,1)
                        carte.reprise(fen1,personnage,item,comp)
                    story.verification_quetes(fen1,personnage,item,comp,carte)
                else :
                    combat.inventFull(fen1,personnage,item,comp)
                    
            
            if event.key == K_2:
                if combat.inventairePlein == 1:
                    verificationQueteVictoire(fen1,event)
                    
                    if personnage.up == 0 or comp.ami == 0 or comp.vie <= 0:
                        carte.reprise(fen1,personnage,item,comp)

                    else :
                        creaComp(fen1,comp.IDCompagnon,1)
                        carte.reprise(fen1,personnage,item,comp)
                    story.verification_quetes(fen1,personnage,item,comp,carte)

                

#Bind qui permet de charger une partie quand on perd et meurt en combat
def BindDefaite(fen1,event):
    global carte,auberge,personnage,GestionPop,item,story,comp
    if event.type == KEYDOWN:
        if event.key == K_1:
            if story.activation_quetes[7] == 1:
                personnage.BatailleVictoire = 0
                personnage.vie = personnage.viemax
                assaut.Affichage_rapport(fen1,personnage,carte,item,comp,story)
            else:
                carte,personnage,auberge,GestionPop,item,story,comp = Chargement(fen1,personnage.save)
                carte.chargement(fen1,personnage,item,comp)


####################################################################################

#Attaque directement le monstre 1 quand un seul monstre
def BindASDirect(fen1,event):
    if event.type == KEYDOWN:
        if personnage.classe == "paladin" :
            if event.key == K_1:
                AS1_anim1(combat,fen1,personnage,item,comp,story)
                time.sleep(0.5)
                competenceSpecialePaladin1M1(combat,fen1,personnage,item,comp,story)
            if event.key == K_2:
                AS2_anim1(combat,fen1,personnage,item,comp,story)
                time.sleep(0.5)
                competenceSpecialePaladin2(combat,fen1,personnage,item,comp,story)#Heal du paladin

        if personnage.classe == "voleur" :
            if event.key == K_1:
                competenceSpecialeAssassin1M1(combat,fen1,personnage,item,comp,story)#Attaque speciale 1 du voleur
            if event.key == K_2:
                competenceSpecialeAssassin2M1(combat,fen1,personnage,item,comp,story)#Attaque speciale 2 du voleur

        if personnage.classe == "mage" :
            if event.key == K_1:
                AS1_anim1(combat,fen1,personnage,item,comp,story)
                time.sleep(0.5)
                competenceSpecialeMage1M1(combat,fen1,personnage,item,comp,story)#Attaque speciale 1 du mage
            if event.key == K_2:
                competenceSpecialeMage2(combat,fen1,personnage,item,comp,story)#Attaque speciale 2 du mage
          
        if event.key == K_3:
            combat.retour(fen1,personnage,item,comp,story)#Retour au menu principale du combat
                

#Bind pour le choix de la cible pour l'attaque spéciale quand plusieurs monstres
def BindASChoix(fen1,event):
    if event.type == KEYDOWN:
        if event.key == K_1:
            combat.choixCibleAS1(fen1,personnage,item,comp)#Choix de la cible pour la compétence 1

        if event.key == K_2:
            if personnage.classe == "voleur" :
                combat.choixCibleAS2(fen1,personnage,item,comp)#Choix de la cible pour la compétence 2

            if personnage.classe == "paladin" :
                AS2_anim1(combat,fen1,personnage,item,comp,story)
                time.sleep(0.5)
                competenceSpecialePaladin2(combat,fen1,personnage,item,comp,story)#Heal du paladin

            if personnage.classe == "mage" :
                AS2_anim1(combat,fen1,personnage,item,comp,story)
                time.sleep(0.5)
                competenceSpecialeMage2(combat,fen1,personnage,item,comp,story)#Météore de l'heretique

        if event.key == K_3:
            combat.retour(fen1,personnage,item,comp,story)#Retour au menu principale du combat


#Choix de la cible pour l'attaque spéciale 1
def BindAS_1_Multi(fen1,event):
    if event.type == KEYDOWN:
        if personnage.classe == "mage" :
            if event.key == K_1:
                AS1_anim1(combat,fen1,personnage,item,comp,story)
                time.sleep(0.5)
                competenceSpecialeMage1M1(combat,fen1,personnage,item,comp,story)
            if event.key == K_2:
                AS1_anim2(combat,fen1,personnage,item,comp,story)
                time.sleep(0.5)
                competenceSpecialeMage1M2(combat,fen1,personnage,item,comp,story)
            if personnage.ennemi == 3 :
                if event.key == K_3:
                    AS1_anim3(combat,fen1,personnage,item,comp,story)
                    time.sleep(0.5)
                    competenceSpecialeMage1M3(combat,fen1,personnage,item,comp,story)

        if personnage.classe == "paladin" :
            if event.key == K_1:
                AS1_anim1(combat,fen1,personnage,item,comp,story)
                time.sleep(0.5)
                competenceSpecialePaladin1M1(combat,fen1,personnage,item,comp,story)
            if event.key == K_2:
                competenceSpecialePaladin1M2(combat,fen1,personnage,item,comp,story)
            if personnage.ennemi == 3 :
                if event.key == K_3:
                    competenceSpecialePaladin1M3(combat,fen1,personnage,item,comp,story)

        if personnage.classe == "voleur" :
            if event.key == K_1:
                competenceSpecialeAssassin1M1(combat,fen1,personnage,item,comp,story)
            if event.key == K_2:
                competenceSpecialeAssassin1M2(combat,fen1,personnage,item,comp,story)
            if personnage.ennemi == 3 :
                if event.key == K_3:
                    competenceSpecialeAssassin1M3(combat,fen1,personnage,item,comp,story)
        


        if personnage.ennemi == 3 :
            if event.key == K_4: combat.retour(fen1,personnage,item,comp,story)
        else :
            if event.key == K_3: combat.retour(fen1,personnage,item,comp,story)
            

#Choix de la cible pour l'attaque spéciale 2
def BindAS_2_Multi(fen1,event):
    if event.type == KEYDOWN:
        if personnage.classe == "voleur" :
            if event.key == K_1:
                competenceSpecialeAssassin2M1(combat,fen1,personnage,item,comp,story)
            if event.key == K_2:
                competenceSpecialeAssassin2M2(combat,fen1,personnage,item,comp,story)
            if personnage.ennemi == 3 :        
                if event.key == K_3:
                    competenceSpecialeAssassin2M3(combat,fen1,personnage,item,comp,story)

            
        if personnage.ennemi == 3:
            if event.key == K_4:
                combat.retour(fen1,personnage,item,comp,story)
        else :
            if event.key == K_3:
                combat.retour(fen1,personnage,item,comp,story)


#Bind de retour si la compétence spéciale n'est plus disponible
def BindRetour(fen1,event):
    if event.type == KEYDOWN:
        if event.key == K_3:
            combat.retour(fen1,personnage,item,comp,story)

####################################################################################



def BindCompetence(fen1,event):
    if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            carte.reprise(fen1,personnage,item,comp)
        if event.key == K_RSHIFT:
            carte.reprise(fen1,personnage,item,comp)
    if personnage.competence > 0:
        if event.type == KEYDOWN:
            if event.key == K_1:
                personnage.viemax += 5
                personnage.vie += 5
                personnage.competence -=1
                AffichageCompetences(fen1,personnage,item,GestionPop,comp)     
            if event.key == K_2:
                personnage.principale += 1
                personnage.competence -= 1
                AffichageCompetences(fen1,personnage,item,GestionPop,comp)
            if event.key == K_3:
                personnage.constitution += 1
                personnage.competence -= 1
                AffichageCompetences(fen1,personnage,item,GestionPop,comp)
            if personnage.esquive < 50:
                if event.key == K_4:
                    personnage.esquive += 1
                    personnage.competence -= 1
                    AffichageCompetences(fen1,personnage,item,GestionPop,comp)

            if personnage.critique < 50 and personnage.esquive <50:
                if personnage.competence >= 2:
                    if event.key == K_5:
                        personnage.critique += 1
                        personnage.competence -= 2
                        AffichageCompetences(fen1,personnage,item,GestionPop,comp)
                    
            if personnage.critique < 50 and personnage.esquive >=50:
                if personnage.competence >= 2:
                    if event.key == K_4:
                        personnage.critique += 1
                        personnage.competence -= 2
                        AffichageCompetences(fen1,personnage,item,GestionPop,comp)

            
#Bind d'event avec la taxe
def BindEventTaxe(fen1,event):
    global combat
    if event.type == KEYDOWN:
        if event.key == K_1 and personnage.argent >= 200:
            Payer_taxe(fen1,personnage,item,carte)
        if event.key == K_2:
            if personnage.classe != "mage" :
                combat = gestionCombat(fen1,personnage,item,carte,comp,story,502,1,1,1)
            if personnage.classe == "mage" :
                combat = gestionCombat(fen1,personnage,item,carte,comp,story,501,1,1,1)


#Bind de l'event du messager
def BindEventMessager(fen1,event):
      if event.type == KEYDOWN:
        if event.key == K_1:
            carte.regenere(fen1,GestionPop,personnage)
            prendreMessage(fen1,personnage,item,carte,comp)


#Bind de l'event des compagnons
def BindEventCompagnon(fen1,event):
    global combat,comp
    if event.type == KEYDOWN:
        if event.key == K_1:
            if personnage.argent >= 200 :
                personnage.argent -= 200
                if comp.ami == 0:
                    creaComp(fen1,personnage.nouveauCompagnonID,1)
                    carte.reprise(fen1,personnage,item,comp)
                else :
                    ID = comp.IDennemi
                    creaComp(fen1,personnage.nouveauCompagnonID,1)
                    combat = gestionCombat(fen1,personnage,item,carte,comp,story,ID,1,1,1)
            else :
                combat = gestionCombat(fen1,personnage,item,carte,comp,story,personnage.nouveauCompagnonIDennemi,1,1,1)

        if event.key == K_2:
            if personnage.argent >= 200 :
                if comp.ami == 0 :
                    departEventCompagnon(fen1,carte,personnage,item,comp)
                else :
                    if personnage.argent >= 400 :
                        personnage.argent -= 400
                        creaComp(fen1,personnage.nouveauCompagnonID,1)
                        carte.reprise(fen1,personnage,item,comp)
                    else :
                        personnage.argent -= 200
                        combatAncienCompagnon = random.randint(1,2)
                        if combatAncienCompagnon == 1 :
                            ID = comp.IDennemi
                            creaComp(fen1,personnage.nouveauCompagnonID,1)
                            combat = gestionCombat(fen1,personnage,item,carte,comp,story,ID,1,1,1)
                        else :
                            creaComp(fen1,personnage.nouveauCompagnonID,1)
                            carte.reprise(fen1,personnage,item,comp)   
            else :
                departEventCompagnon(fen1,carte,personnage,item,comp)

        if event.key == K_3 and personnage.argent >= 200 and comp.ami != 0 :
            departEventCompagnon(fen1,carte,personnage,item,comp)

            
            
#Bind de l'inventaire sur la world map
def BindInventaire(fen1,event) :
    if event.type == KEYDOWN :
        if event.key == K_1:
            item.emplacement(0,personnage,carte,comp)
        if event.key == K_2:
            item.emplacement(1,personnage,carte,comp)
        if event.key == K_3:
            item.emplacement(2,personnage,carte,comp)
        if event.key == K_4:
            item.emplacement(3,personnage,carte,comp)
        if event.key == K_5:
            item.emplacement(4,personnage,carte,comp)
        if event.key == K_6:
            item.emplacement(5,personnage,carte,comp)
        if event.key == K_7:
            item.emplacement(6,personnage,carte,comp)
        if event.key == K_8:
            item.emplacement(7,personnage,carte,comp)
        if event.key == K_9:
            item.emplacement(8,personnage,carte,comp)
        if event.key == K_0:
            item.emplacement(9,personnage,carte,comp)
        if event.key == K_F1 :
            item.emplacement(13,personnage,carte,comp)
        if event.key == K_F2 :
            item.emplacement(10,personnage,carte,comp)
        if event.key == K_F3 :
            item.emplacement(11,personnage,carte,comp)
        if event.key == K_F4 :
            item.emplacement(12,personnage,carte,comp)            
        Inventaire(fen1,item,personnage)
        titreInventaireWorldmap(fen1,item)
    if event.type == KEYDOWN :
        if event.key == K_i:
            carte.reprise(fen1,personnage,item,comp)
        if event.key == K_ESCAPE:
            carte.reprise(fen1,personnage,item,comp)



def BindInventaireFull(fen1,event) :
    global comp
    if event.type == KEYDOWN :      
        if event.key == K_x:
            if combat.nombreObjetEnAttente == 1 :
                combat.nombreObjetEnAttente = 0
                
            elif combat.nombreObjetEnAttente == 2 :
                if combat.objetEnAttente[0] == combat.objetEnAttente[1]:
                    combat.nombreObjetEnAttente = 0
                    
                else :
                    combat.nombreObjetEnAttente -= 1
                    combat.objetEnAttente.remove(combat.objetEnAttente[0])
                    combat.etatInvent(fen1,personnage,item,comp)
                    
            elif combat.nombreObjetEnAttente == 3 :
                if combat.objetEnAttente[0] == combat.objetEnAttente[1] == combat.objetEnAttente[2]:
                    combat.nombreObjetEnAttente = 0
                    
                elif  combat.objetEnAttente[0] == combat.objetEnAttente[1]:
                    combat.objetEnAttente.remove(combat.objetEnAttente[0])
                    combat.objetEnAttente.remove(combat.objetEnAttente[0])
                    combat.nombreObjetEnAttente -= 2
                    combat.etatInvent(fen1,personnage,item,comp)
                    
                    
                elif  combat.objetEnAttente[0] == combat.objetEnAttente[2]:
                    combat.objetEnAttente.remove(combat.objetEnAttente[0])
                    combat.objetEnAttente.remove(combat.objetEnAttente[1])
                    combat.nombreObjetEnAttente -= 2
                    combat.etatInvent(fen1,personnage,item,comp)

                else :
                    combat.objetEnAttente.remove(combat.objetEnAttente[0])
                    combat.nombreObjetEnAttente -= 1
                    combat.etatInvent(fen1,personnage,item,comp)
                    

                    
            if combat.nombreObjetEnAttente == 0 :
                verificationQueteVictoire(fen1,event)
                
                if personnage.up == 0 or comp.ami == 0 or comp.vie <= 0:
                    carte.reprise(fen1,personnage,item,comp)

                else :
                    creaComp(fen1,comp.IDCompagnon,1)
                    carte.reprise(fen1,personnage,item,comp)
                story.verification_quetes(fen1,personnage,item,comp,carte)

        
        if event.key == K_1:
            objitem = ID_objet(item.ID0,personnage,item)
            if objitem.vente != -1 :
                while item.inventaireRempli() == 1:
                    item.objetPerdu(pos=0)
                    Inventaire(fen1,item,personnage)
                    combat.etatInvent(fen1,personnage,item,comp)
        if event.key == K_2:
            objitem = ID_objet(item.ID1,personnage,item)
            if objitem.vente != -1 :
                while item.inventaireRempli() == 1:
                    item.objetPerdu(pos=1)
                    Inventaire(fen1,item,personnage)
                    combat.etatInvent(fen1,personnage,item,comp)
        if event.key == K_3:
            objitem = ID_objet(item.ID2,personnage,item)
            if objitem.vente != -1 :
                while item.inventaireRempli() == 1:
                    item.objetPerdu(pos=2)
                    Inventaire(fen1,item,personnage)
                    combat.etatInvent(fen1,personnage,item,comp)
        if event.key == K_4:
            objitem = ID_objet(item.ID3,personnage,item)
            if objitem.vente != -1 :
                while item.inventaireRempli() == 1:
                    item.objetPerdu(pos=3)
                    Inventaire(fen1,item,personnage)
                    combat.etatInvent(fen1,personnage,item,comp)
        if event.key == K_5:
            objitem = ID_objet(item.ID4,personnage,item)
            if objitem.vente != -1 :
                while item.inventaireRempli() == 1:
                    item.objetPerdu(pos=4)
                    Inventaire(fen1,item,personnage)
                    combat.etatInvent(fen1,personnage,item,comp)
        if event.key == K_6:
            objitem = ID_objet(item.ID5,personnage,item)
            if objitem.vente != -1 :
                while item.inventaireRempli() == 1:
                    item.objetPerdu(pos=5)
                    Inventaire(fen1,item,personnage)
                    combat.etatInvent(fen1,personnage,item,comp)
        if event.key == K_7:
            objitem = ID_objet(item.ID6,personnage,item)
            if objitem.vente != -1 :
                while item.inventaireRempli() == 1:
                    item.objetPerdu(pos=6)
                    Inventaire(fen1,item,personnage)
                    combat.etatInvent(fen1,personnage,item,comp)
        if event.key == K_8:
            objitem = ID_objet(item.ID7,personnage,item)
            if objitem.vente != -1 :
                while item.inventaireRempli() == 1:
                    item.objetPerdu(pos=7)
                    Inventaire(fen1,item,personnage)
                    combat.etatInvent(fen1,personnage,item,comp)
        if event.key == K_9:
            objitem = ID_objet(item.ID8,personnage,item)
            if objitem.vente != -1 :
                while item.inventaireRempli() == 1:
                    item.objetPerdu(pos=8)
                    Inventaire(fen1,item,personnage)
                    combat.etatInvent(fen1,personnage,item,comp)
        if event.key == K_0:
            objitem = ID_objet(item.ID9,personnage,item)
            if objitem.vente != -1 :
                while item.inventaireRempli() == 1:
                    item.objetPerdu(pos=9)
                    Inventaire(fen1,item,personnage)
                    combat.etatInvent(fen1,personnage,item,comp)

        
        
       
            


def BindInventaireLooter(fen1,event):
    global comp
    if event.type == KEYDOWN :
        if event.key == K_1:
            if combat.nombreObjetEnAttente == 1 :
                item.loot(combat.objetEnAttente[0])
                combat.nombreObjetEnAttente = 0
                
            elif combat.nombreObjetEnAttente == 2 :
                if combat.objetEnAttente[0] == combat.objetEnAttente[1]:
                    for i in range(0,2):
                        item.loot(combat.objetEnAttente[0])
                    combat.nombreObjetEnAttente = 0
                    
                else :
                    item.loot(combat.objetEnAttente[0])
                    combat.nombreObjetEnAttente -= 1
                    combat.objetEnAttente.remove(combat.objetEnAttente[0])
                    combat.etatInvent(fen1,personnage,item,comp)
                    
            elif combat.nombreObjetEnAttente == 3 :
                if combat.objetEnAttente[0] == combat.objetEnAttente[1] == combat.objetEnAttente[2]:
                    for i in range(0,3):
                        item.loot(combat.objetEnAttente[0])
                    combat.nombreObjetEnAttente = 0
                    
                elif  combat.objetEnAttente[0] == combat.objetEnAttente[1]:
                    item.loot(combat.objetEnAttente[0])
                    item.loot(combat.objetEnAttente[1])
                    combat.objetEnAttente.remove(combat.objetEnAttente[0])
                    combat.objetEnAttente.remove(combat.objetEnAttente[0])
                    combat.nombreObjetEnAttente -= 2
                    combat.etatInvent(fen1,personnage,item,comp)
                    
                    
                elif  combat.objetEnAttente[0] == combat.objetEnAttente[2]:
                    item.loot(combat.objetEnAttente[0])
                    item.loot(combat.objetEnAttente[2])
                    combat.objetEnAttente.remove(combat.objetEnAttente[0])
                    combat.objetEnAttente.remove(combat.objetEnAttente[1])
                    combat.nombreObjetEnAttente -= 2
                    combat.etatInvent(fen1,personnage,item,comp)

                else :
                    item.loot(combat.objetEnAttente[0])
                    combat.objetEnAttente.remove(combat.objetEnAttente[0])
                    combat.nombreObjetEnAttente -= 1
                    combat.etatInvent(fen1,personnage,item,comp)
                    

                    
            if combat.nombreObjetEnAttente == 0 :
                Inventaire(fen1,item,personnage)
                time.sleep(1)
                verificationQueteVictoire(fen1,event)
                
                if personnage.up == 0 or comp.ami == 0 or comp.vie <= 0:
                    carte.reprise(fen1,personnage,item,comp)

                else :
                    creaComp(fen1,comp.IDCompagnon,1)
                    carte.reprise(fen1,personnage,item,comp)
                story.verification_quetes(fen1,personnage,item,comp,carte)
            

            
#Bind de l'inventaire en combat
def BindInventCombat(fen1,event):
    if event.type == KEYDOWN :
        if event.key == K_1:
            combat.retour(fen1,personnage,item,comp,story)
        if event.key == K_2:
            if item.inventaireLook(0) > 0 and item.inventaireLook(30) > 0 and combat.cooldownPotion == 0:
                combat.potionVie(fen1,personnage,item,comp)
                combat.retour(fen1,personnage,item,comp,story)

            elif item.inventaireLook(0) == 0 and item.inventaireLook(30) > 0 and combat.cooldownPotion == 0:
                combat.potionGroupe(fen1,personnage,item,comp)
                combat.retour(fen1,personnage,item,comp,story)
            
            elif item.inventaireLook(0) > 0 and item.inventaireLook(30) == 0 and combat.cooldownPotion == 0:
                combat.potionVie(fen1,personnage,item,comp)
                combat.retour(fen1,personnage,item,comp,story)

        if event.key == K_3:
            if item.inventaireLook(0) > 0 and item.inventaireLook(30) > 0 and combat.cooldownPotion == 0:
                combat.potionGroupe(fen1,personnage,item,comp)
                combat.retour(fen1,personnage,item,comp,story)
            



def BindAlchimiste(fen1,event):
    if event.type == KEYDOWN :
        if event.key == K_1:
            Fabrication(fen1,0,item,personnage)
        if event.key == K_2:
            if personnage.alchimiste >= 5:
                Fabrication(fen1,30,item,personnage)
        if event.key == K_3:
            if personnage.alchimiste >= 5:
                if personnage.classe != "mage":
                    Fabrication(fen1,31,item,personnage)
                else:
                    Fabrication(fen1,32,item,personnage)
        if event.key == K_4:
            if personnage.alchimiste >= 15:
                Fabrication(fen1,33,item,personnage)
        if event.key == K_5:
            if personnage.alchimiste >= 15:
                Fabrication(fen1,34,item,personnage)
        if event.key == K_6:
            Action(fen1)

           
def BindForgeron_craft(fen1,event):
    global personnage
    if event.type == KEYDOWN :
        if event.key == K_RIGHT or event.key == K_d:
            if personnage.position_pointeur < 3:
                personnage.position_pointeur += 1
                Forgeron_craft(fen1,personnage,item)
        if event.key == K_LEFT or event.key == K_a:
            if personnage.position_pointeur > 0:
                personnage.position_pointeur -= 1
                Forgeron_craft(fen1,personnage,item)
        if event.key == K_1:
            if personnage.position_pointeur == 0:
                if personnage.classe == "mage":
                    Fabrication(fen1,250,item,personnage)
                if personnage.classe == "paladin":
                    Fabrication(fen1,251,item,personnage)
                if personnage.classe == "voleur":
                    Fabrication(fen1,252,item,personnage)
            if personnage.position_pointeur == 1:
                if personnage.classe == "mage":
                    Fabrication(fen1,100,item,personnage)
                if personnage.classe == "paladin":
                    Fabrication(fen1,101,item,personnage)
                if personnage.classe == "voleur":
                    Fabrication(fen1,102,item,personnage)
            if personnage.position_pointeur == 2:
                if personnage.classe == "mage":
                    Fabrication(fen1,150,item,personnage)
                if personnage.classe == "paladin":
                    Fabrication(fen1,151,item,personnage)
                if personnage.classe == "voleur":
                    Fabrication(fen1,152,item,personnage)
            if personnage.position_pointeur == 3:
                if personnage.classe == "mage":
                    Fabrication(fen1,200,item,personnage)
                if personnage.classe == "paladin":
                    Fabrication(fen1,201,item,personnage)
                if personnage.classe == "voleur":
                    Fabrication(fen1,202,item,personnage)
        if event.key == K_2:
            if personnage.forgeron >= 5:
                if personnage.position_pointeur == 0:
                    if personnage.classe == "mage":
                        Fabrication(fen1,253,item,personnage)
                    if personnage.classe == "paladin":
                        Fabrication(fen1,254,item,personnage)
                    if personnage.classe == "voleur":
                        Fabrication(fen1,255,item,personnage)
                if personnage.position_pointeur == 1:
                    if personnage.classe == "mage":
                        Fabrication(fen1,103,item,personnage)
                    if personnage.classe == "paladin":
                        Fabrication(fen1,104,item,personnage)
                    if personnage.classe == "voleur":
                        Fabrication(fen1,105,item,personnage)
                if personnage.position_pointeur == 2:
                    if personnage.classe == "mage":
                        Fabrication(fen1,153,item,personnage)
                    if personnage.classe == "paladin":
                        Fabrication(fen1,154,item,personnage)
                    if personnage.classe == "voleur":
                        Fabrication(fen1,155,item,personnage)
                if personnage.position_pointeur == 3:
                    if personnage.classe == "mage":
                        Fabrication(fen1,203,item,personnage)
                    if personnage.classe == "paladin":
                        Fabrication(fen1,204,item,personnage)
                    if personnage.classe == "voleur":
                        Fabrication(fen1,205,item,personnage)
        if event.key == K_3:
            if personnage.forgeron >= 15:
                if personnage.position_pointeur == 0:
                    if personnage.classe == "mage":
                        Fabrication(fen1,256,item,personnage)
                    if personnage.classe == "paladin":
                        Fabrication(fen1,257,item,personnage)
                    if personnage.classe == "voleur":
                        Fabrication(fen1,258,item,personnage)
                if personnage.position_pointeur == 1:
                    if personnage.classe == "mage":
                        Fabrication(fen1,106,item,personnage)
                    if personnage.classe == "paladin":
                        Fabrication(fen1,107,item,personnage)
                    if personnage.classe == "voleur":
                        Fabrication(fen1,108,item,personnage)
                if personnage.position_pointeur == 2:
                    if personnage.classe == "mage":
                        Fabrication(fen1,156,item,personnage)
                    if personnage.classe == "paladin":
                        Fabrication(fen1,157,item,personnage)
                    if personnage.classe == "voleur":
                        Fabrication(fen1,158,item,personnage)
                if personnage.position_pointeur == 3:
                    if personnage.classe == "mage":
                        Fabrication(fen1,206,item,personnage)
                    if personnage.classe == "paladin":
                        Fabrication(fen1,207,item,personnage)
                    if personnage.classe == "voleur":
                        Fabrication(fen1,208,item,personnage)
                        
        if event.key == K_4:
            Action(fen1)


def BindVente(fen1,event):
    if event.type == KEYDOWN :
        if event.key == K_1:
            Action(fen1)
            
        if event.key == K_UP or event.key == K_w:
            personnage.position_pointeur -= 1
            if personnage.position_pointeur == 0:
                personnage.position_pointeur = 10
            Vente(fen1,personnage,item)
                
        if event.key == K_DOWN or event.key == K_s :
            personnage.position_pointeur += 1
            if personnage.position_pointeur == 11:
                personnage.position_pointeur = 1
            Vente(fen1,personnage,item)
                
        if event.key == K_RETURN :
            Echanger(fen1,personnage,item)
 
            

def BindMenuEsclave(fen1,event):
    global comp
    if event.type == KEYDOWN :
        if event.key == K_1 and personnage.affichageEsclave1 == 0 :
            infoEsclave1(fen1,personnage,comp,item)
            verificationEsclave(fen1,personnage,comp,item,story)
        if event.key == K_2 and personnage.affichageEsclave2 == 0 :
            infoEsclave2(fen1,personnage,comp,item)
            verificationEsclave(fen1,personnage,comp,item,story)
        if event.key == K_3 and personnage.affichageEsclave3 == 0 :
            infoEsclave3(fen1,personnage,comp,item)
            verificationEsclave(fen1,personnage,comp,item,story)
        if event.key == K_4:
            Action(fen1)


def BindAchatEsclave(fen1,event):
    global comp
    if event.type == KEYDOWN :
        if event.key == K_1:
            if comp.prixFinal <= personnage.argent and (story.activation_quetes[5] == 0 or story.activation_quetes[5] == 3):
                personnage.argent -= comp.prixFinal
                creaComp(fen1,comp.IDC,1)
                choixEsclave(fen1,personnage,comp,item)
                menuEsclaves(fen1,personnage,comp,item)
                
            else :
                menuEsclaves(fen1,personnage,comp,item)
                
        if event.key == K_2 and comp.prixFinal <= personnage.argent and (story.activation_quetes[5] == 1 or story.activation_quetes[5] == 2) :
            menuEsclaves(fen1,personnage,comp,item)
                
            
def BindQuetes(fen1,event):
    if event.type == KEYDOWN :
        if event.key == K_k:
            carte.reprise(fen1,personnage,item,comp)
        if event.key == K_ESCAPE:
            carte.reprise(fen1,personnage,item,comp)

            
def BindChoixPotion(fen1,event):
    if event.type == KEYDOWN :
        if event.key == K_1:
            story.activation_quetes[2] = 2
            quete = quest_ID(fen1,2,personnage,item,story,comp,carte)
            Action(fen1)
        if event.key == K_2:
            Action(fen1)

            
def BindChoixRessources(fen1,event):
    if event.type == KEYDOWN :
        if event.key == K_1:
            story.activation_quetes[4] = 2
            quete = quest_ID(fen1,4,personnage,item,story,comp,carte)
        if event.key == K_2:
            Action(fen1)

def BindChoixQuete5(fen1,event):
    global comp,story
    if event.type == KEYDOWN :
        if story.activation_quetes[5] == 3:
            if event.key == K_1:
                if story.ancienComp == 1 :
                    creaComp(fen1,story.ancienCompID,1)
                else : comp.ami = 0
                quete = quest_ID(fen1,6,personnage,item,story,comp,carte)
            
        else :
            if event.key == K_1:
                story.activation_quetes[5] = 1
                story.objectif_quetes[5] = 1
                creaComp(fen1,19,1)
                Action(fen1)
            if event.key == K_2:
                Action(fen1)


def BindChoixQuete6(fen1,event):
    global story,assaut
    if event.type == KEYDOWN :
        if event.key == K_1:
            story.activation_quetes[6] = 3
            story.activation_quetes[7] = 1
            assaut = Quete_assaut(fen1,personnage)
        if event.key == K_2:
            Action(fen1)
            
                
def BindAide(fen1,event):
    if event.type == KEYDOWN :
        if event.key == K_LSHIFT:
            carte.reprise(fen1,personnage,item,comp)
        if event.key == K_ESCAPE:
            carte.reprise(fen1,personnage,item,comp)

def BindAubergeCompagnon(fen1,event):
    global comp
    if event.type == KEYDOWN :
        if event.key == K_1:
            if personnage.argent >= 500 and (story.activation_quetes[5] == 0 or story.activation_quetes[5] == 3):
                if personnage.nouveauCompagnonID == 16 : personnage.karus = 0
                elif personnage.nouveauCompagnonID == 17 : personnage.iriszia = 0
                elif personnage.nouveauCompagnonID == 18 : personnage.archimage = 0

                personnage.argent -= 500
                creaComp(fen1,personnage.nouveauCompagnonID,1)
                Auberge(fen1,personnage,item,carte)

                    
            else : Auberge(fen1,personnage,item,carte)

        if event.key == K_2:
            if personnage.argent >= 500 :
                Auberge(fen1,personnage,item,carte)


def verificationQueteVictoire(fen1,event):
    for i in range (0,len(story.activation_quetes)):
        if story.activation_quetes[i] == 1:
            quete = quest_ID(fen1,i,personnage,item,story,comp,carte)
            if quete.type == "tuerie":
                story.objectif_quetes[i] -= 1
                
            if quete.type == "Chercher":
                if item.inventaireLook(90) == 3:
                    story.objectif_quetes[i] -= 1
                elif comp.ami == 0 :
                    story.echec_quetes(fen1,personnage,item,comp,carte)




def BindPlacementAssaut(fen1,event):
    global assaut
    if event.type == KEYDOWN :
        if event.key == K_1:
            if assaut.soldat >= assaut.unite:
                assaut.front1 += assaut.unite
                assaut.soldat -= assaut.unite
            else:
                assaut.front1 += assaut.soldat
                assaut.soldat = 0
            assaut.placement(fen1)
                
        if event.key == K_2:
            if assaut.soldat >= assaut.unite:
                assaut.front2 += assaut.unite
                assaut.soldat -= assaut.unite
            else:
                assaut.front2 += assaut.soldat
                assaut.soldat = 0
            assaut.placement(fen1)
            
        if event.key == K_3:
            if assaut.soldat >= assaut.unite:
                assaut.front3 += assaut.unite
                assaut.soldat -= assaut.unite
            else:
                assaut.front3 += assaut.soldat
                assaut.soldat = 0
            assaut.placement(fen1)

                
        if event.key == K_LEFT or event.key == K_a:
            if assaut.frontjoueur > 1 and assaut.bataille < 5:
                assaut.frontjoueur -= 1
                assaut.placement(fen1)
                
        if event.key == K_RIGHT or event.key == K_d :
            if assaut.frontjoueur < 3 and assaut.bataille < 5:
                assaut.frontjoueur += 1
                assaut.placement(fen1)
        
        if event.key == K_RETURN:
            assaut.placement_ennemi(fen1,personnage)
    



def BindRapportAssaut(fen1,event):
    global assaut
    if event.type == KEYDOWN :
        if event.key == K_1:
            assaut.front1,assaut.front2,assaut.front3 = 0,0,0
            assaut.bataille += 1
            assaut.placement(fen1)
















