import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    def test_thowes_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 5)
        self.assertRaises(TypeError, even_number_of_evens, "mustafa")
    
    def test_return_False_if_list_is_empty(self):
        self.assertEqual(even_number_of_evens([]), False)


if __name__ ==  "__main__":
    unittest.main()