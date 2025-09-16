mychash = 100.0
fairprice = float(input("How much would you pay for a drink? "))
drink = float(input("How much is the drink? "))

while mychash >= drink:

    if drink >= fairprice:
        print("It's too expensive")
        drinkagain = (input("do you wanna ask other drink? S/N "))
        if drinkagain.upper == "S":
            drink = float(input("How much is other drink? "))
        else:
             break
        
    elif drink >= fairprice:
            mychash -= drink
            print("buy a drink")
            print ("current money is: ",mychash)
         
    else:
        mychash -= drink
        print("buy a drink")
        print ("current money is: ",mychash)

print("no money anymore")

# Class task ->
SecretNumber = 700
GuessNumber = int(input("Guess the number: "))

while GuessNumber != SecretNumber:
    GuessNumber = int(input("it's wrong, guess the number again: "))
print("Congratulations! you got it")

