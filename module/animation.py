import pygame,time
from module.combat import *



################################################################################################
#Animation attaques de base


def anim1(combat,fen1,personnage,item,comp,story):
    if personnage.classe == 'voleur' :
        for i in range(1,23):
            attaque = pygame.image.load("img/Attaque/Voleur/AttaqueAssassin"+str(i)+".png").convert_alpha()
            
            time.sleep(0.01)
            combat.majAnimation(fen1,personnage,item,comp,story)
            fen1.blit(attaque,(600,170))
            
            pygame.display.flip()
            

    if personnage.classe == "paladin" :
            for i in range(9,12):
                attaque = pygame.image.load("img/Attaque/Paladin/marteau"+str(i)+".png").convert_alpha()
                
                time.sleep(0.06)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(attaque,(520,170))
                
                pygame.display.flip()


            for k in range(1,10):
                heurt = pygame.image.load("img/Attaque/Paladin/marteauAttaque"+str(k)+".png").convert_alpha()
                
                time.sleep(0.06)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(heurt,(520,170))
                
                pygame.display.flip()
                
            
    if personnage.classe == 'mage' :
        if comp.ami == 0 :
            fichier = []
            pos = 0


            for i in range(1,7):
                creation = pygame.image.load("img/Attaque/Heretique/creationBDF"+str(i)+".png").convert_alpha()
                time.sleep(0.06)
                fen1.blit(creation,(260,270))
                pygame.display.flip()

            for j in range(1,7):  
                fichier.append(pygame.image.load("img/Attaque/Heretique/bouleDeFeu"+str(j)+".png").convert_alpha())

            attaque = fichier[pos]
            position_attaque = attaque.get_rect()
            position_attaque = position_attaque.move(260,270)

            deplacement = 0

            while deplacement < 355 :
                pos += 1
                if pos not in range(0,6): pos = 0

                attaque = fichier[pos]
                

                position_attaque = position_attaque.move(6,-1.9)
                time.sleep(0.03)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(attaque,position_attaque)
                
                deplacement += 7

                

                pygame.display.flip()

            for k in range(1,12):
                explosion = pygame.image.load("img/Attaque/Heretique/explosionBDF"+str(k)+".png").convert_alpha()
                
                time.sleep(0.035)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(explosion,(570,220))
                
                pygame.display.flip()

        elif comp.ami == 1 :
            fichier = []
            pos = 0


            for i in range(1,7):
                creation = pygame.image.load("img/Attaque/Heretique/creationBDF"+str(i)+".png").convert_alpha()
                time.sleep(0.06)
                fen1.blit(creation,(260,350))
                pygame.display.flip()

            for j in range(1,7):  
                fichier.append(pygame.image.load("img/Attaque/Heretique/bouleDeFeu"+str(j)+".png").convert_alpha())

            attaque = fichier[pos]
            position_attaque = attaque.get_rect()
            position_attaque = position_attaque.move(260,350)

            deplacement = 0

            while deplacement < 355 :
                pos += 1
                if pos not in range(0,6): pos = 0

                attaque = fichier[pos]
                

                position_attaque = position_attaque.move(6,-3.5)
                time.sleep(0.03)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(attaque,position_attaque)
                
                deplacement += 7

                

                pygame.display.flip()

            for k in range(1,12):
                explosion = pygame.image.load("img/Attaque/Heretique/explosionBDF"+str(k)+".png").convert_alpha()
                
                time.sleep(0.035)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(explosion,(570,195))
                
                pygame.display.flip()
        


    

