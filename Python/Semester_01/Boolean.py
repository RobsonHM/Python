#age = int(input("are you 100y old?\n[0] no / [1] yes \n"))
#print(bool(age))
'''
age = int(input("How old are you? "))
print (age >= 25)

if age >= 18:
    print("you're an adult")
else:
    print("get out of here")'''

num1 = int(input("type a number: "))
num2 = int(input("type a number: "))
num3 = int(input("type a number: "))

larger = num1

if (num2 > larger):
        larger = num2
if (num3 > larger):
        larger = num3

print('The largest number is: ',larger)