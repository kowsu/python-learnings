import animal_class as animal_class
class Dog(animal_class.Animal):
    def bark(self):
        print("Dog barks")
    
    def characters(self):
        print("All dogs bites")

if __name__ == "__main__":
    animal = animal_class.Animal()
    dog = Dog()
    animal.eat()
    animal.characters()
    dog.bark()
    dog.characters()