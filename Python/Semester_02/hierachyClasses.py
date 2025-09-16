class videogames:
    counter = 0
    def __init__(self, title, genre, year, platforms):
        self.title = title
        self.genre = genre
        self.year = year
        self.platforms = platforms
        videogames.counter += 1

    def set_score(self, score):
        self.score = score

    def get_details(self):
        for detail in vds:
            detail = f"\n{self.title} is a {self.genre} game that has been released in {self.year} and it is available for {self.platforms}"
            if hasattr(self, "score") :
                detail += f" with {self.score}% on the metacritic"
        return detail

vd = videogames("Resident evil","survival horror", 2023, "Pc, Xbox and Playstation")
vd.set_score(92)
vds = [vd]

print(vd.get_details())
print(vd.counter)

class horror(videogames):
    pass

class suvivor_horror(horror):
    pass

class advanture(videogames):
    pass

class action_advanture(advanture):
    pass