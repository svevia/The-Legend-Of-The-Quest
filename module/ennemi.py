import random

class ennemi :
    """Objet définissant un ennemi en
    combat, définit toutes ses propriétés selon l'ID rentré.
    """

    def __init__ (self,ID,personnage,story,item) :
        self.ID = ID
        self.stats(personnage,story,item)
        self.listHeal = (1,7,104,107,201,204,206,403,404,407,408,501,502,513,514,515,516,518,521)

        self.monstresDesert = (1,2,3,4,5,6,7)
        self.monstresMarais = (101,102,103,104,105,106,107)
        self.monstresPlaine = (201,202,203,204,205,206)
        self.monstresContaminee = (301,302,303)
        
    def stats (self,personnage,story,item) :
        
###########################################################################
        #Monstres du desert ID = 0XX
        
        #001 - Galakran - Chaman
        if self.ID == 1 :
            self.name = 'Chaman Galakran'
            self.img = 'img/monstre/GalakranChaman.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 12 + self.niveau * 4
            self.vie = self.viemax
            self.dgtMin = 1 + self.niveau 
            self.dgtMax = 4 + self.niveau * 2
            self.esquive = 5 + self.niveau
            self.gainxp = 90  + self.niveau * 30
            self.gold = random.randint(0,100)
            self.healMin = 3 + self.niveau * 2
            self.healMax = 3 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #002 - Galakran - Base
        if self.ID == 2 :
            self.name = 'Guerrier Galakran'
            self.img = 'img/monstre/GalakranBase.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 10 + self.niveau * 3
            self.vie = self.viemax
            self.dgtMin = self.niveau * 2
            self.dgtMax = 1 + self.niveau * 3
            self.esquive = 2 + self.niveau
            self.gainxp = 50  + self.niveau * 30
            self.gold = random.randint(0,50)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #003 - Galakran - Manieur De Hache
        if self.ID == 3 :
            self.name = 'Galakran à la hache'
            self.img = 'img/monstre/ManieurDeHache.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 15 + self.niveau * 4 
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau 
            self.dgtMax = 3 + self.niveau * 3
            self.esquive = 10  + self.niveau
            self.gainxp = 80 +  + self.niveau * 30
            self.gold = random.randint(0,150)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #004 - Galakran - Sauvage
        if self.ID == 4 :
            self.name = 'Galakran sauvage'
            self.img = 'img/monstre/GalakranSauvage.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*5
            self.vie = self.viemax
            self.dgtMin = 1 + self.niveau
            self.dgtMax = 6 + self.niveau * 3
            self.esquive = 6 + self.niveau
            self.gainxp = 100 +  + self.niveau * 30
            self.gold = random.randint(0,20)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #005 - Scorpion
        if self.ID == 5 :
            self.name = 'Scorpion'
            self.img = 'img/monstre/Scorpion.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 8 + self.niveau*4
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau * 2
            self.dgtMax = 5 + self.niveau * 4
            self.esquive = 4 + self.niveau
            self.gainxp = 85 +  + self.niveau * 35
            self.gold = random.randint(0,5)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #006 - Plante - Carnivore
        if self.ID == 6 :
            self.name = 'Plante carnivore'
            self.img = 'img/monstre/PlanteCarnivore.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau 
            self.dgtMax = 8 + self.niveau * 2
            self.esquive = 0 + self.niveau
            self.gainxp = 65 + self.niveau * 30
            self.gold = random.randint(0,50)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #007 - Arbre - Tréant
        if self.ID == 7 :
            self.name = 'Jeune pousse'
            self.img = 'img/monstre/JeunePousse.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau * 2
            self.dgtMax = 5 + self.niveau * 2
            self.esquive = 0 + self.niveau
            self.gainxp = 65 + self.niveau * 30
            self.gold = random.randint(0,50)
            self.healMin = 3 + self.niveau * 2
            self.healMax = 3 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)
        


            
