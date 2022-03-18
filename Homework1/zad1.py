from enum import Enum

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"

class Animal:
    isAlive = True
    gender = Gender.FEMALE

    def __init__(self, gender):
        self.gender = gender

    def breed(self, partner):
        try:
            if self.gender == Gender.FEMALE and partner.gender == Gender.MALE and type(self) == type(partner):
                return type(self)(self.gender)
        except AttributeError as err: 
            print("Attribute not found")

class Cat(Animal): 
    genus = "Felis"

    def __init__(self, gender):
        super().__init__(gender)

    def purr(self):
        return "purr purr"

class Dog(Animal): 
    genus = "Canis"

    def __init__(self, gender):
        super().__init__(gender)
    
    def woof(self):
        return "woof woof"

# Test
cat1 = Cat(Gender.FEMALE)
cat2 = Cat(Gender.MALE)
dog1 = Dog(Gender.FEMALE)
dog2 = Dog(Gender.MALE)

cat3 = cat1.breed(cat2)
dog3 = dog1.breed(dog2)

print(dog3)
print(cat3)
print(dog1.woof())