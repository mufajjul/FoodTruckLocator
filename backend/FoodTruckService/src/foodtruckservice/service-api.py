
import logging
from flask import Flask, request
from foodtruckservice.FTLProcessor import FTLProcessor
from foodtruckservice.DataHandler import DataHandler
from os import environ as env
from foodtruckservice import __version__
from dotenv import load_dotenv

__author__ = "Mufy"
__copyright__ = "Mufy"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


app = Flask(__name__)
app.config['DEBUG'] =- True

load_dotenv()

@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route('/', methods=['GET'])
def home():
        return "<h3>welcome to Food sharing service</h3>"


# This is the endpoint to get the nearest food truck locations in JSON format
@app.route('/fts/locator/', methods =['GET'])
def get_food_places():

        coorProcssor = FTLProcessor()

        lat = request.args.get("lat", default=0, type=float)
        lng = request.args.get("lng", default=0, type=float)
        
        _logger.debug ("lat & lng: ==> ", lat, lng)
        _logger.info("request received")
        
        food_truck_file_path = env["FOOD_TRUCK_FILE_PATH"]
        data_handler = DataHandler(food_truck_file_path)
        
        return coorProcssor.get_nearest_places(data_handler.get_food_truck_places_data(), lat, lng)
