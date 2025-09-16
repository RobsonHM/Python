print ("Who are you?")
varbool = input("Would you like to add any book else? Y/N ").lower().strip() == 'y'
name = input("type your name: ")
age = int(input(f"How old are you {name}? "))
print("what's your gender? [1] Male or [2] Female")

while True:
 gender = int(input("your option:"))
 if gender == 1:
    print ("Male")
    pron = "his"
    break
 elif gender == 2:
    print ("Female")
    pron = "her"
    break
 print("try again")

weight = float(input("type your weigth: "))

print (name, "is",age, "years old","and", pron, "weight","is:", weight)