###########################################################################
        #Monstres du marais ID = 1XX

        #101 - Slime
        if self.ID == 101 :
            self.name = 'Slime'
            self.img = 'img/monstre/Slime.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*6
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau * 2
            self.dgtMax = 5 + self.niveau * 2
            self.esquive = 3 + self.niveau
            self.gainxp = 90 + self.niveau * 30
            self.gold = random.randint(0,90)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #102 - Elfe - Archère Elfette
        if self.ID == 102 :
            self.name = 'Archère Elfette'
            self.img = 'img/monstre/ArcherElfette.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*6
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau * 2
            self.dgtMax = 5 + self.niveau * 2
            self.esquive = 3 + self.niveau
            self.gainxp = 90 + self.niveau * 30
            self.gold = random.randint(0,90)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #103 - Elfe - Assassin Elfette
        if self.ID == 103 :
            self.name = 'Assassin Elfette'
            self.img = 'img/monstre/AssassinElfette.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*6
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau * 2
            self.dgtMax = 5 + self.niveau * 2
            self.esquive = 3 + self.niveau
            self.gainxp = 90 + self.niveau * 30
            self.gold = random.randint(0,90)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #104 - Elfe - Mage
        if self.ID == 104 :
            self.name = 'Elfe mage'
            self.img = 'img/monstre/Elfemage.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau
            self.dgtMax = 5 + self.niveau * 4
            self.esquive = 0 + self.niveau
            self.gainxp = 65 + self.niveau * 30
            self.gold = random.randint(0,50)
            self.healMin = 1 + self.niveau * 2
            self.healMax = 4 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #105 - Elfe - Cavaliere Elfette
        if self.ID == 105 :
            self.name = 'Cavalière Elfette'
            self.img = 'img/monstre/CavaliereElfette.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau
            self.dgtMax = 5 + self.niveau * 4
            self.esquive = 0 + self.niveau
            self.gainxp = 65 + self.niveau * 30
            self.gold = random.randint(0,50)
            self.healMin = 1 + self.niveau * 2
            self.healMax = 4 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)
        
        #106 - Elfe - Danselame Elfette
        if self.ID == 106 :
            self.name = 'Danselame Elfette'
            self.img = 'img/monstre/DanselameElfette.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau
            self.dgtMax = 5 + self.niveau * 4
            self.esquive = 0 + self.niveau
            self.gainxp = 65 + self.niveau * 30
            self.gold = random.randint(0,50)
            self.healMin = 1 + self.niveau * 2
            self.healMax = 4 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #107 - Elfe - MoineElfette
        if self.ID == 107 :
            self.name = 'Elfette moine'
            self.img = 'img/monstre/MoineElfette.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau
            self.dgtMax = 5 + self.niveau * 4
            self.esquive = 0 + self.niveau
            self.gainxp = 65 + self.niveau * 30
            self.gold = random.randint(0,50)
            self.healMin = 1 + self.niveau * 2
            self.healMax = 4 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)


###########################################################################
        #Monstres de la plaine ID = 2XX
            

        #201 - Humain - Mage Rouge
        if self.ID == 201 :
            self.name = 'Mage rouge'
            self.img = 'img/monstre/HumainMageRouge.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 2 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau * 2
            self.dgtMax = 5 + self.niveau * 2
            self.esquive = 0 + self.niveau
            self.gainxp = 65 + self.niveau * 30
            self.gold = random.randint(0,50)
            self.healMin = 1 + self.niveau * 3
            self.healMax = 2 + self.niveau * 4
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #202 - Humain - Apprenti
        if self.ID == 202 :
            self.name = 'Apprenti'
            self.img = 'img/monstre/Apprenti.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau * 2
            self.dgtMax = 5 + self.niveau * 2
            self.esquive = 0 + self.niveau
            self.gainxp = 65 + self.niveau * 30
            self.gold = random.randint(0,50)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #203 - Humain - Artilleur Humain
        if self.ID == 203 :
            self.name = 'Artilleur Humain'
            self.img = 'img/monstre/ArtilleurHumain.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau * 2
            self.dgtMax = 5 + self.niveau * 2
            self.esquive = 0 + self.niveau
            self.gainxp = 65 + self.niveau * 30
            self.gold = random.randint(0,50)
            if self.esquive >= 50 : self.esquive = 50    
            self.lootMonstre(personnage,story,item)

        #204 - Humain - Pretre
        if self.ID == 204 :
            self.name = 'Prêtre'
            self.img = 'img/monstre/Pretre.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau * 2
            self.dgtMax = 5 + self.niveau * 2
            self.esquive = 0 + self.niveau
            self.gainxp = 65 + self.niveau * 30
            self.gold = random.randint(0,50)
            self.healMin = 3 + self.niveau * 2
            self.healMax = 3 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #205 - Humain - Fantassin 
        if self.ID == 205 :
            self.name = 'Fantassin'
            self.img = 'img/monstre/Fantassin.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau * 2
            self.dgtMax = 5 + self.niveau * 2
            self.esquive = 0 + self.niveau
            self.gainxp = 65 + self.niveau * 30
            self.gold = random.randint(0,50)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #206 - Humain - Mage 
        if self.ID == 206 :
            self.name = 'Mage'
            self.img = 'img/monstre/Mage.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau * 2
            self.dgtMax = 5 + self.niveau * 2
            self.esquive = 0 + self.niveau
            self.gainxp = 65 + self.niveau * 30
            self.gold = random.randint(0,50)
            self.healMin = 3 + self.niveau * 2
            self.healMax = 3 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)
        

