
from password import generator
import unittest
import string

class TestPassword(unittest.TestCase):
    # def test_generator_default(self):
    #     generator = password(8)
    #     self.assertEqual(len(generator),8)


    def test_password_generation(self):
        # Test with numbers and special characters
        password = generator(8, numbers=True, special_characters=True)
        self.assertEqual(len(password), 8)
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

        # Test without numbers and special characters
        password = generator(8, numbers=False, special_characters=False)
        self.assertEqual(len(password), 8)
        self.assertTrue(password.isalpha())

        # Test with numbers only
        password = generator(8, numbers=True, special_characters=False)
        self.assertEqual(len(password), 8)
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertFalse(any(char in string.punctuation for char in password))

        # Test with special characters only
        password = generator(8, numbers=False, special_characters=True)
        self.assertEqual(len(password), 8)
        self.assertTrue(any(char in string.punctuation for char in password))
        self.assertFalse(any(char.isdigit() for char in password))



if __name__ == '__main__':
    unittest.main() 