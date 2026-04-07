from datetime import datetime
import re
games_list = []

class games():
    def __init__(self,title, year, genre, publisher, price):
        self.title = title
        self.year = year
        self.genre = genre
        self.publisher = publisher
        self.price = price

    def get_details(self):
     return f"\nGame: {self.title}\nYear: {self.year}\nGenre: {self.genre}\nPublisher: {self.publisher}\nPrice: {self.price}\n"

def is_valid_date(date_str):
    try:
       datetime.strptime (date_str, "%Y")
       return True
    except ValueError:
       return False
    
def is_valid_price(price):
   return bool (re.match(r'^[0-9]{2,6}$', price))

def is_save(file_name, content):
   with open (file_name, "w", encoding = "utf-8") as save_list:
      for item in content:
            save_list.write(f"{item.get_details()}\n")
            print("Saved")

while True:

    G_title = input("Name of the Game: ")

    G_year = input("Type only the year please: ")
    while not is_valid_date(G_year):
        print("Type only the year please: ")
        G_year = input("Relesed data: ")

    G_genre = input("Genre: ")
    G_publisher = input("Publisher: ")

    G_price = input("How much coast?: ")
    while not is_valid_price(G_price):
        print("Type numbers only")
        G_price = input("How much coast?: ")

    G_list = games(G_title,G_year,G_genre,G_publisher,G_price)
    games_list.append(G_list)

    add_more = input("Any game else?: Y/N ").strip().lower()
    print("_"*60+"\n")
    if add_more != "n":
       continue
    else:
       for lists in games_list: 
            print(lists.get_details())
    save_file = input("Save list: ").replace(" ","").strip().lower() + (".txt")      
    is_save(save_file, games_list)
    break
