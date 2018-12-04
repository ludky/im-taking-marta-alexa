import unittest
from unittest.mock import patch
import json

from marta import app


class InvokeSkillIntent(unittest.TestCase):

    def test_invoke_skill_success(self):
        event = load_json_from_file('invocation/invocation.json')
        response = app.lambda_handler(event=event, context=None)
        self.assertEqual("Welcome to This is Marta. " +
                         "Say I'm taking Marta to Five Points station or say I took Marta to Five Points.",
                         response['response']['outputSpeech']['text'])


class SaveHomeTrainStationIntent(unittest.TestCase):
    @patch('marta.service.user_service.save_user')
    def test_save_home_train_station(self, mock):
        mock.return_value = None
        event = load_json_from_file('home_station/save_home_train_station.json')
        ret = app.lambda_handler(event, "")
        response = ret['response']
        self.assertEqual(
            "Your home train station is now Chamblee Station.",
            response['outputSpeech']['text'])
        self.assertFalse(response['shouldEndSession'])


class GetHomeTrainStationIntent(unittest.TestCase):
    @patch('marta.service.user_service.get_user')
    def test_get_home_train_station(self, mock):
        mock.return_value = mock_get_home_station_response()
        event = load_json_from_file('home_station/get_home_train_station.json')
        ret = app.lambda_handler(event, "")
        response = ret['response']
        self.assertEqual(
            "Your home train station is Chamblee Station.",
            response['outputSpeech']['text'])
        self.assertFalse(response['shouldEndSession'])

    @patch('marta.service.user_service.get_user')
    def test_get_home_train_station_not_set(self, mock):
        mock.return_value = None
        event = load_json_from_file('home_station/get_home_train_station.json')
        ret = app.lambda_handler(event, "")
        response = ret['response']
        self.assertEqual(
            "You have no home train station.  Say my home station is Five Points Station.",
            response['outputSpeech']['text'])
        self.assertFalse(response['shouldEndSession'])


class RecordTripIntent(unittest.TestCase):

    @patch('marta.service.user_service.get_user')
    @patch('marta.service.google_directions_api_service.get_directions')
    def test_record_trip_and_get_gas_savings(self, directions_mock, home_station_mock):
        directions_mock.return_value = self.mock_get_directions_response()
        home_station_mock.return_value = mock_get_home_station_response()
        event = load_json_from_file('record_trip/record_trip.json')
        ret = app.lambda_handler(event, "")
        response = ret['response']
        self.assertEqual(
            "You saved $1.15 on gas.",
            response['outputSpeech']['text'])
        self.assertTrue(response['shouldEndSession'])

    @staticmethod
    def mock_get_directions_response():
        return [
            {"legs": [
                {
                    "distance": {
                        "text": "11.8 mi"
                    }
                }
            ]}
        ]


def mock_get_home_station_response():
    return {'userId': 'aclifford', 'homeTrainStation': 'Chamblee Station'}


def load_json_from_file(filename):
    test_resources_relative_path = get_test_resources_relative_path()
    with open(test_resources_relative_path + 'requests/' + filename) as jsonFile:
        return json.load(jsonFile)


'''
Gets test resources relative path based on the name of this file at run time.  This allows tests to be run from any
directory in the project.
'''


def get_test_resources_relative_path():
    test_resources_relative_path = str(__name__).split('.')
    print(test_resources_relative_path)
    test_resources_relative_path = str.join("/", test_resources_relative_path[0:len(test_resources_relative_path) - 1])
    print(test_resources_relative_path)
    if test_resources_relative_path is not "":
        test_resources_relative_path += "/"
    return test_resources_relative_path


#
#
# def create_mock_train_response():
#     trains = []
#     train = {'DESINATION': 'FIVE POINTS STATION', 'DIRECTION': 'S', 'EVENT_TIME': '12/27/2013 12:30:06 PM',
#              'LINE': 'GOLD',
#              'NEXT_ARR': '11:42:02 PM', 'STATION': 'CHAMBLEE STATION', 'TRAIN_ID': '302506', 'WAITING_SECONDS': '-7',
#              'WAITING_TIME': 'Boarding'}
#     trains.append(Train(train))
#     return trains
#
#
# def create_mock_two_train_response():
#     trains = []
#     train1 = {'DESINATION': 'FIVE POINTS STATION', 'DIRECTION': 'S', 'EVENT_TIME': '12/27/2013 12:30:06 PM',
#               'LINE': 'GOLD',
#               'NEXT_ARR': '11:42:02 PM', 'STATION': 'CHAMBLEE STATION', 'TRAIN_ID': '302506', 'WAITING_SECONDS': '-7',
#               'WAITING_TIME': 'Boarding'}
#     train2 = {'DESINATION': 'FIVE POINTS STATION', 'DIRECTION': 'S', 'EVENT_TIME': '12/27/2013 12:30:06 PM',
#               'LINE': 'GOLD',
#               'NEXT_ARR': '11:53:02 PM', 'STATION': 'CHAMBLEE STATION', 'TRAIN_ID': '302506', 'WAITING_SECONDS': '-7',
#               'WAITING_TIME': 'Boarding'}
#     trains.append(Train(train1))
#     trains.append(Train(train2))
#     return trains


if __name__ == '__main__':
    unittest.main()
