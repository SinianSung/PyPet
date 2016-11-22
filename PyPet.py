import random
import time

class PyPet:
    # vorlage meiner Haustiere

    #Eigenschaften

    name = ''
    image="""
|\---/|
| o_o |
 \_^_/
 """
    groesse = 0
    gewicht = 0
    energy = 50
    ishungry = True
    isalive = True
    beastMode = False
    happiness = 50
    iq = 100
    memory =[]
    happyMoments ={}
    sadMoments=[]

    # konstruktor der klasse
    def __init__(self,name, gewicht=50, height=10):
        self.name = name
        self.gewicht = gewicht
        self.groesse = height
        self.learn('Geburt')
        self.happyMoments[time.time()]= 'Geburt'
        
    def setHappiness(self, value):
        if self.happiness >=100:
            pass
        elif self.happiness <=0:
            self.isalive = False
        else:
            self.happiness +=value

    def setGewicht(self,value):
        if self.gewicht <=0:
            self.isalive = False
        elif self.gewicht > 1000:
            pass
        else:
            self.gewicht +=value
            beastMode= False

    def setEnergy(self,value):
        if self.energy <=0:
            self.isalive = False
        elif self.energy > 1000:
            beastMode = True
        else:
            self.energy +=value
            beastMode = False
        
    def eat(self,food):
        if self.ishungry:
            print('nomnomnom')
            self.energy +=len(food)
            self.setGewicht(1)
            self.ishungry = False
        else:
            print(' oh no ...')
            self.gewicht += len(food)
            self.energy -=1
            self.setHappiness(-5)
            self.iq -=1
            
    def play(self, item='running'):
        self.happiness +=5
        self.ishungry = True
        self.gewicht -=1
        self.iq +=1
        self.happyMoments['play'] = item

    def learn(self, item):
        self.memory.append(item)
        self.happiness +=1

    def howAreYou(self):
        print(self.happiness)
        if self.happiness <10:
            print(':-(')
        elif self.happiness < 20:
            print(':-|')
        elif self.happiness < 40:
            print('---')
        elif self.happiness < 60:
            print(';-|')
        elif self.happiness < 80:
            print(';-)')
        else:
            pass
        

    def sayHello(self):
        print("Hi, my Name is {}. Look i'm cute: \n{}".format(self.name, self.image))
    
    def talk(self):
        i = random.randrange(0,len(self.memory))
        print(self.memory[i])

            
