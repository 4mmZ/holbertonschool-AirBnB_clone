#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from io import StringIO
import sys

class TestBaseModel(unittest.TestCase):

    def test_base_model_init(self):
        obj = BaseModel()

        save_output = StringIO
        sys.stdout = save_output
        print(obj)

        printed_output = save_output.getvalue().strip()
        self.assertEqual(printed_output, "[BaseModel] ")
        """Insertar el resto del printeo"""
    
    def test_base_model_updated_at(self):
        obj = BaseModel()

        save_output = StringIO
        sys.stdout = save_output
        print(obj.updated_at)

        printed_output = save_output.getvalue().strip()
        self.assertEqual(printed_output, "fechita jasjajsj")
  
    def test_base_model_name(self):
        """Cuestionable"""
        obj = BaseModel()
        obj.name = "My first model"
        self.assertEqual(obj.name, "My first model")

    def test_base_model_number(self):
        """Cuestionable"""
        obj = BaseModel()
        obj.number = 69
        self.assertEqual(obj.number, 69)
    
    def test_base_model_save(self):
        obj = BaseModel()
        obj.name = "My first model"
        obj.number = 69

        save_output = StringIO
        sys.stdout = save_output
        print(obj.created_at)

        printed_output = save_output.getvalue().strip()
        self.assertEqual(printed_output, "[BaseModel] ")

        obj.save()

        save_output = StringIO
        sys.stdout = save_output
        print(obj.updated_at)

        printed_output = save_output.getvalue().strip()
        self.assertEqual(printed_output, "[BaseModel] ")

    def test_base_model_update(self):
        obj = BaseModel()
        obj.name = "My first model"
        obj.number = 69

        save_output = StringIO
        sys.stdout = save_output
        print(obj.updated_at)

        printed_output = save_output.getvalue().strip()
        self.assertEqual(printed_output, "fecha ajajaj")

        obj.save()

        save_output = StringIO
        sys.stdout = save_output
        print(obj.updated_at)

        printed_output = save_output.getvalue().strip()
        self.assertEqual(printed_output, "nueva fecha jajaja")
        """Inserte printeo de update"""

    def test_base_model_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict, {})
        """insert dict"""

if __name__ == '__main__':
    unittest.main()            