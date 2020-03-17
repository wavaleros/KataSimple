from unittest import TestCase

from NumberListStatistics import NumberListStatistics


class TestNumberListStatistics(TestCase):
    testedClass = NumberListStatistics()


class test_number_list_size(TestNumberListStatistics):

    def test_empty_list_return_size_zero(self):
        self.assertTrue(self.testedClass.get_list_size() == 0)

    def test_list_return_size_one(self):
        self.testedClass.processString("1")
        self.assertTrue(self.testedClass.get_list_size() == 1)
