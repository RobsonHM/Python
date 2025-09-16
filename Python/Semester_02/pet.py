class Pet:
    def __init__(self, name, pet_type, age):
        self.name = name
        self.pet_type = pet_type
        self.age = age

class Adopter:
    def __init__(self, name, adopter_id):
        self.name = name
        self.adopter_id = adopter_id
        self.pets = []

    def adopt_pet(self, pet):
        self.pets.append(pet)

dog = Pet("Zezão", "cachorro", 8000)
adopter = Adopter("João", 1)
adopter.adopt_pet(dog)
for pet in adopter.pets:
    print(f"{adopter.name} adotou {pet.name}, um {pet.pet_type} de {pet.age} anos.")
