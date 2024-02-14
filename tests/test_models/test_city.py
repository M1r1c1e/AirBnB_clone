import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_initialization(self):
        """Test City initialization"""
        # Create a City instance
        city = City()
        
        # Check if the state_id and name attributes are empty strings by default
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == "__main__":
    unittest.main()

