import unittest
from mock import patch
from marta import app
from marta.vehicles import Train
import json


class InvokeSkill(unittest.TestCase):
    def test_invoke_skill_success(self):
        event = load_json_from_file('invocation.json')
        response = app.lambda_handler(event=event, context=None)
        self.assertEquals("Welcome to Marta train tracker. Say when is the next train from Chamblee to Five Points",
                          response['response']['outputSpeech']['text'])


class GetTrainArrivalByDirection(unittest.TestCase):
    @patch('marta.api.get_trains')
    def test_get_train_arrival_one_train(self, mock):
        mock.return_value = create_mock_train_response()
        event = load_json_from_file('get_train_arrival_by_direction.json')
        ret = app.lambda_handler(event, "")
        response = ret['response']
        self.assertEquals(
            "The next southbound train arrives at Chamblee Station at 11:42:02",
            response['outputSpeech']['text'])
        self.assertTrue(response['shouldEndSession'])

    @patch('marta.api.get_trains')
    def test_get_train_arrival_two_trains(self, mock):
        mock.return_value = create_mock_two_train_response()
        event = load_json_from_file('get_train_arrival_by_direction.json')
        ret = app.lambda_handler(event, "")
        response = ret['response']
        self.assertEquals(
            "The next southbound trains arrive at Chamblee Station at 11:42:02 and 11:53:02",
            response['outputSpeech']['text'])
        self.assertTrue(response['shouldEndSession'])

    @patch('marta.api.get_trains')
    def test_get_train_arrival_failure(self, mock):
        mock.return_value = '10'
        event = load_json_from_file('get_train_arrival_by_direction_failure.json')
        ret = app.lambda_handler(event, "")
        response = ret['response']
        self.assertEquals(
            "Sorry, I didn't understand that. Ask when is the next train from Chamblee to Five Points",
            response['outputSpeech']['text'])
        self.assertFalse(response['shouldEndSession'])


def load_json_from_file(filename):
    with open('requests/' + filename) as jsonFile:
        return json.load(jsonFile)


def create_mock_train_response():
    trains = []
    train = {'DESINATION': 'FIVE POINTS STATION', 'DIRECTION': 'S', 'EVENT_TIME': '12/27/2013 12:30:06 PM',
             'LINE': 'GOLD',
             'NEXT_ARR': '11:42:02 PM', 'STATION': 'CHAMBLEE STATION', 'TRAIN_ID': '302506', 'WAITING_SECONDS': '-7',
             'WAITING_TIME': 'Boarding'}
    trains.append(Train(train))
    return trains


def create_mock_two_train_response():
    trains = []
    train1 = {'DESINATION': 'FIVE POINTS STATION', 'DIRECTION': 'S', 'EVENT_TIME': '12/27/2013 12:30:06 PM',
              'LINE': 'GOLD',
              'NEXT_ARR': '11:42:02 PM', 'STATION': 'CHAMBLEE STATION', 'TRAIN_ID': '302506', 'WAITING_SECONDS': '-7',
              'WAITING_TIME': 'Boarding'}
    train2 = {'DESINATION': 'FIVE POINTS STATION', 'DIRECTION': 'S', 'EVENT_TIME': '12/27/2013 12:30:06 PM',
              'LINE': 'GOLD',
              'NEXT_ARR': '11:53:02 PM', 'STATION': 'CHAMBLEE STATION', 'TRAIN_ID': '302506', 'WAITING_SECONDS': '-7',
              'WAITING_TIME': 'Boarding'}
    trains.append(Train(train1))
    trains.append(Train(train2))
    return trains


if __name__ == '__main__':
    unittest.main()
