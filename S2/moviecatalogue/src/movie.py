import datetime
from exceptions import *





class Movie:
    def __init__(self, title) -> None:
        validate_title(title)
        self.title = title
        self.date = datetime.datetime.now().time().isoformat(timespec='seconds')
        self.rating = []



    def rate(self, rating):
        rating = validate_rating(rating)
        self.rating.append(rating)


    def get_ratings(self):
        average = sum(self.rating) / len(self.rating)
        return average

    def get_title(self):
        return self.title


def validate_rating(rating):

    if rating < 1 or rating > 5:
        raise InvalidRatingException("rating must be between 0 and 5")
    rating = round(rating)
    return rating


def validate_title(title):
    if title.isspace() or len(title) == 0:
        raise MovieMustCantBeOnlyWhitespace("Movie title must be a string")