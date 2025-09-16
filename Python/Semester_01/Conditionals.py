age = int(input("inform your age: "))

if age >= 18:
    print("allowed")
else:
    print("not allowed")

salary = float(input("inform yopur salary: "))

if salary <= 3000:
    print ("junior")
elif salary > 3000 and salary <= 5000:
    print ("Senior")
elif salary > 5000 and salary <= 15000:
    print ("pleno")
else:
    print ("project manager")

cash = float(input("how much cash do you have in your bank account? "))

if cash <= 100:
    print(" :'( )")
elif cash > 100 and cash <= 1000:
    print("you have to get more money")
elif cash > 1000 and cash <= 3000:
    print ("keep improving it")
elif cash > 3000 and cash <= 10000:
    print("Almost there")
else:
    print("congratulations :) ")