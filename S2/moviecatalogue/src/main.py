from catalogue import Catalogue
from exceptions import MovieDoesNotExistException, MovieAlreadyExistException
from movie import Movie

catalogue = Catalogue()


main_menu_display = """ 
Welcome to the YRSD Movie Catalogue!

1) Add a movie
2) Rate a movie
3) Get rating of movie
4) Get all ratings
5) Exit
"""

while True:
    print(main_menu_display)
    navigate = input('Enter your choice: ')
    match navigate:
        case '1':
            movie_title = input('Enter movie title: ')
            try:
                catalogue.add_movie(Movie(movie_title))
                print("Movie Added Successfully")
            except MovieAlreadyExistException:
                print("Error 419 - Movie Already Exist")

        case '2':
            movie_title = input('Enter movie title: ')
            rated_movie = int(input('Enter movie rating: '))
            try:
                catalogue.rate_movie(movie_title, rated_movie)
                print("Movie Rated Successfully")
            except MovieDoesNotExistException:
                print("Error 420 - Movie Does Not Exist")

        case '3':
            movie_title = input('Enter movie title: ')
            try:
                rates = catalogue.get_ratings(movie_title)
                print(f"The rating for {movie_title} is {rates}")

            except MovieDoesNotExistException:
                print("Error 420 - Movie Does Not Exist")

            except TypeError:
                print("Error 421 - Movie hasn't been rated")

        case '4':
            try:
                print(catalogue.get_all_movies())

            except TypeError:
                print("Error 420 - A movie hasn't been rated")


        case '5':
            print('Goodbye!')
            break

        case _:
            print("Sorry, Invalid Input.")