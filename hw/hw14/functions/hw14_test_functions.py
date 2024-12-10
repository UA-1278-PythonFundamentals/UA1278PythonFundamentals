# You have two python modules fuctions and functions_with_errors with same functions greeting_by_name, get_symbol_position and merge but there are mistakes in the second file in these functions.
# Write unit tests in module and with unittest to cover all possible returns from all fuctions after that test both files.
# On screenshot you can see example of test result for functions with misstakes.

# Отримання звіту про % покриття тестами - в терміналі:
# 1) pip install coverage
# 2) coverage run -m unittest .\hw14_test_functions.py
# 3) coverage html

import unittest
from .functions import greeting_by_name, get_symbol_position, merge


class TestFunctions(unittest.TestCase):

    def test_greeting_by_name(self):
        self.assertEqual(greeting_by_name("Alice"), "Hello Alice!")
        self.assertEqual(greeting_by_name(""), "Hello !")

    def test_get_symbol_position(self):
        self.assertEqual(get_symbol_position("hello", "e"), 2)
        self.assertEqual(get_symbol_position("hello", "z"), "Not found")
        self.assertEqual(get_symbol_position("hello", "ll"),
                         "Error! Symbol can be string with only one letter")

        self.assertEqual(get_symbol_position("", "a"), "Not found")
        self.assertEqual(get_symbol_position("hello", ""), 1)
        self.assertEqual(get_symbol_position("hello", "h"), 1)

    def test_merge(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        expected_result = {"a": 1, "b": 3, "c": 4}

        result = merge(dict1, dict2)
        self.assertEqual(result, expected_result)
        self.assertEqual(dict1, {"a": 1, "b": 2})

        self.assertEqual(merge({}, dict2), dict2)
        self.assertEqual(merge(dict1, {}), dict1)

        self.assertEqual(merge({}, {}), {})


if __name__ == "__main__":
    unittest.main()