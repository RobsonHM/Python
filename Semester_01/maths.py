john = int(input("how many apples does john have? "))
mary = int(input("how many apples does mary have? "))
adam = int(input("how many apples does adam have? "))

apples = [john,mary,adam]

total = max(apples)

if total == john:
    print("\nJohn has more apples than everyone")
elif total == mary:
    print("\nMary has more apples than everyone")
else:
    print("\nAdam has more apples than everyone")

#Type casting
leg_a = float(input("Input first lag length: "))
leg_b = float(input("Input second lag length: "))
print("hypotenuse lengh is ", (leg_a**2 + leg_b**2) ** .5)

hypo = (leg_a**2 + leg_b**2) ** .5
print("hypotenuse lengh is ",hypo)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

'''
a = 3.0
b = 4.0
c = (a**2 + b**2)**0.5
print(c)
'''