# Defining classes for Animals and Pets
"""
Class representing Animal 
"""
class Animal:
    def __init__(self, type) -> None:
        self.type = type

"""
Class extending Animals as Pets
"""
class Pet(Animal):
    def __init__(self, type) -> None:
        super().__init__(type)

"""
Class extending Pets as Dogs
"""
class Dog(Pet):
    voice = "Bow bow"
    type = "Pets"
    def __init__(self, type, voice) -> None:
        self.voice = voice
        self.type = type
        super().__init__(Dog.type)
    
    # Dogs bark
    @classmethod
    def bark(cls, voice):
        cls.voice = voice
        print(cls.voice)
    
    def bark(self):
        print(self.voice)

# Creating object of Dog class
terrier = Dog("Terrier", "How hoow")
dalmitian = Dog("Dalmitian", "Bow how")

# Dogs barking
terrier.bark()
dalmitian.bark()
print(Dog.voice)