# Single Inheritance Example
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.speak())


#Multiple Inheritance Example
class Flyable:
    def fly(self):
        return "I can fly!"

class Bird:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says Chirp!"

class FlyingBird(Bird, Flyable):
    pass

my_bird = FlyingBird("Sparrow")
print(my_bird.speak()) 
print(my_bird.fly())   


# Multilevel Inheritance Example
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class WorkingDog(Dog):
    def work(self):
        return f"{self.name} is working."

my_working_dog = WorkingDog("Rex")
print(my_working_dog.speak()) 
print(my_working_dog.work())   

