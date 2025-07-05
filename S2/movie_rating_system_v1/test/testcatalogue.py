import unittest
from catalogue import *


class MyTestCase(unittest.TestCase):
    def test_that_movie_can_be_added_into_the_catalogue(self):
        catalogue = Catalogue()
        catalogue.add_movie('The Movie')
        self.assertEqual(1, len(catalogue.movies))
        catalogue.add_movie('The Batman')
        self.assertEqual(2, len(catalogue.movies))


    def test_that_added_movie_can_be_rated(self):
        catalogue = Catalogue()
        catalogue.add_movie(Movie('The Movie'))
        catalogue.rate_movie('The Movie', 2)
        self.assertEqual(1, len(catalogue.movies))
        self.assertEqual(2, catalogue.movies[0].get_ratings())
        catalogue.rate_movie('The Movie', 5)
        self.assertEqual(1, len(catalogue.movies))
        self.assertEqual(3.5, catalogue.movies[0].get_ratings())

if __name__ == '__main__':
    unittest.main()
