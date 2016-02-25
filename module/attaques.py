import pygame,random,time
from module.ennemi import *
from module.worldmap_v1 import *
from module.objet import *
from module.menu_inventaire import *
from module.compagnon import *
from module.menu_classe import *
from module.menu_esclaves import *
from module.combat import *


#Fonction pour les attaques des monstres.
#Le % de toucher est lié à l'esquive du personnage, un nombre est tiré aléatoirement entre 1 et 100, si le nombre est plus petit
#ou égale à l'esquive alors le monstre rate son attaque, sinon il touche et inflige des dégâts au joueur.
#Chaque monstre a sa propre chance de toucher, indépendante des autres monstres.
def attaqueMonstre(combat,fen1,personnage,item,comp):
    #1 monstre, il tape avec une chance de rater
    if combat.monstreVivant1 == 1 :
        attaqueMonstre1(combat,fen1,personnage,item,comp)#Appel la fonction gérant l'attaque du monstre 1

    #2 monstres , si le monstre est vivant il tape avec une chance de rater
    if combat.nombreMonstre == 2 or combat.nombreMonstre == 3:  
        if combat.monstreVivant2 == 1 :
            attaqueMonstre2(combat,fen1,personnage,item,comp)#Appel la fonction gérant l'attaque du monstre 2
            
    #3 monstres, si le monstre est vivant il tape avec une chance de rater
    if combat.nombreMonstre == 3 :
        if combat.monstreVivant3 == 1 :
            attaqueMonstre3(combat,fen1,personnage,item,comp)#Appel la fonction gérant l'attaque du monstre 2

                    

#Attaque du monstre 1
def attaqueMonstre1(combat,fen1,personnage,item,comp):
    if combat.stunMonstre1 == 0 :
        toucherMonstre1 = random.randint(1,100) #Chance de toucher
        dgtMonstre1 = random.randint(combat.monstre1.dgtMin,combat.monstre1.dgtMax) #Degat aléatoire entre les dgts min et max

        if combat.monstre1.ID in combat.monstre1.listHeal :
            choixMonstreAttaque = random.randint(1,3)
                       

        if combat.monstre1.ID not in combat.monstre1.listHeal or choixMonstreAttaque < 3 :
            if comp.ami !=0 :
                if comp.IDCompagnon not in comp.listTank : choixAttaque = random.randint(1,2)
                else : choixAttaque = random.randint(1,4)

            if comp.ami == 0 or choixAttaque == 1 or comp.vie <= 0: 
                dgtMstr1 = dgtMonstre1 - (personnage.constitution + personnage.armure) #Degat du monstre (dgtMonstre1) - la resistance du joueur
                if toucherMonstre1 > personnage.esquive : #Le monstre touche le joueur
                    if dgtMonstre1 <= personnage.constitution + personnage.armure : #Degats du monstre inférieur à la resistance du joueur
                        dgtMstr1 = random.randint(0,1) #1 chance sur 2 de faire soit 1 soit 0 de degat au joueur
                        if dgtMstr1 == 1 : personnage.vie -= 1
                        else : personnage.vie -= 0
                    else :
                        personnage.vie -= dgtMstr1 #Degat du monstre - resistance du joueur
                    textDegatMonstre1  = combat.fondtext.render("-" + str(dgtMstr1),1,(255,0,0))
                                                            
                else : textDegatMonstre1  = combat.fondtext.render("Rate",1,(0,0,255))

                if comp.ami == 0 : fen1.blit(textDegatMonstre1,(210,270))
                else : fen1.blit(textDegatMonstre1,(210,330))

            else :
                dgtMstr1 = dgtMonstre1 
                if toucherMonstre1 > comp.esquive :
                    comp.vie -= dgtMstr1
                    textDegatMonstre1  = combat.fondtext.render("-" + str(dgtMstr1),1,(255,0,0))
                                                            
                else : textDegatMonstre1  = combat.fondtext.render("Rate",1,(0,0,255))

                
                fen1.blit(textDegatMonstre1,(210,155))


        else :
            choixMonstre_a_Heal(combat,fen1,personnage,item,comp)
            if choixMonstreHeal == 4 : attaqueMonstre1(combat,fen1,personnage,item,comp)
            else : monstreHeal1(combat,fen1,personnage,item,comp)

                    
    
