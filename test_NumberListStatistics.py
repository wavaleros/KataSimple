from unittest import TestCase

from NumberListStatistics import NumberListStatistics


class TestNumberListStatistics(TestCase):
    testedClass = NumberListStatistics()


class test_number_list_size(TestNumberListStatistics):

    def test_empty_list_return_size_zero(self):
<<<<<<< HEAD
        self.assertTrue(self.testedClass.get_list_size() == 0)
=======
        self.assertTrue(self.testedClass.get_list_size() == 0)
>>>>>>> a853049857c06e6ba6c502324649f73667a5065b