############################################################################
        #Monstres de la zone contaminée ID = 3XX

            
        #301 - Champignon - Griffeur
        if self.ID == 301 :
            self.name = 'Champignon griffeur'
            self.img = 'img/monstre/ChampignonGriffeur.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*6
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau * 2
            self.dgtMax = 2 + self.niveau * 6
            self.esquive = 3 + self.niveau
            self.gainxp = 90 + self.niveau * 30
            self.gold = random.randint(0,90)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)
            

        #302 - Champignon - Chien
        if self.ID == 302 :
            self.name = 'Chien champignon'
            self.img = 'img/monstre/ChampignonChien.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 4 + self.niveau*4
            self.vie = self.viemax
            self.dgtMin = 3 + self.niveau * 2
            self.dgtMax = 6 + self.niveau * 2
            self.esquive = 5 + self.niveau
            self.gainxp = 70 + self.niveau * 30
            self.gold = random.randint(0,80)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)


        #303 - Champignon Galakran contaminé
        if self.ID == 303 :
            self.name = 'Galakran contaminé'
            self.img = 'img/monstre/GalakranContamine.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 5 + self.niveau*5
            self.vie = self.viemax
            self.dgtMin = 2 + self.niveau
            self.dgtMax = 4 + self.niveau * 3
            self.esquive = 4 + self.niveau
            self.gainxp = 80 + self.niveau * 30
            self.gold = random.randint(0,150)
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)