#Attaque du monstre 2
def attaqueMonstre2(combat,fen1,personnage,item,comp):
    if combat.stunMonstre2 == 0 :
        toucherMonstre2 = random.randint(1,100)
        dgtMonstre2 = random.randint(combat.monstre2.dgtMin,combat.monstre2.dgtMax)

        if combat.monstre2.ID in combat.monstre2.listHeal :
            choixMonstreAttaque = random.randint(1,3)
            
            
        if combat.monstre2.ID not in combat.monstre2.listHeal or choixMonstreAttaque < 3 :
            if comp.ami !=0 :
                if comp.IDCompagnon not in comp.listTank : choixAttaque = random.randint(1,2)
                else : choixAttaque = random.randint(1,4)


            if comp.ami == 0 or choixAttaque == 1 or comp.vie <= 0:
                dgtMstr2 = dgtMonstre2 - (personnage.constitution + personnage.armure)
                if toucherMonstre2 > personnage.esquive : #Le monstre touche le joueur
                    if dgtMonstre2 <= personnage.constitution + personnage.armure : #Degats du monstre inférieur à la resistance du joueur
                        dgtMstr2 = random.randint(0,1) #1 chance sur 2 de faire soit 1 soit 0 de degat au joueur
                        if dgtMstr2 == 1 : personnage.vie -= 1
                        else : personnage.vie -= 0
                    else :
                        personnage.vie -= dgtMstr2 #Degat du monstre - resistance du joueur
                    textDegatMonstre2  = combat.fondtext.render("-" + str(dgtMstr2),1,(255,0,0))
                else : textDegatMonstre2  = combat.fondtext.render("Rate",1,(0,0,255))
                    
                if comp.ami == 0 : fen1.blit(textDegatMonstre2,(240,270))
                else : fen1.blit(textDegatMonstre2,(240,330))

            else :
                dgtMstr2 = dgtMonstre2 
                if toucherMonstre2 > comp.esquive :
                    comp.vie -= dgtMstr2
                    textDegatMonstre2  = combat.fondtext.render("-" + str(dgtMstr2),1,(255,0,0))
                                                            
                else : textDegatMonstre2  = combat.fondtext.render("Rate",1,(0,0,255))
                
                fen1.blit(textDegatMonstre2,(240,155))

                
        else :
            choixMonstre_a_Heal(combat,fen1,personnage,item,comp)
            if choixMonstreHeal == 4 : attaqueMonstre2(combat,fen1,personnage,item,comp)
            else : monstreHeal2(combat,fen1,personnage,item,comp)



#Attaque du monstre 3
def attaqueMonstre3(combat,fen1,personnage,item,comp):
    if combat.stunMonstre3 == 0 :
        toucherMonstre3 = random.randint(1,100)
        dgtMonstre3 = random.randint(combat.monstre3.dgtMin,combat.monstre3.dgtMax)

        if combat.monstre3.ID in combat.monstre3.listHeal :
            choixMonstreAttaque = random.randint(1,3)
            
        
        if combat.monstre3.ID not in combat.monstre3.listHeal or choixMonstreAttaque < 3 :      
            if comp.ami !=0 :
                if comp.IDCompagnon not in comp.listTank : choixAttaque = random.randint(1,2)
                else : choixAttaque = random.randint(1,4)


            if comp.ami == 0 or choixAttaque == 1 or comp.vie <= 0:
                dgtMstr3 = dgtMonstre3 - (personnage.constitution + personnage.armure)
                if toucherMonstre3 > personnage.esquive : #Le monstre touche le joueur
                    if dgtMonstre3 <= personnage.constitution + personnage.armure : #Degats du monstre inférieur à la resistance du joueur
                        dgtMstr3 = random.randint(0,1) #1 chance sur 2 de faire soit 1 soit 0 de degat au joueur
                        if dgtMstr3 == 1 : personnage.vie -= 1
                        else : personnage.vie -= 0
                    else :
                        personnage.vie -= dgtMstr3 #Degat du monstre - resistance du joueur
                    textDegatMonstre3  = combat.fondtext.render("-" + str(dgtMstr3),1,(255,0,0))
                else : textDegatMonstre3  = combat.fondtext.render("Rate",1,(0,0,255))
                    
                if comp.ami == 0 : fen1.blit(textDegatMonstre3,(225,250))
                else : fen1.blit(textDegatMonstre3,(225,310))

            else :
                dgtMstr3 = dgtMonstre3 
                if toucherMonstre3 > comp.esquive :
                    comp.vie -= dgtMstr3
                    textDegatMonstre3  = combat.fondtext.render("-" + str(dgtMstr3),1,(255,0,0))
                                                            
                else : textDegatMonstre3  = combat.fondtext.render("Rate",1,(0,0,255))
                
                fen1.blit(textDegatMonstre3,(225,135))
                

        else :
            choixMonstre_a_Heal(combat,fen1,personnage,item,comp)
            if choixMonstreHeal == 4 : attaqueMonstre3(combat,fen1,personnage,item,comp)
            else : monstreHeal3(combat,fen1,personnage,item,comp)



