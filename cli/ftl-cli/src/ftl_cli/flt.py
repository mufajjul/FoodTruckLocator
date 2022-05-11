
from argparse import ArgumentParser
import string
import requests
from dotenv import load_dotenv
from os import environ as env


load_dotenv()

def get_food_places(lat, lng):
    print ("lat: %s" % lat)
    
    flt_uri = env['WEB_SERVICE_URI']
    
    r = requests.get("%s?lat=%s&lng=%s" % (flt_uri, lat, lng))
    
    return r.json()
    
    
if __name__ == '__main__':

    parser = ArgumentParser(prog='flt', description='Service truck locator cli')
    parser.add_argument('get-coor', type=str,  help='current option is only get locations')

    parser.add_argument('--lat', type=float,  help='latitude coordination, e.g 12.2322332', required=True)
    parser.add_argument('--lng', type=float,  help='longitude coordination, e.g -122.2322332', required=True)

    args = parser.parse_args()
    
    print (get_food_places(args.lat, args.lng))
    