def anim2(combat,fen1,personnage,item,comp,story):
    if personnage.classe == 'voleur' :
        for i in range(1,23):
            attaque = pygame.image.load("img/Attaque/Voleur/AttaqueAssassin"+str(i)+".png").convert_alpha()
            
            time.sleep(0.01)
            combat.majAnimation(fen1,personnage,item,comp,story)
            fen1.blit(attaque,(745,250))
            
            pygame.display.flip()
            

    if personnage.classe == "paladin" :
            for i in range(9,12):
                attaque = pygame.image.load("img/Attaque/Paladin/marteau"+str(i)+".png").convert_alpha()
                
                time.sleep(0.06)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(attaque,(520,170))
                
                pygame.display.flip()


            for k in range(1,10):
                heurt = pygame.image.load("img/Attaque/Paladin/marteauAttaque"+str(k)+".png").convert_alpha()
                
                time.sleep(0.06)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(heurt,(520,170))
                
                pygame.display.flip()
                
            
    if personnage.classe == 'mage' :
        if comp.ami == 0 :
            fichier = []
            pos = 0
            

            for i in range(1,7):
                creation = pygame.image.load("img/Attaque/Heretique/creationBDF"+str(i)+".png").convert_alpha()
                time.sleep(0.06)
                fen1.blit(creation,(260,270))
                pygame.display.flip()

            for j in range(1,7):  
                fichier.append(pygame.image.load("img/Attaque/Heretique/bouleDeFeu"+str(j)+".png").convert_alpha())

            attaque = fichier[pos]
            position_attaque = attaque.get_rect()
            position_attaque = position_attaque.move(260,270)

            deplacement = 0

            while deplacement < 290 :
                pos += 1
                if pos not in range(0,6): pos = 0

                attaque = fichier[pos]

                position_attaque = position_attaque.move(6,0)
                time.sleep(0.02)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(attaque,position_attaque)
                
                deplacement += 4


                pygame.display.flip()

            for k in range(1,12):
                explosion = pygame.image.load("img/Attaque/Heretique/explosionBDF"+str(k)+".png").convert_alpha()
                
                time.sleep(0.035)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(explosion,(715,270))
                
                pygame.display.flip()
                

        elif comp.ami == 1 :
            fichier = []
            pos = 0


            for i in range(1,7):
                creation = pygame.image.load("img/Attaque/Heretique/creationBDF"+str(i)+".png").convert_alpha()
                time.sleep(0.06)
                fen1.blit(creation,(260,350))
                pygame.display.flip()

            for j in range(1,7):  
                fichier.append(pygame.image.load("img/Attaque/Heretique/bouleDeFeu"+str(j)+".png").convert_alpha())

            attaque = fichier[pos]
            position_attaque = attaque.get_rect()
            position_attaque = position_attaque.move(260,350)

            deplacement = 0

            while deplacement < 380 :
                pos += 1
                if pos not in range(0,6): pos = 0

                attaque = fichier[pos]
                

                position_attaque = position_attaque.move(8,-1.5)
                time.sleep(0.03)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(attaque,position_attaque)
                
                deplacement += 7

                

                pygame.display.flip()

            for k in range(1,12):
                explosion = pygame.image.load("img/Attaque/Heretique/explosionBDF"+str(k)+".png").convert_alpha()
                
                time.sleep(0.035)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(explosion,(710,295))
                
                pygame.display.flip()

            

