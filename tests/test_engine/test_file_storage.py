import unittest
import os
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from tests.test_models.test_base_model import JSON_FILE_PATH

class TestFileStorageReloadNoFile(unittest.TestCase):
    """Tests the `reload()` method of the FileStorage engine when the JSON file does not exist."""

    def setUp(self) -> None:
        # Remove the JSON file if it exists
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_reload_no_file(self) -> None:
        """Tests reloading when the JSON file does not exist."""
        # Ensure that the JSON file does not exist
        self.assertFalse(os.path.exists(FileStorage._FileStorage__file_path))
        
        # Call the reload method
        storage.reload()

        # Check if the __objects dictionary is empty after reload
        self.assertEqual(len(storage.all()), 0)

    def tearDown(self) -> None:
        # Clean up: remove the JSON file if it was created during the test
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()

