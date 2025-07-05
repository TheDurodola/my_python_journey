import unittest

from movie import *


class MovieTest(unittest.TestCase):

    def test_that_movie_object_can_be_created(self):
        movie1 = Movie("BATMAN")
        self.assertEqual(type(movie1), Movie)

    def test_that_movie_can_be_rated(self):
        movie1 = Movie("BATMAN")
        movie1.rate(1)
        self.assertEqual(1, movie1.get_ratings())

    def test_that_movie_can_be_rated_multiple_times_and_returns_the_average(self):
        movie1 = Movie("BATMAN")
        movie1.rate(2)
        self.assertEqual(2, movie1.get_ratings())
        movie1.rate(3)
        self.assertEqual(2.5, movie1.get_ratings())
        movie1.rate(4)
        self.assertEqual(3, movie1.get_ratings())

    def test_if_movie_is_rated_outside_the_1to5_range_InvalidRatingsException_is_raised(self):
        movie1 = Movie("BATMAN")
        movie1.rate(1)
        rating = 6
        with self.assertRaises(InvalidRatingException):
            movie1.rate(rating)

    def test_that_average_cant_exceed_5(self):
        movie1 = Movie("BATMAN")
        movie1.rate(5)
        movie1.rate(5)
        movie1.rate(5)
        movie1.rate(5)
        movie1.rate(5)
        self.assertEqual(5, movie1.get_ratings())

    def test_that_float_ratings_are_turned_into_rounded_into_the_nearest_int(self):
        movie1 = Movie("FightClub")
        movie1.rate(4.6)
        self.assertEqual(5, movie1.get_ratings())

    def test_that_movie_can_be_added_date_and_time_are_accurate(self):
        movie1 = Movie("BATMAN")
        self.assertEqual(datetime.datetime.now().time().isoformat(timespec='seconds'), movie1.date)

    def test_that_whitespace_only_input_As_movie_title_is_rejected(self):
        with self.assertRaises(MovieMustCantBeOnlyWhitespace):
            movie1 = Movie(" ")









if __name__ == '__main__':
    unittest.main()
