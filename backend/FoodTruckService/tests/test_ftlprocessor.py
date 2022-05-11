import unittest
import os
from foodtruckservice.FTLProcessor import FTLProcessor
from foodtruckservice.DataHandler import DataHandler

class TestFLTProcessor(unittest.TestCase):

    def test_json_output(self):
        
        data_handler = DataHandler("./data/Mobile_Food_Facility_Permit.csv")
        
        ftlpprocessor = FTLProcessor(data_handler.get_nearest_places_data(), '13.33', '-123.45') 
        json_output = ftlpprocessor.get_nearest_places() 
        
        self.assertIsNotNone(json_output) 
        
    if __name__ == '__main__':
        unittest.main()