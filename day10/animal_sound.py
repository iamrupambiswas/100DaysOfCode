class Animal():
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        print("Dog barks!")
        
class Cat(Animal):
    def sound(self):
        print("Cat meows!")
        
def animal_sound(animal):
    animal.sound()
    
dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)