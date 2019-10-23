class Character() :
    def __init__(self):
        self.name = ""
        self.health = 0
        self.power =0

    def alive(self):
        return self.health > 0
    
    def attack(self,enemy):
        enemy.health -= self.power
        print("{} does {} damage to {}.".format(self.name, self.power, enemy.name))

        if not enemy.alive() :
            if enemy.name == "Goblin":
                #print("{} is dead.".format(enemy.name))
                print("The goblin is dead.")
            elif enemy.name == "Hero":
                print("You are dead.")

    def print_status(self):
        print("{} has {} health and {} power".format(self.name, self.health, self.power))

class Hero(Character):
    def __init__(self):
        self.name = "Hero"
        self.health = 10
        self.power = 5

    
class Goblin(Character):
    def __init__(self):
        self.name = "Goblin"
        self.health = 6
        self.power = 2


hero = Hero()
goblin = Goblin()

while goblin.alive() and hero.alive():
    hero.print_status()
    goblin.print_status()
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        hero.attack(goblin)
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))

    if goblin.alive():
        goblin.attack(hero)







        


