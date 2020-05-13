from random import randint
from time import sleep 

NAMES = ["Jaina", "Valeera", "Anduin", "Rexxar", "Illidian", "Malfurion", "Morgl",
    "Uther", "Gulldan", "Garrosh", "Thrall", "Alleria", "Medivh", "Thyrande", "Liadrin",
    "Arthas", "Lunara", "Sylvanas", "Jaraxxus", "Ragnaros", "Maiev", "Khadgar"]

NAMES_LENGTH = len(NAMES)

CLASSES = ["Paladin", "Warrior"]

heroes = []

things = []


class Thing:
    def __init__(self, name, protection, attack, lifetime):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.lifetime = lifetime
        print( f"\nСоздали вещичку: {self.name} c характеристиками: защита={str(self.protection)}" +
         f", атака= {self.attack} и срок жизни={self.lifetime}")
        

    def get_protection(self):
        return self.protection


    def __str__(self):
        return f"Вещичка: {self.name} c характеристиками: защита= {str(self.protection)}" +\
         f", атака={str(self.attack)} и срок жизни={str(self.lifetime)}"

    __repr__ = __str__     


class Person:
    def __init__(self, name, hp_amount, base_attack, base_protection):
        self.name = name
        self.hp_amount = hp_amount
        self.base_protection = base_protection
        self.final_protection = base_protection 
        self.base_attack = base_attack
        self.attack_damage = base_attack
        self.type = "Бесклассовый персонаж"
        self.things = []

    def __str__(self):
        return f"{self.type} {self.name} с характеристиками: здоровье={str(self.hp_amount)}" +\
            f", защита={str(self.final_protection)}, атака={str(self.attack_damage)}"

    __repr__ = __str__        


    def setThings(self, things):
        for thing in things:
            self.things.append(thing)
            self.final_protection += thing.protection 
            self.final_protection = round(self.final_protection)
            self.attack_damage += thing.attack
            self.hp_amount += thing.lifetime


    def attacks(self, defender):
        print(f"{self.name} атакует {defender.name}")
        sleep(1)
        defender.defends(self)


    def defends(self, attacker):  
        self.hp_amount -= (attacker.attack_damage - attacker.attack_damage*self.final_protection)
        self.hp_amount = round(self.hp_amount, 2)

        if self.hp_amount > 0:
            print(f"{self.name} выжил!")
        elif self.hp_amount <= 0:
            print(f"{self.name} проигрывает и удаляется с арены! ")


class Paladin(Person):
    def __init__(self, name, hp_amount, base_attack, base_protection):
        super().__init__(name, hp_amount, base_attack, base_protection)
        self.type = "Паладин"
        self.hp_amount = hp_amount*2
        self.base_protection = round(base_protection*2, 2) 
        self.protection = round(base_protection*2, 2) 
        print(f"\nСоздан новый персонаж: {self.type} {self.name}" + 
            f" с характеристиками: здоровье={str(self.hp_amount)}, защита={str(self.base_protection)}" + 
            f", атака={str(self.base_attack)}" )


class Warrior(Person):
    def __init__(self, name, hp_amount, base_attack, base_protection):
        super().__init__(name, hp_amount, base_attack, base_protection)
        self.type = "Воин"
        self.base_attack = base_attack*2
        self.attack_damage = base_attack*2  
        print(f"\nСоздан новый персонаж: {self.type} {self.name}" + 
            f" с характеристиками: здоровье={str(self.hp_amount)}, защита={str(self.base_protection)}" + 
            f", атака={str(self.base_attack)}" )



def createRandomThings():
    for thing_count in range(0, 20):
        thing = Thing(name="weapon_"+str(thing_count), protection=round(0.01*randint(0, 10), 2), 
         attack=randint(5,25), lifetime=randint(1,15))
        things.append(thing)
        sleep(.5)

    print("\nИтого:\n")
    things.sort(key=lambda x: x.protection) 
    #sorted_things = sorted(things, key=lambda x: x.protection)
    print(things)
    sleep(1)
    print("\nЗавершено создание набора рандомных вещей!\n")  
    sleep(1)
  


def create_and_equip_heroes():
    for hero_num in range(0, 10): 
        hero_class = CLASSES[randint(0, 1)]
        if hero_class == "Paladin":
            hero = Paladin(name=NAMES[randint(0, NAMES_LENGTH-1)], hp_amount=100, base_attack=randint(0,50),\
                base_protection=round(0.01*randint(0,30), 2))
        else:
            hero = Warrior(name=NAMES[randint(0, NAMES_LENGTH-1)], hp_amount=100, base_attack=randint(0,50),\
                base_protection=round(0.01*randint(0,30), 2))
        hero_sack = []
        for item in range(1, randint(1, 4)):
            thing = things[randint(0, 19)]
            hero_sack.append(thing)            
        hero.setThings(hero_sack)
        sleep(.5)
        heroes.append(hero)
        sleep(1)    
    sleep(.5)
    print("\nИтого:\n")    
    print(heroes)        
    sleep(1)
    print("\nГерои созданы и экипированы!\n")


def main():
    

    def init_match():


        sleep(1)        
        print("\nНачинается битва!\n")
        sleep(1)

        round_count = 0

        while len(heroes) > 1:

            round_count+=1
            sleep(1)
            print(f"\nРаунд {round_count}!\n")
            sleep(1)

            fighter1 = heroes[randint(0, len(heroes)-1)]
            fighter2 = heroes[randint(0, len(heroes)-1)]

            while fighter2 == fighter1:
                fighter2 = heroes[randint(0,len(heroes)-1)]

            print(f"На арену выходят: {fighter1.name} и {fighter2.name}") 
            sleep(1)

            while fighter2.hp_amount >= 0 and fighter1.hp_amount >= 0:
                fighter1.attacks(fighter2)
                if fighter2.hp_amount<=0:
                    break
                fighter2.attacks(fighter1)
                sleep(1)

            if fighter1.hp_amount <= 0:
                heroes.remove(fighter1)
            elif fighter2.hp_amount <= 0:
                heroes.remove(fighter2)    
            sleep(1)
                
        winner = heroes[0]
        sleep(.5)
        print("\nМатч завершен!\n")
        sleep(.5)
        print(f"Победитель: {winner.name} с hp={str(winner.hp_amount)}")
        sleep(1)
        print("\nЗвучат фанфары и все чествуют победителя!\n")   
        sleep(1)
         

    print("\nДобро пожаловать в нашу таверну, дорогой друг!\n")
    sleep(1)
    print("\nПрошу заходи, располагайся, скоро начнется Потасовка!\n")
    print("...")
    sleep(1)
    print("...")
    sleep(1)
    print("\n Ну, что-ж, пришло время стартовать!\n")
    sleep(1)
    print("\nСоздаем экипировку!\n")
    sleep(1)
    createRandomThings()

    print("\nСоздаем персонажей!\n")
    sleep(1)
    create_and_equip_heroes()

    init_match()


if __name__ == "__main__":
    main()
