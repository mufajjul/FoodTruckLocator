import unittest
import os
from foodtruckservice.DataHandler import DataHandler


class TestDataHandler(unittest.TestCase):

    def test_datafile(self):
        print (os.getcwd())
        
        file_path = './data/Mobile_Food_Facility_Permit.csv'
        data_handler = DataHandler(file_path)
        
        self.assertIsNotNone (data_handler.get_food_truck_places_data())
        
    if __name__ == '__main__':
        unittest.main()