def anim3(combat,fen1,personnage,item,comp,story):
    if personnage.classe == 'voleur' :
        for i in range(1,23):
            attaque = pygame.image.load("img/Attaque/Voleur/AttaqueAssassin"+str(i)+".png").convert_alpha()
            
            time.sleep(0.01)
            combat.majAnimation(fen1,personnage,item,comp,story)
            fen1.blit(attaque,(635,350))
            
            pygame.display.flip()

    if personnage.classe == "paladin" :
            for i in range(9,12):
                attaque = pygame.image.load("img/Attaque/Paladin/marteau"+str(i)+".png").convert_alpha()
                
                time.sleep(0.06)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(attaque,(520,170))
                
                pygame.display.flip()


            for k in range(1,10):
                heurt = pygame.image.load("img/Attaque/Paladin/marteauAttaque"+str(k)+".png").convert_alpha()
                
                time.sleep(0.06)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(heurt,(520,170))
                
                pygame.display.flip()

                
            
    if personnage.classe == 'mage' :
        if comp.ami == 0 :
            fichier = []
            pos = 0
            

            for i in range(1,7):
                creation = pygame.image.load("img/Attaque/Heretique/creationBDF"+str(i)+".png").convert_alpha()
                time.sleep(0.06)
                fen1.blit(creation,(260,270))
                pygame.display.flip()

            for j in range(1,7):  
                fichier.append(pygame.image.load("img/Attaque/Heretique/bouleDeFeu"+str(j)+".png").convert_alpha())

            attaque = fichier[pos]
            position_attaque = attaque.get_rect()
            position_attaque = position_attaque.move(260,270)

            deplacement = 0

            while deplacement < 260 :
                pos += 1
                if pos not in range(0,6): pos = 0

                attaque = fichier[pos]


                position_attaque = position_attaque.move(7,2)
                time.sleep(0.03)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(attaque,position_attaque)
                
                deplacement += 5


                pygame.display.flip()


            for k in range(1,12):
                explosion = pygame.image.load("img/Attaque/Heretique/explosionBDF"+str(k)+".png").convert_alpha()
                
                time.sleep(0.035)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(explosion,(630,375))
                
                pygame.display.flip()

        elif comp.ami == 1 :
            fichier = []
            pos = 0


            for i in range(1,7):
                creation = pygame.image.load("img/Attaque/Heretique/creationBDF"+str(i)+".png").convert_alpha()
                time.sleep(0.06)
                fen1.blit(creation,(260,350))
                pygame.display.flip()

            for j in range(1,7):  
                fichier.append(pygame.image.load("img/Attaque/Heretique/bouleDeFeu"+str(j)+".png").convert_alpha())

            attaque = fichier[pos]
            position_attaque = attaque.get_rect()
            position_attaque = position_attaque.move(260,350)

            deplacement = 0

            while deplacement < 380 :
                pos += 1
                if pos not in range(0,6): pos = 0

                attaque = fichier[pos]
                

                position_attaque = position_attaque.move(6,0)
                time.sleep(0.03)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(attaque,position_attaque)
                
                deplacement += 7

                

                pygame.display.flip()

            for k in range(1,12):
                explosion = pygame.image.load("img/Attaque/Heretique/explosionBDF"+str(k)+".png").convert_alpha()
                
                time.sleep(0.035)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(explosion,(600,350))
                
                pygame.display.flip()


################################################################################################
#Animation attaques spéciales 1



def AS1_anim1(combat,fen1,personnage,item,comp,story):
    if comp.ami == 0 :     
        if personnage.classe == 'mage' :
                fichier = []
                pos = 0

                for j in range(1,11):
                    accumulation = pygame.image.load("img/Attaque/Heretique/accumulationDrain"+str(j)+".png").convert_alpha()
                    
                    time.sleep(0.04)
                    combat.majAnimation(fen1,personnage,item,comp,story)
                    fen1.blit(accumulation,(530,190))
                    
                    pygame.display.flip()

                
                for i in range(1,11):  
                    fichier.append(pygame.image.load("img/Attaque/Heretique/drainVie"+str(i)+".png").convert_alpha())

                attaque = fichier[pos]
                position_attaque = attaque.get_rect()
                position_attaque = position_attaque.move(520,190)

                deplacement = 0

            
                while deplacement < 395 :
                    pos += 1
                    if pos not in range(0,10): pos = 2

                    attaque = fichier[pos]
                    

                    position_attaque = position_attaque.move(-12,4)
                    time.sleep(0.06)
                    combat.majAnimation(fen1,personnage,item,comp,story)
                    fen1.blit(attaque,position_attaque)
                    
                    deplacement += 20

                    

                    pygame.display.flip()

                for k in range(1,10):
                    drainBaton = pygame.image.load("img/Attaque/Heretique/drainBaton"+str(k)+".png").convert_alpha()
                    time.sleep(0.04)
                    combat.majAnimation(fen1,personnage,item,comp,story)
                    fen1.blit(drainBaton,(260,270))
                    
                    pygame.display.flip()

        


            


