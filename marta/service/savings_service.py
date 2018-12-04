from marta.service import google_directions_api_service as directions_service

# TODO: Make these dynamic/real-time
dollars_per_gallon_gas = 2.40
avg_miles_per_gallon = 24.7


# Get total dollar savings for trip from origin to destination
def get_dollar_savings_for_trip(origin, destination):
    return distance_to_dollar_savings(get_trip_distance(origin, destination))


# Calculate dollar savings from trip distance
def distance_to_dollar_savings(distance):
    dollar_savings = distance / avg_miles_per_gallon * dollars_per_gallon_gas
    return dollar_savings


# Get total trip distance using Google Maps API service
def get_trip_distance(origin, destination):
    directions_result = directions_service.get_directions(origin, destination)
    distance = directions_service.get_directions_total_distance(directions_result)
    return distance
