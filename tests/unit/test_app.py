import unittest
from mock import patch
from marta import app
from marta.vehicles import Train
import json


class InvokeSkill(unittest.TestCase):
    @patch('marta.api.get_trains')
    def test_invoke_skill_success(self, mock):
        event = load_json_from_file('invocation.json')
        response = app.lambda_handler(event=event, context=None)
        self.assertEquals("Welcome to Marta train tracker. Say when is the next train from Chamblee to Five Points", response['response']['outputSpeech']['text'])


class GetTrainArrivalByDestinationSuccess(unittest.TestCase):
    @patch('marta.api.get_trains')
    def test_get_train_arrival_success(self, mock):
        mock.return_value = create_mock_train_response()
        event = load_json_from_file('get_train_arrival_by_destination_success.json')
        ret = app.lambda_handler(event, "")
        response = ret['response']
        self.assertEquals(
            "The next train from Chamblee Station to Five Points Station arrives at 11:42:02",
            response['outputSpeech']['text'])
        self.assertTrue(response['shouldEndSession'])

    @patch('marta.api.get_trains')
    def test_get_train_arrival_failure(self, mock):
        mock.return_value = '10'
        event = load_json_from_file('get_train_arrival_by_destination_failure.json')
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
    train = Train
    train.next_arrival = '11:42:02'
    train.station = 'CHAMBLEE STATION'
    train.destination = 'AIRPORT STATION'
    train.direction = 'SOUTHBOUND'
    train.last_updated = '11:42:02'
    train.line = 'gold'
    train.train_id = '1'
    train.waiting_seconds = '2'
    train.waiting_time = '11:42:02'

    trains.append(train)
    return trains


if __name__ == '__main__':
    unittest.main()

