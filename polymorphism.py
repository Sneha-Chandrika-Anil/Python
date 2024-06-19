class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def details(self):
        print(self.name+" is a dog of breed "+self.breed+". Woof!")

class Cat:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def sound(self):
        print(self.name+" is a cat of breed "+self.breed+". Meow!")

d = Dog("Jack","Pomeranian")
d.sound()
c = Cat("Meredith","Scottish Fold")
c.sound()