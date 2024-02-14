import unittest
from models import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_initialization(self):
        """Test BaseModel initialization"""
        # Create a BaseModel instance without any arguments
        model = BaseModel()
        
        # Check if the id attribute is a string
        self.assertIsInstance(model.id, str)
        
        # Check if created_at and updated_at attributes are datetime objects
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        
    def test_str_representation(self):
        """Test BaseModel string representation"""
        # Create a BaseModel instance
        model = BaseModel()
        
        # Check if __str__ method returns the expected string representation
        expected_string = f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_string)
        
    def test_save_method(self):
        """Test BaseModel save method"""
        # Create a BaseModel instance
        model = BaseModel()
        
        # Get the initial value of updated_at attribute
        initial_updated_at = model.updated_at
        
        # Call the save method
        model.save()
        
        # Check if updated_at attribute is updated after calling save method
        self.assertNotEqual(initial_updated_at, model.updated_at)
        
    def test_to_dict_method(self):
        """Test BaseModel to_dict method"""
        # Create a BaseModel instance
        model = BaseModel()
        
        # Convert the BaseModel instance to a dictionary
        model_dict = model.to_dict()
        
        # Check if the returned dictionary contains expected keys
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("__class__", model_dict)

if __name__ == "__main__":
    unittest.main()

