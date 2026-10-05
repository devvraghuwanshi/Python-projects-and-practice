# Method Chaining: Calling multiple methods sequentially
#                  each object performs an action on the same object and returns self.

class Car:

    def start(self):
        print("You Start the Car")
        return self

    def drive(self):
        print("You drive the Car")
        return self

    def brake(self):
        print("You step on the brake")
        return self

    def turn_off(self):
        print("You turn off the car")
        return self

car = Car()
car.start().drive().brake().turn_off()