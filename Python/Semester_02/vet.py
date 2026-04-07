class animals:
    def __init__(self, owner, name, age, colour, weight, symptom):
        self.owner = owner
        self.name = name
        self.age = age
        self.colour = colour
        self.weight = weight

    def get_datails(self):
     return f"{self.name}"

owner = input("Enter the owner's name: ")
name = input("Enter the animal's name: ")
age = int(input("Enter the animal's age: "))
colour = input("Enter the animal's colour: ")
weight = float(input("Enter the animal's weight: "))

print("-"*60 ,"\n")

animal = animals(owner,name,age,colour,weight)

print(animal.get_datails())
