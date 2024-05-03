

import unittest
import string
from password import generate_password

class TestPassword(unittest.TestCase):

    def test_password_length(self):
        # Test default length
        password = generate_password()
        self.assertEqual(len(password), 8)

        # Test custom length
        password = generate_password(min_length=12)
        self.assertEqual(len(password), 12)

    def test_password_generation(self):
        # Test with numbers and special characters
        password = generate_password(include_numbers=True, include_special_chars=True)
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

        # Test without numbers and special characters
        password = generate_password(include_numbers=False, include_special_chars=False)
        self.assertTrue(password.isalpha())

        # Test with numbers only
        password = generate_password(include_numbers=True, include_special_chars=False)
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertFalse(any(char in string.punctuation for char in password))

        # Test with special characters only
        password = generate_password(include_numbers=False, include_special_chars=True)
        self.assertTrue(any(char in string.punctuation for char in password))
        self.assertFalse(any(char.isdigit() for char in password))

if __name__ == '__main__':
    unittest.main()