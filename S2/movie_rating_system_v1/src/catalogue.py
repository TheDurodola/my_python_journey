from movie import *

class Catalogue:
    def __init__(self):
        self.movies = []



    def add_movie(self, movie: Movie):
        self.movies.append(movie)


    def rate_movie(self, inputted_title, rate):
        for movie in self.movies:
            if  inputted_title == movie.get_title():
                movie.rate(rate)
                return True
        return False
