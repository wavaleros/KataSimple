from unittest import TestCase

from NumberListStatistics import NumberListStatistics


class TestNumberListStatistics(TestCase):
    testedClass = NumberListStatistics()

    def setup(self):
        self.testedClass = NumberListStatistics()


class test_number_list_size(TestNumberListStatistics):

    def test_empty_list_return_size_zero(self):
        response = self.testedClass.processString("")
        self.assertTrue(response[0] == 0)

    def test_list_return_size_one(self):
        response = self.testedClass.processString("1")
        self.assertTrue(response[0] == 1)

    def test_list_return_size_two(self):
        response = self.testedClass.processString("1,2")
        self.assertTrue(response[0] == 2)

    def test_list_return_size_n(self):
        input_list = "1,2,6,7,8,341234,1234"
        response = self.testedClass.processString(input_list)
        self.assertTrue(response[0] == len(input_list.split(',')))


class test_minimum_value(TestNumberListStatistics):
    def test_return_minus_one_with_no_input(self):
        response = self.testedClass.processString("")
        self.assertEqual(-1, response[1])