############################################################################
        #Boss ID = 4XX

        #401 - BOSS - Porc contaminé
        if self.ID == 401 :
            self.name = 'Porc contaminé'
            self.img = 'img/monstre/ChampignonBOSSGroin.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 30 + self.niveau*10
            self.vie = self.viemax
            self.dgtMin = 8 + self.niveau * 2
            self.dgtMax = 12 + self.niveau * 3
            self.esquive = 10 + self.niveau
            self.gainxp = 350 + self.niveau * 120
            self.gold = random.randint(0,650)
            self.loot = 10
            if self.esquive >= 50 : self.esquive = 50

        #402 - BOSS - Porte-peste
        if self.ID == 402 :
            self.name = 'Porte-peste'
            self.img = 'img/monstre/ChampignonBOSSPortepeste.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 25 + self.niveau*12
            self.vie = self.viemax
            self.dgtMin = 6 + self.niveau * 3
            self.dgtMax = 15 + self.niveau * 4
            self.esquive = 5 + 2*self.niveau
            self.gainxp = 350 + self.niveau * 120
            self.gold = random.randint(0,650)
            self.loot = 10
            if self.esquive >= 50 : self.esquive = 50

        #403 - BOSS - Chef de la cabale
        if self.ID == 403 :
            self.name = 'Chef de la Cabale'
            self.img = 'img/monstre/GalakranBOSSChefCabale.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 20 + self.niveau*10
            self.vie = self.viemax
            self.dgtMin = 8 + self.niveau 
            self.dgtMax = 10 + self.niveau * 5
            self.esquive = 12 + 2*self.niveau
            self.gainxp = 350 + self.niveau * 120
            self.gold = random.randint(0,650)
            self.loot = 10
            self.healMin = 3 + self.niveau * 2
            self.healMax = 3 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50

        #404 - BOSS - Le destructeur
        if self.ID == 404 :
            self.name = 'Le destructeur'
            self.img = 'img/monstre/LeDestructeur.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 20 + self.niveau*10
            self.vie = self.viemax
            self.dgtMin = 8 + self.niveau 
            self.dgtMax = 10 + self.niveau * 5
            self.esquive = 12 + 2*self.niveau
            self.gainxp = 350 + self.niveau * 120
            self.gold = random.randint(0,650)
            self.loot = 10
            self.healMin = 3 + self.niveau * 2
            self.healMax = 3 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50

        #405 - BOSS - Rabanos le briseur
        if self.ID == 405 :
            self.name = 'Rabanos le briseur'
            self.img = 'img/monstre/RabanosLeBriseur.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 20 + self.niveau*10
            self.vie = self.viemax
            self.dgtMin = 8 + self.niveau 
            self.dgtMax = 10 + self.niveau * 5
            self.esquive = 12 + 2*self.niveau
            self.gainxp = 350 + self.niveau * 120
            self.gold = random.randint(0,650)
            self.loot = 10
            if self.esquive >= 50 : self.esquive = 50

        #406 - BOSS - Roi
        if self.ID == 406 :
            self.name = 'Roi'
            self.img = 'img/monstre/Roi.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 20 + self.niveau*10
            self.vie = self.viemax
            self.dgtMin = 8 + self.niveau 
            self.dgtMax = 10 + self.niveau * 5
            self.esquive = 12 + 2*self.niveau
            self.gainxp = 350 + self.niveau * 120
            self.gold = random.randint(0,650)
            self.loot = 10
            if self.esquive >= 50 : self.esquive = 50 
        
        #407 - BOSS - Shyrion
        if self.ID == 407 :
            self.name = 'Shyrion'
            self.img = 'img/monstre/Shyrion.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 20 + self.niveau*10
            self.vie = self.viemax
            self.dgtMin = 8 + self.niveau 
            self.dgtMax = 10 + self.niveau * 5
            self.esquive = 12 + 2*self.niveau
            self.gainxp = 350 + self.niveau * 120
            self.gold = random.randint(0,650)
            self.loot = 10
            self.healMin = 3 + self.niveau * 2
            self.healMax = 3 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50 


        #408 - BOSS - LeProfanateur
        if self.ID == 408 :
            self.name = 'Le Profanateur'
            self.img = 'img/monstre/LeProfanateur.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 30 + self.niveau*10
            self.vie = self.viemax
            self.dgtMin = 8 + self.niveau 
            self.dgtMax = 10 + self.niveau * 5
            self.esquive = 12 + 2*self.niveau
            self.gainxp = 550 + self.niveau * 120
            self.gold = random.randint(0,650)
            self.loot = 10
            self.healMin = 5 + self.niveau * 2
            self.healMax = 5 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50 

