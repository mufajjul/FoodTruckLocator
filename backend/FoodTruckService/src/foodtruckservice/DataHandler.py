import pandas as pd
import logging

__author__ = "Mufy"
__copyright__ = "Mufy"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


class DataHandler:
    
    global file_path
    
    def __init__(self, filepath): 
       self.file_path = filepath
              
    def get_food_truck_places_data(self):
        location_df = pd.read_csv(self.file_path)
        return location_df

    def set_file_path(self, filepath):
        self.file_path = filepath
                    
    def get_file_path(self):
        return self.file_path
    
    