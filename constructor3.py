#Create a Movie class with constructor for name, director, year, then make two movie objects and print their directors.

class Movie:
    def __init__(self,name,director,year):
        self.name     = name
        self.director = director
        self.year     = year

movie1 = Movie("Phir Hera Pheri","Neeraj Vohra","2003")
movie2 = Movie("Dhurandhar","Aditya Dhar","2025")

print("Director of Movie 1 :",movie1.director)
print("Director of Movie 2 :",movie2.director)