############################################################################
        #Monstres spéciaux ID = 5XX

        #501 - Paladin
        if self.ID == 501 :
            self.name = 'Paladin'
            self.img = 'img/monstre/PaladinFightGauche.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 15 + self.niveau*5
            self.vie = self.viemax
            self.dgtMin = 6 + self.niveau * 3
            self.dgtMax = 10 + self.niveau * 3
            self.esquive = 0 + self.niveau
            self.gainxp = 250 + self.niveau * 80
            self.gold = random.randint(0,350)
            self.healMin = 3 + self.niveau * 2
            self.healMax = 3 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)
            

        #502 - Hérétique
        if self.ID == 502 :
            self.name = 'Hérétique'
            self.img = 'img/monstre/HeretiqueFightGauche.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 10 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 5 + self.niveau * 2
            self.dgtMax = 10 + self.niveau * 2
            self.esquive = 0 + self.niveau
            self.gainxp = 250 + self.niveau * 80
            self.gold = random.randint(0,350)
            self.healMin = 3 + self.niveau * 2
            self.healMax = 3 + self.niveau * 3
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)


        #503 - Assassin
        if self.ID == 503 :
            self.name = 'Assassin'
            self.img = 'img/monstre/AssassinFightGauche.png'
            self.niveauMin = personnage.niveau - 2
            if self.niveauMin < 1 : self.niveauMin = 1
            self.niveauMax = personnage.niveau + 2
            self.niveau = random.randint(self.niveauMin,self.niveauMax)
            self.viemax = 10 + self.niveau*3
            self.vie = self.viemax
            self.dgtMin = 3 + self.niveau * 4
            self.dgtMax = 6 + self.niveau * 4
            self.esquive = 0 + self.niveau
            self.gainxp = 250 + self.niveau * 80
            self.gold = random.randint(0,350)
            self.loot = 1
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)
            

        #504 - Esclave faible
        if self.ID == 504 :
            self.name = "Esclave faible"
            self.img = "img/monstre/EsclaveFaible1Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 5 + 3 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 1 + 2 * personnage.niveau
            self.dgtMax = 3 + 2 * personnage.niveau
            self.esquive = 2 * personnage.niveau
            self.gainxp = 50 + self.niveau * 20
            self.gold = random.randint(0,50)
            self.loot = 2
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #505 - Esclave faible
        if self.ID == 505 :
            self.name = "Esclave faible"
            self.img = "img/monstre/EsclaveFaible2Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 5 + 3 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 1 + 2 * personnage.niveau
            self.dgtMax = 3 + 2 * personnage.niveau
            self.esquive = 2 * personnage.niveau
            self.gainxp = 50 + self.niveau * 20
            self.gold = random.randint(0,50)
            self.loot = 1
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #506 - Esclave faible
        if self.ID == 506 :
            self.name = "Esclave faible"
            self.img = "img/monstre/EsclaveFaible3Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 5 + 3 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 1 + 2 * personnage.niveau
            self.dgtMax = 3 + 2 * personnage.niveau
            self.esquive = 2 * personnage.niveau
            self.gainxp = 50 + self.niveau * 20
            self.gold = random.randint(0,50)
            self.loot = 2
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #507 - Esclave commun
        if self.ID == 507 :
            self.name = "Esclave commun"
            self.img = "img/monstre/Esclave1Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 10 + 5 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 3 + 2 * personnage.niveau
            self.dgtMax = 5 + 2 * personnage.niveau
            self.esquive = 3 * personnage.niveau
            self.gainxp = 80 + self.niveau * 20
            self.gold = random.randint(0,100)
            self.loot = 1
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #508 - Esclave commun
        if self.ID == 508 :
            self.name = "Esclave commun"
            self.img = "img/monstre/Esclave2Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 10 + 5 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 3 + 2 * personnage.niveau
            self.dgtMax = 5 + 2 * personnage.niveau
            self.esquive = 3 * personnage.niveau
            self.gainxp = 80 + self.niveau * 20
            self.gold = random.randint(0,100)
            self.loot = 1
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #509 - Esclave commun
        if self.ID == 509 :
            self.name = "Esclave commun"
            self.img = "img/monstre/Esclave3Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 10 + 5 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 3 + 2 * personnage.niveau
            self.dgtMax = 5 + 2 * personnage.niveau
            self.esquive = 3 * personnage.niveau
            self.gainxp = 80 + self.niveau * 20
            self.gold = random.randint(0,100)
            self.loot = 1
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)
            
        #510 - Esclave puissant
        if self.ID == 510 :
            self.name = "Esclave puissant"
            self.img = "img/monstre/EsclaveFort1Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 7 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 5 + 3 * personnage.niveau
            self.dgtMax = 8 + 3 * personnage.niveau
            self.esquive = 4 * 2* personnage.niveau
            self.gainxp = 100 + self.niveau * 20
            self.gold = random.randint(0,200)
            self.loot = 1
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #511 - Esclave puissant
        if self.ID == 511 :
            self.name = "Esclave puissant"
            self.img = "img/monstre/EsclaveFort2Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 7 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 5 + 3 * personnage.niveau
            self.dgtMax = 8 + 3 * personnage.niveau
            self.esquive = 4 * 2* personnage.niveau
            self.gainxp = 100 + self.niveau * 20
            self.gold = random.randint(0,200)
            self.loot = 1
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #512 - Esclave puissant
        if self.ID == 512 :
            self.name = "Esclave puissant"
            self.img = "img/monstre/EsclaveFort3Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 7 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 5 + 3 * personnage.niveau
            self.dgtMax = 8 + 3 * personnage.niveau
            self.esquive = 4 * 2* personnage.niveau
            self.gainxp = 100 + self.niveau * 20
            self.gold = random.randint(0,200)
            self.loot = 2
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)
         
        #513 - Esclave mage
        if self.ID == 513 :
            self.name = "Esclave mage"
            self.img = "img/monstre/EsclaveMage1Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 7 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 1 +  personnage.niveau
            self.dgtMax = 3 +  personnage.niveau
            self.healMin = 2 + personnage.niveau
            self.healMax = 4 + 2 * personnage.niveau
            self.esquive = personnage.niveau
            self.gainxp = 100 + self.niveau * 20
            self.gold = random.randint(0,200)
            self.loot = 2
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #514 - Esclave mage
        if self.ID == 514 :
            self.name = "Esclave mage"
            self.img = "img/monstre/EsclaveMage2Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 7 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 1 +  personnage.niveau
            self.dgtMax = 3 +  personnage.niveau
            self.healMin = 2 + personnage.niveau
            self.healMax = 4 + 2 * personnage.niveau
            self.esquive = personnage.niveau
            self.gainxp = 100 + self.niveau * 20
            self.gold = random.randint(0,200)
            self.loot = 2
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #515 - Esclave mage
        if self.ID == 515 :
            self.name = "Esclave mage"
            self.img = "img/monstre/EsclaveMage3Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 7 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 1 +  personnage.niveau
            self.dgtMax = 3 +  personnage.niveau
            self.healMin = 2 + personnage.niveau
            self.healMax = 4 + 2 * personnage.niveau
            self.esquive = personnage.niveau
            self.gainxp = 100 + self.niveau * 20
            self.gold = random.randint(0,200)
            self.loot = 2
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #516 - Compagnon - Paladin
        if self.ID == 516 :
            self.name = "Paladin"
            self.img = "img/monstre/CompagnonPaladinFight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 7 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 5 + 3 * personnage.niveau
            self.dgtMax = 8 + 3 * personnage.niveau
            self.esquive = 4 * 2* personnage.niveau
            self.gainxp = 100 + self.niveau * 20
            self.gold = random.randint(0,200)
            self.loot = 2
            self.healMin = 1 + self.niveau * 3
            self.healMax = 2 + self.niveau * 4
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #517 - Compagnon - Assassin
        if self.ID == 517 :
            self.name = "Assassin"
            self.img = "img/monstre/CompagnonAssassinFight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 7 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 5 + 3 * personnage.niveau
            self.dgtMax = 8 + 3 * personnage.niveau
            self.esquive = 4 * 2* personnage.niveau
            self.gainxp = 100 + self.niveau * 20
            self.gold = random.randint(0,200)
            self.loot = 2
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #518 - Compagnon - Sorcier
        if self.ID == 518 :
            self.name = "Sorcier"
            self.img = "img/monstre/CompagnonHeretiqueFight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 7 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 5 + 3 * personnage.niveau
            self.dgtMax = 8 + 3 * personnage.niveau
            self.esquive = 4 * 2* personnage.niveau
            self.gainxp = 100 + self.niveau * 20
            self.gold = random.randint(0,200)
            self.loot = 2
            self.healMin = 1 + self.niveau * 3
            self.healMax = 2 + self.niveau * 4
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #519 - Compagnon - Karus
        if self.ID == 519 :
            self.name = "Karus"
            self.img = "img/monstre/KarusFight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 7 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 5 + 3 * personnage.niveau
            self.dgtMax = 8 + 3 * personnage.niveau
            self.esquive = 4 * 2* personnage.niveau
            self.gainxp = 100 + self.niveau * 20
            self.gold = random.randint(0,200)
            self.loot = 2
            self.healMin = 1 + self.niveau * 3
            self.healMax = 2 + self.niveau * 4
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #520 - Compagnon - Iriszia
        if self.ID == 520 :
            self.name = "Iriszia"
            self.img = "img/monstre/Iriszia.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 7 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 5 + 3 * personnage.niveau
            self.dgtMax = 8 + 3 * personnage.niveau
            self.esquive = 4 * 2* personnage.niveau
            self.gainxp = 100 + self.niveau * 20
            self.gold = random.randint(0,200)
            self.loot = 2
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)

        #521 - Compagnon - Archimage
        if self.ID == 521 :
            self.name = "Archimage"
            self.img = "img/monstre/ArchimageFight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 7 * personnage.niveau
            self.vie = self.viemax
            self.dgtMin = 5 + 3 * personnage.niveau
            self.dgtMax = 8 + 3 * personnage.niveau
            self.esquive = 4 * 2* personnage.niveau
            self.gainxp = 100 + self.niveau * 20
            self.gold = random.randint(0,200)
            self.loot = 2
            self.healMin = 1 + self.niveau * 3
            self.healMax = 2 + self.niveau * 4
            if self.esquive >= 50 : self.esquive = 50
            self.lootMonstre(personnage,story,item)


    #Cette fonction permet de gérer le loot sur les monstres avec une grande part d'aléatoire
    def lootMonstre(self,personnage,story,item):
        if story.activation_quetes[5] == 1 and self.ID in (301,302,303) and item.inventaireLook(90) < 3:
            self.loot = 90
        else :
                
            loot = random.randint(1,2) #Soit un loot de type bois/minerais/tissus
                                              #Soit un loot dans la liste lootInutile
            if loot == 1:
                typeLoot = random.randint(1,3) #Si 1 loot = bois/minerais, si 2/3 loot = tissus

                if typeLoot == 1:
                    choixLoot = random.randint(1,2)#Si 1 loot = minerais, si 2 loot = bois

                    if choixLoot == 1:
                        if self.niveau <= 10 :
                            self.loot = 1
                        elif self.niveau > 10 and self.niveau <= 15:
                            qualiteLoot = random.randint(1,2)
                            if qualiteLoot == 1 :
                                self.loot = 1
                            elif qualiteLoot == 2 :
                                self.loot = 2
                        elif self.niveau > 15:
                            qualiteLoot = random.randint(1,3)
                            if qualiteLoot == 1 :
                                self.loot = 1
                            elif qualiteLoot == 2 :
                                self.loot = 2
                            elif qualiteLoot == 3 :
                                self.loot = 3
                        
                    elif choixLoot == 2:
                        if self.niveau <= 10 :
                            self.loot = 4
                        elif self.niveau > 10 and self.niveau <= 15:
                            qualiteLoot = random.randint(1,2)
                            if qualiteLoot == 1 :
                                self.loot = 4
                            elif qualiteLoot == 2 :
                                self.loot = 5
                        elif self.niveau > 15:
                            qualiteLoot = random.randint(1,3)
                            if qualiteLoot == 1 :
                                self.loot = 4
                            elif qualiteLoot == 2 :
                                self.loot = 5
                            elif qualiteLoot == 3 :
                                self.loot = 6


                        
                else:
                    if self.niveau <= 10 :
                        self.loot = 7
                    elif self.niveau > 10 and self.niveau <= 15:
                        qualiteLoot = random.randint(1,2)
                        if qualiteLoot == 1 :
                            self.loot = 7
                        elif qualiteLoot == 2 :
                            self.loot = 8
                    elif self.niveau > 15:
                        qualiteLoot = random.randint(1,3)
                        if qualiteLoot == 1 :
                            self.loot = 7
                        elif qualiteLoot == 2 :
                            self.loot = 8
                        elif qualiteLoot == 3 :
                            self.loot = 9


                
            elif loot == 2:
                self.loot = random.choice(item.lootSecondaire)
    
    

            
