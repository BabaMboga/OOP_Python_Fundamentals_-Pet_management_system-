#Class initialisation with default __init__
class Pet:
    def speak(self):
        # print("sound made")
        return ("pet spoke")

Rasmus = Pet()
Rasmus.name = "Rasmus"
print(Rasmus.name)
print(Rasmus.speak())

#A simple class to represent a dog with modified __init__   
class Dog:

    species = "canis lupus familiaris" # class attribute

    def __init__(self,name,breed,age="N/A"):
        self.name = name # instance attribute
        self.breed = breed
        self.age = age

    def speak(self):
        return f"{self.name} says woof! woof!"
    
koba = Dog("Koba","Great Dane", 3)
amad = Dog("amad", "Black Goat") # works because we intialised age with a default value
koba.age = 4
print(koba.speak())
print(koba.age)
print(amad.age)
print(amad.species)
print(amad.name)

print(koba.species)
print(koba.name)


class Cat:
    pass

class Rat:
    pass