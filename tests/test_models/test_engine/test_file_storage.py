import unittest
import os
from models.base_model import BaseModel
from models.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Set up for test cases """
        cls.storage = FileStorage()
        cls.obj = BaseModel()
        cls.obj.save()
        cls.storage.new(cls.obj)
        cls.storage.save()

    @classmethod
    def tearDownClass(cls):
        """ Remove test cases """
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """ Test all method """
        all_objs = self.storage.all()
        self.assertIn(f"{self.obj.__class__.__name__}.{self.obj.id}", all_objs)

    def test_new(self):
        """ Test new method """
        new_obj = BaseModel()
        new_obj.save()
        self.storage.new(new_obj)
        all_objs = self.storage.all()
        self.assertIn(f"{new_obj.__class__.__name__}.{new_obj.id}", all_objs)

    def test_reload(self):
        """ Test reload method """
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertIn(f"{self.obj.__class__.__name__}.{self.obj.id}", all_objs)

if __name__ == "__main__":
    unittest.main()

