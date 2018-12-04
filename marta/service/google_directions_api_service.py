import googlemaps
import os
from datetime import datetime

if 'GOOGLE_API_KEY' in os.environ:
    gmaps_client = googlemaps.Client(key=os.environ['GOOGLE_API_KEY'])
else:
    print("Google API service initialized without USER_TABLE_NAME environment variable, only expected in unit tests.")


def get_directions(origin, destination):
    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps_client.directions(origin + ", GA",
                                                destination + ", GA",
                                                departure_time=now)
    return directions_result


def get_directions_total_distance(directions_result):
    # All legs of trip
    print(directions_result)
    legs = directions_result[0]["legs"]
    # Distance in miles
    distance = 0
    for leg in legs:
        # Distance as text, ex. "11.8 mi"
        leg_distance_text = leg['distance']['text']
        # Distance as float
        leg_distance = float(leg_distance_text[0:len(leg_distance_text) - 3])
        distance += leg_distance
    return distance
