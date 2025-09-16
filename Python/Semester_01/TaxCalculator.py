income = float(input("type your income: "))
tax = 0.0

if income < 85_528.0:
    tax = income * .18 - 556.02
    #print("you paid: ",tax," of tax and you have",income ,"left")
else:
    tax = (income - 85528.0) * .32 + 14_839.02
    #print("you paid",tax,"of Tax and you have",income,"left" )

tax = round(tax,0)

if tax < 0:
    tax = .0
print("The tax is:", tax, "thalers")
