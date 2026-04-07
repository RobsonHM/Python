totalcart = 0.
booksprice = 7.5
books = 0
conditional = True
more = True
discounts = 0.0
finalvalue = 0.0

while totalcart >= 0 :
      
    if conditional == True:
        books = books + int(input("How many books do you want: "))
        booksprice = float(input("How much is each book? "))
        totalcart = books * booksprice 
        print("total is " , totalcart)
        conditional = input("Would you like to add any book else? Y/N ").lower().strip() == 'y'
    else:
        if books >= 3:
          discounts = 0.15 * totalcart 
          finalvalue = totalcart - discounts - 5.0
          print("The total is:",books, "books for ",totalcart,", You have earned: 15% bulk discount and €5 promotion discount. So the final value is:",finalvalue)
          more = input("Would you like to add any book else? Y/N ").lower().strip() == 'y'
          if more == True:
                conditional = True
                print("OK, add more books \n")
          else:
             print("Thank you for the purchased")
             break

        else:
          discounts = 0.15 * totalcart 
          finalvalue = totalcart - discounts
          print("The total is:",books, "books for ",totalcart,", You have earned: 15% bulk discount: So the final value is: ",finalvalue)
          more = input("Would you like to add any book else? Y/N ")
          if more == True:
                conditional = True
                print("OK, so add more books \n")
          else:
             print("Thank you for the purchased")
             break

# Second way to do it using dict to set value and name
# In this case it's possible setting values and names different for each item

books = {}
bookname = ""
MoreBooks = True 
AddMore = True
val = 0.


while AddMore == True:

    if MoreBooks == True:
        bookname = input("What book do you wanna buy? ")
        books[bookname] = float(input("How much is it? "))
        MoreBooks = input("Would you like to add more books? Y/N").lower().strip() == "y"
        
    else:
        val = sum(books.values())
        discaunt = val * 15 / 100
        total = val - discaunt
        for bookss, prices in books.items():
          print(f"{bookss} : {prices}")
        print("The total is:",len(books), "books for ",val,", You have earned: 15% bulk discount: So the final value is: ",total)
        MoreBooks = (input("Any books else? Y/N ")).lower().strip() == "y"
        if MoreBooks == True:
            AddMore = True
        else:
            AddMore = False
            print("Thank you for the purchased")

##teste