
class Pet:
    def __init__(self, name , type , tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def sleep(self): # increases the pets energy by 25
        self.energy += 25
    
    def eat(self): #increases the pet's energy by 5 & health by 10
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5
    
    def noise(self): # prints out the pet's sound
        print("arf")

class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_night = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self): # walks the ninja's pet invoking the pet play() method
        self.pet.play()
    
    def feed(self):  #feeds the ninja's pet invoking the pet eat() method
        self.pet.eat()
    
    def bathe(self): #cleans the ninja's pet invoking the pet noise() method
        self.pet.noise()


john = Ninja("John", "Johns", 30, 100, Pet("Don", "dog", "sit", 100, 100))


john.bathe()
john.walk()
john.feed()

print(john.pet.energy)