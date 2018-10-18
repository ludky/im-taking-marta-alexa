from marta import api

trains = api.get_trains(line=None, station='Chamblee Station', destination=None, api_key='2c01a977-126f-4a02-b208-98d19172ce15')
for train in trains:
    print(train.direction)
    print(train.station)
    print(train.next_arrival)