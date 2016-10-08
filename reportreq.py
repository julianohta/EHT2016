from geolocation.main import GoogleMaps 
from geolocation.distance_matrix.client import DistanceMatrixApiClient
import urllib2
import json

google_maps = GoogleMaps(api_key="AIzaSyA2l1Dg7y6sUMl98CSDudcuC28VLLlXFTk")

def getgeoinfo():
    f = urllib2.urlopen('http://freegeoip.net/json/')
    json_string = f.read()
    f.close()
    location = json.loads(json_string)
    return location

def getLat(addr):
    location=google_maps.search(location=addr)
    print("aaaa" + location.all())
    myloc = location.first()
    return myloc.lat 

def getLng(addr):
    location=google_maps.search(location=addr)
    return location.first().lng 
