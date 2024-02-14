import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_initialization(self):
        """Test User initialization"""
        # Create a User instance
        user = User()
        
        # Check if the email, password, first_name, and 
        #last_name attributes are empty strings by default
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

if __name__ == "__main__":
    unittest.main()

