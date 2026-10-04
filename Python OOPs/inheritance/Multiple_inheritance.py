# Multiple inheritance : When a derived class is derived from more than one parent class.

# Parent classes:
class Prey:

    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):
        print("This animal is hunting")

# child classes:
class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Predator,Prey):
    pass

# Objects:
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()