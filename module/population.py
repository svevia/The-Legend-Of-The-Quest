import random
'''Cette class gère l'augmentation ou la diminution des population huiamines ou de contaminé
La population de contaminé influe la taille du biome contaminé sur la carte'''


class pop :

    def __init__(self):
        self.population = 10000
        self.contamination = 0

    def modifPopulation(self,fen1,personnage,item):
        
        self.mort = random.randint(0,3)
        self.naissance = random.randint(0,2)
        if self.contamination >= 20000:
            self.nouveauConta = random.randint(0,1)
        elif self.contamination >= 1000:
            self.nouveauConta = random.randint(0,2)
        elif self.contamination < 1000:
            self.nouveauConta = random.randint(0,3)
        self.mortConta = random.randint(0,1)
        
        if self.population < 6000 and self.population > 4000 :
            self.population += self.naissance - self.mort - self.mortConta
            
        elif self.population <= 4000 :
            self.population += self.naissance - self.mortConta
            
        elif self.population >= 6000 :
            self.population -= self.mort + self.mortConta
           


        if self.contamination > 100 and (self.contamination < 5000) :
            self.contamination += self.nouveauConta - self.mortConta
            
        elif self.contamination <= 100 :
            self.contamination += self.nouveauConta
            
        elif self.contamination >= 3500 :
            self.contamination -= self.mortConta
