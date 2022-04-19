class Animal():
    pass

class Bird(Animal):
    def fly(self):
        print("fly")

class Farm():
    animal = Animal()

class FarmWithBirds(Farm):
    animal = Bird() # why mypy is ok?

def func(f: Farm):
    f.animal = Animal() # the magic

f = FarmWithBirds()
f.animal.fly() # print "fly"
func(f)
f.animal.fly() # AttributeError: 'Animal' object has no attribute 'fly'
