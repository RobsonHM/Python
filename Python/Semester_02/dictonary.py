user_phone = input("Whats is phone number? ")
user = input("What is your name? ")

people = {"40028922": "Yudi", "30028722":"Maisa", "23009234":"SBT", "78346432":"Silvio"}
people[user_phone] = user

look = input("Would you like to look for a specific person? Y/N ").strip().lower()

if look == "y":
    find_user = input("Type the phone number: ")
    print(f"This phone number {find_user} belongs to {people[find_user]}")
else:
    if user_phone in people:
        print(people[user_phone])
    for phone,name in people.items():
        print(f"{name}: {phone} ")


