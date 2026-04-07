import customtkinter as ctk
from datetime import datetime
import math
import re

allstudents = []

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x500")
app.title("Students list")

name_entry = ctk.CTkEntry(app, placeholder_text="Student Name")
name_entry.pack(pady=5)

birth_entry = ctk.CTkEntry(app,placeholder_text="Birth")
birth_entry.pack(pady=5)

id_entry = ctk.CTkEntry(app,placeholder_text="ID")
id_entry.pack(pady=5)

email_entry = ctk.CTkEntry(app,placeholder_text="Email")
email_entry.pack(pady=5)

phone_entry = ctk.CTkEntry(app,placeholder_text="Phone")
phone_entry.pack(pady=5)

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def is_valid_name(name_str):
    return bool(re.match(r'^[a-zA-Z ]+$', name_str))

def is_valid_id(id_str):
    return bool(re.match(r'^[0-9]{1,5}$', id_str))

def is_valid_Email(email_str):
    return bool (re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_str))

def is_valid_phone_number(phone_str):
    return bool (re.match(r'^\d{3}-\d{3}-\d{4}$',phone_str))
        
class Student():
    def __init__(self,name, age, birth, id, email, phone):
        self.name = name
        self.age = age
        self.birth = birth
        self.id = id
        self.email = email
        self.phone = phone

    def get_details(self):
         return (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Birth: {self.birth}\n"
            f"ID: {self.id}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}")

def submit_students():
    name = name_entry.get()
    birth = birth_entry.get()
    id = id_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if not is_valid_name(name):
        output_label.configure(text="Invalid name.")
        return
    if not is_valid_date(birth):
        output_label.configure(text="Enter birth date (DD/MM/YYYY): ")
        return
    if not is_valid_id(id):
        output_label.configure(text="Max 5 numbers")
        return
    if not is_valid_Email(email):
        output_label.configure(text="Enter the email: ")
        return
    if not is_valid_phone_number(phone):
        output_label.configure(text="Enter the phone (000-000-0000):  ")
        return

    yearbith = datetime.strptime(birth, "%d/%m/%Y")
    age = math.floor((datetime.now() - yearbith).days / 365.25)

    student = Student(name,age,birth,id,email,phone)
    allstudents.append(student)

    output_label.configure(text="Student added")

    for entry in [name_entry, birth_entry, id_entry, email_entry, phone_entry]:
        entry.delete(0, "end")

def view_all_students():
    if not allstudents:
        output_label.configure(text="No students")
        return
    output = "\n\n".join([s.get_details() for s in allstudents])
    output_label.configure(text = output)

def save_students_to_file():
    if not allstudents:
        output_label.configure(text="No students to save.")
        return
    with open("students.txt", "w") as f:
        for student in allstudents:
            f.write(student.get_details() + "\n\n")
    output_label.configure(text="Students saved to students.txt")

submit_btn = ctk.CTkButton(app, text="Submit student", command=submit_students)
submit_btn.pack(pady=10)

view_btn = ctk.CTkButton(app, text="View All Students", command=view_all_students)
view_btn.pack(pady=10)

save_btn = ctk.CTkButton(app, text="Save to File", command=save_students_to_file)
save_btn.pack(pady=10)

output_label = ctk.CTkLabel(app, width=300, height=200, anchor="w", justify="left")
output_label.pack(pady=30)

app.mainloop()