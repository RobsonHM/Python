import time
#Veriable type dict to save all values of blood type
tblood  = {
    "A+": {"gives": ["A+", "AB+"], "receives": ["A+", "A-", "O+", "O-"]},
    "O+": {"gives": ["O+", "A+", "B+", "AB+"], "receives": ["O+", "O-"]},
    "B+": {"gives": ["B+", "AB+"], "receives": ["B+", "B-", "O+", "O-"]},
    "AB+": {"gives": ["AB+"], "receives": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]},
    "A-": {"gives": ["A+", "A-", "AB+", "AB-"], "receives": ["A-", "O-"]},
    "O-": {"gives": ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"], "receives": ["O-"]},
    "B-": {"gives": ["B+", "B-", "AB+", "AB-"], "receives": ["B-", "O-"]},
    "AB-": {"gives": ["AB+", "AB-"], "receives": ["AB-", "A-", "B-", "O-"]},
}
print("\nWelcome to the Blood Type Compatibility Checker!")
print("-"*60)

#variable to keep the while working till the user choose the option 3 that makes it setting the variable as False and stop it
continues = True

while continues == True:
     # 3 seconds of delay to give enough time to read it  
    time.sleep(3)
    print("Choose an option: \n 1. Check who can donate to your blood type. \n 2. Check who you can donate blood to. \n 3. Exit the program.\n")
    option = int(input("Enter your choice (1/2/3): " ))

#if to know what option you want to, 1-receive, 2-donate or 3-exit
    if option in [1,2,3] :

# "ifs" to check if the blood type is valid and to know what type blood is compatible
        if option == 1:
            Myblood = input("Enter your blood type (e.g., A+, O-, AB+): ").strip().upper()
            if Myblood in tblood:
                print(f"Blood Type {Myblood} can receive donations from: {", ".join(tblood[Myblood]["receives"])}\n")
            else:
                print(f"Invalid blood type: {Myblood}. Please try again.\n")

        elif option == 2:
            Myblood = input("Enter your blood type (e.g., A+, O-, AB-): ").strip().upper()
            if Myblood in tblood:
                print(f"Blood Type {Myblood} can donate to: {" , ".join(tblood[Myblood]["gives"])}\n")
            else:
                print(f"Invalid blood type: {Myblood}. Please try again.\n")

        else:
            print("Thank you for using the Blood Type Compatibility Checker. \nGoodbye!")
            continues = False
            break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.\n")