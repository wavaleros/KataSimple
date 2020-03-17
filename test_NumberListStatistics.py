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

    def test_return_the_same_value_with_one_input_value(self):
        value = "2"
        response = self.testedClass.processString(value)
        self.assertEqual(2, response[1])

    def test_return_the_minimum_value_with_two_input_values(self):
        value = "2,1"
        response = self.testedClass.processString(value)
        self.assertEqual(1, response[1])

    def test_return_the_minimum_value_with_n_values(self):
        value = "2,7,4,6,7,90"
        response = self.testedClass.processString(value)
        self.assertEqual(2, response[1])


class test_maximum_value(TestNumberListStatistics):

    def test_return_minus_one_with_no_input(self):
        response = self.testedClass.processString("")
        self.assertEqual(-1, response[2])

    def test_return_the_same_value_with_one_input_value(self):
        response = self.testedClass.processString("3")
        self.assertEqual(3, response[2])

    def test_return_the_maximum_value_with_two_input_values(self):
        value = "2,1"
        response = self.testedClass.processString(value)
        self.assertEqual(2, response[2])

    def test_return_the_maximum_value_with_n_values(self):
        value = "2,7,4,6,7,9,5"
        response = self.testedClass.processString(value)
        self.assertEqual(9, response[2])


class test_mean_value(TestNumberListStatistics):

    def test_return_minus_one_with_no_input(self):
        response = self.testedClass.processString("")
        self.assertEqual(-1, response[3])

    def test_return_the_same_value_with_one_input_value(self):
        response = self.testedClass.processString("3")
        self.assertEqual(3, response[3])

    def test_return_the_mean_value_with_two_input_values(self):
        value = "2,1"
        response = self.testedClass.processString(value)
        self.assertEqual(1.5, response[3])

    def test_return_the_mean_value_with_n_input_values(self):
        value = "0,1,2,3,4,5,6,7,8,9,10"
        response = self.testedClass.processString(value)
        self.assertEqual(5.0, response[3])
