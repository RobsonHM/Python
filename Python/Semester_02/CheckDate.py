from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

date_input = input("Enter birth date (DD/MM/YYYY): ")
while not is_valid_date(date_input):
    print("Invalid date format or values. Please try again.")
    date_input = input("Enter birth date (DD/MM/YYYY): ")
