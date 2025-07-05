import datetime

movie_database = []

def add_movie(movie_title):
    if len(movie_database) > 0:
        for movie in movie_database:
            if movie_title == movie[0]:
                raise MovieAlreadyExistException("MOVIE ALREADY EXISTS")



    date = datetime.date.today()
    time = datetime.datetime.now().time().isoformat(timespec='seconds')
    initial_rating: float = 0
    rating_count = initial_rating
    movie_record = [movie_title, date, time, initial_rating, rating_count]
    movie_database.append(movie_record)

    return movie_database



def add_rating(movie_title_one, rating):
    rating = int(rating)
    validate(rating)
    for movie_record in movie_database:
        if movie_record[0] == movie_title_one:
            movie_record[4] = movie_record[4] + 1
            movie_record[3] = movie_record[3] + rating
            if movie_record[4]!=1:
                movie_record[3] = round(movie_record[3]/ 2)

    return movie_database


def return_all_movies():
    print(f"Movie Title                 Date         Time        Rating  ")
    for movie_record in movie_database:
        print(f"{movie_record[0]}       {movie_record[1]}    {movie_record[2]}       {movie_record[3]}")


def validate(rating):

    if rating < 1 or rating > 5:
        raise InvalidRatingException("rating must be between 0 and 5")

class InvalidRatingException(ValueError):
    pass


class MovieAlreadyExistException(ValueError):
    pass


