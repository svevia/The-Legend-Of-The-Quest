from module.statistiques import *
import random
pygame.init()

class compagnon :




    def __init__(self,ami,IDCompagnon,personnage):
        self.IDCompagnon = IDCompagnon
        self.statsCompagnon(personnage)
        self.ami = ami
        self.IDC = 0
        self.listHeal = (10,11,12,13,15)
        self.listTank = (7,8,9)
        self.prixFinal = 0


        

    def statsCompagnon(self,personnage):


        if self.IDCompagnon == 1 :
            self.name = "Esclave faible"
            self.img = "img/Compagnon/EsclaveFaible1Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 5 + 3 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 1 + 2 * personnage.niveau
            self.degatMax = 3 + 2 * personnage.niveau
            self.esquive = 2 + personnage.niveau
            self.critique =  2 + personnage.niveau
            self.prix = 50
            self.IDennemi = 504
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 2 :
            self.name = "Esclave faible"
            self.img = "img/Compagnon/EsclaveFaible2Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 5 + 3 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 1 + 2 * personnage.niveau
            self.degatMax = 3 + 2 * personnage.niveau
            self.esquive = 2 + personnage.niveau
            self.critique =  2 + personnage.niveau
            self.prix = 50
            self.IDennemi = 505
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 3 :
            self.name = "Esclave faible"
            self.img = "img/Compagnon/EsclaveFaible3Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 5 + 3 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 1 + 2 * personnage.niveau
            self.degatMax = 3 + 2 * personnage.niveau
            self.esquive = 2 + personnage.niveau
            self.critique =  2 + personnage.niveau
            self.prix = 50
            self.IDennemi = 506
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 4 :
            self.name = "Esclave commun"
            self.img = "img/Compagnon/Esclave1Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 10 + 5 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 3 + 2 * personnage.niveau
            self.degatMax = 5 + 2 * personnage.niveau
            self.esquive = 3 + personnage.niveau
            self.critique =  3 + personnage.niveau
            self.prix = 100
            self.IDennemi = 507
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 5 :
            self.name = "Esclave commun"
            self.img = "img/Compagnon/Esclave2Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 10 + 5 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 3 + 2 * personnage.niveau
            self.degatMax = 5 + 2 * personnage.niveau
            self.esquive = 3 * personnage.niveau
            self.critique =  3 * personnage.niveau
            self.prix = 100
            self.IDennemi = 508
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 6 :
            self.name = "Esclave commun"
            self.img = "img/Compagnon/Esclave3Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 10 + 5 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 3 + 2 * personnage.niveau
            self.degatMax = 5 + 2 * personnage.niveau
            self.esquive = 3 * personnage.niveau
            self.critique =  3 * personnage.niveau
            self.prix = 100
            self.IDennemi = 509
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 7 :
            self.name = "Esclave puissant"
            self.img = "img/Compagnon/EsclaveFort1Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 25 + 7 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 5 + personnage.niveau
            self.degatMax = 8 + personnage.niveau
            self.esquive = 4 + personnage.niveau
            self.critique =  4 + personnage.niveau
            self.prix = 200
            self.IDennemi = 510
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 8 :
            self.name = "Esclave puissant"
            self.img = "img/Compagnon/EsclaveFort2Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 25 + 7 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 5 +  personnage.niveau
            self.degatMax = 8 +  personnage.niveau
            self.esquive = 4 + personnage.niveau
            self.critique =  4 +  personnage.niveau
            self.prix = 200
            self.IDennemi = 511
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 9 :
            self.name = "Esclave puissant"
            self.img = "img/Compagnon/EsclaveFort3Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 25 + 7 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 5 +  personnage.niveau
            self.degatMax = 8 +  personnage.niveau
            self.esquive = 4 + personnage.niveau
            self.critique =  4 + personnage.niveau
            self.prix = 200
            self.IDennemi = 512
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 10 :
            self.name = "Esclave mage"
            self.img = "img/Compagnon/EsclaveMage1Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 20 + 3 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 1 +  personnage.niveau
            self.degatMax = 3 +  personnage.niveau
            self.healMin = 2 + personnage.niveau
            self.healMax = 4 + 2 * personnage.niveau
            self.esquive = personnage.niveau
            self.critique =  2 + personnage.niveau
            self.prix = 200
            self.IDennemi = 513
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 11 :
            self.name = "Esclave mage"
            self.img = "img/Compagnon/EsclaveMage2Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 20 + 3 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 1 +  personnage.niveau
            self.degatMax = 3 +  personnage.niveau
            self.healMin = 2 + personnage.niveau
            self.healMax = 4 + 2 * personnage.niveau
            self.esquive = personnage.niveau
            self.critique =  2 + personnage.niveau
            self.prix = 200
            self.IDennemi = 514
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 12 :
            self.name = "Esclave mage"
            self.img = "img/Compagnon/EsclaveMage3Fight.png"
            self.niveau = personnage.niveau
            self.viemax = 20 + 3 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 1 +  personnage.niveau
            self.degatMax = 3 +  personnage.niveau
            self.healMin = 2 + personnage.niveau
            self.healMax = 4 + 2 * personnage.niveau
            self.esquive = personnage.niveau
            self.critique =  2 + personnage.niveau
            self.prix = 200
            self.IDennemi = 515
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50
        

        if self.IDCompagnon == 13 :
            self.name = "Paladin"
            self.img = "img/Compagnon/CompagnonPaladinFight.png"
            self.niveau = personnage.niveau
            self.viemax = 25 + 7 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 5 +  personnage.niveau
            self.degatMax = 8 +  personnage.niveau
            self.esquive = 4 + 2* personnage.niveau
            self.critique =  4 + 2 * personnage.niveau
            self.IDennemi = 516
            self.healMin = 1 + self.niveau * 3
            self.healMax = 2 + self.niveau * 4
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 14 :
            self.name = "Assassin"
            self.img = "img/Compagnon/CompagnonAssassinFight.png"
            self.niveau = personnage.niveau
            self.viemax = 20 + 5 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 5 + 2 * personnage.niveau
            self.degatMax = 8 + 2 * personnage.niveau
            self.esquive = 4 + 2* personnage.niveau
            self.critique =  4 + 2 * personnage.niveau
            self.IDennemi = 517
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 15 :
            self.name = "Sorcier"
            self.img = "img/Compagnon/CompagnonHeretiqueFight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 3 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 5 + 3 * personnage.niveau
            self.degatMax = 8 + 3 * personnage.niveau
            self.esquive = 4 + 2* personnage.niveau
            self.critique =  4 + 2 * personnage.niveau
            self.IDennemi = 518
            self.healMin = 1 + self.niveau * 3
            self.healMax = 2 + self.niveau * 4
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 16 :
            self.name = "Karus"
            self.img = "img/Compagnon/KarusFight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 3 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 5 + 3 * personnage.niveau
            self.degatMax = 8 + 3 * personnage.niveau
            self.esquive = 4 + 2* personnage.niveau
            self.critique =  4 + 2 * personnage.niveau
            self.IDennemi = 519
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 17 :
            self.name = "Iriszia"
            self.img = "img/Compagnon/Iriszia.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 3 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 5 + 3 * personnage.niveau
            self.degatMax = 8 + 3 * personnage.niveau
            self.esquive = 4 + 2* personnage.niveau
            self.critique =  4 + 2 * personnage.niveau
            self.IDennemi = 520
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 18 :
            self.name = "Archimage"
            self.img = "img/Compagnon/ArchimageFight.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 3 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 5 + 3 * personnage.niveau
            self.degatMax = 8 + 3 * personnage.niveau
            self.esquive = 4 + 2* personnage.niveau
            self.critique =  4 + 2 * personnage.niveau
            self.IDennemi = 521
            self.healMin = 1 + self.niveau * 3
            self.healMax = 2 + self.niveau * 4
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        if self.IDCompagnon == 19 :
            self.name = "Scientifique"
            self.img = "img/Compagnon/Scientifique.png"
            self.niveau = personnage.niveau
            self.viemax = 15 + 3 * personnage.niveau
            self.vie = self.viemax
            self.degatMin = 1 + 3 * personnage.niveau
            self.degatMax = 2 + 3 * personnage.niveau
            self.esquive = 4 + 2* personnage.niveau
            self.critique =  4 + 2 * personnage.niveau
            if self.esquive >= 50 : self.esquive = 50
            if self.critique >= 50 : self.critique = 50

        



            



