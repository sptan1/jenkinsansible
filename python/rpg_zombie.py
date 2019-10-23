class Character() :
    def __init__(self):
        self.name = ""
        self.health = 0
        self.power =0

    def alive(self):
        return self.health > 0
    
    def attack(self,enemy):
        if enemy.name == "Zombie":
            print("{} does 0 damage to {}.".format(self.name, enemy.name))
        else :
            enemy.health -= self.power
            print("{} does {} damage to {}.".format(self.name, self.power, enemy.name))

        if enemy.health <= 0 :
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

class Zombie(Character):
    def __init__(self):
        self.name = "Zombie"
        self.health = 10
        self.power = 2

hero = Hero()
#goblin = Goblin()
#zombie = Zombie()
enemy_input = 0

while enemy_input !="2" and enemy_input !="1":

	print("What do you want to attack?")
	print("1. Goblin")
	print("2. Zombie")
	enemy_input = input("> ")

if enemy_input == "1":
	enemy = Goblin()
	enemyname = "Goblin"
elif enemy_input == "2":
	enemy = Zombie()
	enemyname = "Zombie"

while enemy.alive() and hero.alive():
	hero.print_status()
	enemy.print_status()
	print()
	print("What do you want to do?")
	print("1. fight {}".format(enemyname))
	print("2. do nothing")
	print("3. flee")
	print("> ", end=' ')
	raw_input = input()
	if raw_input == "1":
		hero.attack(enemy)
	elif raw_input == "2":
		pass
	elif raw_input == "3":
		print("Goodbye.")
		break
	else:
		print("Invalid input {}".format(raw_input))

	if enemy.alive():
        # Goblin attacks hero
		enemy.attack(hero)







        


