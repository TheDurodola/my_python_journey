import unittest
from catalogue import *


class MyTestCase(unittest.TestCase):

    def test_that_movie_can_be_added_into_the_catalogue(self):
        catalogue = Catalogue()
        catalogue.add_movie(Movie('FightClub'))
        self.assertEqual(1, len(catalogue.movies))
        catalogue.add_movie(Movie('The Batman'))
        self.assertEqual(2, len(catalogue.movies))

    def test_that_added_movie_can_be_rated(self):
        catalogue = Catalogue()
        catalogue.add_movie(Movie('FightClub'))
        catalogue.rate_movie('FightClub', 2)
        self.assertEqual(1, len(catalogue.movies))
        self.assertEqual(2, catalogue.movies[0].get_ratings())
        catalogue.rate_movie('FightClub', 5)
        self.assertEqual(1, len(catalogue.movies))
        self.assertEqual(3.5, catalogue.movies[0].get_ratings())

    def test_that_catalogue_with_multiples_movies_objects_can_be_rated(self):
        catalogue = Catalogue()
        catalogue.add_movie(Movie('FightClub'))
        catalogue.rate_movie('FightClub', 2)
        self.assertEqual(1, len(catalogue.movies))
        self.assertEqual(2, catalogue.movies[0].get_ratings())
        catalogue.rate_movie('FightClub', 5)
        self.assertEqual(1, len(catalogue.movies))
        self.assertEqual(3.5, catalogue.movies[0].get_ratings())
        catalogue.add_movie(Movie('The Batman'))
        self.assertEqual(2, len(catalogue.movies))
        catalogue.rate_movie('The Batman', 5)
        self.assertEqual(5, catalogue.movies[1].get_ratings())

    def test_that_if_movie_has_already_been_added_into_the_catalogue_MovieAlreadyExistException_is_raised(self):
        catalogue = Catalogue()
        catalogue.add_movie(Movie('The Batman'))
        with self.assertRaises(MovieAlreadyExistException):
            catalogue.add_movie(Movie('The Batman'))

    def test_that_average_for_a_particular_movie(self):
        catalogue = Catalogue()
        catalogue.add_movie(Movie('FightClub'))
        catalogue.rate_movie('FightClub', 2)
        self.assertEqual(1, len(catalogue.movies))
        self.assertEqual(2, catalogue.movies[0].get_ratings())
        catalogue.add_movie(Movie('The Batman'))
        self.assertEqual(2, len(catalogue.movies))
        catalogue.rate_movie('The Batman', 5)
        self.assertEqual(5, catalogue.movies[1].get_ratings())

    def test_that_exception_is_raised_incase_the_movie_been_rated_doesnt_exist_in_the_catalogue(self):
        catalogue = Catalogue()
        catalogue.add_movie(Movie('FightClub'))
        with self.assertRaises(MovieDoesNotExistException):
            catalogue.rate_movie('The Batman', 5)

    def test_that_if_user_wants_to_get_rating_for_a_movie_that_doesnt_exist_exception_is_raised(self):
        catalogue = Catalogue()
        catalogue.add_movie(Movie('FightClub'))
        with self.assertRaises(MovieDoesNotExistException):
            catalogue.get_ratings('The Batman')


if __name__ == '__main__':
    unittest.main()
