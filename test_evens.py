import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):
    def test_thowes_error_if_value_passed_in_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 5)
        self.assertRaises(TypeError, even_number_of_evens, "mustafa")
    
    def test_return_False_if_list_is_empty(self):
        self.assertEqual(even_number_of_evens([]), False)
        
    
    def test_return_False_if_number_of_evens_is_odd(self):
        self.assertEqual(even_number_of_evens([2, 3, 1, 5, 4, 6]), False)
    

    def test_return_True_if_number_of_evens_is_even(self):
        self.assertEqual(even_number_of_evens([2, 3, 2]), True)


if __name__ ==  "__main__":
    unittest.main()