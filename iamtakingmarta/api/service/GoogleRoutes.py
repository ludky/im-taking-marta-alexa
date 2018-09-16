import googlemaps
import urllib2
import json

from datetime import datetime

gmaps = googlemaps.Client(key='API_KEY')

# Geocoding an address
#geocode_result = gmaps.geocode('5200 New Peachtree Rd, Chamblee, GA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Chamblee Station, Chamblee, GA",
                                     "Five Points Station, Atlanta, GA",
                                     mode="transit",
                                     departure_time=now)
#data = json.loads(directions_result)

print directions_result[0]["legs"][0]["departure_time"]