def AS1_anim2(combat,fen1,personnage,item,comp,story):
    if comp.ami == 0 :      
        if personnage.classe == 'mage' :
            
                fichier = []
                pos = 0

                for j in range(1,11):
                    accumulation = pygame.image.load("img/Attaque/Heretique/accumulationDrain"+str(j)+".png").convert_alpha()
                    
                    time.sleep(0.04)
                    combat.majAnimation(fen1,personnage,item,comp,story)
                    fen1.blit(accumulation,(680,270))
                    
                    pygame.display.flip()

                
                for i in range(1,11):  
                    fichier.append(pygame.image.load("img/Attaque/Heretique/drainVie"+str(i)+".png").convert_alpha())

                attaque = fichier[pos]
                position_attaque = attaque.get_rect()
                position_attaque = position_attaque.move(670,270)

                deplacement = 0

            
                while deplacement < 395 :
                    pos += 1
                    if pos not in range(0,10): pos = 2

                    attaque = fichier[pos]
                    

                    position_attaque = position_attaque.move(-19,0)
                    time.sleep(0.06)
                    combat.majAnimation(fen1,personnage,item,comp,story)
                    fen1.blit(attaque,position_attaque)
                    
                    deplacement += 20

                    

                    pygame.display.flip()

                for k in range(1,10):
                    drainBaton = pygame.image.load("img/Attaque/Heretique/drainBaton"+str(k)+".png").convert_alpha()
                    time.sleep(0.04)
                    combat.majAnimation(fen1,personnage,item,comp,story)
                    fen1.blit(drainBaton,(260,270))
                    
                    pygame.display.flip()


def AS1_anim3(combat,fen1,personnage,item,comp,story):
    if comp.ami == 0 :      
        if personnage.classe == 'mage' :
            
                fichier = []
                pos = 0

                for j in range(1,11):
                    accumulation = pygame.image.load("img/Attaque/Heretique/accumulationDrain"+str(j)+".png").convert_alpha()
                    
                    time.sleep(0.04)
                    combat.majAnimation(fen1,personnage,item,comp,story)
                    fen1.blit(accumulation,(580,360))
                    
                    pygame.display.flip()

                
                for i in range(1,11):  
                    fichier.append(pygame.image.load("img/Attaque/Heretique/drainVie"+str(i)+".png").convert_alpha())

                attaque = fichier[pos]
                position_attaque = attaque.get_rect()
                position_attaque = position_attaque.move(570,360)

                deplacement = 0

            
                while deplacement < 395 :
                    pos += 1
                    if pos not in range(0,10): pos = 2

                    attaque = fichier[pos]
                    

                    position_attaque = position_attaque.move(-15,-4)
                    time.sleep(0.06)
                    combat.majAnimation(fen1,personnage,item,comp,story)
                    fen1.blit(attaque,position_attaque)
                    
                    deplacement += 20

                    

                    pygame.display.flip()

                for k in range(1,10):
                    drainBaton = pygame.image.load("img/Attaque/Heretique/drainBaton"+str(k)+".png").convert_alpha()
                    time.sleep(0.04)
                    combat.majAnimation(fen1,personnage,item,comp,story)
                    fen1.blit(drainBaton,(260,275))
                    
                    pygame.display.flip()

            

            
################################################################################################
#Animation attaques spéciales 2

def AS2_anim1(combat,fen1,personnage,item,comp,story):
    if personnage.classe == "mage":
        fichier = []
        pos = 0

        for i in range(1,5):  
            fichier.append(pygame.image.load("img/Attaque/Heretique/meteore"+str(i)+".png").convert_alpha())

        attaque = fichier[pos]
        position_attaque = attaque.get_rect()
        position_attaque = position_attaque.move(450,-250)

        deplacement = 0

        while deplacement < 395 :
            pos += 1
            if pos not in range(0,4): pos = 1

            attaque = fichier[pos]
            

            position_attaque = position_attaque.move(1,8)
            time.sleep(0.06)
            combat.majAnimation(fen1,personnage,item,comp,story)
            fen1.blit(attaque,position_attaque)
            
            deplacement += 10

            

            pygame.display.flip()

        for j in range(1,12):
            explosion = pygame.image.load("img/Attaque/Heretique/explosionMeteore"+str(j)+".png").convert_alpha()
                    
            time.sleep(0.06)
            combat.majAnimation(fen1,personnage,item,comp,story)
            fen1.blit(explosion,(575,235))
                
            pygame.display.flip()

        
            
    if comp.ami == 0:
        if personnage.classe == "paladin" :
            for i in range(1,21):
                soin = pygame.image.load("img/Attaque/Paladin/Soin"+str(i)+".png").convert_alpha()
                
                time.sleep(0.065)
                combat.majAnimation(fen1,personnage,item,comp,story)
                fen1.blit(soin,(190,300))
                
                pygame.display.flip()

        
    



        
