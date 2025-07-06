from movie import *


class Catalogue:
    def __init__(self):
        self.movies = []

    def add_movie(self, new_movie: Movie):
        validate_movie(new_movie, self.movies)
        self.movies.append(new_movie)

    def rate_movie(self, inputted_title, rate):
        for movie in self.movies:
            if  inputted_title == movie.get_title():
                movie.rate(rate)
                return True
        raise MovieDoesNotExistException("Movie '{}' does not exist".format(inputted_title))

    def get_ratings(self, inputted_title):
        for movie in self.movies:
            if inputted_title == movie.title:
                return movie.get_ratings()
        raise MovieDoesNotExistException("Movie '{}' does not exist".format(inputted_title))

    def get_all_movies(self):
        print("Title    Rating")
        for movie in self.movies:
            print(f"{movie.get_title()} {movie.get_ratings()}")
        return ""



def validate_movie(new_movie: Movie, movie_list):
    title = new_movie.title
    for movie in movie_list:
        if title == movie.title:
            raise MovieAlreadyExistException