
from scipy.spatial import distance
import numpy as np
from timeit import default_timer as timer
from datetime import timedelta
import logging

__author__ = "Mufy"
__copyright__ = "Mufy"
__license__ = "MIT"

_logger = logging.getLogger(__name__)

class FTLProcessor:
    
    def __init__(self):        
        print ('') 
    
    def get_nearest_places(self, locations_df, lat, lng):

        start = timer()
    
        truck_geo_coor = np.array(locations_df[['Latitude', 'Longitude']])
        current_geo_coor = [lat, lng]
        locations_df['distance_output'] = [distance.euclidean (current_geo_coor, location)  for location in truck_geo_coor]    
        top_five_loc = locations_df.sort_values(by=['distance_output'])[['Latitude', 'Longitude']][:5]
        json_coor = top_five_loc.reset_index().drop(columns=['index']).to_json()

        end = timer()

        _logger.debug(timedelta(seconds=end-start))
        
        return json_coor


        