def choixMonstre_a_Heal(combat,fen1,personnage,item,comp):
    global choixMonstreHeal
    if combat.nombreMonstre == 1 and combat.monstre1.vie != combat.monstre1.viemax :
            choixMonstreHeal = 1
    else : choixMonstreHeal = 4

    if combat.nombreMonstre == 2 :
        if (combat.monstreVivant1 == 1 and combat.monstre1.vie != combat.monstre1.viemax) and (combat.monstreVivant2 == 1 and combat.monstre2.vie != combat.monstre2.viemax) :
            choixMonstreHeal = random.randint(1,2)
        elif (combat.monstreVivant1 == 1 and combat.monstre1.vie != combat.monstre1.viemax) and (combat.monstreVivant2 == 0 or combat.monstre2.vie == combat.monstre2.viemax):
            choixMonstreHeal = 1
        elif (combat.monstreVivant1 == 0 or combat.monstre1.vie == combat.monstre1.viemax) and (combat.monstreVivant2 == 1 and combat.monstre2.vie != combat.monstre2.viemax) :
            choixMonstreHeal = 2
        else : choixMonstreHeal = 4
        
    if combat.nombreMonstre == 3 :
        if (combat.monstreVivant1 == 1 and combat.monstre1.vie != combat.monstre1.viemax) and (combat.monstreVivant2 == 1 and combat.monstre2.vie != combat.monstre2.viemax) and (combat.monstreVivant3 == 1 and combat.monstre3.vie != combat.monstre3.viemax) :
            choixMonstreHeal = random.randint(1,3)
            
        elif (combat.monstreVivant1 == 1 and combat.monstre1.vie != combat.monstre1.viemax) and (combat.monstreVivant2 == 1 and combat.monstre2.vie != combat.monstre2.viemax) and (combat.monstreVivant3 == 0 or combat.monstre3.vie == combat.monstre3.viemax):
            choixMonstreHeal = random.randint(1,2)
            
        elif (combat.monstreVivant1 == 1 and combat.monstre1.vie != combat.monstre1.viemax) and (combat.monstreVivant2 == 0 or combat.monstre2.vie == combat.monstre2.viemax) and (combat.monstreVivant3 == 1 and combat.monstre3.vie != combat.monstre3.viemax):
            monstre = [1,3]
            choixMonstreHeal = random.choice(monstre)
            
        elif (combat.monstreVivant1 == 0 or combat.monstre1.vie == combat.monstre1.viemax) and (combat.monstreVivant2 == 1 and combat.monstre2.vie != combat.monstre2.viemax) and (combat.monstreVivant3 == 1 and combat.monstre3.vie != combat.monstre3.viemax):
            choixMonstreHeal = random.randint(2,3)
            
        elif(combat.monstreVivant1 == 1 and combat.monstre1.vie != combat.monstre1.viemax) and (combat.monstreVivant2 == 0 or combat.monstre2.vie == combat.monstre2.viemax) and (combat.monstreVivant3 == 0 or combat.monstre3.vie == combat.monstre3.viemax):
            choixMonstreHeal = 1
            
        elif (combat.monstreVivant1 == 0 or combat.monstre1.vie == combat.monstre1.viemax) and (combat.monstreVivant2 == 1 and combat.monstre2.vie != combat.monstre2.viemax) and (combat.monstreVivant3 == 0 or combat.monstre3.vie == combat.monstre3.viemax):
            choixMonstreHeal = 2
            
        elif (combat.monstreVivant1 == 0 or combat.monstre1.vie == combat.monstre1.viemax) and (combat.monstreVivant2 == 0 or combat.monstre2.vie == combat.monstre2.viemax) and (combat.monstreVivant3 == 1 and combat.monstre3.vie != combat.monstre3.viemax):
            choixMonstreHeal = 3

        else : choixMonstreHeal = 4

            

def monstreHeal1(combat,fen1,personnage,item,comp):
    healmonstre1 = random.randint(combat.monstre1.healMin,combat.monstre1.healMax)
    if choixMonstreHeal == 1 :
        if combat.monstre1.vie + healmonstre1 > combat.monstre1.viemax :
            healmonstre1 = combat.monstre1.viemax - combat.monstre1.vie
            combat.monstre1.vie += healmonstre1
        else : combat.monstre1.vie += healmonstre1
        textHealMonstre1 = combat.fondtext.render("+" + str(healmonstre1),1,(0,255,0))
        fen1.blit(textHealMonstre1,(590,150))
        
    if choixMonstreHeal == 2 :
        if combat.monstre2.vie + healmonstre1 > combat.monstre2.viemax :
            healmonstre1 = combat.monstre2.viemax - combat.monstre2.vie
            combat.monstre2.vie += healmonstre1
        else : combat.monstre2.vie += healmonstre1
        textHealMonstre1 = combat.fondtext.render("+" + str(healmonstre1),1,(0,255,0))
        fen1.blit(textHealMonstre1,(740,230))
        
    if choixMonstreHeal == 3 :
        if combat.monstre3.vie + healmonstre1 > combat.monstre3.viemax :
            healmonstre1 = combat.monstre3.viemax - combat.monstre3.vie
            combat.monstre3.vie += healmonstre1
        else : combat.monstre3.vie += healmonstre1
        textHealMonstre1 = combat.fondtext.render("+" + str(healmonstre1),1,(0,255,0))
        fen1.blit(textHealMonstre1,(625,330))

        
        

def monstreHeal2(combat,fen1,personnage,item,comp):
    healmonstre2 = random.randint(combat.monstre2.healMin,combat.monstre2.healMax)
    if choixMonstreHeal == 1 :
        if combat.monstre1.vie + healmonstre2 > combat.monstre1.viemax :
            healmonstre2 = combat.monstre1.viemax - combat.monstre1.vie
            combat.monstre1.vie += healmonstre2
        else : combat.monstre1.vie += healmonstre2
        textHealMonstre1 = combat.fondtext.render("+" + str(healmonstre2),1,(0,255,0))
        fen1.blit(textHealMonstre1,(620,150))
        
    if choixMonstreHeal == 2 :
        if combat.monstre2.vie + healmonstre2 > combat.monstre2.viemax :
            healmonstre2 = combat.monstre2.viemax - combat.monstre2.vie
            combat.monstre2.vie += healmonstre2
        else : combat.monstre2.vie += healmonstre2
        textHealMonstre1 = combat.fondtext.render("+" + str(healmonstre2),1,(0,255,0))
        fen1.blit(textHealMonstre1,(770,230))
        
    if choixMonstreHeal == 3 :
        if combat.monstre3.vie + healmonstre2 > combat.monstre3.viemax :
            healmonstre2 = combat.monstre3.viemax - combat.monstre3.vie
            combat.monstre3.vie += healmonstre2
        else : combat.monstre3.vie += healmonstre2
        textHealMonstre1 = combat.fondtext.render("+" + str(healmonstre2),1,(0,255,0))
        fen1.blit(textHealMonstre1,(655,330))
        

