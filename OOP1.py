#-------------------------------------
#-------------Mason Skinner-----------
#----------FP4-F01 Simple OOP---------
#------------April 19, 2022-----------
#-------------------------------------

#--------------Imports----------------
import time
import random

#--------------Functions--------------
class Npc:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
            print(f"Hey there, my name is {self.name}.")
class Fighter(Npc):
    def __init__(self, name, age, level, health):
        super().__init__(name, age)
        self.level = level
        self.health = health
    def duel(self, p_lvl):
        print("You have been challenged to a duel!")
        if self.level > p_lvl:
            print(f"{self.name} overpowers you and claims victory!")
        elif self.level < p_lvl:
            print(f"You overpower {self.name} and claim victory!")
        else:
            print("You wrestle till both parties tire, a stalemate is called!")
class Townsfolk(Npc):
    def __init__(self, name, age, gold, reputation):
        super().__init__(name, age)
        self.gold = gold
        self.reputation = reputation

class Guard(Fighter):
    def __init__(self, name, age, level, health, city, rank):
        super().__init__(name, age, level, health)
        self.city = city
        self.rank = rank
    
        
class Bandit(Fighter):
    def __init__(self, name, age, level, health, faction, rank):
        super().__init__(name, age, level, health)
        self.faction = faction
        self.rank = rank

class Merchant(Townsfolk):
    def __init__(self, name, age, gold, reputation, profession):
        super().__init__(name, age, gold, reputation)
        self.profession = profession
    def trade(self):
        print("I have many wares, take a look!")
class Citizen(Townsfolk):
    def __init__(self, name, age, gold, reputation, profession):
        super().__init__(name, age, gold, reputation)
        self.profession = profession
    def gossip(self):
        x = random.randint(1,2)
        if x == 1:
            print("I hear a war is brewing in the east.")
        elif x == 2:
            print("Word is ale prices are gonna go up.")

def question(request, option1, option2, option3):
    x = False
    while x == False:
        print(request)
        answer = input('> ').lower()
        if answer == option1 or answer == option2 or answer == option3:
            x = True
            if answer == 'null':
                x = False
                print("What did you say?")
        else:
            print("What did you say?")
            time.sleep(2)
    return(answer)
       
def main():
    location = question("Do you go to the tavern, market, or barracks?", 'tavern', 'market', 'barracks')
    if location == 'tavern':
        print(f"inside are 3 citizens, an {citizen1.profession}, {citizen2.profession}, and a {citizen3.profession}")
        job = question("Who would you like to talk too?", citizen1.profession, citizen2.profession, citizen3.profession)
        if job == citizen1.profession:
            npc = citizen1
        elif job == citizen2.profession:
            npc = citizen2
        elif job == citizen3.profession:
            npc = citizen3
        npc.greeting()
        input('> ')
        npc.gossip()
    elif location == 'market':
        print(f"there are 3 stalls, a {merchant1.profession}, {merchant2.profession}, and a {merchant3.profession}")
        job = question("Who would you like to talk too?", merchant1.profession, merchant2.profession, merchant3.profession)
        if job == merchant1.profession:
            npc = merchant1
        elif job == merchant2.profession:
            npc = merchant2
        elif job == merchant3.profession:
            npc = merchant3
        npc.greeting()
        input('> ')
        npc.trade()
    elif location == 'barracks':
        print(f"there are 3 guards, a {guard1.rank}, {guard2.rank}, and a {guard3.rank}")
        job = question("Who would you like to talk too?", guard1.rank, guard2.rank, guard3.rank)
        if job == guard1.rank:
            npc = guard1
        elif job == guard2.rank:
            npc = guard2
        elif job == guard3.rank:
            npc = guard3
        npc.greeting()
        input('> ')
        npc.duel(random.randint(5,101))


#----------------------Objects-----------------------------
guard1 = Guard('Balggar', 32, 50, 250, 'Whiterun', 'captain')
guard2 = Guard('Dengirod', 28, 15, 125, 'Whiterun', 'soldier')
guard3 = Guard('Korur', 40, 100, 800, 'Whiterun', "kings' guard")
merchant1 = Merchant('Denelin', 53, 1000, 'trusted', 'general goods')
merchant2 = Merchant('Stafan', 47, 10000, 'world renowned', 'blacksmith')
merchant3 = Merchant('Caroher', 21, 250, 'untrusted', 'food and produce')
citizen1 = Citizen('Dilingiel', 35, 750, 'respected', 'inn keeper')
citizen2 = Citizen('Timoiper', 20, 400, 'neutral', 'forester')
citizen3 = Citizen('Norbchothee', 27, 150, 'shady', 'porter')


#---------------------Code------------------------------------
main()