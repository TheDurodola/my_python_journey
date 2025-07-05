import unittest
from movieratingsystemfunction import *


class TestMovieRatingSystem(unittest.TestCase):

    def test_that_database_is_empty(self):
        movie_database.clear()
        self.assertEqual(0, len(movie_database))

    def test_that_database_is_not_empty_after_item_is_added(self):
        movie_database.clear()
        movie_name = "Interstellar"
        movie_rating_system = add_movie(movie_name)
        self.assertEqual(1, len(movie_database))

    def test_that_one_movie_with_the_date_and_time_can_be_added(self):
        movie_database.clear()
        movie_name = "Interstellar"
        movie_rating_system = add_movie(movie_name)
        self.assertEqual(movie_rating_system, [["Interstellar", datetime.date(2025, 7, 4),
                                                datetime.datetime.now().time().isoformat(timespec='seconds'), 0,0]])

    def test_that_if_movie_of_the_same_title_is_added_twice_exception_is_thrown(self):
        movie_database.clear()
        movie_name = "Interstellar"
        movie_rating_system = add_movie(movie_name)
        self.assertEqual(movie_rating_system, [["Interstellar", datetime.date(2025, 7, 4),
                                                datetime.datetime.now().time().isoformat(timespec='seconds'), 0, 0]])
        movie_name = "Interstellar"
        self.assertRaises(MovieAlreadyExistException, add_movie, movie_name)
        self.assertEqual(movie_rating_system, [["Interstellar", datetime.date(2025, 7, 4),
                                                datetime.datetime.now().time().isoformat(timespec='seconds'), 0, 0]])

    def test_that_multiple_movies_with_the_date_and_time_can_be_added(self):
        movie_database.clear()
        movie_title_one = "Interstellar"
        movie_rating_system = add_movie(movie_title_one)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'),0,0]
        self.assertEqual(movie_rating_system, [movie_one])

        movie_name = "DarkKnight-Rises"
        movie_rating_system = add_movie(movie_name)
        movie_two = ["DarkKnight-Rises", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 0,0]
        self.assertEqual(movie_rating_system, [movie_one, movie_two])

        movie_name = "FightClub"
        movie_rating_system = add_movie(movie_name)
        movie_three = ["FightClub", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 0,0]
        self.assertEqual(movie_rating_system, [movie_one, movie_two, movie_three])

    def test_that_rating_can_be_added(self):
        movie_database.clear()
        movie_title_one = "Interstellar"
        movie_rating_system = add_movie(movie_title_one)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 0,0]
        self.assertEqual(movie_rating_system, [movie_one])
        rating = 5
        movie_rating_system = add_rating(movie_title_one, rating)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 5,1]
        self.assertEqual(movie_rating_system, [movie_one])

    def test_that_multiple_movies_can_be_rated(self):
        movie_database.clear()
        movie_title_one = "Interstellar"
        movie_rating_system = add_movie(movie_title_one)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 0,0]
        self.assertEqual(movie_rating_system, [movie_one])

        rating = 5
        movie_rating_system = add_rating(movie_title_one, rating)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 5,1]
        self.assertEqual(movie_rating_system, [movie_one])

        movie_name = "DarkKnight-Rises"
        movie_rating_system = add_movie(movie_name)
        movie_two = ["DarkKnight-Rises", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 0,0]
        self.assertEqual(movie_rating_system, [movie_one, movie_two])

        rating = 4
        movie_rating_system = add_rating(movie_name, rating)
        movie_two = ["DarkKnight-Rises", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 4, 1]
        self.assertEqual(movie_rating_system, [movie_one, movie_two])
        return_all_movies()

    def test_that_exception_is_raised_when_rating_with_invalid_rating_is_inputted(self):
        movie_database.clear()
        movie_title_one = "Interstellar"
        movie_rating_system = add_movie(movie_title_one)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 0, 0]
        self.assertEqual(movie_rating_system, [movie_one])

        rating = 6
        self.assertRaises(InvalidRatingException, add_rating,movie_title_one, rating)
        rating = 0
        self.assertRaises(InvalidRatingException, add_rating, movie_title_one, rating)

    def test_one_movie_more_than_one_rating_added_for_the_same_movie_average_is_returned(self):
        movie_database.clear()
        movie_title_one = "Interstellar"
        movie_rating_system = add_movie(movie_title_one)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 0, 0]
        self.assertEqual(movie_rating_system, [movie_one])

        rating = 5
        movie_rating_system = add_rating(movie_title_one, rating)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 5, 1]
        self.assertEqual(movie_rating_system, [movie_one])

        rating = 5
        movie_rating_system = add_rating(movie_title_one, rating)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 5, 2]
        self.assertEqual(movie_rating_system, [movie_one])

        rating = 4
        movie_rating_system = add_rating(movie_title_one, rating)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 4, 3]
        self.assertEqual(movie_rating_system, [movie_one])

        rating = 5
        movie_rating_system = add_rating(movie_title_one, rating)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 4, 4]
        self.assertEqual(movie_rating_system, [movie_one])

    def test_that_the_highest_average_attainable_is_5(self):
        movie_database.clear()
        movie_title_one = "Interstellar"
        movie_rating_system = add_movie(movie_title_one)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 0, 0]
        self.assertEqual(movie_rating_system, [movie_one])
        rating = 5
        movie_rating_system = add_rating(movie_title_one, rating)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 5, 1]
        self.assertEqual(movie_rating_system, [movie_one])
        movie_rating_system = add_rating(movie_title_one, rating)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 5, 2]
        self.assertEqual(movie_rating_system, [movie_one])

    def test_that_if_rating_inputted_is_a_float_an_integer_is_returned(self):

        movie_database.clear()
        movie_title_one = "Interstellar"
        movie_rating_system = add_movie(movie_title_one)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 0, 0]
        self.assertEqual(movie_rating_system, [movie_one])
        rating = 4.5
        movie_rating_system = add_rating(movie_title_one, rating)
        movie_one = ["Interstellar", datetime.date(2025, 7, 4),
                     datetime.datetime.now().time().isoformat(timespec='seconds'), 4, 1]
        self.assertEqual(movie_rating_system, [movie_one])





if __name__ == '__main__':
    unittest.main()
