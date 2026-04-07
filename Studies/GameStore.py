import re

games = []

class GameStore():
    def __init__(self,title, price , year, score, publisher,genre):
        self.title = title
        self.price = price
        self.year = year
        self.score = score
        self.publisher = publisher
        self.genre = genre

    def gamedetails(self):
        return f"{self.title} cjej {self.price}" 
    
def is_text_valid(text):
    return bool(re.match(r'[a-zA-Z0-9]{2,50}', text))

def is_value_valid(value):
    return bool (re.match(r'[0-9]', value))

while True:

    new_game_name = input("Add a new game to the list: ")
    while not is_text_valid(new_game_name):
        print("It's a invalid name, type it again ")
        new_game_name = input("Add a new game to the list: ")

        
    new_game_price = float(input("How much is it?: "))
    while not is_value_valid(new_game_price):
        print("Invalid price")
        new_game_price = float(input("How much is it?: "))

    game_year = input("What year has the game been relesed? ")
    game_score = input("What is the metacric score? ")

    game_publi = input("What is the publisher? ")
    while not is_text_valid(game_publi):
        print("It's a invalid name, type it again ")
        game_publi = input("What is the publisher? ")

    game_genre = input("What is the genre? ")
    while not is_text_valid(game_genre):
        print("It's a invalid name, type it again ")
        game_genre = input("What is the genre? ")
    

    new_game = GameStore(new_game_name,new_game_price,game_year,game_score,game_publi,game_genre)

    games.append(new_game)

    add_more = input("Any game else?: Y/N ").strip().lower()
    print("_"*60+"\n")
    if add_more != "n":
       continue
    else:
       for games in games_list: 
            print(games.gamedetails())
    save_file = input("Save list: ").replace(" ","").strip().lower() + (".txt")      
    is_save(save_file, games_list)
    break