def monstreHeal3(combat,fen1,personnage,item,comp):
    healmonstre3 = random.randint(combat.monstre3.healMin,combat.monstre3.healMax)
    if choixMonstreHeal == 1 :
        if combat.monstre1.vie + healmonstre3 > combat.monstre1.viemax :
            healmonstre3 = combat.monstre1.viemax - combat.monstre1.vie
            combat.monstre1.vie += healmonstre3
        else : combat.monstre1.vie += healmonstre3
        textHealMonstre1 = combat.fondtext.render("+" + str(healmonstre3),1,(0,255,0))
        fen1.blit(textHealMonstre1,(605,130))
        
    if choixMonstreHeal == 2 :
        if combat.monstre2.vie + healmonstre3 > combat.monstre2.viemax :
            healmonstre3 = combat.monstre2.viemax - combat.monstre2.vie
            combat.monstre2.vie += healmonstre3
        else : combat.monstre2.vie += healmonstre3
        textHealMonstre2 = combat.fondtext.render("+" + str(healmonstre3),1,(0,255,0))
        fen1.blit(textHealMonstre2,(755,210))
        
    if choixMonstreHeal == 3 :
        if combat.monstre3.vie + healmonstre3 > combat.monstre3.viemax :
            healmonstre3 = combat.monstre3.viemax - combat.monstre3.vie
            combat.monstre3.vie += healmonstre3
        else : combat.monstre3.vie += healmonstre3
        textHealMonstre3 = combat.fondtext.render("+" + str(healmonstre3),1,(0,255,0))
        fen1.blit(textHealMonstre3,(640,310))


#Attaque du personnage sur le monstre 1, affiche les dégats au dessus du monstre tapé avec une chance de rater, si le monstre meurt il ne tape pas le joueur
#La chance de toucher le monstre est différente pour chaque monstre, si le nombre aléatoire personnage.toucherPerso est supérieur à l'esquive du monstre, alors le joueur
#rate son attaque. Systeme identique pour chaque attaque (en fonction du nombre de monstre).
def degatAttaqueMonstre1(combat,fen1,personnage,item,comp):

    
    if combat.monstre1.vie > 0 :
        if personnage.toucherPerso > combat.monstre1.esquive :
            if personnage.chanceCrit > personnage.critique :
                combat.monstre1.vie -= personnage.degat
                textDegatJoueur = combat.fondtext.render("-" + str(personnage.degat),1,(0,0,0))
            else :
                combat.monstre1.vie -= personnage.degat*2
                textDegatJoueur = combat.fondtext.render("-" + str(personnage.degat*2),1,(255,0,0))
        

        #Si le joueur rate son attaque (personnage.toucherPerso = 0)  
        else:
            fen1.blit(combat.fond, (0,0))
        
            if combat.monstre1.vie > 0 : textDegatJoueur = combat.fondtext.render("Rate",1,(0,0,255))
        
    #Si le monstre est mort, le joueur ne peux pas rater son attaque donc affiche un autre texte
    else : textDegatJoueur = combat.fondtext.render("Dans le vent",1,(0,0,0))
        
    fen1.blit(textDegatJoueur,(560,150))


#Affichage des degats sur monstre 2
def degatAttaqueMonstre2(combat,fen1,personnage,item,comp):
    if combat.monstre2.vie > 0 :
        if personnage.toucherPerso > combat.monstre2.esquive :
            if personnage.chanceCrit > personnage.critique :
                combat.monstre2.vie -= personnage.degat
                textDegatJoueur = combat.fondtext.render("-" + str(personnage.degat),1,(0,0,0))
            else :
                combat.monstre2.vie -= personnage.degat*2
                textDegatJoueur = combat.fondtext.render("-" + str(personnage.degat*2),1,(255,0,0))
        
        
        #Si le joueur rate son attaque (personnage.toucherPerso = 0)  
        else:
            fen1.blit(combat.fond, (0,0))
            
            if combat.monstre2.vie > 0 : textDegatJoueur = combat.fondtext.render("Rate",1,(0,0,255))

    #Si le monstre est mort, le joueur ne peux pas rater son attaque donc affiche un autre texte
    else : textDegatJoueur = combat.fondtext.render("Dans le vent",1,(0,0,0))
        
    fen1.blit(textDegatJoueur,(710,210))

#Affichage des degats sur monstre 3
def degatAttaqueMonstre3(combat,fen1,personnage,item,comp):
    if  combat.monstre3.vie > 0 :
        if personnage.toucherPerso > combat.monstre3.esquive :
            if personnage.chanceCrit > personnage.critique :
                combat.monstre3.vie -= personnage.degat
                textDegatJoueur = combat.fondtext.render("-" + str(personnage.degat),1,(0,0,0))
            else :
                combat.monstre3.vie -= personnage.degat*2
                textDegatJoueur = combat.fondtext.render("-" + str(personnage.degat*2),1,(255,0,0))
       
        
        #Si le joueur rate son attaque (personnage.toucherPerso = 0), affiche le texte "Rate"
        else:
            fen1.blit(combat.fond, (0,0))
            if combat.monstre3.vie > 0 : textDegatJoueur = combat.fondtext.render("Rate",1,(0,0,255))

    #Si le monstre est mort, le joueur ne peux pas rater son attaque donc affiche un autre texte
    else : textDegatJoueur = combat.fondtext.render("Dans le vent",1,(0,0,0))
        
    fen1.blit(textDegatJoueur,(595,310))



