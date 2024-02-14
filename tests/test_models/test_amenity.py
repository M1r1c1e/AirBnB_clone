import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_initialization(self):
        """Test Amenity initialization"""
        # Create an Amenity instance
        amenity = Amenity()
        
        # Check if the name attribute is an empty string by default
        self.assertEqual(amenity.name, "")

if __name__ == "__main__":
    unittest.main()

