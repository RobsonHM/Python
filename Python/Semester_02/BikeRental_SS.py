
import datetime as dt
import time as t
from tabulate import tabulate as tb
import re
import random
import json
from pathlib import Path

"""There will be two classes: one for managing bikes (adding and updating bike information), and another for handling rentals. 
The rental class will only record new customer information for each rental transaction, without the ability to update existing rental records."""

class bikes:

   def __init__(self, bike_id, model, type, available, price):
        self.bike_id = bike_id
        self.model = model
        self.type = type
        self.available = available
        self.price = price
   
   def get_row(self):
        return [self.bike_id, self.model, self.type, self.available,  f"€{self.price:.2f}"]

   def get_details(self):
      data = [[self.bike_id, self.model, self.type, self.available, f"€{self.price:.2f}"]]
      headers = ["ID", "Model", "Type", "Available", "Daily Price"]
      return tb(data, headers=headers, tablefmt="grid")
      
   def save_bikes_items(self):
        return {"bike_id": self.bike_id, "model":self.model,"type": self.type,"available":self.available,"price":self.price}
 
   @classmethod
   def load_bikes_file(cls, data):
        return cls(bike_id=data["bike_id"],model=data["model"],type=data["type"],available=data["available"],price=data["price"])

class rental:

   def __init__(self, customer_name, bike_id, start_time, end_time):
        self.customer_name = customer_name
        self.bike_id = bike_id
        self.start_time = start_time
        self.end_time = end_time

   def get_details(self):
       return f"Customer: {self.customer_name}\nBike ID: {self.bike_id}\nStart time: {self.start_time}\nEnd Time: {self.end_time}"
   
   def save_rental_items(self):
        return {"customer_name":self.customer_name,"bike_id":self.bike_id,"start_time":self.start_time.strftime("%Y-%m-%d %H:%M:%S"),"end_time":self.end_time.strftime("%Y-%m-%d %H:%M:%S")}

   @classmethod
   def load_rental_file(self, data):
       return self(customer_name=data["customer_name"],bike_id=data["bike_id"], start_time=dt.datetime.strptime(data["start_time"], "%Y-%m-%d %H:%M:%S"), end_time=dt.datetime.strptime(data["end_time"], "%Y-%m-%d %H:%M:%S"))

#functions to check if information typed by user is correct and to save and load file

def is_valid_name(name_srt= "Enter your name: "):
    while True:
      name = input(name_srt).strip().lower()
      if not bool(re.match(r'[a-zA-Z ]{2,50}$',name)):
          print("it is not valid")
          continue
      return name

def is_valid_id(id_srt=""):
    while True:
        id = input(id_srt)
        if not bool (re.match(r'[0-9]{1,5}', id)):
            print("\033[31mID is not valid.\033[0m")
            continue
        return int(id)

def is_valid_model(model="What is the model: "):
    while True:
         bikes_model = input(model)
         if not bool(re.match(r"[A-Za-z0-9\- ]{2,30}", bikes_model)):
            print("Type a valid model: ")
            continue
         return bikes_model

def is_valid_type(type_srt="what is the type? "):
      while True:
         bikes_type = input(type_srt)
         if not bool(re.match(r'[a-zA-Z0-9\- ]', bikes_type)):
             print("type a valid type: ")
             continue         
         return bikes_type
    
def is_available(available_srt="Is it already available to be rented? Yes or No "):
    while True:
      bike_available = input(available_srt).strip().lower()
      if bike_available in ["yes", "y"]:
         return "Yes"
      elif bike_available in ["no","n"]:
         return "No"
      else:
            return print("\033[31mInvalid option, Type Yes or No.\033[0m")
    
def is_valid_option(prompt_srt="Choose an option (1-7): "):
    while True:
        value = input(prompt_srt)
        if not value.isdigit():
            print("\033[31mInvalid input. Please enter a number.\033[0m")
            continue 
        int_value = int(value)
        if int_value not in range(1, 8):
            print("\033[31mInvalid option. Choose a number between 1 and 7.\033[0m")
            continue
        return int_value