#Attaque normale sur le monstre 1
def attaqueJoueurMonstre1(combat,fen1,personnage,item,comp,story):
    if combat.cooldown != 0 : combat.cooldown -= 1
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1
    
    personnage.toucherPerso = random.randint(1,100)
    
    fen1.blit(combat.fond, (0,0))

    #Plage de dégats aléatoire entre les dégats min et max du personnage calculés directement grâce à la stat principale
    personnage.dgtMin = int(1/2 * personnage.principale)
    personnage.dgtMax = int(5/4 * personnage.principale)
    personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)#Degat du joueur
    personnage.chanceCrit = random.randint(1,100)#Chance de critique

    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre1(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre1(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)

            

         
    pygame.display.flip()

    

#Attaque normale sur le monstre 2   
def attaqueJoueurMonstre2(combat,fen1,personnage,item,comp,story):
    if combat.cooldown != 0 : combat.cooldown -= 1
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1
    
    personnage.toucherPerso = random.randint(1,100)

    fen1.blit(combat.fond, (0,0))

    #Plage de dégats aléatoire entre les dégats min et max du personnage
    personnage.dgtMin = int(1/2 * personnage.principale)
    personnage.dgtMax = int(5/4 * personnage.principale)
    personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)
    personnage.chanceCrit = random.randint(1,100)

    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre2(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre2(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)

         
    pygame.display.flip()


    

#Attaque du personnage sur le monstre 3, affiche les dégats au dessus du monstre tapé avec une chance de rater, si le monstre meurt il ne tape pas le joueur       
def attaqueJoueurMonstre3(combat,fen1,personnage,item,comp,story):
    if combat.cooldown != 0 : combat.cooldown -= 1
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1
    
    personnage.toucherPerso = random.randint(1,100)

    fen1.blit(combat.fond, (0,0))

    #Plage de dégats aléatoire entre les dégats min et max du personnage
    personnage.dgtMin = int(1/2 * personnage.principale)
    personnage.dgtMax = int(5/4 * personnage.principale)
    personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)
    personnage.chanceCrit = random.randint(1,100)

    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre3(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre3(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)

         
    pygame.display.flip()



#Attaque spéciale 2 de l'assassin, assome le monstre 1 pour le tour (le monstre ne tape pas)
def competenceSpecialeAssassin2M1(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 4
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1
    
    personnage.toucherPerso = random.randint(1,100)
    if personnage.toucherPerso > combat.monstre1.esquive : combat.stunMonstre1 = 1


    #Plage de dégats aléatoire entre les dégats min et max du personnage calculés directement grâce à la stat principale
    personnage.dgtMin = int(1/4 * personnage.principale)
    personnage.dgtMax = int(personnage.principale)
    personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)#Degat du joueur
    personnage.chanceCrit = 100
    
    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre1(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre1(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)

    combat.stunMonstre1 = 0
    
    pygame.display.flip()


#Attaque spéciale 2 de l'assassin, assome le monstre 2 pour le tour (le monstre ne tape pas)     
def competenceSpecialeAssassin2M2(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 4
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1
    
    personnage.toucherPerso = random.randint(1,100)
    if personnage.toucherPerso > combat.monstre2.esquive : combat.stunMonstre2 = 1


    #Plage de dégats aléatoire entre les dégats min et max du personnage
    personnage.dgtMin = int(1/4 * personnage.principale)
    personnage.dgtMax = int(personnage.principale)
    personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)
    personnage.chanceCrit = 100
    
    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre2(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre2(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)

    combat.stunMonstre2 = 0
    
    pygame.display.flip()


#Attaque spéciale 2 de l'assassin, assome le monstre 3 pour le tour (le monstre ne tape pas)     
def competenceSpecialeAssassin2M3(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 4
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1

    personnage.toucherPerso = random.randint(1,100)
    if personnage.toucherPerso > combat.monstre3.esquive : combat.stunMonstre3 = 1
    

    #Plage de dégats aléatoire entre les dégats min et max du personnage
    personnage.dgtMin = int(1/4 * personnage.principale)
    personnage.dgtMax = int(personnage.principale)
    personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)
    personnage.chanceCrit = 100

    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre3(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre3(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)

    combat.stunMonstre3 = 0

    pygame.display.flip()


#Gère les dégats de l'attaque speciale 1 du paladin
def degatsAttaqueSpeciale_1_Paladin(combat,fen1,personnage,item,comp):
    personnage.toucherPerso = 100

    #Plage de dégats aléatoire entre les dégats min et max du personnage calculés directement grâce à la stat principale
    personnage.dgtMin = int(personnage.principale)
    personnage.dgtMax = int(2 * personnage.principale)
    personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax) #Degat du joueur
    personnage.chanceCrit = random.randint(0,100)
    


#Attaque spéciale 1 du paladin sur le monstre 1
def competenceSpecialePaladin1M1(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 2
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1

    degatsAttaqueSpeciale_1_Paladin(combat,fen1,personnage,item,comp)
    
    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre1(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre1(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)
    
    pygame.display.flip()


#Attaque spéciale 1 du paladin sur le monstre 2
def competenceSpecialePaladin1M2(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 2
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1
    
    degatsAttaqueSpeciale_1_Paladin(combat,fen1,personnage,item,comp)
    
    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre2(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre2(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)
    
    pygame.display.flip()


#Attaque spéciale 1 du paladin sur le monstre 3
def competenceSpecialePaladin1M3(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 2
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1
    
    degatsAttaqueSpeciale_1_Paladin(combat,fen1,personnage,item,comp)
    
    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre3(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre3(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)
    
    pygame.display.flip()




#Competence 2 du paladin, soin
def competenceSpecialePaladin2(combat,fen1,personnage,item,comp,story):
    combat.cooldown = 4
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1

    soinMin = int(personnage.principale)
    soinMax = int(2 * personnage.principale)
    soin = random.randint(soinMin,soinMax)

    if personnage.vie + soin > personnage.viemax :
        soin = personnage.viemax - personnage.vie
        personnage.vie += soin
        
    elif personnage.vie == personnage.viemax : soin = 0
    
    else : personnage.vie += soin

    textSoinJoueur = combat.fondtext.render("+" + str(soin),1,(0,255,0))
    fen1.blit(textSoinJoueur,(260,310))
    pygame.display.flip()


    if comp.ami != 0 and comp.vie > 0 :
        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)
        
        pygame.display.flip()


#Gère les dégats de l'attaque spéciale 1 du mage, le vol de vie
def degatsAttaqueSpecial_1_Mage(combat,fen1,personnage,item,comp):
    #Plage de dégats aléatoire entre les dégats min et max du personnage
    personnage.dgtMin = int(1/4 * personnage.principale)
    personnage.dgtMax = int(personnage.principale)
    personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)
    personnage.chanceCrit = 100

    personnage.toucherPerso = 100

#Gère le soin du vol de vie du mage
def soinAttaqueSpecial_1_Mage(combat,fen1,personnage,item,comp):
    #Plage de soin entre la moitié des degats infligés et 100% de ces dégats
    soinMin = int(1/2 * personnage.degat)
    soinMax = int(personnage.degat)
    
    soin = random.randint(soinMin,soinMax)

    if personnage.vie + soin > personnage.viemax :
        soin = personnage.viemax - personnage.vie
        personnage.vie += soin
        
    elif personnage.vie == personnage.viemax : soin = 0
    
    else : personnage.vie += soin


    textSoinJoueur = combat.fondtext.render("+" + str(soin),1,(0,255,0))
    if comp.ami == 0 : fen1.blit(textSoinJoueur,(265,285))
    else : fen1.blit(textSoinJoueur,(265,325))




#Vole de vie du mage sur le monstre 1, il tape un monstre et récupère de la vie
def competenceSpecialeMage1M1(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 2
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1

    degatsAttaqueSpecial_1_Mage(combat,fen1,personnage,item,comp)
    soinAttaqueSpecial_1_Mage(combat,fen1,personnage,item,comp)
    
    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre1(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre1(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)
        
    pygame.display.flip()



#Vole de vie du mage sur le monstre 2, il tape un monstre et récupère de la vie
def competenceSpecialeMage1M2(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 2
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1

    degatsAttaqueSpecial_1_Mage(combat,fen1,personnage,item,comp)
    soinAttaqueSpecial_1_Mage(combat,fen1,personnage,item,comp)
    
    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre2(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre2(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)
        
    pygame.display.flip()



#Vole de vie du mage sur le monstre 3, il tape un monstre et récupère de la vie
def competenceSpecialeMage1M3(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 2
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1

    degatsAttaqueSpecial_1_Mage(combat,fen1,personnage,item,comp)
    soinAttaqueSpecial_1_Mage(combat,fen1,personnage,item,comp)

    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre3(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre3(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)
        
    pygame.display.flip()




#Météore du mage, tape tout les monstres
def competenceSpecialeMage2(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 4
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1

    #Aucune chance de critique mais 100% de chance de toucher
    personnage.chanceCrit = 100
    personnage.toucherPerso = 100
    
    #Plage de dégats aléatoire entre les dégats min et max du personnage, plus fort contre 1 monstre, plus faible contre 3
    if combat.nombreMonstre == 1 :
        personnage.dgtMin = int(1/4 * personnage.principale)
        personnage.dgtMax = int(5/4 * personnage.principale)
        personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)
        degatAttaqueMonstre1(combat,fen1,personnage,item,comp)

    if combat.nombreMonstre == 2 :
        for i in range(0,2):
            if i == 0 :
                personnage.dgtMin = int(1/4 * personnage.principale)
                personnage.dgtMax = int(personnage.principale)
                personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)
                degatAttaqueMonstre1(combat,fen1,personnage,item,comp)
            if i == 1 :
                personnage.dgtMin = int(1/4 * personnage.principale)
                personnage.dgtMax = int(personnage.principale)
                personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)
                degatAttaqueMonstre2(combat,fen1,personnage,item,comp)
                
    if combat.nombreMonstre == 3 :
        for i in range(0,3):
            if i == 0 :
                personnage.dgtMin = int(1/4 * personnage.principale)
                personnage.dgtMax = int(3/4 * personnage.principale)
                personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)
                degatAttaqueMonstre1(combat,fen1,personnage,item,comp)
            if i == 1 :
                personnage.dgtMin = int(1/4 * personnage.principale)
                personnage.dgtMax = int(3/4 * personnage.principale)
                personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)
                degatAttaqueMonstre2(combat,fen1,personnage,item,comp)
            if i == 2 :
                personnage.dgtMin = int(1/4 * personnage.principale)
                personnage.dgtMax = int(3/4 * personnage.principale)
                personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax)
                degatAttaqueMonstre3(combat,fen1,personnage,item,comp)



    if comp.ami == 0 or comp.vie <= 0:
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)
    
    if comp.ami != 0 and comp.vie > 0 :
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)
        
    pygame.display.flip()




#Gère les dégats de l'attaque speciale 1 du paladin
def degatsAttaqueSpeciale_1_voleur(combat,fen1,personnage,item,comp):
    personnage.toucherPerso = 100

    #Plage de dégats aléatoire entre les dégats min et max du personnage calculés directement grâce à la stat principale
    personnage.dgtMin = int(1/2 * personnage.principale)
    personnage.dgtMax = int(personnage.principale)
    personnage.degat = random.randint(personnage.dgtMin,personnage.dgtMax) #Degat du joueur
    personnage.chanceCrit = 100
    


#Attaque spéciale 1 du voleur sur le monstre 1
def competenceSpecialeAssassin1M1(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 2
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1

    degatsAttaqueSpeciale_1_voleur(combat,fen1,personnage,item,comp)

    if combat.monstre1.vie <= int(combat.monstre1.viemax * 0.35) : personnage.degat = combat.monstre1.vie
    
    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre1(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    if comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre1(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)
    
    pygame.display.flip()


#Attaque spéciale 1 du voleur sur le monstre 2
def competenceSpecialeAssassin1M2(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 2
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1
    
    degatsAttaqueSpeciale_1_voleur(combat,fen1,personnage,item,comp)

    if combat.monstre2.vie <= int(combat.monstre1.viemax * 0.35) : personnage.degat = combat.monstre2.vie
    
    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre2(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre2(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)
    
    pygame.display.flip()


#Attaque spéciale 1 du voleur sur le monstre 3
def competenceSpecialeAssassin1M3(combat,fen1,personnage,item,comp,story):
    fen1.blit(combat.fond, (0,0))
    combat.cooldown = 2
    if combat.cooldownPotion != 0 : combat.cooldownPotion -= 1
    
    degatsAttaqueSpeciale_1_voleur(combat,fen1,personnage,item,comp)

    if combat.monstre3.vie <= int(combat.monstre1.viemax * 0.35) : personnage.degat = combat.monstre3.vie
    
    if comp.ami == 0 or comp.vie <= 0:
        degatAttaqueMonstre3(combat,fen1,personnage,item,comp)
        combat.verification3(fen1,personnage,item,comp,story)
        pygame.display.flip()
        
        time.sleep(0.8)
        fen1.blit(combat.fond, (0,0))
        combat.verification(fen1,personnage,item,comp,story)


    elif comp.ami != 0 and comp.vie > 0 :
        degatAttaqueMonstre3(combat,fen1,personnage,item,comp)
        combat.verification2(fen1,personnage,item,comp,story)
        pygame.display.flip()

        if combat.monstreVivant1 != 0 or combat.monstreVivant2 != 0  or combat.monstreVivant3 != 0 :
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            attaqueCompagnon(combat,fen1,personnage,item,comp)
            combat.verification3(fen1,personnage,item,comp,story)
            pygame.display.flip()
            
            time.sleep(0.8)
            fen1.blit(combat.fond, (0,0))
            combat.verification(fen1,personnage,item,comp,story)


    
    pygame.display.flip()



def attaqueCompagnon(combat,fen1,personnage,item,comp):
    degatsComp = random.randint(comp.degatMin,comp.degatMax)



    if comp.IDCompagnon in comp.listHeal:
        heal = random.randint(1,2)
    
    
    if (comp.IDCompagnon not in comp.listHeal) or heal == 1 or (personnage.vie == personnage.viemax and comp.vie == comp.viemax):
        if combat.nombreMonstre == 1 :
            toucherCompagnon = random.randint(0,100)
            
            if toucherCompagnon > combat.monstre1.esquive :
                chanceCrit = random.randint(0,100)
                
                if chanceCrit > comp.critique :
                    combat.monstre1.vie -= degatsComp
                    textDegatCompagnon = combat.fondtext.render("-" + str(degatsComp),1,(0,100,255))
                else :
                    combat.monstre1.vie -= degatsComp * 2
                    textDegatCompagnon = combat.fondtext.render("-" + str(degatsComp*2),1,(255,150,0))
            
            else:
                textDegatCompagnon = combat.fondtext.render("Rate",1,(0,150,255))
            
            fen1.blit(textDegatCompagnon,(550,130))


        if combat.nombreMonstre == 2 :
            if combat.monstreVivant1 == 1 and combat.monstreVivant2 == 1 :
                choix = random.randint(1,2)
            elif combat.monstreVivant1 == 1 and combat.monstreVivant2 == 0 :
                choix = 1
            elif combat.monstreVivant1 == 0 and combat.monstreVivant2 == 1 :
                choix = 2
                
            toucherCompagnon = random.randint(0,100)

            if choix == 1 :
                if toucherCompagnon > combat.monstre1.esquive :
                    chanceCrit = random.randint(0,100)
                    
                    if chanceCrit > comp.critique :
                        combat.monstre1.vie -= degatsComp
                        textDegatCompagnon = combat.fondtext.render("-" + str(degatsComp),1,(0,100,255))
                    else :
                        combat.monstre1.vie -= degatsComp * 2
                        textDegatCompagnon = combat.fondtext.render("-" + str(degatsComp*2),1,(255,150,0))
                
                else:
                    textDegatCompagnon = combat.fondtext.render("Rate",1,(0,150,255))
                
                fen1.blit(textDegatCompagnon,(550,130))


            if choix == 2 :
                if toucherCompagnon > combat.monstre2.esquive :
                    chanceCrit = random.randint(0,100)
                    
                    if chanceCrit > comp.critique :
                        combat.monstre2.vie -= degatsComp
                        textDegatCompagnon = combat.fondtext.render("-" + str(degatsComp),1,(0,100,255))
                    else :
                        combat.monstre2.vie -= degatsComp * 2
                        textDegatCompagnon = combat.fondtext.render("-" + str(degatsComp*2),1,(255,150,0))
                
                else:
                    textDegatCompagnon = combat.fondtext.render("Rate",1,(0,150,255))
                
                fen1.blit(textDegatCompagnon,(700,190))



        if combat.nombreMonstre == 3 :
            if combat.monstreVivant1 == 1 and combat.monstreVivant2 == 1 and combat.monstreVivant3 == 1 :
                choix = random.randint(1,3)
            elif combat.monstreVivant1 == 1 and combat.monstreVivant2 == 1 and combat.monstreVivant3 == 0:
                choix = random.randint(1,2)
            elif combat.monstreVivant1 == 1 and combat.monstreVivant2 == 0 and combat.monstreVivant3 == 1:
                monstre = [1,3]
                choix = random.choice(monstre)
            elif combat.monstreVivant1 == 0 and combat.monstreVivant2 == 1 and combat.monstreVivant3 == 1:
                choix = random.randint(2,3)
            elif combat.monstreVivant1 == 1 and combat.monstreVivant2 == 0 and combat.monstreVivant3 == 0:
                choix = 1
            elif combat.monstreVivant1 == 0 and combat.monstreVivant2 == 1 and combat.monstreVivant3 == 0:
                choix = 2
            elif combat.monstreVivant1 == 0 and combat.monstreVivant2 == 0 and combat.monstreVivant3 == 1:
                choix = 3
            
            toucherCompagnon = random.randint(0,100)

            if choix == 1 :
                if toucherCompagnon > combat.monstre1.esquive :
                    chanceCrit = random.randint(0,100)
                    
                    if chanceCrit > comp.critique :
                        combat.monstre1.vie -= degatsComp
                        textDegatCompagnon = combat.fondtext.render("-" + str(degatsComp),1,(0,100,255))
                    else :
                        combat.monstre1.vie -= degatsComp * 2
                        textDegatCompagnon = combat.fondtext.render("-" + str(degatsComp*2),1,(255,150,0))
                
                else:
                    textDegatCompagnon = combat.fondtext.render("Rate",1,(0,150,255))
                
                fen1.blit(textDegatCompagnon,(550,130))


            if choix == 2:
                if toucherCompagnon > combat.monstre2.esquive :
                    chanceCrit = random.randint(0,100)
                    
                    if chanceCrit > comp.critique :
                        combat.monstre2.vie -= degatsComp
                        textDegatCompagnon = combat.fondtext.render("-" + str(degatsComp),1,(0,100,255))
                    else :
                        combat.monstre2.vie -= degatsComp * 2
                        textDegatCompagnon = combat.fondtext.render("-" + str(degatsComp*2),1,(255,150,0))
                
                else:
                    textDegatCompagnon = combat.fondtext.render("Rate",1,(0,150,255))
                
                fen1.blit(textDegatCompagnon,(700,190))

            if choix == 3:
                if toucherCompagnon > combat.monstre3.esquive :
                    chanceCrit = random.randint(0,100)
                    
                    if chanceCrit > comp.critique :
                        combat.monstre3.vie -= degatsComp
                        textDegatCompagnon = combat.fondtext.render("-" + str(degatsComp),1,(0,100,255))
                    else :
                        combat.monstre3.vie -= degatsComp * 2
                        textDegatCompagnon = combat.fondtext.render("-" + str(degatsComp*2),1,(255,150,0))
                
                else:
                    textDegatCompagnon = combat.fondtext.render("Rate",1,(0,150,255))
                
                fen1.blit(textDegatCompagnon,(585,330))
    else :
        soinCompagnon = random.randint(comp.healMin,comp.healMax)
        if personnage.vie != personnage.viemax and comp.vie == comp.viemax : choixHeal = 1
        elif personnage.vie == personnage.viemax and comp.vie != comp.viemax : choixHeal = 2
        elif personnage.vie != personnage.viemax and comp.vie != comp.viemax : choixHeal = random.randint(1,2)

        if choixHeal == 1 :
            if personnage.vie + soinCompagnon > personnage.viemax :
                soinCompagnon = personnage.viemax - personnage.vie
                personnage.vie += soinCompagnon
                
            else : personnage.vie += soinCompagnon
            
            textHealCompagnon = combat.fondtext.render("+" + str(soinCompagnon),1,(0,255,0))
            fen1.blit(textHealCompagnon,(285,325))

        elif choixHeal == 2 :
            if comp.vie + soinCompagnon > comp.viemax :
                soinCompagnon = comp.viemax - comp.vie
                comp.vie += soinCompagnon
                
            else : comp.vie += soinCompagnon
            
            textHealCompagnon = combat.fondtext.render("+" + str(soinCompagnon),1,(0,255,0))
            fen1.blit(textHealCompagnon,(260,165))



