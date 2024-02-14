import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_initialization(self):
        """Test State initialization"""
        # Create a State instance
        state = State()
        
        # Check if the name attribute is an empty string by default
        self.assertEqual(state.name, "")

if __name__ == "__main__":
    unittest.main()