def is_valid_int(int_srt=""):
    while True:
        value_int = input(int_srt)
        if not value_int.isdigit():
            print("\033[31mInvalid input. Please enter a number.\033[0m")
            continue 
        return int(value_int)

def rent_days(days_srt):
   start_time = dt.datetime.now()
   end_time = start_time + dt.timedelta(days=days_srt)
   print ("\033[31mYou have to return it on\033[0m",end_time.strftime("%Y-%m-%d %H:%M:%S"))
   return start_time, end_time

def is_bike_save(file_name_srt, content_srt):
   with open(file_name_srt, "w", encoding="utf-8") as bike_list_saved:
      json.dump([bikes.save_bikes_items() for bikes in content_srt], bike_list_saved, ensure_ascii=False, indent=4)

def is_rental_save(file_name_r_srt,content_srt):
    with open (file_name_r_srt,"w", encoding="utf-8") as rental_list_saved:
      json.dump([rental.save_rental_items() for rental in content_srt], rental_list_saved, ensure_ascii=False, indent=4)
      print("Saved")

def load_bikes(filename_srt):
    try:
        with open(filename_srt, "r", encoding="utf-8") as load_bike:
            data = json.load(load_bike)
        return [bikes.load_bikes_file(bikes_data) for bikes_data in data]
    except:
        return []
    
def load_rental(filename_srt):
    try:
        with open(filename_srt,"r",encoding="utf-8") as load_rental:
            data = json.load(load_rental)
        return [rental.load_rental_file(rental_data) for rental_data in data]
    except:
        return False

def check_file(*nomes):
    return all(Path(nome).is_file() for nome in nomes)

'''When you save a file, you only need to type a name like "mybikes." The system will automatically add the "bikes_" prefix and the ".json" suffix, 
so the file will be saved as bikes_mybikes.json. To load the file later, simply type "mybikes" again. 
The system will automatically include the necessary prefix and suffix to find your file.
If you want to update an existing file, just save it using the same name, "mybikes," and the changes will be applied.'''

while True:
   load_all = input("\nWould you like to load any file? Yes/No ").strip().lower()
   if load_all in ["yes","y"]:
      What_file = input("what file would you like to load?: ").strip().lower()
      fileload_bike = (f"bikes_{What_file}.json")
      fileload_rental = (f"rental_{What_file}.json" )
      if check_file(fileload_bike,fileload_rental):
         print("\033[32mFile loaded\033[0m")
         all_bikes = load_bikes(fileload_bike)
         all_bikes_rent = load_rental(fileload_rental)
         break
      else:
         print("\033[31mFile not found or invalid.\033[0m")
   elif load_all in ["n","no"]:
       all_bikes = []
       all_bikes_rent = []
       break
   else:
       print("\033[31mOption not valid \033[0m")

#create options using tabulate
menu_items_unavailable = [
    ["\033[31m1. Display all available bikes\033[0m"],
    ["\033[32m2. Add new bike\033[0m"],
    ["\033[31m3. Rent a bike\033[0m"],
    ["\033[31m4. Return a bike\033[0m"],
    ["\033[31m5. Search bikes by type or ID\033[0m"],
    ["\033[31m6. Update details\033[0m"],
    ["\033[32m7. Exit and save data\033[0m"]
]
menu = [
    ["\033[32m1", "Display all available bikes\033[0m"],
    ["\033[32m2", "Add new bike\033[0m"],
    ["\033[32m3", "Rent a bike\033[0m"],
    ["\033[32m4", "Return a bike\033[0m"],
    ["\033[32m5", "Search bikes by type or ID\033[0m"],
    ["\033[32m6", "Update details\033[0m"],
    ["\033[32m7", "Exit and save data\033[0m"]
]

