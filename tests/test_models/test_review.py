import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_initialization(self):
        """Test Review initialization"""
        # Create a Review instance
        review = Review()
        
        # Check if the place_id, user_id, and 
        #text attributes are empty strings by default
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == "__main__":
    unittest.main()

