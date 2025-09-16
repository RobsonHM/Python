from datetime import datetime
import math
import re

allstudents = []

def save_students(file_name, content):
    with open(file_name, "w", encoding="utf-8") as students_save:
        for item in content:
            students_save.write(f"{item.get_details()}\n---\n")
        print("file saved")

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def is_valid_name(name_str):
    return bool(re.match(r'^[a-zA-Z ]{2,50}+$', name_str))

def is_valid_id(id_str):
    return bool(re.match(r'^[0-9]{1,6}$', id_str))

def is_valid_Email(email_str):
    return bool (re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_str))

def is_valid_phone_number(phone_str):
    return bool (re.match(r'^\d{10}$',phone_str))
        
class student():
    def __init__(self,name, age, birth, id, email, phone):
        self.name = name
        self.age = age
        self.birth = birth
        self.id = id
        self.email = email
        self.phone = phone

    def get_details(self):
        return f"Name: {self.name}\nAge: {self.age}\nBirth: {self.birth}\nID: {self.id}\nEmail: {self.email}\nPhone: {self.phone}\n"

while True:
    # check if the name is only letters
    name = input("Enter name: ")
    while not is_valid_name(name):
        print("0._%+- are not allowed") 
        name = input("Enter name: ")

    # check the birth date is valid
    birth = input("Enter birth date (DD/MM/YYYY): ")
    while not is_valid_date(birth):
        print("Invalid date format or values. Please try again.")
        birth = input("Enter birth date (DD/MM/YYYY): ")
    yearbith = datetime.strptime(birth, "%d/%m/%Y")
    age = math.floor((datetime.now() - yearbith).days /365.25)

    #check if the ID is valid
    existing_ids = {student.id for student in allstudents}
    while True:
        id = input("Enter ID: ")
        if not is_valid_id(id):
            print("Max 6 numbers")
            continue
        if id in existing_ids:
            print("ID already exists.")
            continue
        break

    # Check if the email is valid
    email = input("Enter the email: ")
    while not is_valid_Email(email):
        print("invalid email")
        email = input("Enter the email: ")

    # Check if the phone number is valid
    phone = input("Enter the phone (000-000-0000): ")
    while not is_valid_phone_number(phone):
        print("not valid")
        phone = input("Enter the phone (000-000-0000):  ")

    print("-"*60, "\n")
    students = student(name, age, birth, id, email, phone)
    allstudents.append(students)
    anyelse = input("would you like to add anyone else? Y/N: ")
    if anyelse.lower() != "y":
        print("-"*60)
        break

AnyStudent = input("Would you like to choose a specific student? Y/N: ")
print("-"*60)
student_id = ""

while True:
    if AnyStudent.lower() == "y":
        student_id = input("Enter ID: ")
        while not is_valid_id(student_id):
            print("Max 5 numbers")
            student_id = input("Enter ID: ")
            found = False
            for student in allstudents:
                if student.id == student_id:
                    print("\nStudent found:")
                    print(student.get_details())
                    found = True
                    AnyStudent = input("\nwould you like to find someone else? Y/N: ")
                    if AnyStudent.lower() == "y":
                        student_id = input("Enter ID: ")
                        while not is_valid_id(student_id):
                            print("Max 5 numbers")
                            student_id = input("Enter ID: ")        

        if not found:
            print("No student found with that ID.")
    else:
        AnyStudent = input("would you like to see a list of all students? Y/N: ")
        print("-"*60)
        if AnyStudent == "y":
            print("\nAll students:\n")
            for student in allstudents:
                print(student.get_details())
            save_all = input("Would you like to save the list? Y/N: ").strip().lower()
            if save_all == "y":
               save_file = input("Name the file: ").replace(" ","").strip().lower()
               save_file = save_file + ".txt"
               save_students(save_file, allstudents)
               break
        else:
            save_all = input("Would you like to save the list? Y/N: ").strip().lower()
            if save_all == "y":
               save_file = input("Name the file: ").replace(" ","").strip().lower()
               save_file = save_file+".txt"
               save_students(save_file, allstudents)
               break 
        break


"""
    all_bikes = [
    bikes(1, "CityRide 300",   "urban",    True,3),
    bikes(2, "EcoSprint X",    "electric", False,2),
    bikes(3, "MTB Storm 500",  "mountain", True,1),
    bikes(4, "UrbanLite",      "urban",    True,4),
    bikes(5, "TrailBlazer 4",  "mountain", False,3),
    bikes(6, "VoltCity Pro",   "electric", True,2),
    bikes(7, "Speedster 700",  "road",     True,1),
    bikes(8, "CargoMax Duo",   "cargo",    False,2),
    bikes(9, "FlexFold Mini",  "folding",  True,4),
    bikes(10, "Gravel X One",   "gravel",   True,5)
]

all_bikes_rent = [
    rental("Alice", 1, dt.datetime(2025, 7, 1, 9, 0), dt.datetime(2025, 7, 29, 9, 0)),
    rental("Bob", 2, dt.datetime(2025, 7, 2, 10, 30), dt.datetime(2025, 7, 6, 10, 30)),
    rental("Carla", 3, dt.datetime(2025, 7, 3, 14, 15), dt.datetime(2025, 7, 8, 14, 15)),
    rental("Diego", 4, dt.datetime(2025, 7, 4, 8, 45), dt.datetime(2025, 7, 10, 8, 45)),
    rental("Eva", 5, dt.datetime(2025, 7, 5, 13, 0), dt.datetime(2025, 7, 12, 13, 0)),
    rental("Felipe", 6, dt.datetime(2025, 7, 6, 9, 30), dt.datetime(2025, 7, 15, 9, 30)),
    rental("Giovana", 7, dt.datetime(2025, 7, 7, 11, 0), dt.datetime(2025, 7, 14, 11, 0)),
    rental("Hugo", 8, dt.datetime(2025, 7, 8, 16, 20), dt.datetime(2025, 7, 13, 16, 20)),
    rental("Isabela", 9, dt.datetime(2025, 7, 9, 10, 0), dt.datetime(2025, 7, 16, 10, 0)),
    rental("João", 10, dt.datetime(2025, 7, 10, 15, 30), dt.datetime(2025, 7, 17, 15, 30)),
]"""