while True:
   if not all_bikes:
    print(tb(menu_items_unavailable, tablefmt="grid", colalign=("left",)))
    option = is_valid_option()
    while option in [1, 3, 4, 5, 6]:
        print("\033[31mOption not valid, choose another one\033[0m")
        option = is_valid_option()
   else:
      print(tb(menu, tablefmt="grid", colalign=("left",)))
      option = is_valid_option()
          
#display all bikes if there is bikes available
   if option == 1:
      bike_rows = [bikes.get_row() for bikes in all_bikes]
      headers = ["ID", "Model", "Type", "Available", "Daily Price"]
      print(tb(bike_rows, headers=headers, tablefmt="grid"))
      t.sleep(1)

# add a new bike 
   elif option == 2:
         
         while True:
            if not all_bikes: 
               last_id = 1
            else:
                existent_ids = {bike.bike_id for bike in all_bikes}
                last_id = sorted(existent_ids)[-1]
                last_id = last_id + 1   

            bike_models = is_valid_model()    
            bikes_type = is_valid_type()
            bike_avai = is_available()

            #the price of bike it is random between 1 and 5 euros
            bike_price = random.randint(1, 5)

            bike_ids = last_id
            bike = bikes(bike_ids, bike_models, bikes_type, bike_avai, bike_price)
            all_bikes.append(bike)
            add_more = input("add any bike else? Y/N ").strip().lower()
            if not add_more in ["yes", "y"]:
               print("Finishing adding bikes.")
               break

#rent a bike
   elif option == 3:
      customer_name = is_valid_name()

      see_list = input("see the list of available bikes? Y/N ").strip().lower()
      if see_list in ["y", "yes"]:
         bike_rows = [bikes.get_row() for bikes in all_bikes if bikes.available == "Yes"]
         headers = ["ID", "Model", "Type", "Available", "price"]
         print(tb(bike_rows, headers=headers, tablefmt="grid"))
         print("\n")
         t.sleep(1)

      bike_rent = is_valid_id("What bike would you like to rent?: type ID ")

      while True:
         for bikes in all_bikes:
            if bikes.bike_id == bike_rent:
               print(bikes.get_details())
               if bikes.available == "Yes":
                  other_bike = input("Would you like to change the selected bike? Y/N ").strip().lower()
                  if other_bike in ["y","yes"]:
                     bike_rent = is_valid_id("What bike would you like to rent?: type ID ")

                  rent_time = is_valid_int("How many days would you like to rent it?: ")
                 
                  
                  change_day = input("Would you like to change the day to return it back? Y/N ").strip().lower()
                  while change_day not in ["no", "n"]:
                        rent_time = int(input("How many days would you like to rent it?: "))
                        rent_days(rent_time)
                        change_day = input("Would you like to change the day? Y/N ").strip().lower()
                  start_time, end_time = rent_days(rent_time)
                  price_rent = ((end_time - start_time).days * (bikes.price))
                  print(f"The total price is: \033[32m{price_rent:.1f}€ \033[0m")

                  be_sure = input("Are you sure you want to rent this Bike? Y/N ")
                  if be_sure in ["y","yes"]:             
                     rent = rental(customer_name, bike_rent, start_time, end_time)
                     all_bikes_rent.append(rent)
                     
                     all_bikes[bike_rent - 1].available = ("No")
                     print("\033[32mThanks for rent it with us\033[0m")
                     t.sleep(1)
               else:
                   print("\033[31m It is not available \033[0m")
                   t.sleep(1)
         break

#return a bike
   elif option == 4:

      cus_name = is_valid_name()
      id_r = [rental.bike_id for rental in all_bikes_rent if rental.customer_name == cus_name]
      bike_rows = [bikes.get_row() for bikes in all_bikes if bikes.bike_id in id_r]
      headers = ["ID", "Model", "Type", "Available", "price"]
      if id_r == []:
         print("\033[31m It is not available \033[0m")
         t.sleep(1)
      else:
         print(tb(bike_rows, headers=headers, tablefmt="grid"))
         t.sleep(1)
         bikeid = int(input("Type the ID of the bike you want to return: "))

         for bikes in all_bikes:
            if bikes.bike_id == bikeid:
               
               price = bikes.price
               if bikes.available == "No":               
                     print(bikes.get_details())  
                     for rental in all_bikes_rent:
                          if rental.bike_id == bikeid and rental.customer_name == cus_name:
                              end_time = rental.end_time
                              start_time = rental.start_time
                              total = (dt.datetime.now() - end_time).days
                              days_rented = (dt.datetime.now() - start_time).days
                              print(f"You rented it for {(end_time - start_time).days} days")
                              if total > 0:
                                 pay = days_rented * price
                                 print(f"You are late, you have to pay 10% per day delayed, total of days you are with bike: {days_rented}, you have to pay {pay * 0.10:.2f}€ of fine")
                                 print(f"The total you have to pay is: {price * days_rented + pay * 0.10}€\n")
                              else:
                                 print(f"\nyou return the bike {-total} days ealier ")
                                 print(f"you have to pay: {price * days_rented}€\n")
                              
                              return_it = input("\033[31mWould you like to return this bike? Y/N \033[0m \n").strip().lower()
                              if return_it in ["y","yes"]:
                                    all_bikes[bikeid - 1].available = ("Yes")
                                    print("Thanks bike returned it")
                                    break
                              else:
                                 break
                          else:
                              print("\033[31mYou can return only bike that you rented.\033[0m")
                              break
               else:
                  print("\033[31mYou cannot return it because it is already available\033[0m")
                  continue

#search a bike by id or type
   elif option == 5:
      id_ty = input("Would you like to search by ID or Type? ").strip().lower()
      if id_ty == "id":
         bikeid = is_valid_id("What is the bike ID?: ")
         bike_rows = [bikes.get_row() for bikes in all_bikes if bikes.bike_id == bikeid]
         if bike_rows:  
            headers = ["ID", "Model", "Type", "Available", "price"]
            print(tb(bike_rows, headers=headers, tablefmt="grid"))
         else:
             print("\033[31mNo bikes found with that ID.\033[0m")
         t.sleep(1)
     

      elif id_ty == "type":
         bikeid = str(input("What is the Type: ")).strip().lower()
         bike_rows = [bikes.get_row() for bikes in all_bikes if bikes.type == bikeid]
         if bike_rows:  
            headers = ["ID", "Model", "Type", "Available", "price"]
            print(tb(bike_rows, headers=headers, tablefmt="grid"))
         else:
             print("\033[31mNo bikes found with that type.\033[0m")
         t.sleep(1)
      else:
          print("Please enter 'ID' or 'Type'.")

# if you want to update an existent bike
   elif option == 6:
      bikeid = is_valid_id("Type the ID of the bike you want to update: ")
      for bikes in all_bikes:
         if bikes.bike_id == bikeid:
            print(bikes.get_details())

      bike_models = is_valid_model()    
      bikes_type = is_valid_type()
      bike_avai = is_available()

      all_bikes[bikeid - 1].model = bike_models
      all_bikes[bikeid - 1].type = bikes_type
      all_bikes[bikeid - 1].available = bike_avai
      all_bikes[bikeid - 1].price = random.randint(1,5)

#save and exit
#name the file for exemple "allbikes" if you want 
   elif option == 7:
      if not all_bikes:
         break
      else:
         save_all = input("Would you like to save the list?: Y/N ")
         if save_all in ["yes","y"]:
            save_bike = ("bikes_") + input("Save list: ").replace(" ","").strip().lower() + (".json")      
            is_bike_save(save_bike, all_bikes)
            save_rental = save_bike.replace("bikes_","rental_")       
            is_rental_save(save_rental, all_bikes_rent)
            break
      break

   else:
       continue
